# Sources and provenance

## Primary foundation: Manus

1. **Manus Skills documentation** — https://manus.im/docs/features/skills
   - Skill structure, progressive loading, and context-cost levels.
2. **Context Engineering for AI Agents: Lessons from Building Manus** — https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
   - Manus’s published practices on stable prefixes, recoverable file-based context, tools, and attention management.

## External conceptual reference

3. **Sentry Prompt Optimizer** — https://github.com/getsentry/skills/tree/main/skills/prompt-optimizer
   - Main file author according to its commit history: David Cramer (`@dcramer`).
   - Repository licensed under Apache-2.0.
   - This skill uses the conceptual ideas of defining a contract, diagnosing the bottleneck, and evaluating changes. Its implementation, writing, and Manus adaptation are independent.

## Scope

Manus’s public sources describe context-engineering practices. They do not guarantee a quantified improvement for every prompt. This skill requires before/after testing before declaring success.
