# Exit Ticket Reflection Report — 2026-04-25

- **Source file:** `Week 14 Exit Ticket - CSCI 1260.csv`
- **Learned responses:** 14
- **Struggle/question responses:** 11
- **Future-interest responses:** 12
- **Difficulty ratings:** 14

## Course Difficulty Snapshot

- **Mean difficulty:** 6.75/10
- **Median difficulty:** 6.0/10
- **Range:** 5.0–10.0

## Repeated themes in “Learned” responses

- **testing** — 8
- **test** — 5
- **debugging** — 4
- **use** — 3
- **program** — 3
- **different** — 2

## Repeated themes in “Struggled / Questions” responses

- **not** — 3
- **using** — 3
- **code** — 3
- **testing** — 2
- **don** — 2
- **any** — 2

## Repeated themes in “Want to Learn” responses

- **project** — 3
- **using** — 2
- **programming** — 2
- **unity** — 2
- **different** — 2
- **types** — 2

## Overlap between “Learned” and “Struggled”

- testing

## Semantic Teaching Insights

This week’s reflections show strong perceived learning around testing/unit testing and debugging, especially with MSTest and Visual Studio tools. The main instructional gap is not whether students saw the tools, but whether they know how to choose among them and apply them in a real workflow: how thorough tests should be, when MSTest fits into development, and how debugging differs from logging or exception handling. Future interests point toward transfer beyond the current stack, especially Unity, other languages, and broader project contexts. A high-value next step would be a comparison-based, end-to-end example that connects unit tests, debugging, and runtime error/reporting practices in one realistic scenario.

### Top learned concepts

- Testing and unit testing were the clearest perceived takeaways, especially using MSTest to check methods, edge cases, and smaller chunks of larger programs.
- Debugging was a second major learning theme, with students emphasizing practical use of debugger tools to find errors more efficiently.
- Several students specifically connected learning to Visual Studio or Windows/VS tooling rather than only abstract concepts, suggesting the lesson landed as applied workflow knowledge.
- A smaller non-content theme was awareness of course logistics and final-test timing, which appeared among what students reported learning.

### Top struggle clusters

- Applying unit testing in practice: students seem uncertain about what level of thoroughness is expected, when to write MSTest tests, and how unit tests fit into a larger codebase workflow.
- Debugging strategy questions: some students learned the tools but still want guidance on the most efficient way to debug and how to generalize debugging across environments.
- Error handling, logging, and runtime diagnostics: multiple reflections point to confusion about exception handling versus logging, and about surfacing errors that may not appear clearly in a console or IDE.
- Transfer beyond the current stack: students raised questions about using these ideas with other frameworks, other IDEs, game projects, and non-console contexts.
- Low-articulation or no-struggle responses are common this week, so the struggle data likely underrepresents confusion compared with actual uncertainty.

### Future interest clusters

- Cross-platform and cross-language tooling: interest in debugging tools for Python, C++, and different programming languages suggests students want concepts transferred beyond the current C#/Visual Studio context.
- Project-oriented application: students want to use testing and debugging in realistic projects, especially final projects and broader software-development contexts.
- Unity/game-development extensions: several future interests connect course skills to Unity, including improving workflow and extending into assets such as textures and animations.
- Advanced software design/application topics: students expressed interest in interfaces, APIs, and how testing viability changes across different project types.
- More comprehensive testing practice: students want to learn how to push testing further, including broader coverage and checking more edge cases/corners of a project.

### Mismatches

- Students largely reported learning testing/debugging successfully, but the overlap term and struggle reflections show that testing remains both a takeaway and a source of uncertainty.
- The lesson appears to have succeeded at introducing tools, but some students still lack a decision framework for when to use unit tests, exception handling, logging, or debugger-based inspection.
- Future interests extend well beyond the current course stack, indicating students may understand the local tools but are now asking how portable these practices are to other languages, frameworks, and project types.
- A few reflections focus on course logistics or trust in whether reflections are read, which suggests some students may not see the exit ticket primarily as a space for technical reflection.

### Teaching adjustments

- Next class, provide a compact comparison table or mini-demo distinguishing debugging, unit testing, exception handling, and logging: what each is for, when to use it, and what kinds of problems each catches.
- Add one worked example that traces a method through the full workflow: write the method, identify edge cases, add MSTest cases, trigger a failure, debug it, then discuss whether exception handling or logging would also be appropriate.
- Give students a practical heuristic for test scope, such as a checklist for normal cases, edge cases, invalid inputs, and regression cases, to address uncertainty about how thorough tests need to be.
- Explicitly discuss transfer: spend a few minutes framing which ideas are universal (breakpoints, assertions, test cases, logs) versus tool-specific (MSTest, Visual Studio interface).
- Use a short example outside the current default context—such as Unity, Python, or a framework-based app—to validate student interest in applying these concepts beyond console-style assignments.
- Consider a brief reminder that reflections are read for instructional planning, since at least one response questioned that and another used the space for logistics rather than content.

### Suggested follow-up exit-ticket questions

- After this week, when would you choose unit testing instead of manual debugging, and why?
- What part of the testing workflow still feels most unclear: choosing test cases, writing MSTest syntax, interpreting failures, or deciding coverage?
- Can you explain the difference between debugging, exception handling, and logging in your own words?
- How confident do you feel applying this week's tools in a non-C# or non-Visual-Studio project? What transfer question do you still have?
- What is one realistic project context—course project, Unity game, API-based app, etc.—where you want to apply testing or debugging next?
