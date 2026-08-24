---
type: skill
skill_category: software-engineering
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[ML-and-AI-Engineer]]"
prerequisites:
  - "[[Python]]"
related_concepts:
  - "[[AI-Product-Engineering]]"
---

# HTTP / API

## 为什么岗位需要它

AI 能力只有通过稳定接口、认证、错误处理、版本和可观测性才能进入产品与客户系统。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Application Engineer | Core | implement | [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]] | agent backend |
| AI PM | Common | explain | [[OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08]] | API primitives |
| Solutions / FDE | Core | implement | [[Huawei-AI-Solutions-Architect-Shanghai-2026-08]] | solution delivery |

## Job Evidence

[[OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用

设计资源、认证、重试、幂等、限流、超时、错误模型和版本策略。

## Role-specific Target Depth

工程/FDE implement；PM 需要解释契约、成本和失败边界。

## 前置 Skills

[[Python]]、[[Testing]]。

## 学习范围

HTTP、JSON、REST、认证、网关、异步任务和 API observability。

## 核心知识

客户端重试与服务端幂等、权限最小化、数据边界和兼容性。

## Practice

实现带 auth、schema validation、timeout、retry、tests 和日志的 API。

## Pass Evidence

能展示正常、失败、超时和未授权请求的可复查行为。

## 常见失败

把 API key 放前端、无限重试、把模型错误吞掉、没有版本策略。

## 不需要深挖到什么程度

不要求每个岗位设计完整云平台；要能交付可控接口。

## Related Knowledge

[[AI-Product-Engineering]]、[[AI-Agents-and-Tool-Use]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]]、[[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]]。
