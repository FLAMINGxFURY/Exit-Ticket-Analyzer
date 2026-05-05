# Week 14 Study Guide: Testing, Debugging, and When to Use Each Tool

This week’s main review topics are unit testing, debugging, and related error-checking practices. Many students felt they learned the tools well—especially MSTest and Visual Studio debugging—but also want more clarity on when to use each approach, how thorough tests should be, and how these ideas transfer to larger projects, Unity, or other languages. Use this guide to review the big distinctions, practice thinking through workflow decisions, and prepare questions for class.

## Key takeaways to review

- Unit testing was a major takeaway: students especially noted using MSTest to test methods, smaller chunks of code, and edge cases.
- Debugging was another key theme: many students saw it as a practical way to find where and why errors happen more efficiently.
- Visual Studio tools mattered this week, not just the concepts in the abstract. Be ready to connect ideas to actual workflow.
- Testing and debugging are related but not the same: one common area to review is what each tool is for and when to choose it.
- A useful next step is thinking about a full workflow: write code, identify likely edge cases, test it, inspect failures, and debug when needed.
- Some students are already thinking ahead to applying these ideas in final projects, Unity, other IDEs, and other programming languages.

## Common sticking points

- How thorough should unit tests be for a method or block of code? Students seemed unsure what counts as enough coverage.
- When should you write MSTest tests in your workflow—before adding code to a larger project, while building, or after finding bugs?
- What is the difference between debugging, exception handling, and logging? These were not always clearly separated in student reflections.
- What is the most efficient way to debug, especially when you know tools exist but are unsure how to approach a problem systematically?
- How do these ideas transfer beyond the current class setup, such as Unity projects, Python IDEs, C++, or framework-based applications?

## Practice prompts

- In your own words, explain the difference between unit testing and debugging.
- Describe one situation where a unit test would be more useful than manually stepping through code.
- Describe one situation where debugging would be more useful than writing a new test first.
- Make a short checklist for testing a method: normal case, edge case, invalid input, and past bug/regression.
- Pick one tool or idea from this week that feels tool-specific (for example, MSTest or Visual Studio) and one that feels universal across languages.
- Think about your project work: where could testing help you catch mistakes earlier? Where could debugging save time?

## Example problems

- Suppose you wrote a method that calculates a result from input values. List 4 test cases you would want: one normal case, one edge case, one invalid input case, and one case based on a bug you already found.
- A test fails for one specific input but passes for others. What would you do next with the debugger to locate the issue?
- You see a program behave incorrectly during runtime, but there is no obvious console error. What kinds of information would you want to inspect or record to understand the problem?
- A larger project is working overall, but one helper method seems suspicious. Explain why unit testing that smaller method could be useful before checking the whole program manually.

## Practical examples

- If you are building a final project, unit tests can help verify small parts of your logic before those parts are connected to the whole project.
- If you are using Unity or another non-console environment, the exact tools may differ, but the core habits still matter: isolate a problem, define expected behavior, test likely edge cases, and inspect values while the program runs.
- If you are working in another language such as Python or C++, the specific debugger or test framework may change, but breakpoints, assertions, test cases, and logs are still useful ideas.
- If a bug only appears in a specific situation, that situation can become both a debugging target and a future regression test case.

## Self-check questions

- Can I clearly explain what unit testing is checking?
- Can I clearly explain what debugging is helping me investigate?
- Do I know at least a basic rule for choosing test cases, especially edge cases?
- Can I describe one difference between exception handling and logging, even if I still want clarification?
- Do I understand which ideas from this week are general software practices versus Visual Studio/MSTest-specific tools?
- Can I name one way I might apply this week’s material in my own project or a future class?

## Before next class

- Review your notes on MSTest, unit testing, and debugging tools.
- Write down one question you still have about test coverage, debugging strategy, exception handling, or logging.
- Take one method or small piece of code from past work and sketch possible test cases for it.
- Think of one bug you have seen before and ask: would testing, debugging, logging, or exception handling have helped most?
- If you are interested in transfer to Unity, Python, C++, or another environment, bring one concrete example question about how the ideas would carry over.

## Why this guide was generated

This week’s reflections show strong perceived learning around testing/unit testing and debugging, especially with MSTest and Visual Studio tools. The main instructional gap is not whether students saw the tools, but whether they know how to choose among them and apply them in a real workflow: how thorough tests should be, when MSTest fits into development, and how debugging differs from logging or exception handling. Future interests point toward transfer beyond the current stack, especially Unity, other languages, and broader project contexts. A high-value next step would be a comparison-based, end-to-end example that connects unit tests, debugging, and runtime error/reporting practices in one realistic scenario.
