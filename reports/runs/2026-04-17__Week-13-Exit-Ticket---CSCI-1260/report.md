# Exit Ticket Reflection Report — 2026-04-17

- **Source file:** `Week 13 Exit Ticket - CSCI 1260 .csv`
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

## Repeated themes in “Struggled / Questions” responses

- **exception** — 3
- **exceptions** — 2
- **file** — 2
- **data** — 2
- **does** — 2
- **using** — 2

## Repeated themes in “Want to Learn” responses

- **use** — 3
- **error** — 2
- **languages** — 2
- **different** — 2
- **make** — 2

## Overlap between “Learned” and “Struggled”

- exception

## Semantic Teaching Insights

Students largely perceived that they learned the basics of exception handling, especially try/catch in C#, with a secondary learning theme around file I/O and StreamReader. The main struggles were not basic syntax so much as application and design: how many exceptions to handle, which types matter, where error-handling code should live, and how file storage choices work in practice. Future-interest responses reinforce this pattern, with students wanting larger-scale, more realistic examples involving web pages, save data, and cross-language transfer. Difficulty appears moderate overall, and the clearest instructional opportunity is to move from mechanics to design-oriented examples and authentic use cases.

### Top learned concepts

- Exception handling in C#, especially try/catch and basic error-handling flow, was the clearest learning theme.
- A smaller cluster reported learning file I/O concepts, especially StreamReader, parsing data from files, and saving/input-output with files.
- Some students framed the week as learning debugging-oriented practices and writing more user-friendly error behavior.

### Top struggle clusters

- Exceptions were both learned and still uncertain: students asked about handling all exceptions, choosing exception types, and whether exception logic should be centralized or kept local.
- File/data persistence questions remain open, including file size limits, hiding data from users, and whether configuration files are the right storage approach.
- Several responses suggest students want broader application context rather than syntax help alone, such as non-text uses of the classes covered, larger-scale error handling, and more examples.

### Future interest clusters

- Students want to extend this week's topics into authentic applications: web UI error messages, save data/save points, and large-scale exception handling.
- There is continued interest in transferring ideas across contexts, including other languages and similar classes used for different purposes.
- A smaller exploratory cluster points beyond this week to search algorithms, game development, hardware-focused topics, and vector arrays.

### Mismatches

- Exception handling appears in both learned and struggled responses, indicating many students grasped the basic syntax but are unsure about design decisions and edge cases.
- Top learned terms emphasize try/catch mechanics, while struggle and future responses emphasize when, why, and how broadly to apply them in real programs.
- File handling is not dominant in the learned term list overall, but student comments show persistent curiosity about storage, configuration, and save data applications.

### Teaching adjustments

- Differentiate between 'basic exception syntax' and 'exception design choices' in the next class: when to catch specific exceptions, when not to catch everything, and what makes an error message useful.
- Add 1-2 worked examples that connect exceptions with file I/O and persistence, since students are asking about configs, save data, and file-based applications.
- Include a brief discussion of scope and architecture: whether exception handling belongs inline, in helper methods, or in higher-level program layers.
- Provide one 'real-world scale' example, such as error handling in a web page or larger application, to answer interest in what this looks like beyond toy programs.
- Consider a short FAQ or mini-lecture on data storage decisions: plain text files, config files, and what 'hidden' or protected data means at the user/file-system level.
- Use debugging support alongside exception handling examples, since at least some students are connecting the two topics.

### Suggested follow-up exit-ticket questions

- When writing try/catch blocks, what part feels least clear: choosing what to catch, deciding where to catch it, or deciding what message/action should follow?
- After this week, how confident do you feel using file I/O for save data or configuration files, and what specific scenario still feels unclear?
- Would a worked example from a console app, a game/save system, or a web page be most helpful for seeing exception handling in context?
- What is one design question you still have about exceptions that goes beyond syntax?
