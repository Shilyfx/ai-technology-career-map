---
type: assessment
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Start-Here]]"
  - "[[Learning-Path]]"
  - "[[Role-Based-Learning-Paths]]"
---

# Fast-Track Assessment

> 用真实产出跳过已经掌握的部分；不按自我感觉跳过关键闭环。

## 20 分钟定位

| 问题 | 如果能给出证据 | 可先略读 |
| --- | --- | --- |
| 能否解释一次训练的 data→split→baseline→metric→failure→decision？ | 仓库、报告或口头拆解 | [[Training-Evaluation-and-Generalization]] |
| 能否解释 Transformer 从 token/embedding 到 attention/生成？ | 图示 + 关键约束 | [[Transformer-and-Foundation-Models]] |
| 是否做过可复现训练或分析管线？ | 命令、配置、日志、测试 | [[Math-Data-and-Software-Foundations]] |
| 是否做过有任务集的 RAG/Agent，而不仅是 demo？ | task set、trace、eval、失败案例 | [[RAG-and-Knowledge-Systems]]、[[AI-Agents-and-Tool-Use]] |
| 能否报告系统的 p95、成本、回滚和权限边界？ | dashboard、测试或设计文档 | [[AI-Infrastructure-and-MLOps]]、[[Inference-Optimization]] |
| 能否写 threat model 与安全 eval？ | 风险表、攻击样例、mitigation | [[AI-Safety-Security-and-Governance]] |

## 结果解释

- **0–1 项有证据**：按 [[Learning-Path]] 从 Stage 0–2 开始；
- **2–3 项有证据**：跳到最薄弱的一个层，避免平均用力；
- **4–5 项有证据**：从 [[Technology-Radar-2026-08]] 的 Build/Deepen 选择一个新方向；
- **6 项有证据**：重点做 [[Role-Based-Learning-Paths]] 的岗位作品与市场校准。

## Assessment → Evidence → Depth

把每个“有证据”的回答链接到一张实际 Evidence 页：复制 [[Evidence-Card]] 模板创建页面，再把页面链接回这里，并标注它证明的是 `recognize`、`explain`、`use`、`implement`、`optimize` 还是 `research`。没有实际页面、失败分析和判断的自评只能作为线索，不能用于跳过 Stage。

## 常见的“假通过”

- 训练过模型，但 Test 集反复调参；
- 做过 RAG，但没有答案和引用的独立评测；
- 部署过 API，但没有测 tail latency、成本和失败恢复；
- 看过安全文章，但没有一个系统的 threat model；
- 读过论文，但没有复现、对照或失败分析。

这些不是否定已有经验，而是指出下一段学习最有价值的证据缺口。
