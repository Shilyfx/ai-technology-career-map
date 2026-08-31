#!/usr/bin/env python3
"""Recompute role profiles from the audited Batch B evidence rows."""
from collections import Counter, defaultdict
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
UPDATED = "2026-09-01"
sys.path.insert(0, str(ROOT / "scripts"))
from rebuild_applied_evidence import DATA  # noqa: E402

ROLE_FILES = {
    "03-Roles/AI-Application-Engineer.md": {
        "count": 14,
        "samples": [
            "Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md", "Notion-Software-Engineer-AI-Workflows-2026-08.md", "Glean-Software-Engineer-Agents-2026-08.md", "Salesforce-Product-Manager-Agent-Fabric-2026-08.md", "ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md", "ServiceNow-Senior-Staff-Agent-Development-2026-08.md", "Ramp-Applied-AI-Engineer-2026-08.md", "Ramp-Software-Engineer-Enterprise-Product-2026-08.md", "Ramp-Software-Engineer-Frontend-Revenue-2026-08.md", "Zapier-Engineer-Applied-AI-2026-08.md", "Front-AI-Engineer-GTM-Operations-2026-08.md", "Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md", "OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08.md", "OpenAI-Software-Engineer-API-SDK-Seattle-2026-08.md"
        ],
        "basis": "14 curated samples (11 Batch B application/agent-product cards + 3 Batch A API/application cards); employers span Atlassian, Notion, Glean, Salesforce, ServiceNow/Moveworks, Ramp, Zapier, Front and OpenAI. Batch B locations cover Global/US/APAC; seniority is mostly senior/staff, with product-application and agent-platform subtracks.",
        "priority": {"TypeScript-JavaScript":"Common", "Python":"Common", "LLM-API-and-Structured-Outputs":"Core", "Tool-Calling-and-Action-Contracts":"Common", "Agent-Orchestration-and-State":"Common", "Workflow-Automation-and-Business-Process-Design":"Common", "MCP-and-Agent-Interoperability":"Specialized", "Enterprise-Integrations-and-Connectors":"Common", "Agent-Evals-and-Trace-Debugging":"Common", "Human-in-the-Loop-and-Agent-Guardrails":"Common"},
    },
    "03-Roles/AI-Solutions-Architect-and-FDE.md": {
        "count": 12,
        "samples": [
            "Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md", "Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md", "Notion-Forward-Deployed-Architect-Japan-2026-08.md", "Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md", "Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md", "Salesforce-Success-Architect-Agentforce-2026-08.md", "Ramp-Software-Engineer-Enterprise-Product-2026-08.md", "Glean-Founding-Forward-Deployed-Engineer-2026-08.md", "Warp-Forward-Deployed-Engineer-2026-08.md", "Front-AI-Engineer-GTM-Operations-2026-08.md", "Huawei-AI-Solutions-Architect-Shanghai-2026-08.md", "Huawei-OTT-Solutions-Architect-Shanghai-2026-08.md"
        ],
        "basis": "12 curated FDE/Architect/Success samples (10 Batch B + 2 Batch A solution-architecture cards); employers span Atlassian, Notion, Salesforce, Ramp, Glean, Warp, Front and Huawei. Locations cover Global, Japan, US/APAC and China; seniority is senior/staff with field-deployment, product-application and applied-ai-product subtracks.",
        "priority": {"TypeScript-JavaScript":"Common", "Python":"Common", "LLM-API-and-Structured-Outputs":"Common", "Tool-Calling-and-Action-Contracts":"Common", "Agent-Orchestration-and-State":"Common", "Workflow-Automation-and-Business-Process-Design":"Core", "MCP-and-Agent-Interoperability":"Specialized", "Enterprise-Integrations-and-Connectors":"Core", "Agent-Evals-and-Trace-Debugging":"Common", "Human-in-the-Loop-and-Agent-Guardrails":"Common"},
    },
    "03-Roles/AI-Product-Manager.md": {
        "count": 3,
        "samples": ["Salesforce-Product-Manager-Agent-Fabric-2026-08.md", "OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08.md", "OpenAI-Product-Manager-Safety-Measurement-San-Francisco-2026-08.md"],
        "basis": "3 directional senior PM samples: Salesforce Agent Fabric (Batch B) plus OpenAI API Agents and Safety Measurement (Batch A). Employers/regions are Salesforce US/global and OpenAI San Francisco; subtracks are agent platform, API platform and safety measurement. This is not a census.",
        "priority": {"TypeScript-JavaScript":"Prerequisite", "Python":"Prerequisite", "LLM-API-and-Structured-Outputs":"Common", "Tool-Calling-and-Action-Contracts":"Common", "Agent-Orchestration-and-State":"Common", "Workflow-Automation-and-Business-Process-Design":"Common", "MCP-and-Agent-Interoperability":"Specialized", "Enterprise-Integrations-and-Connectors":"Common", "Agent-Evals-and-Trace-Debugging":"Common", "Human-in-the-Loop-and-Agent-Guardrails":"Common"},
    },
    "03-Roles/AI-Infrastructure-and-Inference-Engineer.md": {
        "count": 10,
        "samples": ["ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md", "ServiceNow-Staff-Agent-Eval-Platform-2026-08.md", "OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08.md", "OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08.md", "OpenAI-Software-Engineer-Inference-Performance-San-Francisco-2026-08.md", "Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08.md", "Anthropic-ML-Infrastructure-Engineer-Safeguards-San-Francisco-2026-08.md", "Huawei-AI-Architect-Training-Inference-Beijing-2026-08.md", "Huawei-AI-Bottom-Software-Shanghai-2026-08.md", "Huawei-AI-Algorithm-Expert-Multimodal-Beijing-2026-08.md"],
        "basis": "10 curated platform/runtime samples (8 Batch A frontier/model/infra cards + 2 Batch B ServiceNow Agent Platform cards). Employers are OpenAI, Anthropic, Huawei and ServiceNow/Moveworks; regions are US, Switzerland/Europe and China. Seniority is senior/staff; subtracks are inference, GPU/runtime, safeguards and agent-platform.",
        "priority": {"TypeScript-JavaScript":"Prerequisite", "Python":"Prerequisite", "LLM-API-and-Structured-Outputs":"Common", "Tool-Calling-and-Action-Contracts":"Specialized", "Agent-Orchestration-and-State":"Specialized", "Workflow-Automation-and-Business-Process-Design":"Specialized", "MCP-and-Agent-Interoperability":"Specialized", "Enterprise-Integrations-and-Connectors":"Common", "Agent-Evals-and-Trace-Debugging":"Specialized", "Human-in-the-Loop-and-Agent-Guardrails":"Common"},
    },
}


def extract_rows(name: str):
    return DATA.get(name, [])


def table_for(names, priority):
    counts = defaultdict(Counter)
    samples = defaultdict(set)
    for name in names:
        for row in extract_rows(name):
            skill = row["skill"]
            counts[skill][row["kind"]] += 1
            samples[skill].add(name)
    skills = list(priority)
    lines = ["| Skill | Required N | Preferred N | Responsibility N | Inferred N | Sample N | Priority | Target Depth | Confidence |", "| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |"]
    for skill in skills:
        c = counts[skill]
        total = sum(c.values())
        if total == 0:
            confidence = "context"
        elif any("low" in str(row.get("confidence")) for name in names for row in extract_rows(name) if row["skill"] == skill):
            confidence = "low/medium"
        else:
            confidence = "high/medium"
        depth = "explain/use" if priority[skill] in {"Prerequisite", "Common"} else "use→implement"
        lines.append(f"| [[{skill}]] | {c['required']} | {c['preferred']} | {c['responsibility']} | {c['inferred-prerequisite']} | {len(samples[skill])} | {priority[skill]} | {depth} | {confidence} |")
    return "\n".join(lines)


def main():
    for rel, spec in ROLE_FILES.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"(?m)^updated:\s*\d{4}-\d{2}-\d{2}", f"updated: {UPDATED}", text, count=1)
        text = re.sub(r"(?m)^sample_count:\s*\d+", f"sample_count: {spec['count']}", text, count=1)
        text = re.sub(r"(?ms)^## Sample Basis\n.*?(?=^## (?:Main Deliverables|Evidence Basis|作品证据|Responsibility Clusters))", f"## Sample Basis\n\n{spec['basis']}\n\n", text, count=1)
        start = text.find("## Skill Profile")
        if start < 0:
            raise SystemExit(f"missing Skill Profile in {rel}")
        end = text.find("\n## ", start + 4)
        if end < 0:
            raise SystemExit(f"missing section after Skill Profile in {rel}")
        table = table_for(spec["samples"], spec["priority"])
        replacement = "## Skill Profile\n\n" + table + "\n\nEvidence strength is based on Batch B row classifications; `responsibility` and `preferred` are not counted as required. Language rows with an `Alternative Group` are one-of options, not simultaneous requirements; the core capability is production programming.\n"
        text = text[:start] + replacement + text[end + 1:]
        path.write_text(text, encoding="utf-8")
    print(f"recomputed {len(ROLE_FILES)} role profiles")


if __name__ == "__main__":
    main()
