# Study Guide for Week of 2026-04-17

This week’s reflections suggest that the main ideas to review are hashing/hash tables, collisions and collision handling, dictionaries/associative arrays, and heaps. Many students felt they learned the vocabulary and core ideas, but still want clearer comparison, use-case framing, and practice deciding when to use each structure. Difficulty felt moderate overall, so the best prep before class is a focused review of core terms plus a little application-oriented practice.

## Key takeaways to review

- Hash tables and hashing: why they are useful for efficient lookup/search.
- Hash collisions: what a collision is and why collision handling matters.
- Collision handling methods mentioned this week, especially probing and chaining.
- How dictionaries and associative-array style operations relate to hashing ideas.
- Heaps as a family of data structures, especially binary heaps and binomial heaps.
- The connection between heaps and trees.
- Caching as an example of using data structures in a larger system.
- The basic idea of time/space tradeoffs, since several reflections connected this to caching and efficiency.

## Common sticking points

- Heaps are still the least settled topic: what they are, how variants differ, and when to use one kind over another.
- Students want clearer practical applications, not just definitions.
- Some terminology may still feel blurry: dictionary vs. hash table vs. associative array.
- Hashed indexing and how associative-array behavior is implemented may still need clarification.
- It may be hard to tell which data structure fits which problem.
- A few students may need a compact recap if they missed lecture or relied mostly on readings/peers.

## Practice prompts

- In your own words, explain why a hash table can make searching efficient.
- Write a 2–3 sentence explanation of what a hash collision is.
- Compare chaining and probing: how are they both trying to solve the same problem?
- Make a small chart with these terms: dictionary, associative array, hash table, chaining, probing. Write one short note for each.
- List what you know about heaps so far, then add one question you still have about heap variants or use cases.
- Give one possible real-world style use case for hashing, one for heaps, and one for caching.
- Describe a situation where saving time might require extra space.
- Describe a situation where you might accept more time in order to use less space.

## Self-check questions

- Can I explain the difference between a collision and a hash function?
- Can I describe chaining and probing without mixing them up?
- Do I understand how dictionary-like operations connect to hashing?
- Can I name at least two heap variants mentioned this week?
- Can I explain, at a high level, why someone might want different kinds of heaps?
- Can I give one example of a realistic application for hashing, heaps, or caching?
- Can I say what kind of access pattern a structure supports well, such as fast lookup or priority-based access?
- What feels least clear right now: heap structure, heap variants, hash implementation details, or choosing the right structure?

## Before next class

- Review your notes or readings for hashing, collisions, chaining, probing, dictionaries, and heaps.
- Make a one-page comparison sheet for hash-table-related terms and heap-related terms.
- Prepare one practical question to bring to class, especially about when to choose a certain structure.
- If heaps still feel fuzzy, focus on distinguishing the variants mentioned rather than memorizing every detail.
- If you missed lecture or feel behind, build a short recap from examples in the readings so you have the terminology ready.
- Try to connect each topic to a larger system idea: lookup/indexing, caching, or priority-based processing.

## Why this guide was generated

Students perceived strongest learning around hashing and heaps, with hashing concepts sounding more settled and heaps remaining the main unresolved area. The biggest instructional need is not just more definition-level review, but more comparative and application-driven framing: when to use heaps, what heap variants are for, how hashing-related structures map onto dictionaries/associative arrays, and how these ideas appear in realistic systems such as caching or indexing. Reported difficulty is moderate overall, so a targeted clarification-and-application pass would likely meet the class well.
