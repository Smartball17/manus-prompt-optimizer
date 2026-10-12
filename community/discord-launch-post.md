## Draft Discord launch post

I open-sourced **Manus Prompt Optimizer** — a Manus skill that improves prompts without treating “shorter” as automatically better.

It uses a simple dual-success rule:

- **Quality:** the output must meet the objective and constraints at least as well.
- **Context efficiency:** recurring prompt context must decrease or move to on-demand files.

The skill first checks whether the real bottleneck is actually the prompt. It flags missing data, unclear tools, permissions, duplicated rules, mixed instruction layers, and oversized pasted context before rewriting anything.

It includes:
- a concise prompt-optimization workflow;
- Manus-specific context principles;
- a quality-and-efficiency evaluation rubric;
- a local script that compares visible prompt metrics without pretending they are model-token savings;
- an editable 8-slide overview deck.

**Install:** Skills → + Add → Import from GitHub

`https://github.com/Smartball17/manus-prompt-optimizer`

I would value real failure cases and before/after feedback. The goal is not prettier prompts; it is more reliable execution with less repeated context.
