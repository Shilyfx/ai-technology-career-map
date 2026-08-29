---
type: skill
skill_category: programming
status: developing
stability: stable
evidence_mode: prerequisite-synthesis
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-28
roles:
  - "[[Research-Engineer]]"
  - "[[ML-and-AI-Engineer]]"
  - "[[AI-Application-Engineer]]"
  - "[[Data-and-AI-Engineer]]"
  - "[[AI-Infrastructure-and-Inference-Engineer]]"
prerequisites: []
related_concepts:
  - "[[Math-Data-and-Software-Foundations]]"
---

# Data Structures and Algorithms

## 为什么岗位需要它

AI 岗位不是只调用模型 API。数据管道、检索、评测 runner、队列和服务性能都需要把问题拆成数据结构、复杂度和可验证的不变量。

## Role Demand

这是 Research、ML、Application、Data 和 Infra 工程岗位的通用前置能力；目标是能读懂、实现和分析与交付物相关的算法，不是为了刷题而刷题。

## Job Evidence

当前 Job Sample 的抽取表把 Python、分布式系统、数据和测试分开记录，没有把“数据结构与算法”作为独立标签。因此本页是从各 Role 的代码、规模、可靠性和性能交付物综合出的 prerequisite，不增加招聘频次统计。

## 在岗位中怎么使用

选择 list/hash/index/heap/queue/graph 等结构，分析时间与空间复杂度，处理去重、排序、采样、缓存、调度和流式数据。

## Role-specific Target Depth

Application/Data 需要 use/implement；Research/ML 需要 implement；Infra/Inference 在调度、缓存和性能路径上继续 optimize。

## 前置 Skills

无；可与 [[Python]] 并行学习。

## 学习范围

复杂度、数组/链表、哈希、树/图、堆、队列、排序/搜索、递归、贪心、动态规划、并发下的数据一致性。

## 核心知识

先写不变量和边界，再选结构；先测量瓶颈，再优化复杂度。算法正确不等于系统满足权限、延迟和可观测性要求。

## Practice

用 Python 实现一个带去重、分页、优先级队列和缓存的评测任务 runner；为 1k/10k/100k 输入写基准，记录复杂度和失败输入。

## Pass Evidence

第三方能运行测试和 benchmark；你能解释一个结构选择、一次复杂度权衡和一个被测试捕获的边界错误。

## 常见失败

只背模板、不写不变量；忽略最坏情况；用复杂结构掩盖数据质量问题；优化前没有 profile。

## 不需要深挖到什么程度

目标岗位不是算法研究时，不需要先证明新算法；先掌握能支撑数据、API、评测和服务交付的常用结构。

## Related Knowledge

[[Python]]、[[SQL]]、[[Testing]]、[[Distributed-Systems]]、[[ML-Experimentation]]。

## Actual Evidence

尚无用户能力结论；完成 Practice 后使用 [[Evidence-Card]] 记录。

## Sources

[[Math-Data-and-Software-Foundations]]、[[AI-Environment-Setup-NodeJS-Git-Python]]、[[GitHub-Beginner-Guide]]。

