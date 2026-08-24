---
type: path
status: developing
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Start-Here]]"
  - "[[Current-State]]"
  - "[[AI-Technology-MOC]]"
  - "[[Career-MOC]]"
  - "[[Evidence-Index]]"
---

# Learning Path

> 这条路线按依赖组织，不按热点组织。完成 Stage 的条件是 Evidence，而不是读完链接。

## Learning Unit 格式

每个 Stage 都用同一结构：

- **Goal**：完成后能做什么判断或交付；
- **Prerequisites**：需要先会什么；
- **Concepts**：只读与目标直接相关的概念；
- **Practice**：一个小而可复现的练习；
- **Pass Evidence**：别人可以检查的输出；
- **Next**：通过后进入下一阶段或转入岗位专修。

## Stage 0 — 定位：先分层

- **Goal**：把陌生名词放进技术层和岗位价值链。
- **Prerequisites**：无需预备知识。
- **Concepts**：[[AI-ML-DL-and-Foundation-Models]]、[[AI-Technology-MOC]]、[[Role-Map]]。
- **Practice**：从 [[Terms-Inbox]] 选 10 个名词，填写层级、依赖和所需深度。
- **Pass Evidence**：一张分类表，能解释至少 3 个容易混淆的边界。
- **Next**：进入 Stage 1；有经验者可凭 Evidence 跳到对应深度。

## Stage 1 — 共同底座

- **Goal**：把数据、数学直觉和软件工程连接成可复现输入。
- **Prerequisites**：基本 Python 或其他脚本语言。
- **Concepts**：[[Math-Data-and-Software-Foundations]]。
- **Practice**：对一个小数据集完成 schema、清洗、固定 split、日志和测试。
- **Pass Evidence**：参数化脚本、split manifest、README、一条运行命令和至少一个失败测试。
- **Next**：进入 Stage 2；若已有等价工程证据，记录跳过理由。

## Stage 2 — 机器学习闭环

- **Goal**：能判断一个实验结果是否可信，而不只看总分。
- **Prerequisites**：Stage 1 的可复现数据与脚本。
- **Concepts**：[[Training-Evaluation-and-Generalization]]。
- **Practice**：写出假设、baseline、唯一变化、split 来源、指标、失败切片和停止规则。
- **Pass Evidence**：基线报告，包含数据泄漏检查、过拟合判断、两个 failure slice 和 keep/drop/next 决策。
- **Next**：进入 Stage 3；若结果无效，先修复执行证据。

## Stage 3 — 基础模型时代的核心概念

- **Goal**：解释一次端到端模型调用的输入、训练目标、推理输出和限制。
- **Prerequisites**：Stage 2 的训练/评测闭环。
- **Concepts**：[[Transformer-and-Foundation-Models]]、[[Pretraining-Posttraining-and-Fine-tuning]]、[[Multimodal-Generative-and-Embodied-AI]]。
- **Practice**：画出 token/embedding、attention、训练目标和输出评测的链路。
- **Pass Evidence**：一份带最小实验或可复现调用的解释，明确能力来源和失败边界。
- **Next**：进入 Stage 4，或按 [[Role-Map]] 转向研究/训练岗位。

## Stage 4 — 构建可靠 AI 应用

- **Goal**：交付有任务集、来源、失败分类和成本/延迟记录的应用。
- **Prerequisites**：Stage 2 的评测思维和 Stage 3 的模型边界。
- **Concepts**：[[RAG-and-Knowledge-Systems]]、[[AI-Agents-and-Tool-Use]]、[[Evals-and-Observability]]、[[AI-Product-Engineering]]。
- **Practice**：实现 `用户任务 → context/retrieval → model → tools → validation → feedback` 闭环。
- **Pass Evidence**：固定任务集、可追踪来源、失败分类、成本/延迟记录和一份复盘 Evidence。
- **Next**：进入 Stage 5，或按岗位目标专修应用工程/产品/解决方案。

## Stage 5 — 生产系统与风险

- **Goal**：能说明系统的 SLO、回滚、权限、数据边界、攻击面和成本上限。
- **Prerequisites**：Stage 4 的可靠应用原型。
- **Concepts**：[[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]]、[[Data-Engineering-and-Governance]]、[[AI-Safety-Security-and-Governance]]。
- **Practice**：为原型补齐部署、观测、权限、故障演练和模型更新策略。
- **Pass Evidence**：一份生产设计或演练记录，包含风险、控制、回滚和容量假设。
- **Next**：进入 Stage 6；若不做生产交付，可转安全/评测路径。

## Stage 6 — 岗位专修与作品集

- **Goal**：围绕一个岗位交付端到端作品，并让判断过程可审查。
- **Prerequisites**：前面至少一个与目标岗位匹配的 Evidence。
- **Concepts**：[[Career-MOC]]、[[Job-Skill-Matrix]]、[[Role-Based-Learning-Paths]]。
- **Practice**：选一个岗位，拆出主要交付物、技能深度、接口角色和失败模式。
- **Pass Evidence**：作品集含结果、失败处理、权衡、来源和复现方式，而不只是 demo。
- **Next**：回到 [[Current-State]]，只保留一个下一步；其余候选路线放入 Later/Parking Lot。

## 不建议的顺序

- 先背几十个框架名，再补基础；
- 把 prompt 模板数量当作能力深度；
- 只做聊天界面，不建立评测任务集；
- 只追最高 benchmark，不检查数据与执行有效性；
- 同时学研究、应用、Infra、产品所有路径到同一深度。
