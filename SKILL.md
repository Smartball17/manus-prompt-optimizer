---
name: manus-prompt-optimizer
description: >-
  Optimizes prompts, agent instructions, and reusable templates for Manus while improving both output quality and context efficiency. Use when asked to improve, simplify, structure, deduplicate, or audit a prompt; reduce context load; create a reusable prompt; or diagnose whether a weak result comes from the prompt, context, tools, or missing data. Triggers: "improve this prompt", "optimize this prompt for Manus", "reduce tokens", "make this more reliable", "audit these instructions".
---

# Manus Prompt Optimizer

Optimize for two outcomes at once:

1. **Quality:** the result better fulfills the objective and its constraints.
2. **Efficiency:** recurring context load decreases or moves into on-demand resources.

Do not call an optimization successful when it improves only one outcome. Do not promise exact token savings: measure visible text and recurring context load, then use runtime metrics when available.

## Manus principles

Apply these principles. Read `references/manus-context-principles.md` when creating or changing a reusable prompt, project instructions, a skill, or a file-based workflow.

- Keep durable instructions and tool definitions stable.
- Separate stable rules, variable data, and long sources.
- Store long or recoverable context in files with exact paths; load only the required excerpt.
- Use short, testable, non-duplicated instructions.
- Do not reduce context by removing a constraint that prevents a real failure.

## Fast workflow

Follow this workflow by default. Use extended evaluation only when the prompt is critical, heavily reused, or has recurring failures.

### 0. Decide whether a prompt is the solution

1. Check whether an installed, official, or public skill already solves the work without duplicating instructions.
2. If the objective mainly depends on missing data, an unclear tool, permissions, the model, or an unavailable source, say so before rewriting the prompt.
3. Do not turn a specialized, repeatable workflow into a long prompt when a skill or a file reference is more efficient.

When asked to create a new skill or reusable workflow, search local options first. If none covers the use case, use `internet-skill-finder` before recommending a new skill from scratch.

### 1. Capture the minimum contract

Extract or ask only for information that materially changes the result:

- objective and non-objective;
- audience and exact deliverable;
- inputs, sources, files, and available tools;
- non-negotiable constraints: language, format, length, cost, privacy, date, tone, or sources;
- an example of success or failure, if available.

If a minor detail is missing, state a reasonable assumption and continue. If a critical condition is missing, ask one specific clarification.

### 2. Diagnose before editing

Classify the primary problem:

| Signal | Likely diagnosis | Action |
|---|---|---|
| Ambiguous objective or mixed deliverables | Weak contract | Separate objective, scope, and output. |
| The same rule appears more than once | Duplicated context | Keep one precise version. |
| Stable rules are mixed with per-task data | Mixed layers | Move rules to stable instructions; keep variables in the task request. |
| Long documents are pasted into the prompt | Oversized context | Store or reference them by path and read needed excerpts. |
| Format is wrong despite good content | Output is not testable enough | Define structure and acceptance criteria. |
| Facts are invented or data is missing | Source problem, not wording | Add a source, tool, or uncertainty rule. |
| Wrong tool use or failed actions | Tool or permissions problem | Fix the definition, access, or workflow; do not add redundant prohibitions. |

Remove ornamental reasoning, generic personas, repeated mandates, and examples that do not change a decision. Do not request chain-of-thought. Request the result, observable checks, or a short justification only when useful.

### 3. Structure the optimized version

Use only the sections that are necessary, in this order:

```markdown
## Task
[One verb, one result, and unambiguous scope]

## Relevant context
[Only facts needed for this execution; not permanent policy]

## Inputs and sources
[Data, exact paths, URLs, or available tools]

## Deliverable
[Format, language, length, and audience]

## Constraints
[Non-negotiable rules, once each]

## Final check
[2–5 observable checks before delivery]
```

Design rules:

- Put permanent instructions before variable data and keep them stable across equivalent runs.
- Reference files by exact path. Do not use vague pointers such as “check the documentation.”
- Use clear delimiters for large inputs only when they must travel inside the prompt.
- Define the output format when it reduces ambiguity; do not add tables, tags, or sections by habit.
- Give every rule one owner: project instructions, a skill, or the task prompt — not all three.
- Prefer one short example only when it resolves an ambiguity that the instruction cannot.

### 4. Measure and test

To compare visible size, run:

```bash
python scripts/measure_prompt.py path/to/original.md path/to/optimized.md
```

The script measures characters, words, lines, and duplicated lines. It is not a model token counter.

Apply the same test case to the original and optimized versions whenever possible. Read `references/evaluation.md` for the rubric and dual-success criteria.

- For a fast improvement, use one representative case and review both outcomes.
- For a reusable or high-impact prompt, use 3–5 cases, including an edge case or known failure.
- If quality drops, restore the constraint or context that supported it. Do not sacrifice quality to reduce words.
- If the prompt grows while quality improves, do not call it dual success. Explain the trade-off and propose a second iteration using external context or denser rules.

### 5. Return a short, useful package

Unless another format is requested, return:

```markdown
## Diagnosis
[One sentence: prompt, context, tool, or data]

## Optimized prompt
[Ready-to-use version]

## Changes that matter
- [Change → expected effect]
- [Change → expected effect]

## Validation
- Quality: [criterion and result, or test pending]
- Efficiency: [before/after metric or context moved to a resource]

## Risk or next test
[One action if material uncertainty remains]
```

For simple requests, skip the long report: return the prompt, up to three material changes, and one validation check.

## Limits

- Do not blame a weak result on the prompt without checking for missing data, tools, permissions, or sources.
- Do not claim lower runtime cost, latency, or token use without a real environment metric.
- Do not change security, privacy, authorization, or budget rules without preserving their explicit intent.
- Do not rewrite an entire prompt when a minimal edit satisfies both success outcomes.

## On-demand resources

- `references/manus-context-principles.md`: use for reusable prompts, project instructions, skills, or long context.
- `references/evaluation.md`: use to define tests, the rubric, and dual-success criteria.
- `references/sources.md`: use for provenance and rationale.
- `scripts/measure_prompt.py`: run for a deterministic visible-text comparison.
