---
type: role
role_family: safety-evals-governance
sample_count: 5
status: developing
snapshot_date: 2026-08-31
created: 2026-08-24
updated: 2026-08-31
review_after: 2026-11-24
---

# AI Safety, Evals and Governance

## 这是岗位族，不是单一岗位

| 子方向 | 主要交付 |
| --- | --- |
| Safety Research | 风险假设、模型行为研究、mitigation |
| Evals Engineer/Researcher | 数据集、runner、scorer、回归与测量科学 |
| Red Team / AI Security | 威胁、攻击路径、对抗测试与响应 |
| Trust & Safety | 生产滥用、政策执行、运营与测量 |
| AI Governance / Policy | 责任、标准、审计、法规与组织控制 |
| Interpretability | 理解内部机制或行为因果结构 |

## 共同技能

- ML/LLM 原理与模型行为；
- Python、数据、统计、实验与 measurement；
- threat/risk model、scenario design、coverage；
- 安全、隐私、社会影响或具体高风险领域；
- 写作、跨学科沟通与证据边界。

工程型岗位还会要求评测平台、分布式任务、数据管线与生产监控；治理型岗位需要标准、政策、合规与组织实施，但不能完全脱离技术。

## Sample Observations

本批 Anthropic、Apple 和 OpenAI Job Samples 覆盖 model evaluations、safeguards、测量平台与安全/对齐；岗位标题和公开程度不同，以下 Profile 只保留可追溯的责任簇。

## 作品证据

- 针对一个系统的 threat model；
- 任务/风险 taxonomy 与覆盖矩阵；
- adversarial set、scorer 校准与误报/漏报；
- mitigation 前后对比与残余风险；
- 上线监控、incident 和治理责任闭环。

来源：[Anthropic Jobs](https://www.anthropic.com/careers/jobs)、[Google DeepMind Careers](https://deepmind.google/careers/)、[OpenAI PM, Safety Measurement](https://openai.com/careers/product-manager-safety-measurement-san-francisco/)

## Sample Basis

5 samples across OpenAI, Anthropic and Apple eval/safeguard/measurement roles.

## Evidence Basis

Based on 5 Job Samples in [[Job-Sample-Index]]; employers, regions and seniority are summarized in this profile. Confidence is high for repeated explicit signals and medium for partial or inferred signals.

## Main Deliverables

Risk hypotheses, evaluation suites, safety measurement, controls and governance evidence.

## Responsibility Clusters

Threat/risk modeling; eval data/scoring; production monitoring; policy/governance; communication.

## Skill Profile

| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Model-Evaluation]] | yes |  | measurement validity | 5 | Core | implement | high | Job Samples |
| [[LLM-Evals]] | yes |  | LLM regression | 4 | Core | implement | high | Job Samples |
| [[AI-Safety-Measurement]] | yes |  | risk thresholds | 3 | Core | implement | high | Job Samples |
| [[Python]] | yes |  | data/eval tooling | 3 | Common | implement | medium | Job Samples |
| [[Technical-Communication]] | yes |  | governance decisions | 4 | Core | implement | medium | Job Samples |
| [[Agent-Evals-and-Trace-Debugging]] | common |  | trajectory/rubric diagnosis | 2 | Common | implement | medium | [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] |
| [[Human-in-the-Loop-and-Agent-Guardrails]] | common |  | calibration/approval controls | 2 | Common | implement | medium | [[ServiceNow-Staff-Agent-Eval-Platform-2026-08]] |

## Non-skill Gates

Risk judgment, policy sensitivity, epistemic humility and willingness to escalate.

## Seniority/Subtrack Differences

Evals engineering emphasizes systems; research emphasizes validity; governance emphasizes standards and accountability.

## Portfolio Evidence

Threat model, adversarial set, scorer calibration, mitigation comparison and residual-risk decision.

## Adjacent Roles

[[Research-Engineer]]、[[AI-Product-Manager]]、[[Data-and-AI-Engineer]]。

## Source Limitations

Public job pages expose different detail levels; inferred skills are marked in each Job Sample.

## Refresh

Refresh job evidence every 30–60 days and safety methods every 60–90 days.

## Learning prerequisites

安全/Evals 方向先完成 [[Technical-Communication]]、[[Statistics-and-Experiment-Design]]、[[Model-Evaluation]] 和 [[LLM-Evals]]，再根据子方向进入 [[Agent-Evals-and-Trace-Debugging]]、[[Human-in-the-Loop-and-Agent-Guardrails]] 或 [[AI-Safety-Measurement]]；做 Agent、数据或上线评审时必须补 [[Security-Privacy-and-Access-Control]] 与 [[Prompt-and-Context-Engineering]]。
