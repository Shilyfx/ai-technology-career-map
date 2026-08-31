---
type: skill
skill_category: programming
status: developing
stability: stable
created: 2026-08-24
updated: 2026-08-24
review_after: 2027-02-24
roles:
  - "[[Research-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[Data-and-AI-Engineer]]"
prerequisites: []
recommended_foundations:
  - "[[Data-Structures-and-Algorithms]]"
related_concepts:
  - "[[Math-Data-and-Software-Foundations]]"
---

# Python

## 为什么岗位需要它

它在研究实验、数据管道、服务端和评测工具之间提供可迁移的实现能力；样本把它作为明确语言要求或日常工程基础。

## Role Demand

| Role | Priority | Target Depth | Job Evidence | Note |
| --- | --- | --- | --- | --- |
| Research Engineer | Core | implement | [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]] | 实验与评测系统 |
| ML / AI Engineer | Core | implement | [[Apple-Machine-Learning-Engineer-Search-Cupertino-2026-06]] | 生产 ML |
| Application Engineer | Core | implement | [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]] | 后端服务 |

## Job Evidence

[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Search-Cupertino-2026-06]] 的 `Skill Extraction` 是本 Skill 的 Job Evidence；只把明确要求作为 required 证据，职责推断保留为 inferred。

## 在岗位中怎么使用

写可测试的 pipeline、API、训练/评测脚本和数据处理，而不是只维护 notebook。

## Role-specific Target Depth

PM 以 explain 为边界；工程岗位通常需要 implement，研究/系统岗位再按任务加深。

## 前置 Skills

无；先掌握 Git、测试和基础数据结构。

## 学习范围

模块、类型、异常、并发边界、包管理、测试、日志和可复现环境。

## 核心知识

函数与对象、I/O、数据结构、pytest、虚拟环境、性能诊断。

## Practice

做一个参数化数据→评测命令行工具，含配置、日志、测试和失败输入。

## Pass Evidence

别人可按 README 运行，并看到至少一个自动化测试捕获错误输入。

## 常见失败

只会调用 SDK、没有测试、把环境差异误判为模型差异。

## 不需要深挖到什么程度

不因某个岗位出现 Python 就要求解释 CPython 内部；以目标交付为准。

## Related Knowledge

[[Math-Data-and-Software-Foundations]]、[[AI-Product-Engineering]]。

## Actual Evidence

尚无用户能力结论；使用 [[Evidence-Card]] 创建实际记录。

## Sources

[[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]]、[[Apple-Machine-Learning-Engineer-Search-Cupertino-2026-06]]。
