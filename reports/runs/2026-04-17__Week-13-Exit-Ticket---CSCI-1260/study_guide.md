# CSCI 1260 Study Guide — Week of 2026-04-17

This week’s main review topic is exception handling in C#, especially basic try/catch flow and how it connects to debugging, user-friendly errors, and file I/O. Many students felt okay with the basic syntax, but still want clarification on design decisions: what to catch, whether to catch everything, where exception-handling code should go, and how file-based storage works in realistic programs. Before next class, focus on moving from 'I can write a try/catch' to 'I can explain why this catch belongs here and what should happen next.'

## Key takeaways to review

- Exception handling was the clearest core concept from the week: try/catch, handling errors, and keeping programs from crashing unexpectedly.
- Basic error handling is connected to user experience: a program can respond with a clearer message instead of failing silently or stopping abruptly.
- File I/O also appeared as an important secondary topic, especially StreamReader, parsing data from files, and saving/input/output with files.
- Debugging and exception handling are related but not identical: exceptions help manage runtime problems, while debugging helps you investigate why they happen.
- The main next step is not just syntax review, but understanding design choices in realistic programs.

## Common sticking points

- Knowing the syntax of try/catch but not knowing which exception types matter in practice.
- Wondering whether it is a good idea to handle all exceptions or only specific ones.
- Uncertainty about where exception-handling code should live: directly in one method, in helper methods, or in a larger program layer.
- Wanting more examples that combine exception handling with file reading, save data, or configuration files.
- Questions about file/data usage in real programs, including storage choices and what it means for data to be hidden or protected from users.

## Practice prompts

- In your own words, explain what a try block does and what a catch block does.
- Describe one reason a program might choose to catch a specific exception instead of catching everything broadly.
- Write a short plan for how a program should respond if reading a file fails: what should the user see, and what should the program do next?
- Think of a small app, game, or webpage. Where might error handling happen in that program, and why there?
- Compare these goals: prevent crashes, show useful messages, and keep code organized. How might exception-handling choices affect each one?

## Self-check questions

- Can I explain the difference between learning try/catch syntax and making good exception-handling design decisions?
- Do I know at least one reason not to catch every exception in the same way?
- Can I describe how exception handling and debugging support each other?
- Can I give a realistic example of exception handling with file I/O or save data?
- If I saw exception-handling code in a larger project, could I ask whether it belongs locally or at a higher level?

## Before next class

- Review your notes on try/catch and exception handling in C#.
- Revisit any examples involving StreamReader, file input/output, parsing data, or saving data.
- Practice explaining exception behavior in plain language, not just code syntax.
- Prepare one question about design, such as what to catch, where to catch it, or how to structure error-handling code.
- If helpful, sketch a tiny real-world scenario: loading a config file, reading save data, or showing an error message to a user. Be ready to discuss how exceptions should be handled there.

## Why this guide was generated

Students largely perceived that they learned the basics of exception handling, especially try/catch in C#, with a secondary learning theme around file I/O and StreamReader. The main struggles were not basic syntax so much as application and design: how many exceptions to handle, which types matter, where error-handling code should live, and how file storage choices work in practice. Future-interest responses reinforce this pattern, with students wanting larger-scale, more realistic examples involving web pages, save data, and cross-language transfer. Difficulty appears moderate overall, and the clearest instructional opportunity is to move from mechanics to design-oriented examples and authentic use cases.
