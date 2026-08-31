---
type: skill
skill_category: Evals-Safety
status: developing
stability: current
created: 2026-08-31
updated: 2026-09-01
review_after: 2026-11-30
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Product-Manager]]"
prerequisites:
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Security-Privacy-and-Access-Control]]"
recommended_foundations:
  - "[[Agent-Evals-and-Trace-Debugging]]"
related_concepts:
  - "[[Workflow-Automation-and-Business-Process-Design]]"
sample_batch: enterprise-applied-ai-2026-08
---

# Human-in-the-Loop 与 Agent Guardrails

## Skill Boundary

本卡处理风险分类和人机边界：approval、interrupt/resume、escalation、pre-tool guard、post-tool verification、rollback、audit、least privilege、policy vs prompt、sandbox。它不是“加一句安全 prompt”，也不是完整 eval 平台。

## 为什么岗位需要它

企业 Agent 会修改工单、退款、删除数据或发送外部邮件；Atlassian、Salesforce、Warp 等样本把合规、审批和安全交付放在职责/要求中。

## Role Demand

工程师实现策略执行点；FDE 与客户定义风险矩阵；PM 负责 policy、审计和人工运营，而不是把所有风险推给模型。

## Job Evidence

[[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]] 将 AI risk/privacy/GDPR 作为 requirement；[[Salesforce-Product-Manager-Agent-Fabric-2026-08]]、[[Warp-Forward-Deployed-Engineer-2026-08]] 的 approvals/permissions 属于职责或前置推断。

## 前置 Skills

硬前置：[[Tool-Calling-and-Action-Contracts]] 与 [[Security-Privacy-and-Access-Control]]；推荐 [[Agent-Evals-and-Trace-Debugging]]。

## 学习范围

风险等级、auto-allow/confirm/manual-only/deny、approval、interrupt/resume、escalation、pre-tool policy guard、post-tool verification、rollback、audit、least privilege、policy/prompt 分离、sandbox。

## 核心知识

- 用动作和影响分类风险，不用“模型自信度”替代权限；删除/退款/外发默认高风险。
- policy 在工具执行前强制生效，prompt 只是行为提示；执行后仍要验证状态并记录 audit。
- approval 必须可恢复、过期、绑定资源和参数；拒绝/超时要有安全 fallback。

## Practice

为 refund、delete、external email、modify ticket 建风险矩阵，分别落到 auto allow、confirm、manual only、deny；实现 pre-tool guard、审批 interrupt/resume、post-tool verify、rollback、审计和 sandbox fixture。

## Pass Evidence

提交四类动作的决策表、policy test、权限 scope、审批/拒绝/超时/篡改参数 trace、回滚结果和审计记录；证明绕过 prompt 仍无法绕过 policy。

## 常见失败

所有动作都 auto-allow；把 prompt 当 policy；审批后参数被替换；没有 post-tool verify；rollback 不可用；审计缺 actor/resource/policy version。

## 不需要深挖到什么程度

不要求先完成企业合规认证；先把四类动作做成可执行、可审计的风险边界。

## Related Knowledge

[[Tool-Calling-and-Action-Contracts]]、[[Agent-Evals-and-Trace-Debugging]]、[[Security-Privacy-and-Access-Control]]、[[Workflow-Automation-and-Business-Process-Design]]

## Practice Boundary

通过线是 policy-enforced action boundary；业务领域的法律解释仍需专业审查。

## Actual Evidence

用 [[Evidence-Card]]记录一次被 guard 拦截的高风险动作和一次成功回滚。

## Sources

### Official / normative

- [OpenAI Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/)
- [OpenAI Agents SDK human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)

### Job evidence

- [[Atlassian-Senior-Principal-Forward-Deployed-Engineer-2026-08]]
- [[Salesforce-Product-Manager-Agent-Fabric-2026-08]]
- [[Warp-Forward-Deployed-Engineer-2026-08]]

### Practice

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
