---
type: moc
domain: skills
page_kind: prerequisite-map
status: reference
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-28
related:
  - "[[Skill-Index]]"
  - "[[Role-Skill-Paths]]"
  - "[[Role-Map]]"
  - "[[JasonAI-Source-Index]]"
---

# Prerequisite Foundation Map

> 这是学习导航，不是新的招聘统计。先选 Role，再沿前置层做最小实践；通过证据后才进入正式 Skill 的更深层。

## 六个前置层

1. [[Data-Structures-and-Algorithms]]：把问题拆成可计算、可测试的结构；
2. [[Statistics-and-Experiment-Design]]：把“变好了”变成可比较、带不确定性的结论；
3. [[Databases-and-Data-Modeling]]：让数据、反馈、评测和索引可追溯；
4. [[Software-Design-and-Architecture]]：把模型能力放入有边界、可恢复的系统；
5. [[Security-Privacy-and-Access-Control]]：在工具、数据和记忆进入生产前建立权限和撤销；
6. [[Prompt-and-Context-Engineering]]：控制模型看到什么、输出什么，以及如何回归。

## 选择顺序

| 目标 | 先学 | 接着进入 |
| --- | --- | --- |
| Research / ML | [[Data-Structures-and-Algorithms]] → [[Python]] → [[Statistics-and-Experiment-Design]] | [[ML-Experimentation]] → [[Model-Evaluation]] → [[PyTorch]] |
| AI Application | [[Data-Structures-and-Algorithms]] → [[Python]] → [[HTTP-API]] | [[Software-Design-and-Architecture]] → [[Prompt-and-Context-Engineering]] → [[RAG]] |
| Data / AI | [[Data-Structures-and-Algorithms]] → [[Python]] + [[SQL]] | [[Databases-and-Data-Modeling]] → [[Data-Quality-and-Lineage]] |
| Infra / Inference | [[Data-Structures-and-Algorithms]] → [[Linux]] → [[Testing]] | [[Software-Design-and-Architecture]] → [[Distributed-Systems]] → [[Model-Serving]] |
| PM / Safety / FDE | [[Technical-Communication]] → [[Statistics-and-Experiment-Design]] | [[Model-Evaluation]] → [[LLM-Evals]] → [[AI-Safety-Measurement]] / [[API-Product-Delivery]] |

## 每个前置 Skill 的通过门

不要以“读完文章”作为完成条件。每个页面都包含 Practice 和 Pass Evidence；完成后把命令、指标、失败样本和判断写进 [[Evidence-Index]]，再回到 [[Role-Skill-Assessment]]。

## 来源如何使用

JasonAI 资料中的 Agent、Memory、RAG、MCP、Obsidian CLI、Git 和环境文章作为练习材料，入口见 [[JasonAI-Source-Index]]。工具教程只提供场景，不自动改变 Skill 的岗位优先级。

