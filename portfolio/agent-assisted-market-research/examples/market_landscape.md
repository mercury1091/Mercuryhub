# Agent-Assisted Market Research — AI Agent tooling landscape

> **Portfolio demonstration — DRAFT.** Public GitHub repository metadata and **analyst hypotheses**. No interviews, sales, paid customers, SaaS revenue or product impact measured.

**Sources:** 10 | **Status:** DRAFT — requires human review | **Evidence:** official repository metadata snapshot

## Research question

Why might an existing Codex/Claude Code user pay for a separate agent orchestration layer? Test hypotheses around recoverability, reduced supervision, task visibility and reusable workflows. These need actual buyer validation.

## Open-source alternatives and workflow references

| Repository/source | Category | Stars at observation | Potential buyer (hypothesis) | Buyer pain (hypothesis) | Validation question |
|---|---|---:|---|---|---|
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | browser agent | 118025 | Teams doing recurring public-web research | Brittle browser tasks and manual retries consume operator time | Can a real test reduce supervision minutes per validated output? |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | web research | 191684 | Teams gathering public web content for agent research | Extraction reliability and citations are hard to preserve | How often does sourced extraction miss or misstate a page? |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | agent orchestration | 43300 | Developer teams shipping stateful workflows | Recoverability and human oversight are expensive to build | Would the team buy a higher-level interface over their current framework? |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | workflow automation | 207430 | Operators connecting many business tools | Cross-tool state and error handling become hard to manage | When does an operator choose code-first agents versus visual workflows? |
| [anthropics/skills](https://github.com/anthropics/skills) | agent skills | 181250 | AI tool power users standardizing repeatable tasks | Instructions and reference knowledge are hard to reuse consistently | Will teams adopt structured skills with versioned quality checks? |
| [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) | browser quality assurance | 14197 | Developers and product ops validating product sites | Reproducible UI checks can be difficult to automate | Which test artifacts reduce QA review time without masking failures? |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | agent tools and access | 91277 | Teams connecting agent tools to external data | Safe and traceable tool access requires careful permission design | What permissions and logs are essential before live deployment? |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | multi-agent orchestration | 59719 | Teams exploring multiple specialized agent roles | Delegation and evaluation are hard to reproduce | When are multiple agents worth the additional cost and monitoring? |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | browser agent | 38166 | Operators connecting agents to web applications | Tool schema and UI state can make agent reliability fragile | Does CLI or MCP produce a cheaper reliable action loop? |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | typed agent framework | 20625 | Python developer teams building maintainable agents | Unstructured agent outputs create downstream validation work | How much do typed outputs reduce QA errors? |

**Interpretation warning:** Stars/Forks signal developer attention only. They do not establish customers, paid usage, annual revenue, implementation quality, or a competitive ranking.

## Proposed experiment — not launched

**Hypothesis:** A guided first-task template with transparent retry/status information might improve time-to-first-success for high-frequency agent users.

**Test population:** Users who already work with CLI AI agents (recruit consented test participants)

**Primary metric:** Verified first-task completion within 24 hours (requires real analytics)

**Secondary metrics:** time-to-first-success, manual oversight minutes per accepted run, retry count

**Guardrail:** incorrect or unapproved external actions (target zero)

**Baseline / success threshold:** TBD with real user data, before testing.

## QA and human sign-off

- [x] Validate source identity, URL, nonnegative counts, duplicate research targets.
- [x] Preserve source URLs and observation timestamp.
- [x] Label buyer and product-fit conclusions as hypotheses.
- [ ] Conduct real interviews and validate feature/price assumptions.
- [ ] Obtain explicit human approval before publishing, client outreach or experiment launch.

**No external messaging, account changes or publishing are performed by this code.**

## Reproduce

```bash
python research_agent.py --mode fixture
python -m unittest discover -s tests -v
# Optional: refresh read-only live GitHub metadata
python research_agent.py --mode live
```