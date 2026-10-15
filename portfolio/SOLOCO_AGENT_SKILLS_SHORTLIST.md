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


## Verified GitHub popularity scan — 2026-10-15

The source repository information below was checked from GitHub metadata today. Counts are time-specific and approximate indicators of **developer attention, not proof Mercury has tried the tools, nor proof of product revenue**. These are curated references in a private index; no GitHub Star or Fork action was performed.

| Project | Stars (2026-10-15) | What to explore next | Status |
|---|---:|---|---|
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 207,430 | visual workflow vs agent-driven orchestration; retries and operator audit | Studied public docs; no local installation claim |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 191,684 | public website extraction, source provenance, respect AGPL-3.0 | Studied public docs; no local installation claim |
| [anthropics/skills](https://github.com/anthropics/skills) | 181,250 | SKILL.md packaging, reusable instructions + tests; check licenses per component | Studied public docs; no local installation claim |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 118,025 | browser research automation with safe read-only tests | Studied public docs; no local installation claim |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 91,277 | MCP tool interfaces and permission boundaries | Studied public docs; no local installation claim |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 59,719 | delegation among analyst, reviewer and editor roles | Studied public docs; no local installation claim |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 43,300 | long-lived agent state, resumability, approval gates | Studied public docs; no local installation claim |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | 38,166 | accessibility-tree-based browser tool for agent QA | Studied public docs; no local installation claim |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | 30,558 | tool access, OAuth, granular scopes and tool execution | Studied public docs; no local installation claim |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | 30,285 | long-running agent harness with files and task decomposition | Studied public docs; no local installation claim |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 20,625 | typed and validated AI output and evidence contracts | Studied public docs; no local installation claim |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | 14,197 | reproducible browser checks on user's own site | Studied public docs; no local installation claim |
| [openai/plugins](https://github.com/openai/plugins) | 7,448 | current OpenAI plugin/skills architecture reference | Studied public docs; no local installation claim |

### Our actual created work (distinguish from upstream)

[Agent-Assisted Market Research](./agent-assisted-market-research/README.md): source-linked local Python research workflow; read-only GitHub source snapshots; QA checks; experiment proposal; human approval gate; optional source-bounded LLM reviewer. Implemented with AI assistance, validated through **11 local unit tests**. No true browser agent used, no paid customers studied, no direct use of the reference projects claimed.

### To actually Star or Fork on GitHub

Use each upstream repository link above, click **Star** only for projects you genuinely want to follow. If you Fork code, preserve the upstream attribution and license. A Star/Fork is a bookmark or copy, **not evidence of personal hands-on usage**. Genuine use can be documented with commands, anonymized input/output, test logs, fixes, your commits and a reproducible case study.
