---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "AI时代的图表语言！Mermaid 新手入门教程：让你用文本秒生流程图、甘特图，思维导图…… | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/mermaid-beginner-tutorial-flowchart-gantt-mindmap/"
source_url: "https://jasonai.me/download/AI时代的图表语言-Mermaid-新手入门教程-让你用文本秒生流程图-甘特图-思维导图.md"
published: 2025-07-28
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[Technical-Communication]]"
  - "[[AI-Product-Engineering]]"
  - "[[AI-Product-Manager]]"
---

Mermaid 是一种基于 JavaScript 的图表和图表绘制工具，它使用类似 Markdown 的文本定义来动态生成图表和可视化内容。 由于其语法简单直观，用户可以轻松地将复杂的图表以文本形式嵌入到文档、网站和笔记中，便于维护和版本控制。




```mermaid
pie
    title 一份工作报告的时间分配
    "资料收集与整理" : 45
    "数据分析" : 20
    "报告撰写" : 29
    "图表制作" : 70
```


```mermaid
mindmap
  root((核心主题))
    分支1
      子主题 A
      子主题 B
    分支2
      子主题 C
      子主题 D
        更深层次的主题 E
    分支3
      子主题 F
```



```mermaid
flowchart TD
    A[开始] --> B{条件判断}
    B -->|是| C[执行操作1]
    B -->|否| D[执行操作2]
    C --> E[结束]
    D --> E
```

```mermaid
sequenceDiagram
    participant 用户
    participant 系统
    用户->>系统: 登录请求
    系统->>用户: 验证请求
    用户->>系统: 提交凭证
    系统-->>用户: 登录成功
```

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title       项目发布计划

    section 项目准备
    需求分析与规格书      :done,    req, 2024-07-29, 7d
    UI/UX 设计          :active,  design, 2024-08-05, 10d
    技术选型与架构设计    :         arch, 2024-08-05, 5d

    section 核心开发
    前端开发            :         frontend, after design, 20d
    后端开发            :         backend, after arch, 25d
    数据库设计          :crit,     db, 2024-08-12, 5d

    section 测试与上线
    集成测试            :         testing, after backend, 7d
    用户验收测试 (UAT)   :         uat, after testing, 5d
    正式上线            :         deploy, 2024-10-01, 2d
```


```mermaid
journey
    title 购物流程
    section 浏览商品
      用户: 5: 查看商品列表
      系统: 3: 加载推荐
    section 下单
      用户: 4: 加入购物车
      系统: 2: 库存检查
```


```mermaid
gantt
    title 企业级CRM系统上线项目 
    dateFormat  YYYY-MM-DD

    section 规划与准备
    项目启动与需求分析      :done, 2025-09-01, 7d
    制定详细实施方案        :active, 2025-09-10, 5d

    section 系统实施与测试
    系统核心功能配置        : 2025-09-17, 15d
    数据迁移与验证          : 2025-10-08, 10d
    用户验收测试 (UAT)      : 2025-10-22, 7d

    section 上线与支持
    用户培训                : 2025-11-04, 5d
    系统正式上线            : 2025-11-11, 1d
    上线后初步支持          : 2025-11-12, 5d
```

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
