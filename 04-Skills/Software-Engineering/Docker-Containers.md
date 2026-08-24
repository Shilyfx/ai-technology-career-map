---
type: skill
skill_category: software-engineering
status: seed
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
prerequisites:
  - "[[Linux]]"
related_concepts:
  - "[[AI-Infrastructure-and-MLOps]]"
---

# Docker / Containers

## 为什么岗位需要它

容器把应用、训练和推理环境的依赖边界固定下来，是部署、复现和隔离的工程手段。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Infra | Common | implement | [[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]] | reproducible systems |
| ML / AI Engineer | Common | use | [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]] | train/inference stack |
| Application Engineer | Common | use | [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]] | orchestration |

## Job Evidence

[[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用

构建镜像、隔离依赖、挂载数据、限制资源、健康检查和发布回滚。

## Role-specific Target Depth

Infra implement；其他工程岗至少能复现和诊断容器化服务。

## 前置 Skills

[[Linux]]。

## 学习范围

镜像、层、网络、卷、权限、资源和供应链安全。

## 核心知识

容器不是虚拟机；需要明确运行时、GPU/NPU 透传和数据生命周期。

## Practice

把一个模型 API 打成可复现镜像，并加入健康检查、资源限制和版本标签。

## Pass Evidence

在 clean host 上按命令启动，并记录镜像、依赖、配置和一次失败恢复。

## 常见失败

镜像不可复现、把密钥烘进镜像、忽略 GPU 驱动兼容性。

## 不需要深挖到什么程度

非 Infra 岗位不要求实现容器运行时；要能安全交付。

## Related Knowledge

[[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]]、[[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]]。
