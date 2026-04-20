# Exit Ticket Reflection Report — 2026-04-19

- **Source file:** `Week 13 Exit Ticket - CSCI 2910.csv`
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
- **used** — 3
- **use** — 3
- **windows** — 2
- **tests** — 2

## Repeated themes in “Struggled / Questions” responses

- **tests** — 3
- **does** — 3
- **same** — 2
- **unit** — 2
- **different** — 2
- **unit tests** — 2
- **pushing** — 2

## Repeated themes in “Want to Learn” responses

- **docker** — 2
- **use** — 2
- **tests** — 2
- **work** — 2
- **trying** — 2
- **big** — 2
- **different** — 2
- **something** — 2
- **side** — 2
- **projects** — 2

## Overlap between “Learned” and “Struggled”

- tests
- unit

## Semantic Teaching Insights

Students perceived substantial learning this week around operating systems, virtualization/hypervisors, Docker, and unit testing/CI. The main struggles were not simple recall problems but application and differentiation problems: how similar technologies relate, what tests to write in realistic systems, and how CI/GitHub workflows behave in collaborative settings. Future interest strongly points toward more Docker, Linux/OS comparison, deeper testing practice, and extending CI into CD/deployment. Instructionally, the clearest opportunity is to unify these topics with a single end-to-end project and explicit comparison frameworks so students can connect the mechanics to the larger software engineering picture.

### Top learned concepts

- Core OS infrastructure cluster: operating systems, virtualization, hypervisors, Hyper-V, and how resources relate across hardware/OS/application layers.
- Containerization and environment packaging: Docker and the idea that containers bundle what an application needs to run.
- Testing and quality workflows: unit tests, CI, and how tests support server-side development.
- Platform/tool awareness: some students specifically noticed Windows-based virtualization tools and system-level tooling.

### Top struggle clusters

- Concept boundary confusion between related technologies: students seem unsure how VMs, hypervisors, containers, and virtualization differ and relate.
- Testing design transfer: students are asking less about syntax and more about what tests to write, how testing differs across languages, and how to test apps, APIs, databases, and bots.
- CI/CD at team scale: uncertainty about GitHub pushing workflows, merge conflicts, branch protection, and what CI actually catches when multiple developers contribute.
- System/networking details remain fuzzy: Hyper-V networking, virtual switches, checkpoints, and the consequences of not having a hypervisor.
- Big-picture integration challenge: some reflections suggest the topics feel broad and disconnected, making it hard to see how all the pieces fit in real development environments.

### Future interest clusters

- More hands-on Docker/container work.
- Broader OS exposure, especially Linux or comparing non-Windows environments.
- Deeper virtualization topics, including checkpoints and VM infrastructure behavior.
- Applied testing beyond basic unit tests: APIs, databases, SQL, bots, and realistic server-side projects.
- CI/CD continuation into deployment: interest in the CD side, including automated deployment to cloud platforms.
- Collaboration workflows for larger projects using GitHub.

### Mismatches

- Unit testing appears in both learned and struggled themes, suggesting students grasp the basic idea but lack confidence applying it to authentic project components.
- Docker/containerization was perceived as learned by some students, but others still question its importance and want more depth, indicating uneven buy-in or understanding of use cases.
- Virtualization/hypervisor content registered as a key takeaway, yet students still seem unclear on distinctions among VMs, hypervisors, and related infrastructure details.
- Students reported learning CI, but struggle responses show unresolved confusion about how CI behaves in multi-developer, real-company workflows.
- Difficulty ratings are moderately high overall (mean 5.82, median 6) despite many concrete learning takeaways, which fits a pattern of successful exposure but incomplete conceptual integration.

### Teaching adjustments

- Teach a comparison matrix or diagram for hypervisors vs VMs vs containers vs host OS, with one concrete example stack students can revisit.
- Add a short 'what problem does this solve?' segment for Docker, CI, hypervisors, and virtual networking to address perceived relevance, not just mechanics.
- Use one worked project to connect the pipeline end-to-end: write tests, push to GitHub, run CI, resolve a conflicting change scenario, and optionally discuss deployment.
- Differentiate testing instruction into levels: what to test, examples of good unit tests, and how strategies change for APIs, databases, bots, and multi-language stacks.
- Include a practical collaboration mini-lesson on branching, pull requests, branch protection, merge conflicts, and why passing local tests may still fail after integration.
- Provide an architecture-level recap at the end of class that links OS/virtualization/container/testing concepts into one ecosystem view, since several students seem to need the big picture before details fully stick.

### Suggested follow-up exit-ticket questions

- Which distinction is still least clear: hypervisor vs VM, VM vs container, or CI vs CD?
- For your current or recent project, what is one component you would want to test but are unsure how to test?
- How confident are you that you could explain why a developer would use Docker in a real project? Why?
- What part of team-based GitHub workflow feels most unclear right now: branching, pull requests, conflicts, reviews, or CI checks?
- Would a Linux-based demo or lab help you understand these topics better than a Windows-only example?
