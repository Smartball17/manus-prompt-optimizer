# Manus Prompt Optimizer

> Improve Manus prompts without trading output quality for context efficiency.

**Manus Prompt Optimizer** is a reusable Agent Skill for diagnosing, restructuring, and validating prompts, agent instructions, and reusable templates in Manus.

It treats an optimization as successful only when it achieves both:

1. **Better or equal output quality** against defined acceptance criteria.
2. **Lower recurring context load** through less repetition or on-demand file-based context.

It does **not** claim exact token, cost, or latency savings without runtime measurements.

## What it does

- Checks whether a prompt is the real bottleneck before rewriting it.
- Detects ambiguous objectives, duplicated rules, mixed instruction layers, oversized context, missing sources, and tool or permission issues.
- Produces a minimal, testable prompt structure.
- Keeps stable policy, per-task data, and long evidence in separate layers.
- Compares original and optimized visible-text metrics with a local script.
- Uses a dual-success gate instead of rewarding shorter prompts by default.

## Install in Manus

1. In Manus, open **Skills**.
2. Select **+ Add → Import from GitHub**.
3. Paste:

```text
https://github.com/Smartball17/manus-prompt-optimizer
```

4. Trigger it with requests such as:

```text
Improve this prompt
Optimize this prompt for Manus
Reduce tokens without losing quality
Audit these instructions
```

## The operating flow

| Step | Question | Output |
|---|---|---|
| 0. Reuse | Is a prompt the right solution? | Existing skill, data, tool, or a prompt rewrite |
| 1. Contract | What must the result achieve? | Objective, deliverable, constraints, sources |
| 2. Diagnose | What is actually weak? | Prompt, context, tool, permissions, or data finding |
| 3. Structure | What belongs in the prompt? | Minimal task-ready prompt |
| 4. Measure | Did both variables improve? | Quality and context-efficiency evidence |
| 5. Deliver | What is ready to use? | Prompt, changes, validation, and residual risk |

## The dual-success gate

| Outcome | Pass condition |
|---|---|
| **Quality** | The optimized output matches or improves the selected acceptance criteria, with no material regression. |
| **Efficiency** | Recurring text, duplication, or always-loaded context decreases, with visible metrics or a verifiable move to an on-demand resource. |
| **Success** | Both conditions are true. |

If quality improves while the prompt grows, the result is **quality improvement with efficiency pending**. If the prompt gets shorter but quality drops, it is an **invalid reduction**.

## Prompt structure

```markdown
## Task
[One verb, one result, and unambiguous scope]

## Relevant context
[Only facts needed for this execution]

## Inputs and sources
[Data, exact paths, URLs, or tools]

## Deliverable
[Format, language, length, and audience]

## Constraints
[Non-negotiable rules, once each]

## Final check
[2–5 observable checks]
```

## Measure visible-text changes

```bash
python scripts/measure_prompt.py path/to/original.md path/to/optimized.md
```

The script reports deterministic text metrics: characters, words, lines, and duplicated lines. It intentionally does **not** estimate tokens, cost, or latency because those depend on the model and runtime.

## Package contents

```text
SKILL.md                         # Skill workflow and triggers
references/                      # Manus principles, evaluation, provenance
scripts/measure_prompt.py        # Local visible-text comparison
presentation/                    # Editable overview deck
community/                       # Draft launch copy for community channels
```

## Presentation

[Download the editable presentation](presentation/manus-prompt-optimizer-overview.pptx)

## Sources and provenance

- [Manus Skills documentation](https://manus.im/docs/features/skills)
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Sentry Prompt Optimizer](https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer) — conceptual reference; this implementation and Manus adaptation are independent.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The useful contribution is not a longer prompt; it is evidence that a change improves quality, recurring context load, or both.

## License

[Apache-2.0](LICENSE)
