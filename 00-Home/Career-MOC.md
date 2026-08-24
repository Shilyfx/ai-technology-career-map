---
type: moc
domain: ai-careers
status: reference
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
related:
  - "[[Role-Map]]"
  - "[[Job-Skill-Matrix]]"
  - "[[2026-08-AI-Job-Market-Snapshot]]"
---

# Career MOC

> 不从岗位名称猜工作内容；从“主要交付物”判断岗位。

## 岗位价值链

```mermaid
flowchart LR
  RS["Research Scientist\n新知识/新方法"] --> RE["Research Engineer\n可运行规模化实验"]
  RE --> ML["ML / AI Engineer\n可靠模型能力"]
  ML --> APP["AI Application Engineer\n可用产品工作流"]
  APP --> FDE["FDE / Solutions Architect\n客户场景落地"]
  INF["AI Infra / Inference\n算力与平台"] --> RE
  INF --> ML
  DATA["Data / AI Engineer\n可信数据流"] --> ML
  DATA --> APP
  SAFE["Safety / Evals / Governance\n风险与证据"] --> RS
  SAFE --> APP
  PM["AI Product Manager\n取舍与结果"] --> APP
```

## 岗位页

- [[Research-Scientist]]
- [[Research-Engineer]]
- [[ML-and-AI-Engineer]]
- [[AI-Application-Engineer]]
- [[AI-Infrastructure-and-Inference-Engineer]]
- [[Data-and-AI-Engineer]]
- [[AI-Product-Manager]]
- [[AI-Solutions-Architect-and-FDE]]
- [[AI-Safety-Evals-and-Governance]]

## 选择方法

优先问：

1. 你更想发现新方法，还是把已知方法做成可靠系统？
2. 你喜欢模型行为、用户工作流、底层性能，还是组织风险？
3. 你的最佳证据是论文、代码仓库、线上指标、客户交付，还是治理框架？
4. 你愿意承担哪种失败：实验不成立、系统不稳定、产品没人用、成本失控或风险漏检？

然后用 [[Job-Skill-Matrix]] 对照，不要被相似职位名迷惑。

## 市场证据

- 当前结论与限制：[[2026-08-AI-Job-Market-Snapshot]]
- 来源清单：[[Source-Index]]
- 角色和技能矩阵是对样本的综合解释，不是招聘承诺。
