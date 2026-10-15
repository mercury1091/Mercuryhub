# SoloCo JD-4 | AI Agent Skills & Reference Shortlist

Private research list for Mercury Qing — prepared 2026-10-15.

> **Status:** Links researched; these are **other teams' repositories**, not projects authored or implemented by Mercury. They are not evidence of personal technical proficiency. Do not copy source files or claim to have built these projects. Review licenses and security before running anything. This index is stored in a **private** repository and is not intended as a public portfolio artifact.

## Shortlist, sorted by usefulness for a credible Product Ops / Growth demonstration

| Reference | Why it matters to SoloCo-type workflows | First experiment | Status |
| --- | --- | --- | --- |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Browser automation by AI agents, with CLI/Python/cloud routes. Co-authored by Gregor Žunič and Magnus Müller. | Collect **public demo-site** product FAQ details, keep citations and human review; no account credentials. | Research only |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | Browser-driving interface with an agent-friendly CLI + skill approach, useful for reproducible research and product QA. | Automated QA on your own personal website, capturing test results without collecting visitors' personal data. | Research only |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Stateful, durable agent orchestration, checkpoints and human-in-the-loop workflow design. | Explore approved→rejected/retry task states in a synthetic feedback-to-experiment workflow. | Research only |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills packaging format; reusable instructions, scripts, references and assets. | Convert the QA workflow into a small custom SKILL.md and test it. | Research only |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference MCP servers and controlled tool/data interfaces (educational, not production-ready). | Explore safely scoped filesystem reads and provenance checks for mock inputs. | Research only |
| [openai/plugins](https://github.com/openai/plugins) | Current OpenAI public plugin / skill examples (previous openai/skills repo marks itself deprecated). | Compare skill packaging and appropriate approval boundaries. | Research only |

## Suggested **original** public-safe portfolio idea

**Agent-assisted Product Research → QA → Experiment Brief**

1. Select a publicly documented product or create a fictional sample. Obtain source URLs without accessing private services or scraping gated accounts.
2. Use Browser Use or Playwright CLI to collect a small, consent-safe set of public pages and retain URLs, timestamps, and the exact quoted evidence.
3. Generate a structured feature/value comparison and user-interview hypotheses with explicit uncertainty.
4. Check data validity, source references, duplicate claims, and unsupported recommendations in an automated validation step.
5. Require human approval before publishing an experiment brief, changing content or contacting anyone.
6. Measure number of records validated, time spent on human review, and errors caught. Do not claim conversion improvements without real data.

**Proof criteria:** own reproducible code, synthetic/public data, clear source attribution, a test command, actual run output, limitations, and an honest breakdown of what Mercury implemented versus what AI assistance produced.

## Profile privacy / portfolio release

- [ ] Consider GitHub Settings → Public profile → Contributions & Activity → *Make profile private and hide activity* if the Stars tab is currently a privacy concern.
- [ ] Audit public repositories and public forks separately. Changing profile privacy does not turn public repositories into private repositories.
- [ ] Leave private workspaces private; never paste client lists, account credentials, personal chats, job applications, phone numbers or API keys into portfolio repositories.
- [ ] Share the personal website and an independently reviewed **public** demo repository with SoloCo once ready.
- [ ] If publishing derivative work, respect upstream license and attribute accurately. Prefer your own independently written showcase that links to dependencies/references.

## Current prototype location

[Feedback-to-Experiment](./product-ops-feedback-to-experiment/README.md) — **synthetic, Python rule-based and offline; no real LLM Agent integration**.

Do not present a Star, fork, research note, prototype README or AI-generated draft as proof of a shipped production AI system.
