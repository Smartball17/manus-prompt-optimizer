# Prompt evaluation

An optimization is successful only when it improves or preserves **quality** and reduces **recurring context load**. Do not treat a subjective impression as evidence.

## Select a test

| Case | Minimum test |
|---|---|
| One-off prompt | One representative real case and a short acceptance list. |
| Reusable template | Three distinct cases representing normal use. |
| Agent, project instructions, or skill | Three to five cases, including an edge case or known failure. |
| High-risk process | Owner-defined cases and human review before deployment. |

Keep input data, available sources, and the deliverable constant when comparing the original and optimized versions.

## Quality rubric

Select the three to five criteria that actually define the case. Score each as `pass`, `partial`, or `fail`.

| Criterion | Control question |
|---|---|
| Objective fidelity | Does it solve the specific request without drifting? |
| Constraints | Does it respect language, format, length, privacy, dates, and applicable limits? |
| Rigor | Does it use the correct sources and distinguish facts from uncertainty? |
| Useful completeness | Does it cover what is needed without filler? |
| Actionability | Can the recipient use the result without reinterpreting it? |

Record a concrete failure, not a vague judgment. For example: `fail: required sources were not included`.

## Measure efficiency

Run `scripts/measure_prompt.py` to calculate visible-text metrics before and after:

- characters and words: comparable size, not runtime tokens;
- non-empty lines: prompt density;
- duplicated lines: literal repetition to remove or consolidate.

Also record context that moved from recurring load to on-demand reading:

```markdown
| Content | Before | After | Reason |
|---|---|---|---|
| 1,200-word style guide | Pasted into every task | `references/style.md` on demand | Needed only for branded deliverables |
```

## Dual-success criterion

Call the result `success` only when both conditions hold:

1. The optimized version matches or improves quality on the selected criteria and introduces no material regression.
2. It reduces recurring text, repetition, or always-loaded context; the comparison includes visible metrics or a verifiable move to an on-demand resource.

If quality improves but the prompt grows, report `quality improvement with efficiency pending`. If text decreases but quality drops, report `invalid reduction`.

## Minimum record

```markdown
| Variable | Original | Optimized | Verdict |
|---|---|---|---|
| Quality | 3/4 criteria pass | 4/4 criteria pass | Improved |
| Visible text | 1,840 characters | 1,190 characters | -35.3% |
| Recurring context | Guide pasted | On-demand path | Reduced load |
| Dual success | — | Yes | Validated on case A |
```

## Measurement limits

Character or word count does not predict exact tokens, cost, or latency. Those depend on the model, serialization, cache behavior, tools, conversation history, and runtime. Use visible metrics to compare design; use real runtime metrics when available to claim savings.
