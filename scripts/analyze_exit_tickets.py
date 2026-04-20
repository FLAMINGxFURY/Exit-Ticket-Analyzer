#!/usr/bin/env python3
"""
Analyze weekly exit-ticket reflection CSVs and optionally ask OpenAI for a semantic summary.

Expected D2L-style columns based on the sample file:
- Q # / Q Text / Answer
- difficulty rating stored in "Answer Match" for the 1-10 difficulty prompt

This script:
1. Loads all CSVs under data/exit_tickets/
2. Treats each CSV as one run/week
3. Extracts:
   - learned reflections
   - struggle/questions reflections
   - future interest reflections
   - numeric course difficulty ratings
4. Builds deterministic metrics
5. Optionally calls OpenAI for semantic clustering / teaching recommendations
6. Writes Markdown + JSON reports to reports/
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median
from typing import Iterable

import pandas as pd

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "exit_tickets"
REPORTS_DIR = ROOT / "reports"

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4")
ENABLE_OPENAI_SUMMARY = os.getenv("ENABLE_OPENAI_SUMMARY", "false").lower() == "true"

STOPWORDS = {
    "a","an","and","are","as","at","be","but","by","for","from","how","i","if","in","into",
    "is","it","its","of","on","or","so","that","the","their","them","they","this","to","we",
    "was","what","when","where","which","who","why","with","you","your","about","have","has",
    "had","can","could","would","should","will","just","really","more","much","one","week",
    "learn","learned","learning","like","thing","things","still","class","content","covered",
    "far","future","want","would","like","know","dont","didnt","cant","im","ive"
}

REFLECTION_SCHEMA = {
    "name": "reflection_insights",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "top_learned_concepts": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 8
            },
            "top_struggle_clusters": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 8
            },
            "future_interest_clusters": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 8
            },
            "mismatches": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 6
            },
            "teaching_adjustments": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 6
            },
            "followup_exit_ticket_questions": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 5
            },
            "short_instructor_summary": {"type": "string"}
        },
        "required": [
            "top_learned_concepts",
            "top_struggle_clusters",
            "future_interest_clusters",
            "mismatches",
            "teaching_adjustments",
            "followup_exit_ticket_questions",
            "short_instructor_summary"
        ]
    }
}


@dataclass
class WeekBundle:
    label: str
    source_file: str
    learned: list[str]
    struggled: list[str]
    future: list[str]
    difficulty_ratings: list[float]


def clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    text = re.sub(r"\s+", " ", text)
    return text


def is_nonresponse(text: str) -> bool:
    normalized = re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()
    return normalized in {
        "",
        "n a",
        "na",
        "none",
        "idk",
        "i dont know",
        "dont know",
        "i do not know",
        "not sure",
        "nothing",
        "no",
        "nope",
        "i cant think of one for this week",
        "i dont have one for this week",
        "i do not have one for this week",
    }


def tokenize_phrases(texts: Iterable[str], min_len: int = 3) -> Counter:
    counter: Counter[str] = Counter()
    for text in texts:
        lowered = re.sub(r"[^a-z0-9\s]", " ", text.lower())
        tokens = [t for t in lowered.split() if len(t) >= min_len and t not in STOPWORDS]
        for token in tokens:
            counter[token] += 1
        for i in range(len(tokens) - 1):
            phrase = f"{tokens[i]} {tokens[i+1]}"
            if all(part not in STOPWORDS for part in phrase.split()):
                counter[phrase] += 1
    return counter


def top_items(counter: Counter, limit: int = 12, min_count: int = 2) -> list[tuple[str, int]]:
    return [(k, v) for k, v in counter.most_common() if v >= min_count][:limit]


def normalize_question_text(text: str) -> str:
    lowered = text.lower()
    return re.sub(r"\s+", " ", lowered).strip()


def classify_row(question_text: str) -> str:
    q = normalize_question_text(question_text)
    if "what is one thing you learned" in q:
        return "learned"
    if "what is one question you have" in q or "what did you struggle" in q:
        return "struggled"
    if "what is one thing you'd like to learn" in q or "what do you want to learn" in q:
        return "future"
    if "how difficult" in q and "1-10" in q or "scale of 1-10" in q:
        return "difficulty"
    return "other"


def extract_difficulty_value(row: pd.Series) -> float | None:
    # In the sample dataset, the numeric difficulty rating is in Answer Match.
    candidates = [row.get("Answer"), row.get("Answer Match"), row.get("Difficulty")]
    for value in candidates:
        if pd.isna(value):
            continue
        try:
            numeric = float(value)
        except Exception:
            continue
        if 1 <= numeric <= 10:
            return numeric
    return None


def derive_label(csv_path: Path, df: pd.DataFrame) -> str:
    stem = csv_path.stem
    for col in ("Attempt End", "Attempt Start"):
        if col in df.columns:
            parsed = pd.to_datetime(df[col], errors="coerce")
            parsed = parsed.dropna()
            if not parsed.empty:
                return parsed.max().strftime("%Y-%m-%d")
    return stem


def load_week(csv_path: Path) -> WeekBundle:
    df = pd.read_csv(csv_path)
    required_cols = {"Q Text", "Answer"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"{csv_path.name} is missing required columns: {sorted(missing)}")

    learned: list[str] = []
    struggled: list[str] = []
    future: list[str] = []
    difficulty_ratings: list[float] = []

    for _, row in df.iterrows():
        q_type = classify_row(clean_text(row.get("Q Text", "")))
        answer = clean_text(row.get("Answer", ""))

        if q_type in {"learned", "struggled", "future"}:
            if not is_nonresponse(answer):
                if q_type == "learned":
                    learned.append(answer)
                elif q_type == "struggled":
                    struggled.append(answer)
                else:
                    future.append(answer)
        elif q_type == "difficulty":
            value = extract_difficulty_value(row)
            if value is not None:
                difficulty_ratings.append(value)

    label = derive_label(csv_path, df)

    return WeekBundle(
        label=label,
        source_file=csv_path.name,
        learned=learned,
        struggled=struggled,
        future=future,
        difficulty_ratings=difficulty_ratings,
    )


def deterministic_summary(bundle: WeekBundle) -> dict:
    learned_counts = top_items(tokenize_phrases(bundle.learned))
    struggled_counts = top_items(tokenize_phrases(bundle.struggled))
    future_counts = top_items(tokenize_phrases(bundle.future))

    difficulty = {
        "count": len(bundle.difficulty_ratings),
        "mean": round(mean(bundle.difficulty_ratings), 2) if bundle.difficulty_ratings else None,
        "median": round(median(bundle.difficulty_ratings), 2) if bundle.difficulty_ratings else None,
        "min": min(bundle.difficulty_ratings) if bundle.difficulty_ratings else None,
        "max": max(bundle.difficulty_ratings) if bundle.difficulty_ratings else None,
    }

    overlap = sorted(
        set(item for item, _ in learned_counts[:10]).intersection(item for item, _ in struggled_counts[:10])
    )

    return {
        "week_label": bundle.label,
        "source_file": bundle.source_file,
        "response_counts": {
            "learned": len(bundle.learned),
            "struggled": len(bundle.struggled),
            "future": len(bundle.future),
            "difficulty_ratings": len(bundle.difficulty_ratings),
        },
        "difficulty_summary": difficulty,
        "top_learned_terms": [{"term": k, "count": v} for k, v in learned_counts],
        "top_struggled_terms": [{"term": k, "count": v} for k, v in struggled_counts],
        "top_future_terms": [{"term": k, "count": v} for k, v in future_counts],
        "overlap_terms": overlap,
        "sample_reflections": {
            "learned": bundle.learned[:12],
            "struggled": bundle.struggled[:12],
            "future": bundle.future[:12],
        }
    }


def build_openai_prompt(metrics: dict) -> str:
    return (
        "You are helping a university computer science instructor interpret anonymous weekly reflection data.\n\n"
        "Important constraints:\n"
        "- These are completion-grade reflections, not correctness-based assessments.\n"
        "- Focus on perceived learning, perceived struggle, and future interests.\n"
        "- Use only the supplied data. Do not invent counts or quote students unless paraphrasing themes.\n"
        "- Prefer pedagogically actionable groupings over generic summaries.\n\n"
        "Analyze the following JSON payload and return structured insights.\n\n"
        f"{json.dumps(metrics, ensure_ascii=False, indent=2)}"
    )


def call_openai(metrics: dict) -> dict | None:
    if not ENABLE_OPENAI_SUMMARY:
        return None
    if OpenAI is None:
        raise RuntimeError("openai package is not installed, but ENABLE_OPENAI_SUMMARY=true.")
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set, but ENABLE_OPENAI_SUMMARY=true.")

    client = OpenAI()
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=build_openai_prompt(metrics),
        text={
            "format": {
                "type": "json_schema",
                "name": REFLECTION_SCHEMA["name"],
                "schema": REFLECTION_SCHEMA["schema"],
                "strict": True,
            }
        },
    )

    raw = response.output_text
    return json.loads(raw)


def render_markdown(metrics: dict, ai_summary: dict | None) -> str:
    lines: list[str] = []
    lines.append(f"# Exit Ticket Reflection Report — {metrics['week_label']}")
    lines.append("")
    lines.append(f"- **Source file:** `{metrics['source_file']}`")
    lines.append(f"- **Learned responses:** {metrics['response_counts']['learned']}")
    lines.append(f"- **Struggle/question responses:** {metrics['response_counts']['struggled']}")
    lines.append(f"- **Future-interest responses:** {metrics['response_counts']['future']}")
    lines.append(f"- **Difficulty ratings:** {metrics['response_counts']['difficulty_ratings']}")
    lines.append("")

    diff = metrics["difficulty_summary"]
    if diff["count"]:
        lines.append("## Course Difficulty Snapshot")
        lines.append("")
        lines.append(f"- **Mean difficulty:** {diff['mean']}/10")
        lines.append(f"- **Median difficulty:** {diff['median']}/10")
        lines.append(f"- **Range:** {diff['min']}–{diff['max']}")
        lines.append("")

    def add_term_section(title: str, key: str):
        lines.append(f"## {title}")
        lines.append("")
        items = metrics.get(key, [])
        if not items:
            lines.append("_No repeated terms surfaced above the minimum threshold._")
            lines.append("")
            return
        for item in items[:10]:
            lines.append(f"- **{item['term']}** — {item['count']}")
        lines.append("")

    add_term_section("Repeated themes in “Learned” responses", "top_learned_terms")
    add_term_section("Repeated themes in “Struggled / Questions” responses", "top_struggled_terms")
    add_term_section("Repeated themes in “Want to Learn” responses", "top_future_terms")

    if metrics.get("overlap_terms"):
        lines.append("## Overlap between “Learned” and “Struggled”")
        lines.append("")
        for term in metrics["overlap_terms"]:
            lines.append(f"- {term}")
        lines.append("")

    if ai_summary:
        lines.append("## Semantic Teaching Insights")
        lines.append("")
        lines.append(ai_summary["short_instructor_summary"])
        lines.append("")

        for heading, key in [
            ("Top learned concepts", "top_learned_concepts"),
            ("Top struggle clusters", "top_struggle_clusters"),
            ("Future interest clusters", "future_interest_clusters"),
            ("Mismatches", "mismatches"),
            ("Teaching adjustments", "teaching_adjustments"),
            ("Suggested follow-up exit-ticket questions", "followup_exit_ticket_questions"),
        ]:
            lines.append(f"### {heading}")
            lines.append("")
            for item in ai_summary.get(key, []):
                lines.append(f"- {item}")
            lines.append("")
    else:
        lines.append("## Semantic Teaching Insights")
        lines.append("")
        lines.append("_OpenAI summary disabled. Set `ENABLE_OPENAI_SUMMARY=true` and `OPENAI_API_KEY` to generate semantic clustering and teaching recommendations._")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def write_outputs(bundle: WeekBundle, metrics: dict, ai_summary: dict | None) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    latest_json = REPORTS_DIR / "latest_metrics.json"
    latest_md = REPORTS_DIR / "latest_report.md"
    dated_json = REPORTS_DIR / f"{bundle.label}_metrics.json"
    dated_md = REPORTS_DIR / f"{bundle.label}_report.md"

    payload = {"metrics": metrics, "ai_summary": ai_summary}
    latest_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    dated_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    md = render_markdown(metrics, ai_summary)
    latest_md.write_text(md, encoding="utf-8")
    dated_md.write_text(md, encoding="utf-8")


def write_trend_csv(all_weeks: list[WeekBundle]) -> None:
    rows = []
    for bundle in sorted(all_weeks, key=lambda x: x.label):
        rows.append({
            "week_label": bundle.label,
            "source_file": bundle.source_file,
            "learned_count": len(bundle.learned),
            "struggled_count": len(bundle.struggled),
            "future_count": len(bundle.future),
            "difficulty_count": len(bundle.difficulty_ratings),
            "difficulty_mean": round(mean(bundle.difficulty_ratings), 2) if bundle.difficulty_ratings else None,
            "difficulty_median": round(median(bundle.difficulty_ratings), 2) if bundle.difficulty_ratings else None,
        })
    if rows:
        pd.DataFrame(rows).to_csv(REPORTS_DIR / "trend_summary.csv", index=False)


def main() -> None:
    csv_files = sorted(DATA_DIR.glob("*.csv"))
    if not csv_files:
        raise SystemExit(f"No CSV files found in {DATA_DIR}")

    bundles = [load_week(path) for path in csv_files]
    latest = max(bundles, key=lambda x: x.label)

    metrics = deterministic_summary(latest)
    ai_summary = call_openai(metrics)
    write_outputs(latest, metrics, ai_summary)
    write_trend_csv(bundles)

    print(f"Analyzed {latest.source_file} as week {latest.label}")
    print(f"Reports written to {REPORTS_DIR}")


if __name__ == "__main__":
    main()
