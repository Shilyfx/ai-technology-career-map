---
type: job-sample
company: Anthropic
role_title: TPU Kernel Engineer
role_family: ai-infrastructure-inference
seniority: experienced
location: San Francisco, US
region: US
source_url: https://job-boards.greenhouse.io/anthropic/jobs/4720576008
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

# Anthropic — TPU Kernel Engineer

## Source Scope
官方 Greenhouse 职位页；重点为 accelerator kernel 和低精度优化。

## Role Summary
为 TPU/加速器设计高性能 kernel、通信和数值实现。

## Responsibilities
- 优化 kernel、低精度算子和 collective communication；
- 建立性能模型并分析瓶颈；
- 与模型、编译器和硬件团队协作。

## Explicit Requirements
- accelerator/kernel 优化；
- 数值、性能和系统编程；
- 能读写低层实现或 assembly。

## Preferred/Nice-to-have
- TPU、GPU、编译器、MLIR、CUDA 或分布式通信经验。

## Skill Extraction
| Skill | Evidence type | Why counted |
| --- | --- | --- |
| [[CUDA-GPU-Basics]] | inferred | accelerator reasoning |
| [[Distributed-Systems]] | explicit | collective communication |
| [[ML-Experimentation]] | inferred | performance models |
| [[Testing]] | inferred | numerical correctness |

## Non-skill Gates
低层调试耐心、数值正确性和硬件协作。

## Role Mapping
Primary: [[AI-Infrastructure-and-Inference-Engineer]]. Adjacent: [[Research Engineer]].

## Limitations
TPU 专项岗位；CUDA 链接是可迁移基础而非页面逐字要求。

## Evidence Trace

- Source Section: `Responsibilities`, `Explicit Requirements`, and `Preferred/Nice-to-have` in the official posting.
- Evidence Type: Explicit requirements are countable Job Skill Evidence; responsibility-based mappings remain inferred context.
- Extraction Decision: Normalize one skill once per sample; alternatives are not double-counted, and inferred signals do not increase required frequency.
- Confidence: high; source_access is recorded in frontmatter and limitations remain local to this sample.
