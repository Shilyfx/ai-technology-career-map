---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Notion MCP新手入门: 让你的Notion不再只是一个记事本 | 从0开始搭建第一个Notion MCP工作流 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/notion-mcp-beginner-guide/"
source_url: "https://jasonai.me/download/Notion-MCP新手入门-让你的Notion不再只是一个记事本-从0开始搭建第一个Notion-MCP工作流.md"
published: 2025-08-30
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[Tool-Calling-Agent-Workflow]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
---

#### 生成Shell代码读取RSS订阅提示词

````markdown
请帮我用 PowerShell 编写一个脚本，作为 RSS 订阅聚合器。
这个脚本应该是通用的，可以轻松修改其订阅源。

**核心功能：**

1.  **可配置的输入源**：
    在脚本的开头，请定义一个名为 `$feedUrls` 的数组变量。这个变量将包含所有我想要订阅的 RSS 源 URL。请为我预先填入一些占位符或示例 URL，并加上注释，告诉我应该在这里修改或替换成我需要的 RSS 地址。

    例如：
    ```powershell
    # 请在这里替换为你需要订阅的 RSS 源 URL 列表
    $feedUrls = @(
        "https://www.dpreview.com/feeds/news.xml",  # 示例：摄影新闻
        "https://uavcoach.com/feed/",             # 示例：无人机资讯
        "https://www.4wd.com/feed"                 # 示例：越野资讯
    )
    ```

2.  **处理流程**：
    *   遍历 `$feedUrls` 数组中的每一个 URL。
    *   对于每个 URL，使用一个像 `feed2json.org` 这样的公共 API 服务，通过发送 HTTP GET 请求将其从 XML 格式转换为 JSON 格式。请在请求中加上 `-UseBasicParsing` 参数以增加兼容性。
    *   在获取到 JSON 数据后，遍历其中的每一篇文章条目（通常在 `items` 数组中）。

3.  **数据标准化**：
    *   由于不同 RSS 源的字段名可能不同，我需要你为每个条目创建一个结构统一的对象。
    *   这个对象应该包含以下五个字段：`title`, `url`, `summary`, `published`, `source`。
    *   在从原始数据映射到这个标准对象时，请遵循以下规则：
        *   `title`: 直接使用原始条目的 `title` 字段。
        *   `url`: 优先使用原始条目的 `url` 字段；如果不存在，则使用 `link` 字段。
        *   `summary`: 按顺序检查并使用第一个非空的字段：`summary` -> `description` -> `content_html`。
        *   `published`: 按顺序检查并使用第一个非空的字段：`published` -> `date_published` -> `pubDate`。
        *   `source`: 记录该条目来自的原始 RSS 源 URL。

4.  **输出**：
    *   将所有处理和标准化后的文章对象汇总到一个数组中。
    *   将这个数组转换为 JSON 格式。
    *   将生成的 JSON 字符串写入到当前脚本所在目录下的 `hotspots.json` 文件中，并确保文件编码为 UTF-8。
    *   脚本执行完毕后，在控制台打印一条消息，显示成功写入的文件名以及其中包含的文章总数。
````

#### Notion MCP提示词：读取并处理JSON数据，写入Notion数据库

````markdown
任务：知识洞察管道（面向“学习 AI 知识”）  
输入文件：./hotspots.json（格式：{"items":[{title,url,summary,published,source}]})  

目标：自动处理 hotspots.json 中的条目（最多取前 10 条），与我 Notion 工作区的最近 200 条笔记做比对，给出分类（Category）和建议 Action，然后把经我确认的条目写入 Notion 的 Knowledge Inbox（Status=draft）。  

流程：  
1) 读取并解析 ./hotspots.json，按时间排序，取前 10 条（若少于 10 则全取）。  
2) 使用 Notion MCP：读取名为 "Knowledge Inbox" 的数据库（若找不到，请提示我如何创建，或展示我已有数据库列表）。从我的 Notes（如果存在）读取最近 200 条供比对：只需 title、summary、Category。  
3) 对每个 hotspot 做“轻量语义比对”：  
   - 判断是否与现有笔记重复或高度相关（若相关请返回最相关的 note 的 title + link + 相似理由）  
   - 基于比对结果，把 hotspot 标为：New Concept / Update / Practical Technique / Reference / Duplicate / ReadingList  
4) 基于分类给出 Action 建议（Create evergreen note / Create flashcards / Schedule reading / Merge into note / None）和 Priority（0-100）。  
5) 生成写入 Notion 的候选数据，字段对应关系为：  
   - Title → json.title  
   - Published Date → json.published  （需要你进行格式转换，json中的格式是字符串，需要你转换为date格式，从而保证顺利插入到notion数据库的Published Date字段中，Published Date字段为日期格式）
   - Summary → json.summary  
   - URL → json.url  
   - Status → draft  
   - Category → AI 自动给出（基于内容和比对结果）  
6) **回显**：以表格形式在这里展示前 5 条建议（含：Title, Category, Action, Priority, 相关笔记链接（如有））。请等待我确认“OK 写入”或“跳过 #n”。  
7) 若我回复 “OK 写入” 且列出你要写入的序号，你再使用 Notion MCP 创建对应条目到 Knowledge Inbox，并把创建的 Notion 链接返回给我。  

约束：  
- 读取 Notion 的历史时只需要最近 200 条，避免过长上下文。  
- 写入前必须等待我确认“OK 写入”。  
- 不要在消息中显示任何秘钥或 token 信息；若缺权限，提示需要哪项具体权限（如：read database, create pages）。  

现在请先读取 hotspots.json，并展示你打算写入的 **表格预览（最多 5 条）**，我随后会选择确认写入哪些条目。


````


| 工具                 | 收费情况                                           | 使用地区/限制                  | 功能特性                                              | 扩展性/插件生态                           | 使用体验与适用场景                                     |
| ------------------ | ---------------------------------------------- | ------------------------ | ------------------------------------------------- | ---------------------------------- | --------------------------------------------- |
| **Cursor**         | 部分功能免费；完整功能需订阅（类似Copilot Pro，约 $20/月）          | 全球可用                     | 集成 AI 辅助编程（基于Claude/GPT）；支持MCP；支持上下文代码补全、Refactor | 可扩展 VS Code 插件；MCP兼容               | 类似 VS Code，但优化了 AI 编程体验；适合开发者想要 AI 深度辅助写代码的场景 |
| **Claude Desktop** | 免费（Claude 3.5 Sonnet 免费额度有限），Claude Pro ~$20/月 | 仅支持部分地区（目前不支持中国大陆IP，需代理） | 支持MCP客户端；支持长上下文对话（20万token级别）；桌面应用启动快             | 扩展性较弱（偏向对话而非开发工具）                  | 适合需要 Claude 强大对话和知识处理能力的人，办公/学习类工作流场景更适合      |
| **VS Code Cline**  | 免费；需自备 API Key（OpenAI/Anthropic 等）             | 全球可用（API需对应地区支持）         | VS Code 插件，支持MCP；可运行代码、调用外部API；与VS Code生态深度融合     | 插件丰富（VS Code Marketplace）；MCP高度可拓展 | 对开发者极友好，适合已经在 VS Code 中写代码的人；灵活，但需一定配置成本      |
| **Windsurf**       | 免费基础版；高级功能可能收费（类似Cursor）                       | 全球可用                     | 基于 AI 的轻量 IDE；支持MCP；偏向团队协作与云端环境                   | 插件生态较小，扩展性不如 VS Code               | 界面简洁，轻量化，适合对Cursor太重但仍想用 AI+MCP 的用户           |



| 特性 | Notion MCP | Notion AI | Dify / n8n |
| :--- | :--- | :--- | :--- |
| **核心定位** | 通过外部AI工具访问和操作Notion，充当AI大模型与Notion沟通的“嘴巴和耳朵” | Notion应用程序内部的原生AI功能 | 可视化的AI或自动化工作流平台，用于连接不同应用和执行任务 |
| **操作方式** | 依赖AI的理解和推理能力，通过简单的AI提示词，由大语言模型来主导操作 | 在Notion应用内，通过特定功能（如写作、总结）进行AI操作 | 通过调用Notion API，需要在工作流节点中进行精确、无歧义的配置来操作特定内容 |
| **交互逻辑** | AI是主角，MCP是沟通桥梁，整个流程依赖于AI的理解和推理 | 用户在Notion界面直接与AI功能交互 | 用户预设工作流，定义好每个节点的具体操作和触发条件 |
| **任务复杂度** | 能够创建工作流，实现更复杂的任务，将Notion从封闭的孤岛变成联通不同世界的枢纽 | 局限于Notion内部的AI任务，如内容生成、摘要等 | 能够搭建复杂的跨应用自动化流程，但对Notion的每一步操作都需要精确定义 |
| **主要优势** | 将Notion的潜力彻底发挥，使其能够与外部世界（AI工具）联动 | 与Notion无缝集成，操作便捷 | 强大的流程自动化和应用集成能力，可连接多种服务 |
| **学习成本** | 需要学习如何使用MCP客户端，例如Cursor, VS Code插件或Claude Desktop等 | 学习成本较低，功能直观 | 需要学习工作流平台的搭建逻辑和节点配置 |

## RSS订阅列表

|                |                              |                                                                              |     |                       |
| -------------- | ---------------------------- | ---------------------------------------------------------------------------- | --- | --------------------- |
| 领域 (Field)     | 来源/网站 (Source/Website)       | RSS 订阅 URL (RSS Feed URL)                                                    | 语言  | 备注                    |
| **AI 知识**      | **arXiv - 人工智能 (cs.AI)**     | https://export.arxiv.org/rss/cs.AI                                           | 英文  | 学术前沿，专业性强，原脚本已包含      |
|                | **机器之心 (Synced)**            | https://www.jiqizhixin.com/rss                                               | 中文  | 国内领先的 AI 产业与技术媒体      |
|                | **量子位 (QbitAI)**             | https://www.qbitai.com/feed/                                                 | 中文  | 专注 AI 和前沿科技的媒体        |
|                | **谷歌 AI 博客**                 | https://ai.googleblog.com/feeds/posts/default?alt=rss                        | 英文  | 谷歌官方 AI 研究成果发布，原脚本已包含 |
| **AI 提示词知识**   | **Prompt Engineering Daily** | https://www.promptingguide.ai/rss.xml                                        | 英文  | 专注于提示工程的指南和新闻         |
|                | **Learn Prompting**          | https://learnprompting.org/feed.xml                                          | 英文  | 提供免费的提示工程教程和资源        |
| **商业知识**       | **哈佛商业评论 (HBR)**             | https://hbr.org/rss/regular                                                  | 英文  | 顶级的商业管理思想与实践          |
|                | **36氪 (36Kr)**               | https://36kr.com/feed                                                        | 中文  | 关注中国互联网创业和商业的媒体       |
|                | **虎嗅 (Huxiu)**               | https://www.huxiu.com/rss/0.xml                                              | 中文  | 有深度的商业资讯和观点           |
| **摄影**         | **蜂鸟网 (fengniao)**           | https://www.fengniao.com/rss/index.xml                                       | 中文  | 国内知名的专业摄影门户网站         |
|                | **PetaPixel**                | https://petapixel.com/feed/                                                  | 英文  | 全球知名的摄影新闻、教程和评测博客     |
|                | **Fstoppers**                | https://fstoppers.com/feed                                                   | 英文  | 面向专业摄影师和爱好者的社区和新闻     |
| **无人机**        | **The Verge - Drones**       | https://www.theverge.com/rss/drones/index.xml                                | 英文  | 科技媒体 The Verge 的无人机专栏 |
|                | **DroneDJ**                  | https://dronedj.com/feed/                                                    | 英文  | 专注于无人机新闻和产品评测         |
| **越野**         | **越野e族 (fblife)**            | https://www.fblife.com/rss.php?fid=20                                        | 中文  | 国内大型的越野、SUV、改装主题社区    |
|                | **OutdoorX4 Magazine**       | https://outdoorx4.com/feed/                                                  | 英文  | 专注于车辆探险和越野生活方式的杂志     |
| **钓鱼**         | **Wired2Fish**               | https://www.wired2fish.com/feed                                              | 英文  | 提供钓鱼技巧、装备评测和新闻        |
|                | **Field & Stream - Fishing** | https://www.fieldandstream.com/category/fishing/feed/                        | 英文  | 知名户外杂志的钓鱼专栏           |
| **英语学习**       | **BBC Learning English**     | http://www.bbc.co.uk/learningenglish/english/features/6-minute-english/rss   | 英文  | BBC 出品的六分钟英语，非常适合日常学习 |
|                | **VOA Learning English**     | https://learningenglish.voanews.com/api/z$-oqv_tq_                           | 英文  | 美国之音的慢速英语，适合初中级学习者    |
| **科技新闻 (拓展)**  | **少数派 (sspai)**              | https://sspai.com/feed                                                       | 中文  | 高质量的消费电子产品评测和软件应用分享   |
|                | **爱范儿 (ifanr)**              | https://www.ifanr.com/feed                                                   | 中文  | 关注前沿科技、消费电子和未来趋势      |
|                | **TechCrunch**               | https://techcrunch.com/feed/                                                 | 英文  | 全球顶尖的科技创业新闻源          |
| **个人理财 (拓展)**  | **Investopedia**             | https://www.investopedia.com/feedbuilder/feed/getfeed/?feedName=rss_articles | 英文  | 权威的投资和金融知识学习网站        |
|                | **NerdWallet**               | https://www.nerdwallet.com/blog/feed                                         | 英文  | 提供信用卡、储蓄、投资等全方位的理财建议  |
| **旅行 (拓展)**    | **穷游网 (qyer)**               | http://feed.qyer.com/                                                        | 中文  | 提供旅行攻略和游记的知名中文社区      |
|                | **Nomadic Matt**             | https://www.nomadicmatt.com/travel-blog/feed/                                | 英文  | 全球知名的穷游和深度旅行博客        |
| **健康与健身 (拓展)** | **丁香医生 (dxy)**               | https://dxy.com/view/i/feed                                                  | 中文  | 提供专业、可信赖的健康科普知识       |
|                | **Men's Health**             | https://www.menshealth.com/rss/all.xml/                                      | 英文  | 关注男性健康、健身、营养和生活方式     |

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
