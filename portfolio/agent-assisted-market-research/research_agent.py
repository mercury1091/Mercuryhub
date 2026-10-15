#!/usr/bin/env python3
"""Read-only GitHub market signals -> checked hypotheses -> review-gated experiment brief.
No scraping, outbound messaging, publishing or account changes.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
REPO_RX = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
MAX_REPOS = 20

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def write_json(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def validate_targets(targets):
    if not isinstance(targets, list) or not 1 <= len(targets) <= MAX_REPOS:
        raise ValueError(f"targets must be an array of 1–{MAX_REPOS} objects")
    seen = set()
    for x in targets:
        for k in ("repo", "category", "possible_buyer", "pain_hypothesis", "evaluation_question"):
            if not isinstance(x.get(k), str) or not x[k].strip():
                raise ValueError(f"target missing nonempty {k}")
        if not REPO_RX.fullmatch(x["repo"]) or any(part in (".", "..") for part in x["repo"].split("/")):
            raise ValueError("invalid repository slug: " + x["repo"])
        if x["repo"].lower() in seen:
            raise ValueError("duplicate research target: " + x["repo"])
        seen.add(x["repo"].lower())
    return targets

def validate_observation(item, expected_slug):
    if not isinstance(item, dict):
        raise ValueError("observation must be an object")
    if item.get("full_name", "").lower() != expected_slug.lower():
        raise ValueError("repository identity mismatch for " + expected_slug)
    if item.get("html_url") != "https://github.com/" + expected_slug:
        raise ValueError("source URL does not match target: " + expected_slug)
    if not isinstance(item.get("stargazers_count"), int) or isinstance(item.get("stargazers_count"), bool) or item["stargazers_count"] < 0:
        raise ValueError("invalid star count: " + expected_slug)
    if not isinstance(item.get("forks_count"), int) or item["forks_count"] < 0:
        raise ValueError("invalid forks count: " + expected_slug)
    if not isinstance(item.get("description", ""), str):
        raise ValueError("invalid description: " + expected_slug)
    return item

def github_get(slug):
    # Only official GitHub REST repository metadata, read-only; rate limits apply.
    request = Request("https://api.github.com/repos/" + slug, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "Mercury-ProductOps-ResearchDemo/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    with urlopen(request, timeout=12) as res:
        raw = json.load(res)
    return {k: raw.get(k) for k in ("full_name", "html_url", "description", "stargazers_count", "forks_count", "language", "updated_at", "license")}

def collect(targets, mode, snapshot_path):
    observed = []
    if mode == "fixture":
        snapshot = read_json(snapshot_path)
        raw_items = {x["full_name"].lower(): x for x in snapshot["repositories"]}
        captured = snapshot.get("captured_at", "unknown")
    else:
        raw_items = {}
        captured = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for t in targets:
        slug = t["repo"]
        raw = raw_items.get(slug.lower()) if mode == "fixture" else github_get(slug)
        if raw is None:
            raise ValueError("fixture missing source: " + slug)
        validate_observation(raw, slug)
        observed.append({"target": t, "source": raw, "captured_at": captured, "mode": mode})
    return observed

def ranking(obs):
    # A popularity bin is an open-source research signal, NEVER a customer/paid adoption measure.
    stars = obs["source"]["stargazers_count"]
    return "100k+" if stars >= 100000 else ("30k–99k" if stars >= 30000 else "under 30k")

def brief(observations):
    if not observations:
        raise ValueError("empty observations")
    for x in observations:
        validate_observation(x["source"], x["target"]["repo"])
    categories = Counter(x["target"]["category"] for x in observations)
    data = {
        "report_status": "DRAFT — requires human review",
        "data_type": "public open-source repository metadata + analyst hypotheses",
        "evidence_scope": "GitHub repo metadata; no validated customer interviews or pricing data",
        "sources": len(observations),
        "categories": dict(sorted(categories.items())),
        "records": [{
            "repo": x["target"]["repo"],
            "source_url": x["source"]["html_url"],
            "observed_at": x["captured_at"],
            "stars_snapshot": x["source"]["stargazers_count"],
            "forks_snapshot": x["source"]["forks_count"],
            "attention_band": ranking(x),
            "category": x["target"]["category"],
            "possible_buyer_HYPOTHESIS": x["target"]["possible_buyer"],
            "pain_HYPOTHESIS": x["target"]["pain_hypothesis"],
            "validation_question": x["target"]["evaluation_question"],
        } for x in observations],
        "next_experiment": {
            "hypothesis": "A guided first-task template with transparent retry/status information might improve time-to-first-success for high-frequency agent users.",
            "population": "Users who already work with CLI AI agents (recruit consented test participants)",
            "primary_metric": "Verified first-task completion within 24 hours (requires real analytics)",
            "secondary_metrics": ["time-to-first-success", "manual oversight minutes per accepted run", "retry count"],
            "safety_metric": "incorrect or unapproved external actions (target zero)",
            "baseline": None,
            "threshold": None,
            "status": "PROPOSED ONLY — not executed",
        },
        "approval_gate": {"status": "PENDING", "publishing_allowed": False, "messaging_allowed": False, "required": [
            "Verify high-priority claims from primary sources", "Separate analyst hypotheses from factual product claims",
            "Obtain permission for real user research", "Agree experiment owner, baseline, cost cap and success threshold",
            "Approve any publication or external action explicitly",
        ]},
    }
    return data

def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ").replace("\r", " ")

def markdown(data):
    lines = [
        "# Agent-Assisted Market Research — AI Agent tooling landscape", "",
        "> **Portfolio demonstration — DRAFT.** Public GitHub repository metadata and **analyst hypotheses**. "
        "No interviews, sales, paid customers, SaaS revenue or product impact measured.", "",
        f"**Sources:** {data['sources']} | **Status:** {data['report_status']} | "
        "**Evidence:** official repository metadata snapshot", "",
        "## Research question", "",
        "Why might an existing Codex/Claude Code user pay for a separate agent orchestration layer? "
        "Test hypotheses around recoverability, reduced supervision, task visibility and reusable workflows. "
        "These need actual buyer validation.", "",
        "## Open-source alternatives and workflow references", "",
        "| Repository/source | Category | Stars at observation | Potential buyer (hypothesis) | Buyer pain (hypothesis) | Validation question |", "|---|---|---:|---|---|---|",
    ]
    for x in data["records"]:
        lines.append("| ["+esc(x["repo"])+"]("+x["source_url"]+") | "+esc(x["category"])+" | "+str(x["stars_snapshot"])+" | "+esc(x["possible_buyer_HYPOTHESIS"])+" | "+esc(x["pain_HYPOTHESIS"])+" | "+esc(x["validation_question"])+" |")
    lines.extend([
        "", "**Interpretation warning:** Stars/Forks signal developer attention only. They do not establish customers, paid usage, annual revenue, implementation quality, or a competitive ranking.", "",
        "## Proposed experiment — not launched", "",
    ])
    e = data["next_experiment"]
    lines += [
        "**Hypothesis:** "+e["hypothesis"], "",
        "**Test population:** "+e["population"], "",
        "**Primary metric:** "+e["primary_metric"], "",
        "**Secondary metrics:** "+", ".join(e["secondary_metrics"]), "",
        "**Guardrail:** "+e["safety_metric"], "",
        "**Baseline / success threshold:** TBD with real user data, before testing.", "",
        "## QA and human sign-off", "",
        "- [x] Validate source identity, URL, nonnegative counts, duplicate research targets.",
        "- [x] Preserve source URLs and observation timestamp.",
        "- [x] Label buyer and product-fit conclusions as hypotheses.",
        "- [ ] Conduct real interviews and validate feature/price assumptions.",
        "- [ ] Obtain explicit human approval before publishing, client outreach or experiment launch.", "",
        "**No external messaging, account changes or publishing are performed by this code.**", "",
        "## Reproduce", "",
        "```bash", "python research_agent.py --mode fixture", "python -m unittest discover -s tests -v", "# Optional: refresh read-only live GitHub metadata", "python research_agent.py --mode live", "```", "",
    ]
    return "\n".join(lines)

def run(argv=None):
    p = argparse.ArgumentParser(description="Read-only AI Agent market landscape research, human review required")
    p.add_argument("--mode", choices=["fixture", "live"], default="fixture")
    p.add_argument("--targets", type=Path, default=ROOT / "data" / "targets.json")
    p.add_argument("--snapshot", type=Path, default=ROOT / "data" / "github_snapshot.json")
    p.add_argument("--out", type=Path, default=ROOT / "output")
    args = p.parse_args(argv)
    targets = validate_targets(read_json(args.targets))
    observations = collect(targets, args.mode, args.snapshot)
    result = brief(observations)
    args.out.mkdir(parents=True, exist_ok=True)
    write_json(args.out / "research_audit.json", result)
    (args.out / "market_landscape.md").write_text(markdown(result), encoding="utf-8")
    print(f"{args.mode}: checked {len(observations)} public-source observations; output is DRAFT pending human approval")
    print(f"Wrote {args.out / 'market_landscape.md'} and {args.out / 'research_audit.json'}")
    return result

if __name__ == "__main__":
    try:
        run()
    except (ValueError, FileNotFoundError, HTTPError, URLError, TimeoutError) as e:
        print(f"Research failed safely: {e}", file=sys.stderr)
        sys.exit(1)