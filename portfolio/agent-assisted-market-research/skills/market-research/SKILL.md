---
name: market-research-evidence-first
description: Build a reproducible, source-linked research brief from authorized public GitHub data, with human-review gates. Use for competitive research and early Product Ops growth hypotheses.
---

# Market Research: Evidence First

Use the Python workflow in this repository for public, permitted research. Never import private contact lists or unpublished user/customer materials.

1. Define a business problem, a constrained set of public target repositories, and exact source URLs.
2. Run `python research_agent.py --mode fixture` for the deterministic demonstration or `--mode live` to read official public repo metadata.
3. Read `output/research_audit.json` and `output/market_landscape.md`.
4. Mark repository facts as facts with timestamps; mark target buyer, willingness to pay, pain and market-entry claims as hypotheses.
5. If LLM review is desired, inspect what will be shared, set `OPENAI_API_KEY` and `OPENAI_MODEL`, then explicitly run `python llm_reviewer.py --confirm-share-public-metadata`. Its output is unverified draft only.
6. Ask human reviewer to approve any client contact, experiment execution or publication. Never auto-send, auto-edit customer records or auto-publish.

**Success evidence:** reproducible command + test results + dated source list + safe output + hypothesis-to-question traceability. **Do not** treat stars, forks, copied code or a repository bookmark as personal usage evidence.