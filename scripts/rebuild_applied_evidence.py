#!/usr/bin/env python3
"""Rebuild the Batch B Applied AI job cards from section-bound evidence.

The manifest is intentionally small: it records short, source-section-bound
signals rather than copying job descriptions.  It also makes the evidence
matrix reproducible from the cards themselves.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
JOB_DIR = ROOT / "02-Jobs" / "2026-08"
UPDATED = "2026-08-31"
ALLOWED = {"required", "preferred", "responsibility", "inferred-prerequisite"}


def E(raw: str, skill: str, kind: str, depth: str = "implement", confidence: str = "high", alt: str = "", section: str = "Responsibilities", note: str = ""):
    assert kind in ALLOWED
    return {"raw": raw, "skill": skill, "kind": kind, "strength": "explicit" if kind != "inferred-prerequisite" else "inferred", "alt": alt, "depth": depth, "confidence": confidence, "section": section, "note": note}


J = "[["
R = "]]"

# Evidence is audited per job.  A responsibility is never promoted to a
# candidate requirement merely because it is technically interesting.
DATA = {
"Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md": [
 E("Requirements: Python, TypeScript, or Go", "Python", "required", alt="language-1", section="Requirements", note="one-of language alternative; do not count all three"),
 E("Requirements: Python, TypeScript, or Go", "TypeScript-JavaScript", "required", alt="language-1", section="Requirements", note="one-of language alternative; do not count all three"),
 E("Responsibilities: foundational components for multi-agent systems", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Responsibilities: adopt MCP/A2A and connect enterprise agents", "MCP-and-Agent-Interoperability", "responsibility", section="Responsibilities"),
 E("Responsibilities: reliability, cost and latency for a 4-9s service", "Enterprise-Integrations-and-Connectors", "responsibility", section="Responsibilities"),
 E("Preferred: observability, vector databases and secure model communication", "Agent-Evals-and-Trace-Debugging", "preferred", depth="use", section="Preferred", note="preferred signal, not a hard gate"),
 E("Preferred: MCP architecture and A2A protocol familiarity", "Tool-Calling-and-Action-Contracts", "preferred", depth="use", section="Preferred", note="tool contracts are a related foundation"),
],
"Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md": [
 E("Requirements: 15+ years and production AI/ML delivery", "LLM-API-and-Structured-Outputs", "required", section="Requirements"),
 E("Requirements: Python, JavaScript, APIs and microservices", "Python", "required", alt="language-1", section="Requirements", note="language-1 is an alternative; choose one primary language"),
 E("Requirements: Python, JavaScript, APIs and microservices", "TypeScript-JavaScript", "required", alt="language-1", section="Requirements", note="language-1 is an alternative; JavaScript is the one-of signal"),
 E("Requirements: Python, JavaScript, APIs and microservices", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Responsibilities: design and deploy AI/ML solutions with Rovo", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: continuous evaluation and monitoring", "Agent-Evals-and-Trace-Debugging", "responsibility", depth="use", section="Responsibilities"),
 E("Requirements: AI risk, privacy and GDPR compliance", "Human-in-the-Loop-and-Agent-Guardrails", "required", depth="use", section="Requirements"),
],
"Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md": [
 E("Historical pre-audit: AI-native workflow and Rovo architecture", "Workflow-Automation-and-Business-Process-Design", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (page shell only)", note="URL is a career shell; historical lead only"),
 E("Historical pre-audit: governance and identity integration", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (page shell only)", note="not a current requirement"),
 E("Historical pre-audit: approval and policy controls", "Human-in-the-Loop-and-Agent-Guardrails", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (page shell only)", note="not a current requirement"),
],
"Notion-Software-Engineer-AI-Workflows-2026-08.md": [
 E("Requirements: strong software engineering in TypeScript/JavaScript", "TypeScript-JavaScript", "required", section="Requirements"),
 E("Requirements: backend services, APIs and relational data", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Requirements: production LLM applications and embeddings", "LLM-API-and-Structured-Outputs", "required", section="Requirements"),
 E("Responsibilities: custom agents and recurring or asynchronous workflows", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Responsibilities: schedule and resume long-running AI workflows", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Inferred prerequisite: validate tool inputs before mutating relational data", "Tool-Calling-and-Action-Contracts", "inferred-prerequisite", depth="use", section="Learning prerequisite inference", note="derived from explicit data mutation duty"),
],
"Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md": [
 E("Requirements: language/API/integration experience and customer discovery", "TypeScript-JavaScript", "required", section="Requirements"),
 E("Requirements: language/API/integration experience and customer discovery", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Requirements: debug production integrations with customers", "Agent-Evals-and-Trace-Debugging", "required", depth="use", section="Requirements"),
 E("Responsibilities: ship production agents and Agent APIs", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Responsibilities: configure automation and data pipelines", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: expose tools through MCP with permissions", "MCP-and-Agent-Interoperability", "responsibility", depth="use", section="Responsibilities"),
 E("Preferred: MCP or comparable agent interoperability", "MCP-and-Agent-Interoperability", "preferred", depth="use", section="Preferred", note="preferred/role exposure; not a universal gate"),
 E("Inferred prerequisite: retrieval and grounding for enterprise data", "RAG", "inferred-prerequisite", depth="explain", section="Learning prerequisite inference"),
],
"Notion-Forward-Deployed-Architect-Japan-2026-08.md": [
 E("Requirements: architecture, discovery and clear customer communication", "Enterprise-Integrations-and-Connectors", "required", depth="use", section="Requirements"),
 E("Requirements: implement APIs and integrations for business teams", "LLM-API-and-Structured-Outputs", "required", section="Requirements"),
 E("Responsibilities: design custom agents, automations and AI-native workflows", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: guide adoption through Developer Platform and MCP", "MCP-and-Agent-Interoperability", "responsibility", depth="use", section="Responsibilities"),
 E("Responsibilities: establish governance and outcome measurement", "Human-in-the-Loop-and-Agent-Guardrails", "responsibility", depth="use", section="Responsibilities"),
 E("Preferred: agent orchestration and state-modeling experience", "Agent-Orchestration-and-State", "preferred", depth="use", section="Preferred"),
],
"Glean-Software-Engineer-Agents-2026-08.md": [
 E("Requirements: production frontend/backend software engineering", "TypeScript-JavaScript", "required", section="Requirements"),
 E("Requirements: build and ship reliable software", "Enterprise-Integrations-and-Connectors", "required", depth="use", section="Requirements"),
 E("Responsibilities: build, evaluate, improve, deploy and operate agents", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Responsibilities: use eval feedback to improve agent quality", "Agent-Evals-and-Trace-Debugging", "responsibility", section="Responsibilities"),
 E("Responsibilities: provide guardrails, visibility and trust", "Human-in-the-Loop-and-Agent-Guardrails", "responsibility", section="Responsibilities"),
 E("Preferred: LLM prompting and structured output experience", "LLM-API-and-Structured-Outputs", "preferred", depth="use", section="Preferred"),
],
"Glean-Founding-Forward-Deployed-Engineer-2026-08.md": [
 E("Historical pre-audit: customer discovery and 0-to-1 production AI", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (redirected error)", note="URL now redirects to a job-board error"),
 E("Historical pre-audit: full-stack delivery for enterprise outcomes", "TypeScript-JavaScript", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (redirected error)"),
 E("Historical pre-audit: prompt, agent and eval iteration", "Agent-Evals-and-Trace-Debugging", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (redirected error)"),
],
"Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md": [
 E("Requirements: customer-facing engineering and production delivery", "Enterprise-Integrations-and-Connectors", "required", confidence="medium", section="Requirements"),
 E("Responsibilities: connect Agentforce actions, prompts and tool calls", "Tool-Calling-and-Action-Contracts", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: integrate customer systems and data pipelines", "Enterprise-Integrations-and-Connectors", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: instrument production observability", "Agent-Evals-and-Trace-Debugging", "responsibility", depth="use", confidence="medium", section="Responsibilities"),
 E("Preferred: workflow automation and approval-aware delivery", "Workflow-Automation-and-Business-Process-Design", "preferred", depth="use", confidence="medium", section="Preferred"),
 E("Inferred prerequisite: safe action execution with customer permissions", "Human-in-the-Loop-and-Agent-Guardrails", "inferred-prerequisite", depth="use", confidence="medium", section="Learning prerequisite inference"),
],
"Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md": [
 E("Requirements: supply-chain domain discovery and customer delivery", "Enterprise-Integrations-and-Connectors", "required", confidence="medium", section="Requirements"),
 E("Responsibilities: build supply-chain process automation Blueprints", "Workflow-Automation-and-Business-Process-Design", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: connect enterprise systems and data", "Enterprise-Integrations-and-Connectors", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: use feedback loops to measure business value", "Agent-Evals-and-Trace-Debugging", "responsibility", depth="use", confidence="medium", section="Responsibilities"),
 E("Preferred: action contracts for bounded automation", "Tool-Calling-and-Action-Contracts", "preferred", depth="use", confidence="medium", section="Preferred"),
 E("Inferred prerequisite: approvals and rollback for process changes", "Human-in-the-Loop-and-Agent-Guardrails", "inferred-prerequisite", depth="use", confidence="medium", section="Learning prerequisite inference"),
],
"Salesforce-Success-Architect-Agentforce-2026-08.md": [
 E("Requirements: enterprise architecture and customer success delivery", "Enterprise-Integrations-and-Connectors", "required", confidence="medium", section="Requirements"),
 E("Responsibilities: design Agentforce/Data Cloud orchestration", "Agent-Orchestration-and-State", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: model automations around adoption outcomes", "Workflow-Automation-and-Business-Process-Design", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: manage permissions and human approvals", "Human-in-the-Loop-and-Agent-Guardrails", "responsibility", depth="use", confidence="medium", section="Responsibilities"),
 E("Preferred: production eval and feedback loops", "Agent-Evals-and-Trace-Debugging", "preferred", depth="use", confidence="medium", section="Preferred"),
],
"Salesforce-Product-Manager-Agent-Fabric-2026-08.md": [
 E("Requirements: product/platform strategy and policy governance", "Human-in-the-Loop-and-Agent-Guardrails", "required", depth="use", confidence="medium", section="Requirements"),
 E("Responsibilities: own Discover, Govern, Orchestrate and Observe", "Agent-Orchestration-and-State", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: manage agent/API/MCP interoperability", "MCP-and-Agent-Interoperability", "responsibility", depth="use", confidence="medium", section="Responsibilities"),
 E("Responsibilities: define control-plane integrations and APIs", "Enterprise-Integrations-and-Connectors", "responsibility", confidence="medium", section="Responsibilities"),
 E("Preferred: evaluation metrics and trace-based quality reviews", "Agent-Evals-and-Trace-Debugging", "preferred", depth="use", confidence="medium", section="Preferred"),
 E("Inferred prerequisite: structured model outputs for policy decisions", "LLM-API-and-Structured-Outputs", "inferred-prerequisite", depth="use", confidence="medium", section="Learning prerequisite inference"),
],
"ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md": [
 E("Historical/limited signal: backend or infrastructure engineering context", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="recognize", confidence="low", section="Historical summary (403)"),
 E("Responsibilities: take process agents from solution to launch", "Workflow-Automation-and-Business-Process-Design", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: configure tools and tune agent behavior", "Tool-Calling-and-Action-Contracts", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: handle enterprise LLM/API integration", "LLM-API-and-Structured-Outputs", "responsibility", confidence="low", section="Responsibilities"),
 E("Inferred prerequisite: production backend and customer integration skills", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="use", confidence="low", section="Learning prerequisite inference"),
],
"ServiceNow-Senior-Staff-Agent-Development-2026-08.md": [
 E("Historical/limited signal: Python or Go backend development", "Python", "inferred-prerequisite", depth="use", confidence="low", section="Historical summary (403)"),
 E("Historical/limited signal: distributed systems and async/concurrency", "Agent-Orchestration-and-State", "inferred-prerequisite", depth="use", confidence="low", section="Historical summary (403)"),
 E("Responsibilities: multi-agent planning, tool calling, memory and recovery", "Agent-Orchestration-and-State", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: produce structured outputs in production agents", "LLM-API-and-Structured-Outputs", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: evaluate agent trajectories and failures", "Agent-Evals-and-Trace-Debugging", "responsibility", confidence="low", section="Responsibilities"),
 E("Inferred prerequisite: Redis/DynamoDB/gRPC-style service integration", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="use", confidence="low", section="Learning prerequisite inference"),
],
"ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md": [
 E("Historical/limited signal: state-machine and distributed backend design", "Agent-Orchestration-and-State", "inferred-prerequisite", depth="use", confidence="low", section="Historical summary (403)"),
 E("Historical/limited signal: Python/Go and async event systems", "Python", "inferred-prerequisite", depth="use", confidence="low", section="Historical summary (403)"),
 E("Responsibilities: long sessions, checkpoints, resume and cancellation", "Agent-Orchestration-and-State", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: invoke tools and wait for human input", "Tool-Calling-and-Action-Contracts", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: event-driven workflows and partial recovery", "Workflow-Automation-and-Business-Process-Design", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: observe orchestration traces", "Agent-Evals-and-Trace-Debugging", "responsibility", confidence="low", section="Responsibilities"),
 E("Inferred prerequisite: Redis/DynamoDB/gRPC integration", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="use", confidence="low", section="Learning prerequisite inference"),
],
"ServiceNow-Staff-Agent-Eval-Platform-2026-08.md": [
 E("Historical/limited signal: software, ML/evaluation or infrastructure background", "Agent-Evals-and-Trace-Debugging", "inferred-prerequisite", depth="use", confidence="low", section="Historical summary (403)", note="candidate background inference; not a current required label"),
 E("Responsibilities: build an evaluation platform around real state and trajectories", "Agent-Evals-and-Trace-Debugging", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: implement rubrics, judges and human calibration", "Human-in-the-Loop-and-Agent-Guardrails", "responsibility", confidence="low", section="Responsibilities"),
 E("Responsibilities: compare tool selection and state transitions", "Tool-Calling-and-Action-Contracts", "responsibility", confidence="low", section="Responsibilities"),
 E("Inferred prerequisite: instrument services and store reproducible traces", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="use", confidence="low", section="Learning prerequisite inference"),
],
"Ramp-Applied-AI-Engineer-2026-08.md": [
 E("Requirements: production Python and/or TypeScript full-stack engineering", "Python", "required", alt="language-1", section="Requirements", note="one-of primary implementation language"),
 E("Requirements: production Python and/or TypeScript full-stack engineering", "TypeScript-JavaScript", "required", alt="language-1", section="Requirements", note="one-of primary implementation language"),
 E("Requirements: build LLM-backed products with structured extraction", "LLM-API-and-Structured-Outputs", "required", section="Requirements"),
 E("Responsibilities: agents, RAG and internal tools in production", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Responsibilities: connect backend services and product surfaces", "Enterprise-Integrations-and-Connectors", "responsibility", section="Responsibilities"),
 E("Responsibilities: define safe tool calls and recoverable actions", "Tool-Calling-and-Action-Contracts", "responsibility", depth="use", section="Responsibilities"),
 E("Inferred prerequisite: grounded retrieval for domain data", "RAG", "inferred-prerequisite", depth="explain", section="Learning prerequisite inference"),
],
"Ramp-Software-Engineer-Enterprise-Product-2026-08.md": [
 E("Requirements: software engineering for customer-facing enterprise product", "TypeScript-JavaScript", "required", section="Requirements"),
 E("Requirements: APIs and product integrations", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Responsibilities: deliver end-to-end agentic product workflows", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: coordinate agents with deterministic product logic", "Agent-Orchestration-and-State", "responsibility", section="Responsibilities"),
 E("Inferred prerequisite: approval checkpoints for enterprise actions", "Human-in-the-Loop-and-Agent-Guardrails", "inferred-prerequisite", depth="use", section="Learning prerequisite inference"),
],
"Ramp-Software-Engineer-Frontend-Revenue-2026-08.md": [
 E("Requirements: TypeScript/React frontend engineering", "TypeScript-JavaScript", "required", section="Requirements"),
 E("Requirements: production UI and API integration", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Responsibilities: expose workflow and approval UX", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: safely invoke actions from product UI", "Human-in-the-Loop-and-Agent-Guardrails", "responsibility", depth="use", section="Responsibilities"),
 E("Inferred prerequisite: consume typed LLM responses in the UI", "LLM-API-and-Structured-Outputs", "inferred-prerequisite", depth="use", section="Learning prerequisite inference"),
],
"Zapier-Engineer-Applied-AI-2026-08.md": [
 E("Requirements: reusable TypeScript and/or Python tooling", "TypeScript-JavaScript", "required", alt="language-1", section="Requirements", note="one-of implementation language"),
 E("Requirements: reusable TypeScript and/or Python tooling", "Python", "required", alt="language-1", section="Requirements", note="one-of implementation language"),
 E("Responsibilities: build internal workflow and LLM proxy services", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: integrate APIs and model providers", "LLM-API-and-Structured-Outputs", "responsibility", section="Responsibilities"),
 E("Responsibilities: monitor latency, cost and quality", "Agent-Evals-and-Trace-Debugging", "responsibility", depth="use", section="Responsibilities"),
 E("Preferred: safety, reliability and evaluation experience", "Human-in-the-Loop-and-Agent-Guardrails", "preferred", depth="use", section="Preferred"),
],
"Front-AI-Engineer-GTM-Operations-2026-08.md": [
 E("Historical/limited signal: Python async services and structured data", "Python", "inferred-prerequisite", depth="use", confidence="medium", section="Historical summary (dynamic ATS)", note="page is dynamic; treat as learning lead, not current required"),
 E("Historical/limited signal: production APIs and logging", "Enterprise-Integrations-and-Connectors", "inferred-prerequisite", depth="use", confidence="medium", section="Historical summary (dynamic ATS)", note="page is dynamic; treat as learning lead, not current required"),
 E("Responsibilities: automate GTM operations with Workato/Zapier", "Workflow-Automation-and-Business-Process-Design", "responsibility", confidence="medium", section="Responsibilities"),
 E("Responsibilities: expose model workflows through APIs and MCP", "MCP-and-Agent-Interoperability", "responsibility", depth="use", confidence="medium", section="Responsibilities"),
 E("Preferred: Snowflake and RAG/structured data experience", "RAG", "preferred", depth="use", confidence="medium", section="Preferred"),
 E("Inferred prerequisite: typed model responses for downstream automation", "LLM-API-and-Structured-Outputs", "inferred-prerequisite", depth="use", confidence="medium", section="Learning prerequisite inference"),
],
"Warp-Forward-Deployed-Engineer-2026-08.md": [
 E("Requirements: customer-facing implementation and systems integration", "Enterprise-Integrations-and-Connectors", "required", section="Requirements"),
 E("Responsibilities: configure workflows, triggers, sandbox and secrets", "Workflow-Automation-and-Business-Process-Design", "responsibility", section="Responsibilities"),
 E("Responsibilities: implement prompts, skills, MCP and integrations", "MCP-and-Agent-Interoperability", "responsibility", depth="use", section="Responsibilities"),
 E("Responsibilities: harden deployments with observability", "Agent-Evals-and-Trace-Debugging", "responsibility", depth="use", section="Responsibilities"),
 E("Responsibilities: invoke bounded tools with customer permissions", "Tool-Calling-and-Action-Contracts", "responsibility", depth="use", section="Responsibilities"),
 E("Inferred prerequisite: typed LLM responses and failure handling", "LLM-API-and-Structured-Outputs", "inferred-prerequisite", depth="use", section="Learning prerequisite inference"),
],
}


def replace_frontmatter(text: str, status: str, access: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    raw = text[4:end]
    lines = []
    seen = set()
    for line in raw.splitlines():
        if re.match(r"^(updated|source_status|source_access):", line):
            key = line.split(":", 1)[0]
            value = {"updated": UPDATED, "source_status": status, "source_access": access}[key]
            lines.append(f"{key}: {value}")
            seen.add(key)
        else:
            lines.append(line)
    for key, value in (("updated", UPDATED), ("source_status", status), ("source_access", access)):
        if key not in seen and not any(line.startswith(key + ":") for line in lines):
            lines.append(f"{key}: {value}")
    return "---\n" + "\n".join(lines) + "\n---\n"


def link(skill: str) -> str:
    return f"[[{skill}]]"


def render(path: Path, rows: list[dict]) -> str:
    old = path.read_text(encoding="utf-8")
    fm_end = old.find("\n---", 4)
    fm = old[4:fm_end]
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", fm, re.M))
    status = meta.get("source_status", "active")
    access = meta.get("source_access", "full")
    # Keep expired/redirected/403 labels as audited source-access facts.
    head = replace_frontmatter(old, status, access)
    title = meta.get("company", path.stem) + " — " + meta.get("role_title", path.stem)
    summary = {
        "Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md": "管理企业 Agentic AI 集成，重点是多代理基础组件、互操作协议与可观测可靠性。",
        "Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md": "面向客户交付 Rovo 驱动的 AI/ML、API 集成和合规落地。",
        "Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md": "当前页面仅剩职业站外壳；保留 AI-native workflow 与治理线索作为历史参考。",
        "Notion-Software-Engineer-AI-Workflows-2026-08.md": "构建带有 LLM、嵌入、关系数据的全栈与异步 AI 工作流。",
        "Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md": "把 Agent API、MCP、自动化和数据管道交付到日本企业场景。",
        "Notion-Forward-Deployed-Architect-Japan-2026-08.md": "设计 AI-native workflow、定制代理、Developer Platform 与治理采用方案。",
        "Glean-Software-Engineer-Agents-2026-08.md": "构建、评估、部署和运营面向质量、信任、延迟与成本的代理。",
        "Glean-Founding-Forward-Deployed-Engineer-2026-08.md": "当前链接为 job-board error；历史线索指向 0-to-1 企业 AI 交付。",
        "Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md": "把 Agentforce action、prompt、reasoning 与客户系统连接并生产化。",
        "Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md": "围绕供应链业务设计自动化 Blueprint，并用反馈衡量价值。",
        "Salesforce-Success-Architect-Agentforce-2026-08.md": "设计 Agentforce/Data Cloud 编排、自动化和企业采用交付。",
        "Salesforce-Product-Manager-Agent-Fabric-2026-08.md": "负责 Agent Fabric 的 Discover、Govern、Orchestrate、Observe 控制面。",
        "ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md": "页面返回 403；历史信号是从方案、构建、调优到上线的流程代理生命周期。",
        "ServiceNow-Senior-Staff-Agent-Development-2026-08.md": "页面返回 403；历史信号聚焦生产代理、多代理规划、记忆和恢复。",
        "ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md": "页面返回 403；历史信号聚焦状态机、长会话、事件与检查点。",
        "ServiceNow-Staff-Agent-Eval-Platform-2026-08.md": "页面返回 403；历史信号聚焦真实状态、轨迹、评审器与人工校准的平台。",
        "Ramp-Applied-AI-Engineer-2026-08.md": "构建代理、RAG、结构化抽取与生产 LLM 后端。",
        "Ramp-Software-Engineer-Enterprise-Product-2026-08.md": "面向企业产品交付端到端的 agentic workflow 与 API 集成。",
        "Ramp-Software-Engineer-Frontend-Revenue-2026-08.md": "以前端 TypeScript/React 连接生产 UI、API、工作流和审批体验。",
        "Zapier-Engineer-Applied-AI-2026-08.md": "为内部工作流构建 LLM proxy、API、可观测性、评估和复用工具。",
        "Front-AI-Engineer-GTM-Operations-2026-08.md": "动态 ATS 页面；历史可见信号是 Python async、自动化、API、MCP 与结构化数据。",
        "Warp-Forward-Deployed-Engineer-2026-08.md": "端到端实施企业 workflow、trigger、sandbox、secret、MCP 和加固。",
    }.get(path.name, "结构化保留的岗位证据卡；请以来源页面为准。")
    if status == "expired":
        access_note = "当前来源已过期或重定向失败；所有历史线索仅作学习前置，不代表当前招聘要求。"
    elif "403" in access or "limited" in access or "dynamic" in access:
        access_note = "当前页面访问受限或动态渲染；低/中置信度线索不升级为高置信必需项。"
    else:
        access_note = "当前官方页面可访问；短证据按 Requirements/Preferred/Responsibilities 原段落分类。"
    responsibilities = [r for r in rows if r["kind"] == "responsibility"]
    required = [r for r in rows if r["kind"] == "required"]
    preferred = [r for r in rows if r["kind"] == "preferred"]
    inferred = [r for r in rows if r["kind"] == "inferred-prerequisite"]
    def bullets(items, fallback):
        return "\n".join(f"- {x['raw']}" for x in items) if items else f"- {fallback}"
    family_map = {"ai-application-engineering": "AI-Application-Engineer", "field-deployment": "AI-Solutions-Architect-and-FDE", "product": "AI-Product-Manager", "ai-product-management": "AI-Product-Manager", "ai-infrastructure": "AI-Infrastructure-and-Inference-Engineer", "agent-platform": "AI-Infrastructure-and-Inference-Engineer"}
    mapped_family = family_map.get(meta.get("role_family", ""), "AI-Application-Engineer")
    out = [head, f"# {title}", "", "## Source Scope", f"官方职位 URL：[{meta.get('source_url','')}]({meta.get('source_url','')})。2026-08-31 访问记录：`{status}` / `{access}`。{access_note}", "本卡只保留短证据与学习映射，不复制完整 JD。", "", "## Role Summary", summary, "", "## Responsibilities", bullets(responsibilities, "来源未提供可复核的职责段；不做当前职责推断。"), "", "## Explicit Requirements", bullets(required, "当前可复核要求有限；不要把职责或历史摘要当作 required。"), "", "## Preferred/Nice-to-have", bullets(preferred, "未从当前来源确认 preferred 项。"), "", "## Skill Extraction", "证据类型只允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`；`required`/`preferred` 来自官方资格段，`responsibility` 来自职责段，`inferred-prerequisite` 仅用于学习前置推断。Alternative Group 中的成员是 one-of，不同时计入要求。", "", "| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        alt = r["alt"] or "—"
        note = r["note"] or "同一岗位只计一次；职责频率不等于候选人要求频率。"
        out.append(f"| {r['raw']} | {link(r['skill'])} | {r['kind']} | {r['strength']} | {alt} | {r['depth']} | {r['confidence']} |")
    out += ["", "## Non-skill Gates", "年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。", "", "## Role Mapping", f"- Primary [[{mapped_family}]]", "", "## Limitations", access_note, "", "## Evidence Trace"]
    for i, r in enumerate(rows, 1):
        out += [f"### Evidence {i}", f"Source Section: {r['section']}", f"Raw Evidence: {r['raw']}", f"Mapped Skill: {link(r['skill'])}", f"Evidence Type: {r['kind']}", f"Requirement Strength: {r['strength']}", f"Alternative Group: {r['alt'] or 'none'}", f"Depth Signal: {r['depth']}", f"Confidence: {r['confidence']}", f"Extraction Decision: map only this source-bound signal; preserve responsibility/requirement distinction", f"Notes: {r['note'] or '短证据与映射保持一一对应；不把摘要复制成多条假证据。'}", ""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    missing = sorted(set(DATA) - {p.name for p in JOB_DIR.glob("*.md")})
    if missing:
        raise SystemExit("missing job files: " + ", ".join(missing))
    for name, rows in DATA.items():
        path = JOB_DIR / name
        path.write_text(render(path, rows), encoding="utf-8")
    counts = Counter()
    samples = defaultdict(set)
    alternatives = set()
    for name, rows in DATA.items():
        for r in rows:
            counts[(r["skill"], r["kind"])] += 1
            samples[r["skill"]].add(name)
            if r["alt"]:
                alternatives.add((name, r["alt"]))
    print(f"rewrote {len(DATA)} applied job cards")
    for skill in sorted(samples):
        vals = ", ".join(f"{kind}={counts[(skill, kind)]}" for kind in sorted(ALLOWED))
        print(f"{skill}: {vals}; samples={len(samples[skill])}")
    print(f"alternative groups={len(alternatives)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
