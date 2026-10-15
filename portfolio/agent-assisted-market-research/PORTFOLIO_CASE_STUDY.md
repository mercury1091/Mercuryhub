# Case Study — AI Agent Tooling Market Research

**Business question:** What value would persuade teams already using Codex/Claude Code, scripts and Agent frameworks to pay for an orchestration layer?

**Approach:** Investigate public technical alternatives and develop *testable* buyer-problem hypotheses. Analyze where developers can already self-build and where operational friction (recovery, oversight, auditability, visibility) may justify additional software spending.

**What was implemented:** A local reproducible Python research agent (a staged workflow, not an LLM) that loads a target list, validates factual GitHub metadata, classifies open-source alternatives, and produces an attributed Markdown report plus review-gated experiment brief and machine-readable QA audit. Automated unit tests support reproducibility.

**User impact:** Not measured; no actual interviews, sales, product conversion data or competitor prices were used. Current repository Star counts are only evidence of developer attention. Findings are *hypotheses requiring research*, not conclusions.

**What is promising:** A first-run workflow with clear output expectations and retry visibility could be tested among high-frequency users. Next: real discovery interviews, first-task success instrumentation, deliberate privacy controls, reviewer approval, and source-linked LLM analysis.

**Authenticity:** This prototype was built as an AI-assisted portfolio exercise. Mercury's established commercial leadership and workflow practice are separate historical experiences; this prototype must not be presented as personally hand-coded without assistance or as a product already shipped to clients.

**Optional extension:** Source-bounded LLM reviewer and a reusable Agent Skill have been scaffolded, with a required explicit opt-in and no claim of successful live API execution.