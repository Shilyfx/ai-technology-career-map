---
type: role
role_family: ml-engineering
sample_count: 7
status: developing
snapshot_date: 2026-08-24
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-11-24
---

# ML and AI Engineer

## 主要使命

把数据和模型能力做成可靠、可维护、可上线的系统。与 Research Engineer 相比，通常更直接对产品/业务指标、部署和生命周期负责。

## 常见变体

- 传统 ML：分类、排序、推荐、预测；
- Deep Learning Engineer：CV/NLP/speech/multimodal；
- LLM Engineer：fine-tuning、RAG、eval、serving；
- Applied Scientist：研究与业务算法之间，边界因公司不同；
- Robotics ML Engineer：感知、规划、控制和硬件系统。

## 技能重点

- Python、SQL、PyTorch/TensorFlow；
- 数据 pipeline、feature/label、split 与质量；
- baseline、训练、调参、评测与失败切片；
- API/service、容器、云、CI/CD、monitoring；
- 模型漂移、回滚、成本、隐私与安全。

## 作品证据

完整展示 `data → baseline → training → eval → deploy → monitor`，并回答：

- 数据为什么可信？
- 相对 baseline 的收益是什么？
- 线上/线下指标为何可能不一致？
- 模型或数据变化时如何回归与回滚？
- 成本和延迟是否满足任务？

## 不要把岗位简化成

- 只会训练 notebook；
- 只会调用大模型 API；
- 只会部署现成容器；
- 只追一个总指标。

## 相邻岗位

[[Research-Engineer]]、[[AI-Application-Engineer]]、[[AI-Infrastructure-and-Inference-Engineer]]、[[Data-and-AI-Engineer]]。

## Sample Basis
7 Apple, Huawei and adjacent ML/algorithm samples spanning search, video, NLU, LLM, multimodal and data.

## Main Deliverables
Validated model capability from data through training, evaluation, deployment and monitoring.

## Responsibility Clusters
Data/split; modeling/training; experiment/eval; serving; product metrics and lifecycle.

## Skill Profile
| Skill | Required | Preferred | Responsibility | Sample N | Role Priority | Target Depth | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [[Python]] | yes |  | model and pipeline code | 7 | Core | implement | high | Job Samples |
| [[PyTorch]] | yes |  | training/experiments | 5 | Core | implement | high | Job Samples |
| [[ML-Experimentation]] | yes |  | controlled iteration | 6 | Core | implement | high | Job Samples |
| [[Model-Evaluation]] | yes |  | quality and regression | 5 | Core | implement | high | Job Samples |
| [[Data-Quality-and-Lineage]] |  | yes | trustworthy datasets | 4 | Common | use | medium | Job Samples |

## Non-skill Gates
Data and metric judgment, product constraints, reproducibility and responsible deployment.

## Seniority/Subtrack Differences
Search/ranking emphasizes data and online metrics; generative tracks add LLM/vision; production tracks add serving.

## Portfolio Evidence
Data contract, baseline, training/eval run, error slices, deployment and rollback/monitoring evidence.

## Adjacent Roles
[[Research-Engineer]]、[[Data-and-AI-Engineer]]、[[AI-Application-Engineer]]。

## Source Limitations
Public Apple/Huawei samples are company and domain biased; job titles hide team-level variation.

## Refresh
Refresh current tools every 30–60 days; revisit stable ML foundations every 180–365 days。
