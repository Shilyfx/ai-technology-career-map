#!/usr/bin/env python3
"""Rebuild Batch B cards from source-bound, one-fact evidence rows.

This script reproduces audited evidence. It must not invent or normalize
evidence without source review.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
JOB_DIR = ROOT / "02-Jobs" / "2026-08"
UPDATED = "2026-09-01"

# file | type | skill | source section | raw evidence | confidence | alt | fidelity | mapping rationale
ROWS = r'''
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Python|Requirements|Proficiency in Python, TypeScript, or Go|high|language-1|direct|Python is one member of the explicit language alternative.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|TypeScript-JavaScript|Requirements|Proficiency in Python, TypeScript, or Go|high|language-1|direct|TypeScript is one member of the explicit language alternative.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Model-Serving|Requirements|Hands-on experience with AI/ML platform engineering and model serving|high|||close-paraphrase|Platform engineering and model serving are explicit serving-system signals.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Agent-Orchestration-and-State|Requirements|Hands-on experience with agent frameworks such as LangChain or Semantic Kernel|high|||close-paraphrase|Agent frameworks are an explicit implementation signal for orchestration and state.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Distributed-Systems|Requirements|Experience with high-scale distributed systems|high|||direct|The requirement explicitly names distributed systems.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Databases-and-Data-Modeling|Requirements|Experience with vector databases|high|||direct|Vector databases are database/data-model work; the source does not claim a RAG workflow.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|required|Observability|Requirements|Experience with observability pipelines|high|||direct|Observability pipelines are an explicit operational requirement.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|responsibility|Agent-Orchestration-and-State|Key Responsibilities|Deliver foundational components for multi-agent systems|high|||direct|The responsibility is directly about multi-agent runtime components.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|responsibility|MCP-and-Agent-Interoperability|Key Responsibilities|Lead adoption of protocols like MCP and A2A|high|||direct|MCP/A2A are interoperability protocols, not automatically tool-calling contracts.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|responsibility|Observability|Key Responsibilities|Maintain high-reliability services while optimizing cost and latency|high|||close-paraphrase|Reliability, cost, and latency are operational measurement concerns, not agent evaluation by themselves.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|preferred|MCP-and-Agent-Interoperability|Preferred Skills|Familiarity with MCP architecture and the A2A specification|high|||direct|The preferred item explicitly names MCP/A2A interoperability.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|preferred|Enterprise-Integrations-and-Connectors|Preferred Skills|Experience with enterprise integration patterns and API governance|high|||direct|Enterprise integration patterns and API governance match the connector skill.
Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md|preferred|Security-Privacy-and-Access-Control|Preferred Skills|Experience with secure model-to-model communication|high|||close-paraphrase|Secure model communication is an explicit security signal.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|responsibility|LLM-API-and-Structured-Outputs|What You'll Do|Lead design, development, and deployment of AI/ML-powered solutions using Rovo|high|||close-paraphrase|Applied AI/ML delivery is explicit, but structured output is not asserted.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|required|Python|On the first day, we'll expect you to have|Proficiency in Python, JavaScript, or similar languages|high|language-1|direct|Python is one explicit language alternative.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|required|TypeScript-JavaScript|On the first day, we'll expect you to have|Proficiency in Python, JavaScript, or similar languages|high|language-1|direct|JavaScript is one explicit language alternative.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|required|HTTP-API|On the first day, we'll expect you to have|Application integrations with APIs and microservices|high|||close-paraphrase|APIs and microservices are an explicit service-integration signal.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|required|Enterprise-Integrations-and-Connectors|On the first day, we'll expect you to have|Application integrations with enterprise-scale systems|high|||direct|Enterprise-scale integration is explicitly required.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|What You'll Do|Champion AI-augmented workflow automation in customer environments|high|||direct|The source explicitly assigns workflow-automation adoption.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|responsibility|Agent-Evals-and-Trace-Debugging|What You'll Do|Ensure continuous evaluation and improvement|high|||close-paraphrase|Continuous evaluation is an explicit agent-quality signal.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|responsibility|Observability|What You'll Do|Ensure continuous monitoring and improvement|high|||close-paraphrase|Monitoring is observability and is kept separate from evaluation.
Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md|responsibility|Security-Privacy-and-Access-Control|What You'll Do|Navigate AI risk assessment, data privacy, and GDPR requirements|high|||direct|Risk, privacy, and compliance are explicit security responsibilities.
Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md|inferred-prerequisite|Workflow-Automation-and-Business-Process-Design|Historical summary (page shell only)|Historical lead: AI-native workflow and Rovo architecture|low||inferred|The page is a historical shell; this is a learning lead, not a current requirement.
Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md|inferred-prerequisite|Human-in-the-Loop-and-Agent-Guardrails|Historical summary (page shell only)|Historical lead: approval and policy controls|low||inferred|Approval and policy controls are a study lead, but the source no longer exposes a role body.
Notion-Software-Engineer-AI-Workflows-2026-08.md|required|LLM-API-and-Structured-Outputs|Skills You'll Need to Bring|Experience building AI products using LLMs, embeddings, and other ML technologies|medium|||direct|LLMs are explicit; structured outputs are not asserted.
Notion-Software-Engineer-AI-Workflows-2026-08.md|required|Databases-and-Data-Modeling|Skills You'll Need to Bring|Familiarity with relational databases such as Postgres or MySQL|medium|||direct|Relational database experience is explicitly required.
Notion-Software-Engineer-AI-Workflows-2026-08.md|responsibility|Agent-Orchestration-and-State|About the Role|Custom Agents automate recurring workflows such as filing tasks, writing reports, and answering knowledge-base questions|medium|||close-paraphrase|The role context explicitly describes custom agents executing recurring workflows.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|required|Python|Skills You'll Need to Bring|Proficiency in at least one programming language such as Java, JavaScript, Node.js, SQL, or Python|medium|language-1|direct|Python is one member of the explicit at-least-one language set.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|required|TypeScript-JavaScript|Skills You'll Need to Bring|Proficiency in at least one programming language such as Java, JavaScript, Node.js, SQL, or Python|medium|language-1|direct|JavaScript is represented by the existing TypeScript-JavaScript skill.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|required|HTTP-API|Skills You'll Need to Bring|Hands-on experience with APIs|medium|||direct|The source explicitly requires APIs.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|required|Enterprise-Integrations-and-Connectors|Skills You'll Need to Bring|Hands-on experience with data integration|medium|||direct|The source explicitly requires data integration.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|required|Software-Design-and-Architecture|Skills You'll Need to Bring|Lead technical discovery, assess feasibility, identify risks, and translate ambiguity into an executable plan|medium|||close-paraphrase|Discovery, feasibility, risk, and executable planning are architecture/design activities.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|responsibility|Agent-Orchestration-and-State|About The Role|Design and deploy production-grade custom agents|medium|||close-paraphrase|Custom agents are explicit delivery responsibility.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|responsibility|MCP-and-Agent-Interoperability|About The Role|Use MCP and Agent APIs in production-grade deployments|medium|||close-paraphrase|MCP is explicitly named as the interoperability mechanism.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|About The Role|Design and deploy production-grade AI workflows|medium|||close-paraphrase|AI workflows are explicitly part of delivery scope.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|preferred|MCP-and-Agent-Interoperability|Nice to Haves|AI-powered workflows including MCPs|medium|||direct|MCP is explicitly preferred, not inferred.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|preferred|Prompt-and-Context-Engineering|Nice to Haves|AI-powered workflows including prompt engineering|medium|||direct|Prompt engineering is explicitly preferred.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|preferred|RAG|Nice to Haves|AI-powered workflows including retrieval/RAG systems|medium|||direct|Retrieval/RAG is explicitly preferred, not an inferred prerequisite.
Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md|preferred|Workflow-Automation-and-Business-Process-Design|Nice to Haves|AI-powered workflows including workflow orchestration|medium|||direct|Workflow orchestration is explicitly preferred.
Notion-Forward-Deployed-Architect-Japan-2026-08.md|required|Workflow-Automation-and-Business-Process-Design|Skills You'll Need to Bring|Hands-on AI builder mindset: use AI tools to design, prototype, automate, or improve real business workflows|medium|||direct|The skills section explicitly requires AI workflow building experience.
Notion-Forward-Deployed-Architect-Japan-2026-08.md|preferred|Agent-Orchestration-and-State|Nice to Haves|Experience designing or deploying Agents, automations or AI-powered workflows with Customers|medium|||direct|Agents and automations are explicitly preferred experience.
Notion-Forward-Deployed-Architect-Japan-2026-08.md|preferred|HTTP-API|Nice to Haves|Experience with APIs|medium|||direct|APIs are explicitly listed as a nice-to-have.
Notion-Forward-Deployed-Architect-Japan-2026-08.md|preferred|MCP-and-Agent-Interoperability|Nice to Haves|Experience with MCPs|medium|||direct|MCP is explicitly preferred and is an interoperability protocol.
Notion-Forward-Deployed-Architect-Japan-2026-08.md|preferred|Agent-Orchestration-and-State|Nice to Haves|Experience with coding agents and developer platform workflows|medium|||close-paraphrase|Coding agents and platform workflows are preferred orchestration exposure.
Glean-Software-Engineer-Agents-2026-08.md|required|Python|About you|Strong coding skills in Go, Python, Java, or TypeScript, with reliable, well-tested systems|high|language-1|direct|Python is one explicit language alternative.
Glean-Software-Engineer-Agents-2026-08.md|required|TypeScript-JavaScript|About you|Strong coding skills in Go, Python, Java, or TypeScript, with reliable, well-tested systems|high|language-1|direct|TypeScript is one explicit language alternative.
Glean-Software-Engineer-Agents-2026-08.md|required|Testing|About you|Reliable, well-tested systems|high|||close-paraphrase|The phrase explicitly requires well-tested systems.
Glean-Software-Engineer-Agents-2026-08.md|responsibility|Agent-Orchestration-and-State|About the Role|Build, evaluate, self-improve, deploy, and operate powerful agents|high|||direct|Agent lifecycle operation is explicit role responsibility.
Glean-Software-Engineer-Agents-2026-08.md|responsibility|Agent-Evals-and-Trace-Debugging|You will|Design and ship workflows that help users evaluate agent quality and understand failure modes|high|||direct|Agent quality evaluation and failure modes are explicit eval signals.
Glean-Software-Engineer-Agents-2026-08.md|responsibility|Human-in-the-Loop-and-Agent-Guardrails|You will|Deploy and operate agents with guardrails and controls|high|||close-paraphrase|Guardrails and controls are explicit safety concerns.
Glean-Software-Engineer-Agents-2026-08.md|responsibility|Observability|You will|Deploy and operate agents with visibility|high|||close-paraphrase|Visibility is observability and is separate from evals.
Glean-Software-Engineer-Agents-2026-08.md|preferred|Workflow-Automation-and-Business-Process-Design|About you|Experience building AI, agentic, workflow, automation, or developer-product experiences|high|||direct|Workflow and automation experience is explicitly a strong plus.
Glean-Founding-Forward-Deployed-Engineer-2026-08.md|inferred-prerequisite|Enterprise-Integrations-and-Connectors|Historical summary (redirected error)|Historical lead: customer discovery and 0-to-1 production AI delivery|low||inferred|The job URL redirects to a job-board error; the old lead is for study only.
Glean-Founding-Forward-Deployed-Engineer-2026-08.md|inferred-prerequisite|Agent-Evals-and-Trace-Debugging|Historical summary (redirected error)|Historical lead: prompt, agent, and eval iteration|low||inferred|The old summary suggested eval iteration, but the official page is no longer available.
Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md|responsibility|Tool-Calling-and-Action-Contracts|Redirected official role summary|Connect Agentforce actions, prompts, reasoning, and tool calls|medium|||close-paraphrase|The archived summary explicitly describes action/tool-call integration; the official URL redirects.
Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md|responsibility|Enterprise-Integrations-and-Connectors|Redirected official role summary|Integrate customer systems and data pipelines|medium|||close-paraphrase|Customer-system and data-pipeline integration is connector responsibility.
Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md|responsibility|Observability|Redirected official role summary|Instrument production observability|medium|||close-paraphrase|Observability is operational, not an agent-evaluation claim.
Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md|responsibility|Security-Privacy-and-Access-Control|Redirected official role summary|Execute actions with customer permissions|medium|||close-paraphrase|Permissions and safe action execution are access-control concerns.
Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Redirected official role summary|Build supply-chain process automation Blueprints|medium|||close-paraphrase|Blueprint process automation is workflow-design responsibility.
Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md|responsibility|Enterprise-Integrations-and-Connectors|Redirected official role summary|Connect enterprise systems and data|medium|||close-paraphrase|Enterprise-system/data connection is integration responsibility.
Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md|responsibility|Observability|Redirected official role summary|Use feedback loops to measure business value|medium|||close-paraphrase|Measurement feedback is kept as operational observability because no agent-quality evaluation is stated.
Salesforce-Success-Architect-Agentforce-2026-08.md|responsibility|Agent-Orchestration-and-State|Redirected official role summary|Design Agentforce/Data Cloud orchestration|medium|||close-paraphrase|The archived role summary explicitly assigns orchestration design.
Salesforce-Success-Architect-Agentforce-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Redirected official role summary|Model automations around adoption outcomes|medium|||close-paraphrase|Adoption automations are workflow-design work.
Salesforce-Success-Architect-Agentforce-2026-08.md|responsibility|Human-in-the-Loop-and-Agent-Guardrails|Redirected official role summary|Manage permissions and human approvals|medium|||close-paraphrase|Permissions and approvals directly map to guardrails/HITL.
Salesforce-Product-Manager-Agent-Fabric-2026-08.md|responsibility|Agent-Orchestration-and-State|Redirected official role summary|Own Orchestrate control-plane capabilities|medium|||close-paraphrase|Orchestrate is an explicit control-plane responsibility.
Salesforce-Product-Manager-Agent-Fabric-2026-08.md|responsibility|Observability|Redirected official role summary|Own Observe control-plane capabilities|medium|||close-paraphrase|Observe is an explicit operational responsibility.
Salesforce-Product-Manager-Agent-Fabric-2026-08.md|responsibility|MCP-and-Agent-Interoperability|Redirected official role summary|Manage agent, API, and MCP interoperability|medium|||close-paraphrase|MCP interoperability is mapped to MCP, not generic tool calling.
Salesforce-Product-Manager-Agent-Fabric-2026-08.md|responsibility|Security-Privacy-and-Access-Control|Redirected official role summary|Policy governance for agent operations|medium|||close-paraphrase|Policy governance is a security/access-control responsibility.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Core Responsibilities & Impact|Own the AI Agent delivery lifecycle: Vision-Lock, Solution Design/Architecture, Building, Tuning, and launch|high| |direct|The source explicitly assigns end-to-end workflow/agent delivery.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|Software-Design-and-Architecture|Core Responsibilities & Impact|Architect and design customer AI solutions|high|||close-paraphrase|Custom solution architecture is an explicit design responsibility.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|Enterprise-Integrations-and-Connectors|Core Responsibilities & Impact|Integrate the platform with customer enterprise systems|high|||close-paraphrase|Enterprise-system integration is explicit.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|Security-Privacy-and-Access-Control|Core Responsibilities & Impact|Integrate the platform securely with customer systems|high|||close-paraphrase|Secure integration is an explicit security concern.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|HTTP-API|About You|Strong grasp of API-based systems integration|high|||direct|The source explicitly calls out API-based integration.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|responsibility|Prompt-and-Context-Engineering|About You|LLM-based systems design including prompt engineering and context engineering|high|||direct|Prompt and context engineering are explicit system-design duties.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|required|Workflow-Automation-and-Business-Process-Design|Qualifications|Build full-stack workflows and automations|high|||close-paraphrase|Full-stack workflows and automations are an explicit qualification.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|required|HTTP-API|Qualifications|Build full-stack workflows and automations using REST APIs, iPaaS, or scripting|high|implementation-1|direct|REST APIs are one explicit implementation route.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|required|Python|Qualifications|Build full-stack workflows and automations using REST APIs, iPaaS, or Python/JavaScript/Golang scripting|high|implementation-1|direct|Python is one explicit scripting route.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|preferred|Enterprise-Integrations-and-Connectors|Preferred Qualifications|Familiarity with enterprise platforms such as ServiceNow, Jira, Zendesk, Workday, or Okta|high|||direct|Enterprise platforms are explicitly preferred integration context.
ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md|preferred|Linux|Preferred Qualifications|Familiarity with Linux and Windows environments and the command line|high|||direct|Linux command-line familiarity is explicitly preferred.
ServiceNow-Senior-Staff-Agent-Development-2026-08.md|inferred-prerequisite|Python|Historical summary (unavailable page)|Historical lead: Python or Go backend development|low||inferred|The official URL returns 404; the old summary is retained only as a study lead.
ServiceNow-Senior-Staff-Agent-Development-2026-08.md|inferred-prerequisite|Distributed-Systems|Historical summary (unavailable page)|Historical lead: distributed systems and async/concurrency|low||inferred|The page is unavailable, so this cannot support a current requirement.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|responsibility|Agent-Orchestration-and-State|What you get to do in this role|A state machine manages long-running agent sessions across planning, execution, and user interaction|high|||direct|The source explicitly describes an agent orchestration state machine.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|responsibility|Agent-Orchestration-and-State|What you get to do in this role|Distributed session management uses DynamoDB leases, heartbeats, crash recovery, and checkpointing|high|||direct|Checkpointed session state is explicit orchestration responsibility.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|responsibility|Distributed-Systems|What you get to do in this role|Event-driven message pipelines use SQS, Kafka, and gRPC/Socket.IO|high|||direct|Queues and streaming are explicit distributed-systems work.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|responsibility|Python|What you get to do in this role|Structured concurrency uses Python asyncio TaskGroups and cancellation|high|||direct|Python asyncio is explicit implementation responsibility; the source also names Go.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|responsibility|Observability|What you get to do in this role|OpenTelemetry instrumentation and distributed trace context propagation|high|||direct|OpenTelemetry and tracing are explicit observability signals.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|required|Distributed-Systems|Qualifications|Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf|high|areas-3-of-6|direct|Distributed systems is one of six areas from which the source requires at least three.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|required|Observability|Qualifications|Deep experience in distributed systems, concurrency, event-driven architectures, databases, observability, or gRPC/protobuf|high|areas-3-of-6|direct|Observability is one of six explicit qualification areas.
ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md|required|Python|Required|Strong in Python or Go|high|language-2|direct|Python is one member of the explicit language alternative.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Agent-Evals-and-Trace-Debugging|The Role|Build the judgement layer: rubrics, judges, calibration against human labels, and trajectory scoring|high|||close-paraphrase|Judges, rubrics, calibration, and trajectory scoring are explicit agent-evaluation signals.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Agent-Evals-and-Trace-Debugging|Eval orchestration at scale|Execute scenarios, collect traces/final state, validate, score, and tear down|high|||close-paraphrase|The source explicitly describes an end-to-end evaluation harness.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Eval orchestration at scale|Scheduling, retries, high-concurrency execution, run isolation, and versioned reports|high|||close-paraphrase|Harness scheduling/retry runtime is workflow orchestration.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Observability|Agent observability and tracing|OpenTelemetry-native observability and a span data model for agent trajectories|high|||direct|OpenTelemetry, spans, and trajectory traces are explicit observability work.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Human-in-the-Loop-and-Agent-Guardrails|The Role|Rubrics, judges, and calibration against human labels|high|||direct|Human-label calibration is explicit human-in-the-loop activity.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|responsibility|Testing|Stateful simulation|Contract-testing mocks against real API schemas in CI|high|||direct|Contract testing is explicitly named.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|required|Distributed-Systems|Qualifications|Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf|high|areas-3-of-6|direct|Distributed systems is one of six explicit qualification areas.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|required|Observability|Qualifications|Deep experience in distributed systems, orchestration, observability, concurrency, data pipelines, or gRPC/protobuf|high|areas-3-of-6|direct|Observability is one of six explicit qualification areas.
ServiceNow-Staff-Agent-Eval-Platform-2026-08.md|required|Python|Required|Strong in Python or Go|high|language-1|direct|Python is one member of the explicit language alternative.
Ramp-Applied-AI-Engineer-2026-08.md|required|Software-Design-and-Architecture|What You Need|Proficiency in full-stack development across web frameworks, backend systems, and cloud infrastructure|medium|||direct|The qualification asks for full-stack/system design breadth.
Ramp-Applied-AI-Engineer-2026-08.md|responsibility|Agent-Orchestration-and-State|About the Role|Production use cases of LLMs including AI Agents|medium|||direct|AI-agent production work is explicit role scope.
Ramp-Applied-AI-Engineer-2026-08.md|responsibility|RAG|About the Role|Retrieval-Augmented Generation|medium|||direct|RAG is explicitly named as a project area.
Ramp-Applied-AI-Engineer-2026-08.md|responsibility|LLM-API-and-Structured-Outputs|About the Role|Structured Extraction|medium|||direct|Structured extraction is an explicit structured-output signal.
Ramp-Applied-AI-Engineer-2026-08.md|required|Distributed-Systems|What You Need|Backend systems and infrastructure that support AI-driven products|medium|||close-paraphrase|Supporting AI products with backend/infrastructure systems is a runtime/scale requirement.
Ramp-Software-Engineer-Enterprise-Product-2026-08.md|responsibility|Agent-Orchestration-and-State|About the Role|Build internal and external agents to solve customer blockers|medium|||direct|Building agents is explicit role responsibility.
Ramp-Software-Engineer-Enterprise-Product-2026-08.md|responsibility|Enterprise-Integrations-and-Connectors|About the Role|Deliver solutions end to end for the largest and most complex companies|medium|||close-paraphrase|Customer-facing end-to-end delivery implies integration context, but remains a responsibility.
Ramp-Software-Engineer-Enterprise-Product-2026-08.md|preferred|Agent-Orchestration-and-State|What You Need|Extensive experience building with and for agents|medium|||direct|Agent-building experience is explicitly preferred.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|required|TypeScript-JavaScript|What You Need|Deep frontend expertise in TypeScript and React|medium|||direct|TypeScript is explicitly required.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|responsibility|HTTP-API|What You’ll Do|Shape APIs, workflows, and data contracts behind product experiences|medium|||direct|API/data-contract work is explicit responsibility.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|responsibility|Human-in-the-Loop-and-Agent-Guardrails|What You’ll Do|Design human-in-the-loop workflows with approvals and execution status|medium|||direct|Human review and approvals are explicit HITL work.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|responsibility|Agent-Orchestration-and-State|What You Need|Interfaces for asynchronous systems with partial results, errors, retries, and user intervention|medium|||direct|Long-running async state and recovery are orchestration concerns.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|preferred|Agent-Evals-and-Trace-Debugging|Nice to Haves|Human-in-the-loop AI systems including evaluation|medium|||close-paraphrase|Evaluation is explicitly preferred agent-quality experience.
Ramp-Software-Engineer-Frontend-Revenue-2026-08.md|preferred|Human-in-the-Loop-and-Agent-Guardrails|Nice to Haves|Human-in-the-loop AI systems including review, approvals, tool execution, and recovery|medium|||close-paraphrase|Review and approvals are explicitly preferred HITL experience.
Zapier-Engineer-Applied-AI-2026-08.md|required|TypeScript-JavaScript|Requirements|Reusable TypeScript and/or Python tooling|medium|language-1|close-paraphrase|TypeScript is one explicit implementation-language alternative.
Zapier-Engineer-Applied-AI-2026-08.md|required|Python|Requirements|Reusable TypeScript and/or Python tooling|medium|language-1|close-paraphrase|Python is one explicit implementation-language alternative.
Zapier-Engineer-Applied-AI-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Responsibilities|Build internal workflow services|medium|||close-paraphrase|Internal workflows are explicit delivery work.
Zapier-Engineer-Applied-AI-2026-08.md|responsibility|LLM-API-and-Structured-Outputs|Responsibilities|Build internal LLM proxy services|medium|||close-paraphrase|LLM proxy services are API integration work; structured output is not asserted.
Zapier-Engineer-Applied-AI-2026-08.md|responsibility|Observability|Responsibilities|Monitor latency, cost, and quality|medium|||direct|Latency, cost, and monitoring are observability signals, not automatically Agent Evals.
Zapier-Engineer-Applied-AI-2026-08.md|preferred|Agent-Evals-and-Trace-Debugging|Preferred|Safety, reliability, and evaluation experience|medium|||direct|Evaluation is explicitly preferred, not inferred.
Front-AI-Engineer-GTM-Operations-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|Responsibilities|Automate GTM operations with Workato/Zapier|medium|||close-paraphrase|Automation is explicit role work.
Front-AI-Engineer-GTM-Operations-2026-08.md|responsibility|HTTP-API|Responsibilities|Expose model workflows through APIs|medium|||close-paraphrase|APIs are explicit integration work.
Front-AI-Engineer-GTM-Operations-2026-08.md|responsibility|MCP-and-Agent-Interoperability|Responsibilities|Expose model workflows through MCP|medium|||close-paraphrase|MCP is an explicit interoperability signal.
Front-AI-Engineer-GTM-Operations-2026-08.md|preferred|RAG|Preferred|Snowflake and RAG/structured data experience|medium|||direct|RAG is explicitly preferred.
Front-AI-Engineer-GTM-Operations-2026-08.md|inferred-prerequisite|Python|Historical dynamic ATS signal|Python async services and structured data|medium||inferred|The dynamic page does not expose a stable requirements section; retain this as a study lead only.
Warp-Forward-Deployed-Engineer-2026-08.md|required|Docker-Containers|You may be a good fit if...|Strong infrastructure fundamentals: Docker, CI/CD, cloud infrastructure, and container orchestration|high|||close-paraphrase|Docker/containers are explicitly required fundamentals.
Warp-Forward-Deployed-Engineer-2026-08.md|required|Linux|You may be a good fit if...|Strong infrastructure fundamentals: Linux|high|||close-paraphrase|Linux is explicitly named as an infrastructure fundamental.
Warp-Forward-Deployed-Engineer-2026-08.md|responsibility|Workflow-Automation-and-Business-Process-Design|As a Founding Forward Deployed Engineer, you will...|Architect agent workflows with triggers, webhooks, cron schedules, and API calls|high|||direct|Triggers and multi-step workflows are explicit workflow-design responsibility.
Warp-Forward-Deployed-Engineer-2026-08.md|responsibility|Security-Privacy-and-Access-Control|As a Founding Forward Deployed Engineer, you will...|Set up environments, secrets, and integrations|high|||close-paraphrase|Secrets and environment boundaries are explicit security responsibilities.
Warp-Forward-Deployed-Engineer-2026-08.md|responsibility|MCP-and-Agent-Interoperability|As a Founding Forward Deployed Engineer, you will...|Set up MCP servers and integrations|high|||close-paraphrase|MCP servers are explicit interoperability work.
Warp-Forward-Deployed-Engineer-2026-08.md|responsibility|Observability|As a Founding Forward Deployed Engineer, you will...|Debug agent runs using session sharing and observability tools|high|||direct|Observability tools support operational debugging; no eval claim is added.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|Prompt-and-Context-Engineering|You may be a good fit if...|Understand prompt engineering|high|||direct|Prompt engineering is explicit fit criteria, retained as preferred.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|Agent-Orchestration-and-State|You may be a good fit if...|Understand agent architectures|high|||direct|Agent architectures are explicit fit criteria for orchestration.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|Tool-Calling-and-Action-Contracts|You may be a good fit if...|Understand tool use|high|||direct|Tool use is explicit fit criteria for action contracts.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|Agent-Evals-and-Trace-Debugging|You may be a good fit if...|Understand evaluating non-deterministic systems|high|||direct|Evaluating non-deterministic systems is explicit eval experience.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|HTTP-API|Bonus...|Experience with APIs/SDKs, GitHub Actions, webhooks, and event-driven automation|high|||direct|APIs and webhooks are explicit integration experience.
Warp-Forward-Deployed-Engineer-2026-08.md|preferred|Security-Privacy-and-Access-Control|Bonus...|Familiarity with enterprise security and compliance requirements|high|||direct|Security/compliance is explicit bonus experience.
'''

STATUS = {
    "Atlassian-Principal-Architecture-AI-Native-Workflows-2026-08.md": ("expired", "page-shell-only"),
    "Atlassian-Senior-Engineering-Manager-Agentic-AI-Integrations-2026-08.md": ("active", "full"),
    "Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08.md": ("active", "full"),
    "Notion-Software-Engineer-AI-Workflows-2026-08.md": ("active", "dynamic-partial"),
    "Notion-Forward-Deployed-Engineer-GTM-Japan-2026-08.md": ("active", "dynamic-partial"),
    "Notion-Forward-Deployed-Architect-Japan-2026-08.md": ("active", "dynamic-partial"),
    "Glean-Software-Engineer-Agents-2026-08.md": ("active", "full"),
    "Glean-Founding-Forward-Deployed-Engineer-2026-08.md": ("expired", "page-shell-only"),
    "Salesforce-Forward-Deployed-Engineer-Agentforce-2026-08.md": ("redirected", "partial"),
    "Salesforce-Forward-Deployed-Engineer-Supply-Chain-2026-08.md": ("redirected", "partial"),
    "Salesforce-Success-Architect-Agentforce-2026-08.md": ("redirected", "partial"),
    "Salesforce-Product-Manager-Agent-Fabric-2026-08.md": ("redirected", "partial"),
    "ServiceNow-AI-Agent-Engineer-Moveworks-2026-08.md": ("active", "full"),
    "ServiceNow-Senior-Staff-Agent-Development-2026-08.md": ("unavailable", "blocked"),
    "ServiceNow-Senior-Staff-Agentic-Systems-Moveworks-2026-08.md": ("active", "full"),
    "ServiceNow-Staff-Agent-Eval-Platform-2026-08.md": ("active", "full"),
    "Ramp-Applied-AI-Engineer-2026-08.md": ("active", "dynamic-partial"),
    "Ramp-Software-Engineer-Enterprise-Product-2026-08.md": ("active", "dynamic-partial"),
    "Ramp-Software-Engineer-Frontend-Revenue-2026-08.md": ("active", "dynamic-partial"),
    "Zapier-Engineer-Applied-AI-2026-08.md": ("active", "dynamic-partial"),
    "Front-AI-Engineer-GTM-Operations-2026-08.md": ("active", "dynamic-partial"),
    "Warp-Forward-Deployed-Engineer-2026-08.md": ("active", "full"),
}

def parse_rows():
    rows = defaultdict(list)
    for line in ROWS.splitlines():
        if not line.strip():
            continue
        f, kind, skill, section, raw, confidence, alt, fidelity, rationale = line.split("|", 8)
        # Empty Alternative Group is written as `||`; tolerate the older
        # three-separator spelling so all rows still parse deterministically.
        if not fidelity and rationale.startswith(("direct|", "close-paraphrase|", "inferred|")):
            fidelity, rationale = rationale.split("|", 1)
        rows[f].append({"kind": kind, "skill": skill, "section": section, "raw": raw, "confidence": confidence, "alt": alt.strip(), "fidelity": fidelity, "rationale": rationale})
    return rows

DATA = parse_rows()

def replace_frontmatter(text, status, access, audit):
    end = text.find("\n---", 4)
    raw = text[4:end]
    repl = {"updated": UPDATED, "retrieved": UPDATED, "source_status": status, "source_access": access, "evidence_audit_status": audit}
    out, seen = [], set()
    for line in raw.splitlines():
        key = line.split(":", 1)[0] if ":" in line else ""
        if key in repl:
            out.append(f"{key}: {repl[key]}"); seen.add(key)
        else:
            out.append(line)
    for key, val in repl.items():
        if key not in seen: out.append(f"{key}: {val}")
    return "---\n" + "\n".join(out) + "\n---\n"

def render(path, rows):
    old = path.read_text(encoding="utf-8")
    fm_end = old.find("\n---", 4)
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", old[4:fm_end], re.M))
    status, access = STATUS[path.name]
    audit = "verified" if access == "full" else ("historical" if status in {"expired", "unavailable"} else "partial")
    head = replace_frontmatter(old, status, access, audit)
    title = meta.get("company", path.stem) + " — " + meta.get("role_title", path.stem)
    rs = [r for r in rows if r["kind"] == "responsibility"]
    rq = [r for r in rows if r["kind"] == "required"]
    pr = [r for r in rows if r["kind"] == "preferred"]
    inf = [r for r in rows if r["kind"] == "inferred-prerequisite"]
    def bullets(xs, fallback):
        seen = set()
        unique = []
        for r in xs:
            if r["raw"] not in seen:
                unique.append(r)
                seen.add(r["raw"])
        return "\n".join(f"- {r['raw']}" for r in unique) if unique else f"- {fallback}"
    fam = {"ai-application-engineering":"AI-Application-Engineer", "field-deployment":"AI-Solutions-Architect-and-FDE", "product":"AI-Product-Manager", "ai-product-management":"AI-Product-Manager", "ai-infrastructure":"AI-Infrastructure-and-Inference-Engineer", "agent-platform":"AI-Infrastructure-and-Inference-Engineer"}.get(meta.get("role_family", ""), "AI-Application-Engineer")
    note = "官方页面完整可读；证据按源段落逐事实记录。" if access == "full" else "页面需动态渲染、重定向或部分可读；仅保留可复核的中/低置信事实。"
    if audit == "historical": note = "来源已失效、重定向错误或不可用；所有行仅作历史学习前置，不代表当前招聘要求。"
    out = [head, f"# {title}", "", "## Source Scope", f"官方职位 URL：[{meta.get('source_url','')}]({meta.get('source_url','')})。审计日期：`{UPDATED}`；状态：`{status}` / `source_access: {access}` / `evidence_audit_status: {audit}`。{note}", "每条证据只保留一个可回溯事实；未适配当前 Skill 的信号不强行归类。", "", "## Role Summary", "本卡以官方职位页面为证据边界；请优先阅读下方来源段落与 Evidence Trace。", "", "## Responsibilities", bullets(rs, "当前来源未确认可复核职责。"), "", "## Explicit Requirements", bullets(rq, "当前来源未确认可复核要求；不要把职责或历史摘要当作 required。"), "", "## Preferred/Nice-to-have", bullets(pr, "当前来源未确认 preferred 项。"), "", "## Skill Extraction", "证据类型允许 `required`、`preferred`、`responsibility`、`inferred-prerequisite`。Alternative Group 表示 one-of 或 at-least-N 选择关系。", "", "| Raw Evidence | Skill | Evidence Type | Requirement Strength | Alternative Group | Depth Signal | Confidence |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows:
        strength = "inferred" if r["kind"] == "inferred-prerequisite" else "explicit"
        out.append(f"| {r['raw']} | [[{r['skill']}]] | {r['kind']} | {strength} | {r['alt'] or 'none'} | use | {r['confidence']} |")
    out += ["", "## Non-skill Gates", "年限、客户沟通、领域经验、地点、授权与合规语境保留在岗位判断中，不自动归一化为 Skill。", "", "## Role Mapping", f"- Primary [[{fam}]]", "", "## Limitations", note, "", "## Evidence Trace"]
    for i, r in enumerate(rows, 1):
        strength = "inferred" if r["kind"] == "inferred-prerequisite" else "explicit"
        if r["fidelity"] == "close-paraphrase":
            note = f"paraphrased from official {r['section']} section; mapping kept to {r['skill']} only."
        elif r["fidelity"] == "direct":
            note = f"quoted or lightly normalized from official {r['section']} section; mapping kept to {r['skill']} only."
        else:
            note = f"inferred learning lead from {r['section']}; not a current job requirement."
        if r["alt"]:
            note += " Alternative group is not summed."
        out += [f"### Evidence {i}", f"Source Section: {r['section']}", f"Source Fidelity: {r['fidelity']}", f"Raw Evidence: {r['raw']}", f"Mapped Skill: [[{r['skill']}]]", f"Evidence Type: {r['kind']}", f"Requirement Strength: {strength}", f"Alternative Group: {r['alt'] or 'none'}", "Depth Signal: use", f"Confidence: {r['confidence']}", f"Mapping Rationale: {r['rationale']}", f"Notes: {note}", ""]
    return "\n".join(out).rstrip() + "\n"

def main():
    data = parse_rows()
    expected = set(STATUS)
    missing = sorted(expected - {p.name for p in JOB_DIR.glob("*.md")})
    if missing: raise SystemExit("missing job files: " + ", ".join(missing))
    missing_rows = sorted(expected - set(data))
    if missing_rows: raise SystemExit("missing evidence rows: " + ", ".join(missing_rows))
    for name, rows in data.items():
        (JOB_DIR / name).write_text(render(JOB_DIR / name, rows), encoding="utf-8")
    counts = Counter((r["skill"], r["kind"]) for rows in data.values() for r in rows)
    samples = defaultdict(set)
    for name, rows in data.items():
        for r in rows: samples[r["skill"]].add(name)
    print(f"rewrote {len(data)} applied job cards; rows={sum(map(len, data.values()))}")
    for skill in sorted(samples):
        print(skill + ": " + ", ".join(f"{k}={counts[(skill,k)]}" for k in ("required","preferred","responsibility","inferred-prerequisite")) + f"; samples={len(samples[skill])}")

if __name__ == "__main__": main()
