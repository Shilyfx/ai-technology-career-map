---
type: market-snapshot
status: active
snapshot_date: 2026-08-24
geography: global-aggregates-us-postings-plus-china-official-samples
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Role-Map]]"
  - "[[Job-Skill-Matrix]]"
  - "[[Technology-Radar-2026-08]]"
---

# AI Job Market Snapshot — 2026-08

> 本页是可替换的市场快照。它只描述所列样本与时间，不宣称覆盖全部国家、公司或职级。

## 结论先行

1. **AI 招聘技能正在从“知道模型/聊天工具”扩展到“能把系统运行起来”。** 2025 年美国 AI 岗位的高频技能既包括 Python、计算机科学和数据科学，也包括 scalability、automation、workflow management、SQL 和 AWS。[Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)
2. **Agent 是当前增长信号，不是单独的万能岗位。** 统计中 Agentic AI、AI agents、LangGraph 等词增长很快；对应的可迁移能力是工具调用、工作流、状态、评测、权限和系统可靠性，而非记住单一框架。[Lightcast 对 AI Index 2026 的解读](https://lightcast.io/resources/research/stanford-ai-index-2026)
3. **前沿研究、应用工程、Infra、产品、方案与安全的技能重叠，但交付物不同。** 因此学习应该先共享底座，再选主深度；见 [[Role-Map]]。
4. **人类能力没有被排除在外。** WEF 报告把分析思维、创造力、韧性/适应性、领导与社会影响与 AI/大数据、网络安全、技术素养一起列为上升技能；LinkedIn 的 2026 报告也显示 AI literacy 已扩散到技术和非技术职能。[WEF 2025](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/), [LinkedIn 2026](https://economicgraph.linkedin.com/research/labor-market-report-2026)

## 研究问题与范围

**问题**：截至 2026-08，哪些 AI 技术与能力在可复核的岗位市场样本中反复出现？它们如何映射到不同岗位？

**包含**：

- Stanford/Lightcast 的 2025 美国在线岗位统计；
- WEF 的全球雇主调查与 LinkedIn 的 2026 劳动力市场报告；
- OpenAI、Google DeepMind、Anthropic 的官方职业页面；
- 华为中国官方 AI 岗位样本（算法/训练推理/底层软件/解决方案）。

**不包含**：薪资预测、职位数量预测、对中国整体市场的普查、猎头平台二手转述、单条 JD 的普适化结论。

## 关键市场信号：事实

| 观察 | 证据 | 如何解读 |
| --- | --- | --- |
| AI 技能出现在 2.5% 的美国在线岗位中，较上年增长 55% | [Lightcast/AI Index 2026](https://lightcast.io/resources/research/stanford-ai-index-2026) | 在线职位技能是需求信号，不等于从业者总数 |
| Agentic AI 技能簇从 2024 的 0.06% 升至 2025 的 0.23%，约 9 万职位 | [Lightcast/AI Index 2026](https://lightcast.io/resources/research/stanford-ai-index-2026) | 说明“任务型/工作流型 AI”进入招聘描述；不证明某一工具成为标准 |
| AI、ML、GenAI、Agent、NLP、视觉、机器人、治理等技能簇同时存在 | [AI Index 2026，第 4.4 节](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) | AI 岗位不是一个单一职业，技术深度分层明显 |
| WEF 将 AI/大数据、网络与安全、技术素养列为增长最快的技能 | [WEF Future of Jobs 2025](https://www.weforum.org/publications/the-future-of-jobs-report-2025/digest/) | 是雇主预期调查，不等于实时职位词频 |
| 美国要求 AI literacy（如 prompt engineering）的职位同比增长 70% | [LinkedIn Labor Market Report 2026](https://economicgraph.linkedin.com/research/labor-market-report-2026) | 适用于广泛职能的“基础 AI 素养”，不等价于 AI 工程师岗位 |

## AI 岗位高频专业技能：美国 2025

下表是 AI Index/Lightcast 的“AI job postings”统计；同一职位可出现多个技能，不能相加为职位数。

| 技能 | 2025 出现次数 | 相对 2013–15 变化 |
| --- | ---: | ---: |
| Python | 258,674 | +391% |
| Computer science | 257,127 | +165% |
| Scalability | 197,744 | +733% |
| Automation | 190,758 | +610% |
| Workflow management | 186,325 | +818% |
| Data analysis | 170,396 | +210% |
| SQL | 151,191 | +132% |
| Project management | 149,865 | +147% |
| Data science | 142,120 | +431% |
| Amazon Web Services | 142,037 | +1,358% |

来源：[Stanford AI Index 2026, Figure 4.4.3](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)。

## 官方岗位样本：观察到的技能簇

| 岗位样本 | 明确技能/职责 | 映射到的岗位族 |
| --- | --- | --- |
| [OpenAI Research Engineer](https://openai.com/careers/research-engineer-san-francisco/) | 强编程、大规模分布式 ML、深度学习高性能实现 | Research Engineer |
| [Google DeepMind Roles](https://deepmind.google/careers/) | RE 的工程+数学+研究、分布式基础设施；Scientist 的假设/模型；PM 的技术到产品翻译 | Research / Engineering / PM |
| [OpenAI Model Inference](https://openai.com/careers/software-engineer-model-inference-san-francisco/) | PyTorch、GPU、CUDA、NCCL、InfiniBand/MPI/NVLink、低延迟高可用分布式系统 | Inference / AI Infra |
| [OpenAI PM, API Agents](https://openai.com/careers/product-manager-api-agents-san-francisco/) | Agent builder、SDK/API、可靠性、安全、开发者体验与技术协作 | AI PM / Application |
| [OpenAI PM, Safety Measurement](https://openai.com/careers/product-manager-safety-measurement-san-francisco/) | 生产安全测量、数据/统计、研究工程政策协作 | Safety / Evals / PM |
| [Anthropic Jobs](https://www.anthropic.com/careers/jobs) | pretraining、RL、research tools、ML systems、GPU/inference、safeguards、model evals、red team | 前沿岗位分化与安全交叉 |
| [华为 AI 解决方案架构师](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=28741) | 大模型应用、搜推、GPU/NPU、框架、架构、项目交付、行业沟通 | Solutions Architect |
| [华为 AI 大模型架构师](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=28183) | Python/C++、训练/RL、量化、KV 压缩、投机推理、vLLM/SGLang、GPU/NPU | Training / Inference |
| [华为底层 AI 软件](https://career.huawei.com/reccampportal/portal5/social-recruitment-detail.html?dataSource=1&jobId=32189) | LLVM/MLIR、Runtime、kernel、通信、编译、性能 profiling | AI Infra / Compiler |

## 综合解释：推断，不是直接统计

基于上述聚合数据与官方岗位样本，最稳妥的职业策略是：

```text
共同底座（Python + software + data + ML literacy + eval）
→ 选择一条主纵向（research / application / infra / product / field / safety）
→ 建立一个相邻协作面（例如 application + eval，research + systems）
→ 用可复核作品证明，而不是堆工具名
```

这是对证据的推断。它不意味着所有岗位都要 GPU kernel，也不意味着所有企业都需要多 Agent 系统。

## 中国样本校准

华为官方 AI 专区同一时期同时列出“算法专家（多模态/大模型/搜广推）”“AI 大模型架构师（训练/推理）”“昇腾大模型训练/推理专家”“AI 解决方案架构师”等岗位。[华为 AI 招聘专区](https://career.huawei.com/reccampportal/portal5/social-recruitment-ai.html)

这些样本特别强调软硬协同、国产 GPU/NPU、训练/推理优化、框架/算子、行业交付。它们适合校准中国高技术岗位的深度，但仍不代表所有中国公司或初中级岗位。

## 证据质量与限制

| 来源族 | 对什么最有力 | 主要限制 |
| --- | --- | --- |
| Stanford/Lightcast | 美国在线岗位的技能词频和变化 | 分类法、在线职位覆盖、地域与时间边界 |
| WEF | 全球雇主的 2025–2030 预期 | 调查预期，不是实际 JD 计数 |
| LinkedIn | 平台内人才与职位趋势 | 平台样本与技能定义 |
| 官方职位页 | 某公司、某职级、某地点的真实门槛 | 高级/前沿公司偏差，职位会下线或变更 |
| 中国官方岗位页 | 具体中国技术岗位的职责与技能 | 公司、部门、地点与职级偏差 |

尤其要避免两个错误：

- 把前沿实验室的 senior JD 当作入门清单；
- 把“关键词出现增长”解释成“工资/稳定性/未来必然增长”。

## 如何刷新

每季度替换本页时：

1. 保留旧快照，创建新的 `YYYY-MM-AI-Job-Market-Snapshot.md`；
2. 记录地理范围、抓取日期、来源与岗位样本；
3. 抽取职责、技能、交付物、资历，不只抽标题；
4. 至少用一个聚合统计来源和 6 个官方职位样本交叉检查；
5. 更新 [[Technology-Radar-2026-08]] 与 [[Job-Skill-Matrix]] 时，把“事实”和“解释”分开；
6. 标出失效链接，不静默删除原有证据。

## AI 辅助说明

本快照由 AI 协助检索、提炼和组织；数值与岗位要求均已链接到公开的原始/官方页面。仍应在投递具体职位前打开当天的 JD 核验。
