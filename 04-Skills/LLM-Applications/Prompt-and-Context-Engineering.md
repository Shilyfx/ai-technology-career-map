---
type: skill
skill_category: llm-applications
status: developing
stability: current
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2026-11-29
roles:
  - "[[AI-Application-Engineer]]"
  - "[[AI-Product-Manager]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
  - "[[AI-Safety-Evals-and-Governance]]"
  - "[[Research-Engineer]]"
prerequisites:
  - "[[Transformer-LLM-Fundamentals]]"
  - "[[Technical-Communication]]"
related_concepts:
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[RAG-and-Knowledge-Systems]]"
  - "[[Agent-Memory-and-Knowledge-Operations]]"
---

# Prompt and Context Engineering

## 为什么岗位需要它

模型行为取决于任务定义、可见上下文、工具结果、约束和输出协议。把这些因素设计成可测量的输入，才能区分“模型能力不足”和“上下文/流程设计错误”。

## Role Demand

Application/FDE 需要 implement；PM 需要 explain 产品边界；Safety 需要用它构造对抗与拒答测试；Research 需要理解上下文对实验的影响。

## Job Evidence

当前 Job Sample 没有把 Prompt/Context Engineering 作为独立标签；它嵌在 Agent、RAG、API、评测和产品交付中。本页是面向学习的 prerequisite-synthesis，不把文章中的提示词模板当作招聘证据。

## 在岗位中怎么使用

写系统/开发者/用户指令，组织上下文和引用，设计结构化输出、工具 schema、拒答条件、上下文预算、版本和回归集。

## Role-specific Target Depth

Application/FDE implement/use；PM explain/decide；Safety implement 对抗与边界；Research use 以保持实验控制。

## 前置 Skills

[[Transformer-LLM-Fundamentals]]、[[Technical-Communication]]。

## 学习范围

任务分解、角色和约束、few-shot、结构化输出、上下文选择、上下文压缩、引用、prompt injection、版本化和评测。

## 核心知识

Prompt 不是魔法指令；上下文越多不一定越好；示例和约束必须进入回归评测；系统提示词不能替代权限和业务规则。

## Practice

为同一个 RAG/Agent 任务做三版 prompt/context：无约束、结构化输出、带引用与拒答；固定模型、数据和任务集，比较正确性、引用、拒答、成本和延迟。

## Pass Evidence

能展示一次提示或上下文改动带来的指标变化，并定位至少一个 prompt、retrieval、tool 或 model 层失败；所有模板都有版本和回归测试。

## 常见失败

堆叠角色词；把秘密写进 prompt；让模型决定权限；上下文无来源；只展示成功样例；用一次对话证明泛化。

## 不需要深挖到什么程度

先掌握任务/上下文/输出协议和评测；不必把“提示词工程”当成脱离 Python、数据和系统设计的独立职业。

## Related Knowledge

[[Transformer-LLM-Fundamentals]]、[[RAG]]、[[Tool-Calling-and-Action-Contracts]]、[[LLM-Evals]]、[[Security-Privacy-and-Access-Control]]。

## Actual Evidence

尚无用户能力结论；完成三版对照 Practice 后使用 [[Evidence-Card]] 记录。

## Sources

[[Gemini-System-Instructions-Hallucination]]、[[NotebookLM-Advanced-Tips]]、[[YAML-Frontmatter-AI-Prompts]]、[[Agent-Memory-Basic-Memory-Guide]]。

