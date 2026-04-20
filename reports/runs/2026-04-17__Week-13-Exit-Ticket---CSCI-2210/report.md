# Exit Ticket Reflection Report — 2026-04-17

- **Source file:** `Week 13 Exit Ticket - CSCI 2210.csv`
- **Learned responses:** 26
- **Struggle/question responses:** 17
- **Future-interest responses:** 22
- **Difficulty ratings:** 26

## Course Difficulty Snapshot

- **Mean difficulty:** 5.62/10
- **Median difficulty:** 6.0/10
- **Range:** 1.0–8.9

## Repeated themes in “Learned” responses

- **hash** — 12
- **heaps** — 9
- **fibonacci** — 6
- **collisions** — 5
- **hashing** — 5
- **hash collisions** — 4
- **did** — 4
- **chaining** — 4
- **sequence** — 4
- **some** — 3

## Repeated themes in “Struggled / Questions” responses

- **heaps** — 4
- **questions** — 4
- **not** — 3
- **time** — 3
- **data** — 2
- **applications** — 2
- **there** — 2
- **other** — 2
- **any** — 2
- **nothing** — 2

## Repeated themes in “Want to Learn” responses

- **data** — 3
- **structures** — 3
- **data structures** — 3
- **hashing** — 3
- **legs** — 2
- **don** — 2
- **algorithms** — 2
- **nothing** — 2
- **other** — 2

## Overlap between “Learned” and “Struggled”

- heaps

## Semantic Teaching Insights

Students perceived strongest learning around hashing and heaps, with hashing concepts sounding more settled and heaps remaining the main unresolved area. The biggest instructional need is not just more definition-level review, but more comparative and application-driven framing: when to use heaps, what heap variants are for, how hashing-related structures map onto dictionaries/associative arrays, and how these ideas appear in realistic systems such as caching or indexing. Reported difficulty is moderate overall, so a targeted clarification-and-application pass would likely meet the class well.

### Top learned concepts

- Hash tables and hashing were the clearest perceived learning area, especially search efficiency, collisions, probing, chaining, buckets, and dictionary-style operations.
- Heaps were a major takeaway, including binary heaps, binomial heaps, and their relationship to trees.
- Students also noticed broader design ideas around caching and time/space tradeoffs, though these appeared less consistently than hashing and heaps.
- A smaller cluster of students connected the week’s material to familiar abstractions like dictionaries/associative arrays and practical data-structure operations.

### Top struggle clusters

- Heaps are the main overlap area: students both learned them and still felt uncertain about what heaps are, what variants exist, and when to use different heap types.
- Application/transfer questions are prominent: several responses ask about practical applications, realistic use cases, and when particular data structures are appropriate.
- Hashing implementation details remain muddy for some students, especially hashed indexing and associative arrays.
- A process/access issue appears in reflections about lack of lecture attendance, time, or conflicts, suggesting some struggle may come from course engagement conditions rather than topic difficulty alone.
- Some struggle responses indicate no specific confusion, so the absence of reported questions should not be interpreted as full mastery.

### Future interest clusters

- Students want deeper treatment of heaps, especially more examples and distinctions among heap variants.
- They want more about hashing and related dictionary/associative-array usage.
- There is interest in seeing data structures and algorithms situated in larger, realistic projects, including caching in broader systems and interview-style applications.
- Students appear interested in comparative framing: older or less-used data structures, when to choose one structure over another, and algorithm-focused continuation.

### Mismatches

- Hashing appears strongly in perceived learning but less in reported struggle, suggesting students may feel they grasp the vocabulary while still wanting more application-oriented depth.
- Heaps show up as both a major learned topic and the only explicit learned/struggled overlap, marking them as a likely fragile understanding area.
- Future-interest responses emphasize realistic applications more than learned responses do, indicating students may understand isolated concepts but want stronger context for use.
- Several struggle responses report 'nothing' or no questions, but future-interest answers still ask for more depth, so low reported struggle does not mean low curiosity or complete comprehension.

### Teaching adjustments

- Prioritize a short follow-up segment on heap taxonomy: binary heap vs. binomial heap, what problem each solves, and simple rules of thumb for when each is appropriate.
- Add one or two concrete application case studies tying structures to real systems, such as hashing for lookup/indexing, caching in larger software, and heaps for priority scheduling.
- Use a comparison table for dictionary, hash table, associative array, probing, and chaining so students can align terminology and implementation ideas.
- Revisit the time-space tradeoff explicitly, since students connected caching and dynamic programming ideas and asked about the inverse tradeoff.
- Provide a brief 'choosing the right data structure' decision guide centered on workload patterns: search-heavy, priority access, memory sensitivity, collision handling, etc.
- Because some students may be relying on peers/readings instead of lectures, offer a compact recap artifact such as a one-page concept map or annotated examples to reduce gaps from uneven attendance.

### Suggested follow-up exit-ticket questions

- What is one practical scenario where you would choose a hash table over another data structure, and why?
- What is still unclear about heaps: their structure, operations, variants, or use cases?
- After this week, how would you explain the difference between chaining and probing to a classmate?
- What is one example of a time/space tradeoff from this unit that now makes sense to you?
- Which data structure from this week feels most useful in a real project, and what project would you use it in?
