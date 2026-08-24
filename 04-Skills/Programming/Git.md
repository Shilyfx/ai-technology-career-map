---
type: skill
skill_category: programming
status: seed
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[Research-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites: []
related_concepts:
  - "[[Math-Data-and-Software-Foundations]]"
---

# Git

## 为什么岗位需要它

研究与生产协作都需要可审查、可回滚、可复现的代码历史；它是软件交付门槛而非 AI 专属工具。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Research Engineer | Common | implement | [[Anthropic-ML-Infrastructure-Engineer-Safeguards-San-Francisco-2026-08]] | 研究工具依赖 |
| ML / AI Engineer | Common | use | [[Apple-Machine-Learning-Engineer-Video-Cupertino-2026-06]] | 生命周期协作 |
| Infra | Common | implement | [[Huawei-AI-Bottom-Software-Shanghai-2026-08]] | 工程与发布 |

## 在岗位中怎么使用

分支、review、最小提交、回滚、标签和实验配置追踪。

## Role-specific Target Depth

工程岗位 implement；PM 只需理解变更与发布证据。

## 前置 Skills

无。

## 学习范围

提交、分支、冲突、rebase/merge 的风险、review 和 CI。

## 核心知识

一条提交应对应一个判断；实验数据和密钥不能随意提交。

## Practice

为一个小项目建立分支、测试门禁、review 记录和回滚提交。

## Pass Evidence

可从 clean checkout 按命令复现结果，并能回滚到上一版本。

## 常见失败 / 误区

大提交、把凭证提交到仓库、用 force push 掩盖未审查的冲突。

## 不需要深挖到什么程度

不需要实现 Git 内部对象模型；需要可靠地协作与恢复。

## Related Concepts

[[Math-Data-and-Software-Foundations]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[Huawei-AI-Bottom-Software-Shanghai-2026-08]]。
