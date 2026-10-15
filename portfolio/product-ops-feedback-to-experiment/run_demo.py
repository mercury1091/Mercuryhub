#!/usr/bin/env python3
"""Reproducible synthetic-feedback triage demo. No external APIs or messaging."""
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "demo_feedback.json"

def main():
    payload = json.loads(SRC.read_text(encoding="utf-8"))
    feedback = payload["feedback"]
    allowed = {"activation", "retention", "value"}
    seen, scored = set(), []
    for row in feedback:
        for field in ["id", "persona", "stage", "comment", "severity", "occurrences"]:
            if field not in row:
                raise ValueError(f"Missing {field} in {row.get('id', 'unknown')}")
        if row["id"] in seen:
            raise ValueError(f"Duplicate feedback ID: {row['id']}")
        seen.add(row["id"])
        if row["stage"] not in allowed or not 1 <= row["severity"] <= 5 or row["occurrences"] < 1:
            raise ValueError(f"Invalid stage/score for {row['id']}")
        priority = row["severity"] * row["occurrences"]
        scored.append({**row, "triage_score": priority})

    scored.sort(key=lambda x: (-x["triage_score"], x["id"]))
    counts = Counter(x["stage"] for x in feedback)
    top = scored[:3]
    lines = [
        "# Product Ops feedback triage — demo output", "",
        "> **Synthetic demo data.** All feedback is fabricated; no user research or commercial metrics are claimed.", "",
        "## Research intake and QA",
        f"- Entries passing validation: **{len(scored)}**",
        "- Checks performed: required fields, unique IDs, valid stage, severity range, occurrence count.",
        "- No emails, external calls, or published content. Human approval required before any product changes.", "",
        "## Theme counts (illustrative)",
    ]
    for stage in sorted(allowed):
        lines.append(f"- {stage}: {counts[stage]} example records")
    lines.extend(["", "## Prioritized research questions", ""])
    for i, item in enumerate(top, 1):
        lines.append(f"{i}. **{item['id']} — {item['stage']}** (triage score {item['triage_score']}; severity {item['severity']} x occurrences {item['occurrences']})")
        lines.append(f"   - Observed in synthetic brief: {item['comment']}")
        lines.append("   - Validate with real user interviews and product analytics before drawing conclusions.")
    lines.extend([
        "", "## Proposed product-growth experiment (NOT executed)",
        "- **Hypothesis:** A guided first-run template and explicit run-status/retry UI may improve successful first-task completion.",
        "- **Segment:** New users who already use Claude Code / Codex.",
        "- **Proposed measure:** First task completed within 24 hours; time to first successful output; retry/support rate.",
        "- **Countermetric:** Manual review time and failed external actions.",
        "- **Decision rule:** Define a baseline and minimum meaningful improvement with the real team before launch.",
        "- **Owners:** Product + engineering + growth; no unsupported claims of product access or shipped impact.",
        "", "## Human decision gate",
        "- [ ] Verify themes against real interviews.",
        "- [ ] Confirm analytics definitions and privacy compliance.",
        "- [ ] Approve an experiment brief and owner.",
        "- [ ] Execute only after approval; record outcome and rollback path.",
        "", "## Positioning for JD-4",
        "This demo is a **local reproducible scaffold** for intake → quality checks → transparent prioritization → experiment brief → human approval. It does not call LLMs and is not presented as a production AI Agent system."
    ])
    (ROOT / "DEMO_OUTPUT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    audit = {"synthetic": True, "input": SRC.name, "records": len(scored), "validated": len(scored),
             "top_ids": [x["id"] for x in top], "external_actions": 0, "human_approval_required": True}
    (ROOT / "audit.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Validated {len(scored)} synthetic feedback items. Wrote DEMO_OUTPUT.md and audit.json")

if __name__ == "__main__":
    main()
