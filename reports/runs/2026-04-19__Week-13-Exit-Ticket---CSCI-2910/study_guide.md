# Study Guide for 2026-04-19: OS, Virtualization, Docker, Testing, and CI

This week introduced several connected infrastructure and software engineering ideas: operating systems, virtualization and hypervisors, Docker/containers, unit testing, and CI workflows. Many students could identify the main ideas, but several reflections showed that the harder part is telling similar tools apart, understanding why they matter, and applying them in realistic projects. Before class, focus on building a clear big-picture map and reviewing how these topics connect in a development workflow.

## Key takeaways to review

- Operating systems manage system resources for applications.
- Virtualization and hypervisors relate hardware, operating systems, and resource allocation.
- Hyper-V and other virtualization tools are examples students encountered this week.
- Containers package what an application needs to run.
- Docker is a key example of container-based workflow mentioned by many students.
- Unit tests help check whether parts of a program are working correctly.
- CI connects code changes and automated testing in a development workflow.
- These topics are related: system setup, packaging, testing, and code integration all support building and maintaining software.

## Common sticking points

- Keeping the boundaries clear between hypervisors, virtualization, VMs, and containers.
- Understanding why Docker is useful beyond just knowing how to run it.
- Deciding what unit tests to write for real applications, not just small examples.
- Knowing how testing ideas transfer across languages or project types.
- Figuring out how to test more complex components like APIs, databases, or bots.
- Understanding GitHub/CI workflows when multiple developers push changes.
- Seeing the 'big picture' of how OS concepts, containers, testing, and CI fit together.

## Practice prompts

- Make a simple comparison chart: operating system vs hypervisor vs VM vs container. For each, write what role it plays.
- In one or two sentences, explain why a developer might use Docker in a real project.
- Think of a recent program you wrote. List 2-3 parts that could be unit tested.
- For one feature in a server-side project, describe what you would want to verify with tests.
- Write a short workflow summary: code change -> push to GitHub -> tests run in CI -> next step.
- Identify one place where team workflows could fail even if individual code changes seem correct.
- If the topics feel disconnected, try grouping them by purpose: system resources, environment setup, testing, and collaboration.

## Self-check questions

- Can I explain the difference between a VM and a container at a high level?
- Can I explain what a hypervisor does in relation to hardware and operating systems?
- Can I describe one practical reason containers are useful?
- Can I give an example of what a unit test checks?
- Do I understand that knowing test syntax is different from knowing what should be tested?
- Can I describe what CI does after code is pushed?
- Do I know which part is least clear to me right now: virtualization concepts, Docker, testing strategy, or team workflow?

## Before next class

- Review your notes and identify one distinction that still feels blurry, especially among hypervisors, VMs, containers, CI, and CD.
- Bring one example from a current or past project of something you are unsure how to test.
- If possible, revisit any Docker or virtualization demo/material and focus on what problem the tool solves.
- Think about how a team project on GitHub might need more than just passing tests, such as coordination and review.
- Prepare one question about the big-picture connection between systems topics and software development workflow.

## Why this guide was generated

Students perceived substantial learning this week around operating systems, virtualization/hypervisors, Docker, and unit testing/CI. The main struggles were not simple recall problems but application and differentiation problems: how similar technologies relate, what tests to write in realistic systems, and how CI/GitHub workflows behave in collaborative settings. Future interest strongly points toward more Docker, Linux/OS comparison, deeper testing practice, and extending CI into CD/deployment. Instructionally, the clearest opportunity is to unify these topics with a single end-to-end project and explicit comparison frameworks so students can connect the mechanics to the larger software engineering picture.
