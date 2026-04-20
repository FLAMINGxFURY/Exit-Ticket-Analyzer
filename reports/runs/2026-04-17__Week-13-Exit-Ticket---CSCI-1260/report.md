# Exit Ticket Reflection Report — 2026-04-17

- **Source file:** `Week 13 Exit Ticket - CSCI 1260.csv`
- **Learned responses:** 15
- **Struggle/question responses:** 11
- **Future-interest responses:** 13
- **Difficulty ratings:** 16

## Course Difficulty Snapshot

- **Mean difficulty:** 6.25/10
- **Median difficulty:** 6.0/10
- **Range:** 1.0–10.0

## Repeated themes in “Learned” responses

- **handling** — 7
- **exception** — 5
- **exception handling** — 5
- **catch** — 3
- **try** — 3
- **error** — 3
- **exceptions** — 2
- **handle** — 2
- **use** — 2
- **streamreader** — 2

## Repeated themes in “Struggled / Questions” responses

- **exception** — 3
- **exceptions** — 2
- **file** — 2
- **data** — 2
- **does** — 2
- **using** — 2
- **possible** — 2
- **all** — 2
- **handling** — 2
- **exception handling** — 2

## Repeated themes in “Want to Learn” responses

- **use** — 3
- **error** — 2
- **languages** — 2
- **different** — 2
- **make** — 2

## Overlap between “Learned” and “Struggled”

- exception
- exception handling
- exceptions
- handling

## Semantic Teaching Insights

Students largely perceived exception handling as the main thing they learned, especially try/catch in C#, with file I/O and StreamReader as a secondary theme. Struggles were less about remembering syntax and more about judgment and transfer: which exceptions matter, whether everything can be handled, how to organize error-handling code, and how file/data practices work in real applications. Future interest points strongly toward scaled-up, practical contexts such as web/UI error handling, games/save data, and cross-language comparisons. A productive next step would be to keep the syntax review brief and spend more time on decision-making, worked file-I/O examples, and real-world application patterns.

### Top learned concepts

- Exception handling as the central takeaway, especially the try/catch pattern in C#.
- Basic error-handling goals: preventing crashes, showing user-friendly messages, and continuing execution after errors.
- File and text-input topics through StreamReader and file parsing.
- Program data persistence and file I/O, including saving data and reading/writing files.
- Some students connected the week to debugging, suggesting they saw exception handling as part of troubleshooting workflows.

### Top struggle clusters

- Applying exception handling beyond the syntax: students asked about which exception types matter, whether all exceptions can be handled, and how exception-handling code should be organized.
- File/data management questions rather than raw syntax issues: file size limits, hidden files/data, configuration storage, and saving data appropriately.
- Transfer to broader software contexts: students want to know how these classes/tools apply outside simple text-based examples and in larger applications.
- Need for more worked examples: at least one clear request for additional exception-handling examples, alongside several exploratory questions that suggest partial understanding rather than confusion.
- A subset reported little or no struggle, so the class appears mixed: many grasped the basics, while others are ready for design-level questions.

### Future interest clusters

- Scaling error handling up: students want to see what exception handling looks like in larger systems and UI/web contexts such as Blazor.
- Cross-language and cross-platform transfer: interest in C++, other programming languages, and analogous tools/classes in different environments.
- Game/project applications of file I/O: save data, savepoints, and persistent state in programs or games.
- Broader CS topics adjacent to the course: search algorithms, hardware-oriented topics, and vector/array-like structures.
- Concrete consequences and case studies: interest in examples where poor exception handling caused larger software problems.

### Mismatches

- Exception handling appeared as both the dominant learned concept and the dominant struggle area, indicating students often understand the basic idea while still lacking confidence in edge cases and design decisions.
- Instruction seems to have centered on C# try/catch and StreamReader, while several student questions moved quickly to architecture, storage strategy, and real-world application; this suggests curiosity is extending beyond the current level of abstraction.
- Some future-interest responses were only loosely tied to the week's material, so not all students are using the reflection prompt to identify next steps within the current topic.
- Perceived difficulty was moderate overall (mean 6.25, median 6), which fits a week where fundamentals landed for many students but deeper implications still felt uncertain.

### Teaching adjustments

- Differentiate between 'basic syntax mastery' and 'exception design judgment' in the next class: briefly review try/catch, then explicitly address when to catch specific exceptions, when not to catch everything, and how to structure handlers responsibly.
- Add a small comparison table or mini-lesson on common exception-handling decisions: generic vs specific catches, user-facing messages vs debugging details, and local handling vs centralized handling.
- Use one or two authentic file-I/O examples that connect to student interests, such as save files, config files, or reading structured text data.
- Provide a worked example that combines StreamReader/file parsing with exception handling, so students can see the interaction between file access, parsing failures, and user feedback.
- Include at least one 'larger-scale' example, even if simplified, showing how exceptions surface through a UI or web page flow.
- Reserve a few minutes for 'what this looks like outside toy examples,' since several questions point to transfer into games, websites, and non-text applications.

### Suggested follow-up exit-ticket questions

- When writing a C# program, how confident are you in deciding which exceptions to catch versus letting them propagate?
- What is still unclear about exception handling: syntax, choosing exception types, organizing code, or deciding what message to show users?
- How confident are you using file I/O together with exception handling in a small program?
- Which real-world example would help most next: save files in games, config files, web/UI error handling, or debugging workflows?
- After this week, do exceptions feel mostly like a syntax topic or a program design topic to you, and why?
