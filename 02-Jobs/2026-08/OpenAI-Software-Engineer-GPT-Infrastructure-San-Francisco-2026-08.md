---
type: job-sample
company: OpenAI
role_title: Software Engineer, GPT Infrastructure
role_family: ai-infrastructure-inference
seniority: experienced
location: San Francisco, US
region: US
source_url: https://openai.com/careers/software-engineer-gpt-infrastructure-san-francisco/
source_kind: official-career-page
source_status: current
source_access: full
snapshot_date: 2026-08-24
retrieved: 2026-08-24
posted: 2026-08-24
status: developing
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-09-24
---

# OpenAI — Software Engineer, GPT Infrastructure

## Source Scope
官方职位页；抽取模型执行、编译器/运行时和系统整合信号。

## Role Summary
支撑大模型执行、训练与评测的基础设施和安全集成。

## Responsibilities
- 建造分布式模型执行和 runtime 组件；
- 优化性能、可靠性和资源利用；
- 连接模型、编译器、服务和评测系统。

## Explicit Requirements
- 分布式系统和生产软件工程；
- 模型执行、编译器或运行时经验；
- 处理性能、容量和故障问题。

## Preferred/Nice-to-have
- C++/Python、GPU、编译器、云基础设施或安全集成经验。

## Skill Extraction
| Skill | Evidence type | Why counted |
| --- | --- | --- |
| [[Distributed-Systems]] | explicit | model execution at scale |
| [[Model-Serving]] | explicit | production execution |
| [[CUDA-GPU-Basics]] | inferred | accelerator execution |
| [[Observability]] | inferred | reliability and capacity |
| [[Testing]] | explicit | safe infrastructure changes |

## Non-skill Gates
Systems ownership and comfort operating critical services.

## Role Mapping
Primary: [[AI-Infrastructure-and-Inference-Engineer]]. Adjacent: [[Research Engineer]].

## Limitations
Infrastructure posting; exact compiler/runtime depth is team-specific.

## Evidence Trace

- Source Section: `Responsibilities`, `Explicit Requirements`, and `Preferred/Nice-to-have` in the official posting.
- Evidence Type: Explicit requirements are countable Job Skill Evidence; responsibility-based mappings remain inferred context.
- Extraction Decision: Normalize one skill once per sample; alternatives are not double-counted, and inferred signals do not increase required frequency.
- Confidence: high; source_access is recorded in frontmatter and limitations remain local to this sample.
