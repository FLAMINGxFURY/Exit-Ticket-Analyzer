# CSCI 2910 Study Guide – Week of 2026-04-19

This week introduced several connected ideas: virtualization and hypervisors, Docker/containers, operating systems, CI, and unit testing. Many students recognized the main terms, but the biggest challenge was seeing how the pieces fit together in real projects. Use this guide to review the vocabulary, clarify key comparisons, and practice applying the ideas to software development workflows.

## Key takeaways to review

- Virtualization and hypervisors: review how hardware, operating systems, and virtualized resources relate.
- Docker/containers: remember that containers package what an application needs to run.
- Operating systems context: connect course topics to Windows, Linux, and cross-platform development environments.
- CI and testing: review how automated tests fit into a development workflow.
- Unit testing: focus not just on writing tests, but on deciding what parts of a program should be tested first.
- Big picture: these topics are related through deployment, reproducibility, collaboration, and reliable software delivery.

## Common sticking points

- Telling apart containers, virtual machines, hypervisors, and operating systems.
- Understanding platform-specific ideas such as Hyper-V, virtual switches/networking, and checkpoints.
- Knowing what makes Docker important or when it is worth using.
- Choosing useful unit tests for web apps, APIs, bots, and other server-side projects.
- Understanding how testing ideas transfer across languages and tools like C#, Python, APIs, and databases/SQL contexts without assuming the exact syntax is the same everywhere.

## Practice prompts

- Explain, in your own words, the difference between a container, a VM, a hypervisor, and an operating system.
- Write a 3–4 sentence answer to: Why might a developer use Docker in a project?
- Choose one project component you know well and list 3 things that could be unit tested.
- Describe what CI does after code is pushed to a repository.
- Think through this question: if two developers each make changes that work separately, what additional workflow steps besides tests might help protect the main branch?
- Write down one thing that belongs to the 'big picture' of modern development: environment setup, testing, collaboration, packaging, or deployment—and explain how it connects to the others.

## Self-check questions

- Can I clearly distinguish Docker from a VM without using the terms as if they mean the same thing?
- Can I describe what a hypervisor does at a high level?
- Do I understand that learning unit testing includes both how to write tests and how to choose what to test?
- Can I explain one way CI helps a team, and one thing CI alone does not solve?
- Can I name one part of the overall workflow that still feels unclear so I can ask about it next class?

## Before next class

- Review your notes on virtualization, hypervisors, containers, and CI as one connected topic rather than isolated terms.
- Make a one-page comparison sheet: container vs VM vs hypervisor vs OS.
- Pick one current or past coding project and identify 2–3 unit tests you would add first.
- If you use GitHub, trace the path from 'write code' to 'push' to 'checks run' to 'merge' and note where confusion starts.
- Come to class with one specific question about either testing in real projects, Docker/Linux environments, or team collaboration workflows.

## Why this guide was generated

Students perceived meaningful learning in virtualization, hypervisors, Docker, CI, and unit testing, but their questions show that understanding is still mostly introductory. The strongest struggle pattern is not lack of exposure but difficulty distinguishing related concepts and applying them in real project settings. Testing is a key example: students say they learned unit testing, yet they still want guidance on what to test, how testing transfers across languages/tools, and how to test more complex systems. A second major need is workflow coherence: students want the big picture of how Docker, GitHub, CI, and multi-developer collaboration fit together in authentic software practice. The most actionable next step is to move from topic introduction to structured comparisons and integrated demonstrations.
