---
type: matrix
status: active
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Role-Map]]"
  - "[[2026-08-AI-Job-Market-Snapshot]]"
---

# Job–Skill Matrix

> H = 主深度；M = 能独立工作/协作；L = 具备判断与沟通能力；— = 通常不是主门槛。矩阵是学习资源分配工具，不是简历打分器。

## 技能深度矩阵

| 岗位 | 数学/统计 | ML/DL | 研究实验 | 软件工程 | 分布式/性能 | 数据/SQL | RAG/Agent | Evals/安全 | 云/MLOps | 产品/用户 | 领域沟通 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Research Scientist | H | H | H | M | M | M | L–M | M–H | L | L | M |
| Research Engineer | M–H | H | H | H | H | M | M | H | M–H | L | M |
| ML / AI Engineer | M | H | M | H | M | M–H | M | H | H | M | M |
| AI Application Engineer | L–M | M | L | H | L–M | M | H | H | M–H | H | H |
| AI Infra / Inference | M | M–H | L–M | H | H | M | L | H | H | L | M |
| Data / AI Engineer | L–M | M | L | H | M | H | M | H | H | M | M–H |
| AI Product Manager | M（统计） | M（概念） | L | L–M | L | M | M | H（指标/风险） | L | H | H |
| Solutions Architect / FDE | L–M | M | L | H | M | M | H | H | H | H | H |
| Safety / Evals / Governance | M–H | M–H | H | M–H | L–M | M–H | M | H | M | M | H |

## 所有技术岗的共同底座

1. Python；
2. 数据结构、算法与基本系统设计；
3. 数据质量、切分、版本与 SQL；
4. ML/DL 与评测基础；
5. Git、测试、Linux、API、日志；
6. 能读英文文档/论文和验证来源；
7. 写清问题、假设、失败与权衡。

2025 美国 AI 岗位的高频技能数据也显示，Python、computer science、scalability、automation、workflow management、data analysis、SQL、project management、data science 和 AWS 同时出现。岗位需求已经明显跨越“模型算法”单层，详见 [[2026-08-AI-Job-Market-Snapshot]]。

## 作品集证据矩阵

| 岗位 | 一个有说服力的项目 | 必须展示 |
| --- | --- | --- |
| Research Scientist | 新方法或严谨复现/反证 | RQ、baseline、消融、统计、限制 |
| Research Engineer | 可扩展训练/评测系统 | correctness、吞吐、复现、研究反馈 |
| ML / AI Engineer | 端到端模型生命周期 | data、training、eval、deploy、monitor |
| Application Engineer | 真实任务的 RAG/Agent 产品 | task set、trace、failure、cost、UX |
| Infra / Inference | 服务或训练性能优化 | profile、瓶颈、前后对比、回退 |
| Data / AI Engineer | 可信数据/embedding pipeline | contract、lineage、quality、permission |
| AI PM | 从问题到上线决策 | 用户证据、指标树、取舍、风险 |
| Solutions / FDE | 行业工作流落地 | discovery、architecture、delivery、adoption |
| Safety / Evals | 评测与控制系统 | threat model、dataset、coverage、residual risk |

## T 型选择建议

```text
共同横向：software + data + ML literacy + eval + communication
主纵向：research / application / infra / product / field / safety 选一
相邻接口：再选一个能和主纵向形成完整交付的方向
```

例：AI Application Engineer 的主纵向是应用工程，相邻接口可选 data/RAG 或 eval/safety；不必同时深挖 CUDA kernel 和理论 RL。
