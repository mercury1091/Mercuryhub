# Agent design notes (proposed, not yet implemented)

## Inputs and evidence contract

- Event logs with timestamp, session ID, build/version, task-result code, no raw user secrets.
- Support/feedback notes redacted and anonymized, with clear user consent and retention period.
- Source provenance mandatory. Distinguish direct user quotes from machine-inferred themes.

## Roles

1. **Intake:** Parse structured feedback, standardize taxonomy, attach evidence IDs.
2. **Analyst:** Suggest problem themes and hypotheses with explicit uncertainty, no invented usage counts.
3. **QA:** Validate schema, traceability, PII redaction, denominator for rates, duplicates, and unsupported claims.
4. **Experiment planner:** Propose a specific metric, population, baseline, cost cap, risk and rollback.
5. **Human reviewer:** Approve changes. The workflow must never autonomously send emails or change live product data.

## Potential metrics (require real instrumentation)

- Activation: percentage of new users completing first verified task within 24h.
- Reliability: percentage of tasks producing validated output, and manual-recovery rate.
- Retention: returning weekly task creators among activated cohorts.
- Time saved: measured human supervision minutes per accepted output.
- Conversion: trial-to-paid only after real monetization is available.

## Product insight to discuss with SoloCo

The incremental buyer value over a CLI plus scripts must be measured through task reliability, visibility, resumability, and reduced orchestration overhead. A product tour without a successful first-run outcome is a weak activation signal.
