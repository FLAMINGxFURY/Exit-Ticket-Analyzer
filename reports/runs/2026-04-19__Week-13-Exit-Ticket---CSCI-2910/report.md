# Exit Ticket Reflection Report — 2026-04-19

- **Source file:** `Week 13 Exit Ticket - CSCI 2910 .csv`
- **Learned responses:** 17
- **Struggle/question responses:** 11
- **Future-interest responses:** 12
- **Difficulty ratings:** 17

## Course Difficulty Snapshot

- **Mean difficulty:** 5.82/10
- **Median difficulty:** 6.0/10
- **Range:** 4.0–7.0

## Repeated themes in “Learned” responses

- **systems** — 6
- **operating** — 5
- **operating systems** — 5
- **unit** — 3
- **run** — 3
- **system** — 3

## Repeated themes in “Struggled / Questions” responses

- **tests** — 3
- **does** — 3
- **same** — 2
- **unit** — 2
- **different** — 2
- **unit tests** — 2

## Repeated themes in “Want to Learn” responses

- **docker** — 2
- **use** — 2
- **tests** — 2
- **work** — 2
- **trying** — 2
- **big** — 2

## Overlap between “Learned” and “Struggled”

- unit

## Semantic Teaching Insights

Students perceived meaningful learning in virtualization, hypervisors, Docker, CI, and unit testing, but their questions show that understanding is still mostly introductory. The strongest struggle pattern is not lack of exposure but difficulty distinguishing related concepts and applying them in real project settings. Testing is a key example: students say they learned unit testing, yet they still want guidance on what to test, how testing transfers across languages/tools, and how to test more complex systems. A second major need is workflow coherence: students want the big picture of how Docker, GitHub, CI, and multi-developer collaboration fit together in authentic software practice. The most actionable next step is to move from topic introduction to structured comparisons and integrated demonstrations.

### Top learned concepts

- Virtualization and hypervisors as core systems concepts, including how hardware, OSes, and resource management relate
- Docker/containers as application packaging and runtime environments
- CI and unit testing as parts of modern development workflow
- Operating systems and cross-system/platform context, including Windows and interest in Linux

### Top struggle clusters

- Distinguishing related infrastructure concepts: Docker vs VMs, virtualization vs Hyper-V specifics, and how virtual networking/checkpoints work
- Applying testing in practice: what unit tests to write, how testing differs across languages, and how to test bots/APIs/databases/web applications
- Understanding collaboration/CI at scale: GitHub pushing workflows, multiple developers, merge conflicts, branch protections, and what CI does or does not catch
- Connecting tools to purpose and scope: how important Docker is, what happens without a hypervisor, and fitting these topics into the bigger picture

### Future interest clusters

- More hands-on depth with Docker, virtualization, and Linux/alternative OS environments
- Broader and deeper testing coverage, especially for APIs, databases, and possibly SQL
- CI/CD beyond testing, especially deployment workflows to cloud platforms like Azure or AWS
- Team-based development practices for larger GitHub projects and collaborative workflows

### Mismatches

- Students reported learning key terms and concepts in systems/virtualization, but many questions show uncertainty about conceptual boundaries between containers, VMs, hypervisors, and platform-specific tools
- Unit testing appeared in both learned and struggled responses, suggesting students feel introduced to it but not yet confident applying it to authentic project contexts
- CI was perceived as learned, but reflections indicate unresolved understanding of how CI interacts with collaboration practices such as reviews, branch protection, and integration failures
- Difficulty ratings were moderately high overall, consistent with reflections describing these topics as broad and hard to fit into a coherent big picture

### Teaching adjustments

- Teach a comparison frame explicitly: container vs VM vs hypervisor vs operating system, with one visual diagram and one concrete scenario for each
- Add a short application-focused testing mini-workshop where students generate test cases for a web app, API endpoint, or bot, emphasizing how to decide what to test
- Clarify the boundary between unit, integration, and end-to-end tests so students can map testing methods to different project components
- Demonstrate a realistic GitHub workflow with branches, pull requests, required checks, and an example of code that passes alone but fails after integration
- Include a brief 'why this matters' segment for Docker and virtualization to address questions about importance, tradeoffs, and industry use
- Provide one cross-language testing bridge example, since students are asking how testing ideas transfer between C#, Python, SQL, and API contexts

### Suggested follow-up exit-ticket questions

- What is still unclear about the difference between containers, virtual machines, and hypervisors?
- If you had to add tests to one part of your current project, what part would you choose and what would you test first?
- What aspect of GitHub/CI collaboration feels most confusing right now: branching, pull requests, merge conflicts, required checks, or deployment?
- Would a hands-on Linux/Docker lab help you connect the big picture? Why or why not?
- What kind of real-project testing example would be most useful next: API, database, Discord bot, or web app?
