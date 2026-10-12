# Context principles for Manus

Apply these principles when designing reusable prompts, project instructions, skills, and file-reading workflows.

## 1. Stability before ornament

Keep durable rules in a stable, deterministic prefix. Do not place volatile data — such as a timestamp or per-run status — inside stable instructions when it can live in the task-data block.

**Apply it:** preserve the same order, labels, and durable rules across equivalent runs. Add context only when it changes a decision or the result.

## 2. Separate policy, task, and evidence

| Layer | Correct content | Preferred location |
|---|---|---|
| Stable policy | priorities, boundaries, cross-cutting style | project instructions or a skill |
| Repeatable procedure | domain steps and checks | `SKILL.md` and on-demand resources |
| Per-run data | request, data, dates, audience | task prompt |
| Long evidence | PDFs, tables, transcripts, research | a file with an exact path |

Do not repeat a rule across layers. If an overlap is intentional, state which layer wins.

## 3. Use the file system as recoverable memory

Do not paste long documents when the agent can access a file. Preserve the exact path, a description of the contents, and the sections it must consult.

**Good:** `Read the “Pricing” and “Limitations” sections in /home/ubuntu/project/research.md before drafting.`

**Weak:** `Review the documentation.`

External information must remain recoverable. Never delete the only copy of data that might matter later just to reduce context.

## 4. Progressive loading

Keep `SKILL.md` as a concise selection and workflow guide. Put variants, long examples, documentation, and domain data in `references/` so they load only when useful.

The main skill body should contain the procedure needed for most cases. Exceptions and variable detail belong in a directly linked reference.

## 5. Testable instructions

Replace ambiguous adjectives with observable output conditions.

| Avoid | Prefer |
|---|---|
| “Write a complete, professional analysis.” | “Deliver: a three-sentence conclusion, five evidence-backed findings, and three prioritized risks.” |
| “Use appropriate sources.” | “Cite the public sources consulted; mark claims without a source as unverified.” |
| “Be concise.” | “Use at most 250 words and five bullets.” |

Do not turn every sentence into a constraint. A condition deserves context only when it prevents a material failure or defines the outcome.

## 6. Tools and errors

If a failure comes from a tool, permissions, unavailable data, or a broken path, resolve that cause. Adding more prohibitions to the prompt usually weakens the signal and increases context load.

Keep a relevant error and its outcome when it helps prevent repeating the same action. Do not hide a real limitation behind optimistic instructions.

## Official source

These principles adapt Manus’s published practices on stable prefixes, recoverable file-based context, and progressive skill loading. See `sources.md` for URLs and claim scope.
