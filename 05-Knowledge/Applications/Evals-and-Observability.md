---
type: concept
domain: evaluation
status: developing
stability: current
depth: implement
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
aliases:
  - Evals
  - LLM Observability
related:
  - "[[Training-Evaluation-and-Generalization]]"
  - "[[AI-Agents-and-Tool-Use]]"
---

# Evals and Observability

## Evals 回答“是否更好”

Evals 是针对具体能力、任务、风险或用户结果设计的测量体系，不等于公开 benchmark，也不等于让另一个 LLM 随便打分。

```text
task definition
→ dataset / scenario
→ runner
→ scorer / rubric
→ slices
→ regression gate
→ decision
```

## 四类评测

- **Capability**：能不能完成目标任务；
- **Quality**：正确性、相关性、faithfulness、格式；
- **Safety**：滥用、越权、泄漏、偏差与有害输出；
- **System**：延迟、成本、可用性、tool success、恢复能力。

## LLM-as-a-judge 的边界

它适合规模化评审复杂文本，但需要 rubric、校准样本、盲测、顺序偏差检查、人与模型一致性评估。对高风险结论不能只依赖单一模型裁判。

## Observability 回答“发生了什么”

- input/output 与版本；
- prompt/context/retrieval/tool trace；
- token、延迟、成本、错误、重试；
- 用户反馈与业务结果；
- 隐私脱敏、保留周期与访问权限。

Evals 没有 trace 时难以定位原因；trace 没有任务定义时只是日志。

## 最小实践

为一个 RAG 或 Agent 系统创建：

1. 30 个真实任务；
2. 5 个高风险/对抗任务；
3. 规则评分 + 人工 rubric + 可校准 judge；
4. 按任务、来源、长度、用户类型切片；
5. 每次模型、prompt 或检索变更的回归报告。
