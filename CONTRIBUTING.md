# Contributing

Contributions are welcome when they make the skill more reliable, more reusable, or more context-efficient.

## Contribution standard

Every proposed change should state:

1. **Problem:** What failure or ambiguity does it address?
2. **Change:** What instruction, reference, or script changes?
3. **Quality evidence:** Which acceptance criteria improve or remain intact?
4. **Efficiency evidence:** What recurring text, duplication, or always-loaded context decreases?
5. **Risk:** What could regress or require a new test?

## Do not contribute

- Generic advice that an agent already knows.
- More emphasis markers, repetition, or long personas without evidence.
- Claims of token, cost, or latency savings without runtime metrics.
- Instructions that solve a tool, source, or permissions problem only with prompt wording.

## Tests

- Run the provided visible-text comparison script for prompt-size changes.
- Use the same input data and deliverable when comparing original versus optimized prompts.
- For reusable prompts, include three to five representative cases and at least one edge case or known failure.

## License

By contributing, you agree that your contribution is licensed under Apache-2.0.
