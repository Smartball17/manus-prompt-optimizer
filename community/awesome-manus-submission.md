# Awesome Manus use-case draft

## Title
Prompt Optimization: Improve Manus Results Without Inflating Context

## Short description
A reusable Manus skill that diagnoses prompt failures, removes duplicated context, and validates that prompt changes improve output quality while reducing recurring context load.

## Suggested categories
- Skills
- Product Management
- Business Analysis

## Problem
Teams often make prompts longer to solve unreliable outputs. This creates duplicated instructions, mixes permanent rules with one-off data, and pastes long sources into every run. The result may use more context without becoming more reliable.

## What Manus does
Manus Prompt Optimizer first checks whether the issue is actually a prompt issue. It distinguishes ambiguous tasks, missing sources, unclear tools, permissions problems, repeated rules, and oversized context. It then produces a minimal prompt structure and evaluates the original and optimized versions on the same test case.

## Practical outcome
The skill calls success only when both conditions are met:

1. Output quality matches or improves against defined acceptance criteria.
2. Recurring context load decreases through deduplication or on-demand file references.

## Reuse
Import the skill from GitHub:

`https://github.com/Smartball17/manus-prompt-optimizer`

Then ask: `Improve this prompt`, `Optimize this prompt for Manus`, or `Reduce tokens without losing quality`.
