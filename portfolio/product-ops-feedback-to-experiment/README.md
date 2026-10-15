# Feedback → Priorities → Experiment

A small **Product Ops / Growth workflow prototype** designed to turn raw feedback into traceable product questions and a proposed experiment, with a human approval step.

**Status:** offline prototype with synthetic data, created in October 2026 as a portfolio exercise. It does **not** access SoloCo customers, call an LLM, operate actual agents, or claim measured user growth.

## What it does

1. Reads six fabricated feedback records from JSON.
2. Validates required fields, distinct record IDs, stages and severity ranges.
3. Assigns a transparent prioritization heuristic: \`severity × occurrences\`.
4. Creates a Markdown report with the three highest-scored feedback examples, a testable experiment brief, metrics, risk checks and approval steps.
5. Writes an audit summary. Makes no network calls or external changes.

## Run locally

Requires Python 3.9+ (standard library only).

\`\`\`bash
python run_demo.py
\`\`\`

Review \`DEMO_OUTPUT.md\` and \`audit.json\` after running. You can alter \`demo_feedback.json\` to observe changes in ranking and rerun. All records are made up for demonstration.

## Business question

For an AI Agent orchestration product, what would persuade someone already using Codex / Claude Code to adopt another orchestration layer? Possible hypotheses include more reliable task execution, lower supervision overhead, easier retry/recovery, auditability and reusable workflows. These are **hypotheses**, not verified customer findings.

The proposed first-run experiment tests whether a guided first-task template and clearer run-status/retry states may help users reach a successful first output. True activation, retention and paid conversion metrics require instrumentation and user consent.

## Implementation boundaries

- Scoring is a simplistic triage heuristic, **not** a validated impact estimate or an unbiased prioritization model.
- No real interviews, usage data or revenue figures are represented here.
- The current implementation does **not** integrate LLMs or autonomous agents.
- See \`AGENT_DESIGN.md\` for a proposed future extension including source evidence, QA, permission controls and human review.
- Personal experience using AI tools should be demonstrated separately with dated, permission-safe artifacts.

## Walkthrough for an interview

> "I created a small reproducible Product Ops prototype using synthetic feedback. It demonstrates data validation, transparent prioritization, a proposed experiment and a human approval gate. I would next connect consented user research, real activation events and an agent-assisted analysis layer. My interest is in reliable workflows that turn feedback into decisions, not in claiming impact before testing."

*This exercise was built with AI assistance and reviewed as a runnable demonstration; it is intentionally presented with its technical and data limitations.*
