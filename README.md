# Exit Ticket Reflection Automation Starter

This starter kit watches for new CSV files in `data/exit_tickets/` and generates:

- `reports/latest_report.md`
- `reports/latest_metrics.json`
- `reports/trend_summary.csv`

It is designed for **completion-grade student reflections**, not correctness-based assessment.

## Assumptions based on your sample file

The script expects a D2L-style CSV with these columns:

- `Q Text`
- `Answer`
- `Answer Match` for the numeric 1–10 difficulty rating

The reflection prompts in the sample file map like this:

- **Learned:** `What is one thing you learned this week?`
- **Struggled / Questions:** `What is one question you have about the content we have covered so far?`
- **Future:** `What is one thing you'd like to learn in the future?`
- **Difficulty:** `On a scale of 1-10, how difficult has this class been so far?`

If your wording changes later, update `classify_row()` in `scripts/analyze_exit_tickets.py`.

## Repo layout

```text
.
├── .github/workflows/analyze-exit-tickets.yml
├── data/exit_tickets/
├── reports/
├── requirements.txt
└── scripts/analyze_exit_tickets.py
```

## Setup

1. Create a GitHub repo.
2. Copy these files into it.
3. Add your CSV exports to `data/exit_tickets/`.
4. In GitHub, add a repository secret named `OPENAI_API_KEY`.
5. Push to GitHub.

The workflow runs automatically when a new CSV is pushed to `data/exit_tickets/`.

## What the analysis does

### Deterministic metrics
The Python script always computes:
- response counts by reflection type
- mean / median difficulty
- repeated terms and repeated short phrases
- overlap terms between “learned” and “struggled”

### Semantic teaching summary
If `ENABLE_OPENAI_SUMMARY=true`, the script also asks OpenAI to produce:
- top learned concepts
- top struggle clusters
- future interest clusters
- mismatches
- teaching adjustments
- suggested follow-up exit-ticket questions

## Notes

- This starter treats **each CSV as one week/run**.
- The latest file by inferred date becomes `latest_report.md`.
- A cross-week `trend_summary.csv` is also generated.
- Non-responses like `I don't know`, `N/A`, and blank entries are filtered out before semantic analysis.

## Suggestions for your next iteration

- track trends by course section
- compare sections if you export separate files
- preserve a course-specific concept taxonomy
- post the Markdown report to Discord/Slack via webhook
- generate a “next class adjustments” checklist automatically
