# Study Guide for 2026-04-17: Exception Handling, File I/O, and Next-Step Practice

This week’s main review topic is exception handling in C#, especially the basic try/catch pattern. Many students also connected the week to file I/O, StreamReader, parsing data from files, saving data, and debugging. Overall difficulty felt moderate: many students understood the core idea, but several still want clarification on how exception handling works in bigger programs, how to choose what to catch, and how file/data features apply in real projects. Before class, focus on reviewing the basics and preparing to ask questions about design choices rather than just syntax.

## Key takeaways to review

- Know the purpose of exception handling: preventing crashes, responding to errors, and giving user-friendly feedback.
- Review the basic try/catch structure in C# and what each part is meant to do.
- Connect exception handling to debugging: exceptions are not just syntax, but part of finding and managing problems in programs.
- Review how StreamReader and file parsing fit into file input tasks.
- Review the idea of saving and loading data with files.
- Be ready to think about exception handling as a decision-making topic, not only a code-format topic.

## Common sticking points

- Understanding exception handling in principle, but not yet feeling confident about edge cases or design choices.
- Knowing that exceptions can be caught, but being unsure which exception types matter most.
- Wondering whether all exceptions should or even can be handled the same way.
- Deciding how to organize exception-handling code without making programs messy.
- Applying file I/O ideas beyond simple text examples.
- Questions about file/data practices in real software, such as config files, save data, hidden data, and large files.
- Wanting more worked examples that combine file access, parsing, and exception handling together.
- Transferring this week’s ideas to larger systems such as games, websites, or UI-based apps.

## Practice prompts

- Explain in your own words what problem try/catch is meant to solve.
- Write or trace a very small example where a program reads from a file and something goes wrong.
- Identify the difference between a user-facing error message and information that is mainly useful for debugging.
- Take a simple file-reading example and ask: what errors could happen here?
- Think of one small program feature, like save data or config loading, where file I/O and exception handling would need to work together.
- Compare these questions: What can go wrong? What should the program do? What should the user see?
- Prepare one example of a situation where catching every exception might not be the best design choice.
- If you worked with StreamReader this week, review the steps of opening, reading, and parsing data, then consider where errors might occur in that process.

## Self-check questions

- Can I explain what an exception is without just naming try/catch syntax?
- Do I understand why a program might handle an error instead of just crashing?
- Can I describe the role of try and the role of catch?
- Can I name a few kinds of problems that might happen during file reading or file parsing?
- Do I feel confident using file I/O together with exception handling in a small program?
- Am I more unsure about syntax, or about choosing the right design decision?
- Can I think of how this topic might appear in a game, a save system, or a web/UI setting?
- Do I know at least one question I still have about exception handling in larger programs?

## Before next class

- Quickly review your notes on try/catch in C#.
- Review any examples involving StreamReader, file parsing, saving data, or reading/writing files.
- If basic syntax already makes sense, spend your review time on judgment questions: what to catch, what message to show, and where handling should happen.
- Bring one real-world application example you are curious about, such as save files, config files, or web/UI error handling.
- Write down one question about exception design or file/data management that you want clarified in class.
- Be ready for examples that connect this week’s basics to larger and more practical software contexts.

## Why this guide was generated

Students largely perceived exception handling as the main thing they learned, especially try/catch in C#, with file I/O and StreamReader as a secondary theme. Struggles were less about remembering syntax and more about judgment and transfer: which exceptions matter, whether everything can be handled, how to organize error-handling code, and how file/data practices work in real applications. Future interest points strongly toward scaled-up, practical contexts such as web/UI error handling, games/save data, and cross-language comparisons. A productive next step would be to keep the syntax review brief and spend more time on decision-making, worked file-I/O examples, and real-world application patterns.
