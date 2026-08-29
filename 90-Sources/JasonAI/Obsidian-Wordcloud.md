---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian 教程：如何制作炫酷词云图表：一眼看穿知识库重点 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-wordcloud-tutorial/"
source_url: "https://jasonai.me/download/Obsidian-教程-如何制作炫酷词云图表-一眼看穿知识库重点.md"
published: 2025-08-10
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

```chartsview
# 1. 定义图表类型为词云图
type: WordCloud

# 2. 配置图表选项
options:
  wordField: "word"
  weightField: "count"
  colorField: "word"
  wordStyle:
    rotation: 0

# 3. 使用 dataviewjs 返回一个超大、超丰富的静态假数据
# 词汇量翻倍，并引入了计算机、效率工具、开发工具等大量相关词汇
data: |
  dataviewjs:
  return [
    { "word": "AI", "count": 1850 },
  { "word": "Obsidian", "count": 1620 },
  { "word": "Notion", "count": 1480 },
  { "word": "提示词", "count": 1350 },
  { "word": "视频", "count": 1120 },
  { "word": "工作流", "count": 1050 },
  { "word": "自动化", "count": 980 },
  { "word": "知识库", "count": 950 },
  { "word": "YouTube", "count": 910 },
  { "word": "模型", "count": 880 },
  { "word": "n8n", "count": 760 },
  { "word": "提示词工程", "count": 730 },
  { "word": "API", "count": 690 },
  { "word": "插件", "count": 650 },
  { "word": "GitHub", "count": 620 },
  { "word": "Gemini", "count": 590 },
  { "word": "上下文", "count": 580 },
  { "word": "课程", "count": 550 },
  { "word": "RAG", "count": 540 },
  { "word": "代码", "count": 480 },
  { "word": "小红书", "count": 450 },
  { "word": "标题", "count": 420 },
  { "word": "Dify", "count": 400 },
  { "word": "结构化", "count": 380 },
  { "word": "独立站", "count": 350 },
  { "word": "双链", "count": 280 },
  { "word": "MOC", "count": 250 },
  { "word": "Claude", "count": 820 },
  { "word": "DeepSeek", "count": 780 },
  { "word": "MCP", "count": 750 },
  { "word": "Cursor", "count": 720 },
  { "word": "GGUF", "count": 680 },
  { "word": "Zotero", "count": 650 },
  { "word": "DeepL", "count": 630 },
  { "word": "Grammarly", "count": 610 },
  { "word": "JavaScript", "count": 590 },
  { "word": "TypeScript", "count": 570 },
  { "word": "YAML", "count": 550 },
  { "word": "Frontmatter", "count": 530 },
  { "word": "Metadata", "count": 510 },
  { "word": "原子笔记", "count": 490 },
  { "word": "Zettelkasten", "count": 470 },
  { "word": "PARA", "count": 450 },
  { "word": "ROI", "count": 430 },
  { "word": "MCP Server", "count": 350 },
  { "word": "Structured", "count": 330 },
  { "word": "CSV", "count": 310 },
  { "word": "TSV", "count": 290 },
  { "word": "Regex", "count": 270 },
  { "word": "数字分身", "count": 250 },
  { "word": "Hook", "count": 230 },
  { "word": "Callout", "count": 210 },
  { "word": "Deep Research", "count": 190 },
  { "word": "跨境支付", "count": 170 }
  ];
```

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
