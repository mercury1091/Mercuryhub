# Agent-Assisted Market Research

**A reproducible Product Ops portfolio project: public-market research → source validation → buyer hypotheses → growth experiment → human review.**

Designed for a discussion of AI Agent workflow products. Demonstrates a small offline-capable research pipeline using standard-library Python, plus optional read-only live GitHub data collection.

## Run locally

```bash
python research_agent.py --mode fixture
python -m unittest discover -s tests -v
# Refresh public repository signals from the official GitHub API (internet access required):
python research_agent.py --mode live
```

Results are written to `output/market_landscape.md` and `output/research_audit.json`. No third-party dependencies; no API key necessary for demo mode. GitHub live mode uses public unauthenticated endpoints and may hit rate limits. It does not modify accounts, follow people, star repositories, fork projects, publish to GitHub or send emails.

## Optional LLM step (explicit permission required)

If you want AI synthesis on top of the validated research, configure `OPENAI_API_KEY` and `OPENAI_MODEL` locally, inspect the public metadata in `output/research_audit.json`, and run:

```bash
python llm_reviewer.py --confirm-share-public-metadata
```

It sends the public repository metadata and labeled hypotheses to the OpenAI Responses API, then saves `output/llm_hypotheses_DRAFT.md`. It does not upload client data or publish the result. This network integration has not been exercised in the offline test environment.

A reusable local Agent Skill is also included at `skills/market-research/SKILL.md`.

## Workflow / decision design

1. **Intake:** controlled list of 10 public open-source references in `data/targets.json`.
2. **Collection:** dated fixture (`data/github_snapshot.json`) or official read-only GitHub API.
3. **Quality assurance:** prevent duplicate or malformed repository slugs, reject mismatched URLs and impossible metrics.
4. **Analysis:** compare agent-related technical categories; separate observed open-source activity from **hypotheses about buyers**. Stars are never claimed as business revenue or paid adoption.
5. **Growth planning:** propose a first-task activation experiment with clear measures and explicitly unknown baseline / success threshold.
6. **Review gate:** all exported reports marked `DRAFT`; no customer outreach, publishing or product decisions occur automatically.

## What's real vs proposed

| Item | Status |
| --- | --- |
| Python research and validation workflow | Implemented and testable |
| Deterministic demo using 10 public-repository observations | Implemented; captured 2026-10-15 |
| Optional live official GitHub metadata fetch | Implemented, requires network; unverified in restricted offline runtime |
| Source-linked Markdown brief + JSON audit | Implemented and generated |
| User interviews, pricing, revenue, paid customers | **Not conducted / not known** |
| Optional source-bounded LLM review | Implemented as an opt-in integration; **not executed with a real API** |
| Autonomous browser agent in this repository | **Not implemented** |
| Product-growth experiment with real users | **Proposed; not executed** |

This project was prepared **with AI assistance** as a new portfolio demonstration. External open-source projects cited are sources/references, **not authored by Mercury**. Existing past work with Codex/Claude Code should be documented separately with accurate history and privacy-safe run artifacts. The example hypotheses are not SoloCo's official strategy.

## Future upgrade path

Connect a consent-safe browser research collector, store actual evidence spans and time of observation, use an LLM for sourced summarization, check claims against primary sources, and include a human approval UI. Measure whether the workflow reduces analyst time compared with manual research. Maintain permission boundaries and respect website terms and privacy.

## Privacy

No passwords, email inboxes, user credentials, API keys, customer leads, personal contact details, or actual client data. This demo does not scrape LinkedIn or access private APIs. Do not upload real client spreadsheets to a public repo.

See [case study](PORTFOLIO_CASE_STUDY.md), [source notes](SOURCE_NOTES.md), and [example output](examples/market_landscape.md).