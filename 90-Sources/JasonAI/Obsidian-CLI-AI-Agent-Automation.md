---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian CLI 详细教程：官方命令行工具，激进拥抱智能体，高效 + 自动化 + 降低Token消耗。 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-cli-ai-agent-automation/"
source_url: "https://jasonai.me/download/Obsidian-CLI-详细教程-官方命令行工具-激进拥抱智能体-高效-自动化-降低Token消耗.md"
published: 2026-03-09
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

## Obsidian CLI 核心原理

Obsidian CLI 是一个通过命令行操作 Obsidian 笔记库的官方工具（需要 Obsidian 1.12 以上版本）。它的核心功能是为 AI 智能体（如 Gemini CLI、Claude Code、OpenClaw）和自动化工作流（如 n8n）提供原生交互接口，解决 AI 扫描整个笔记库产生高额 Token 消耗的问题。

### 架构机制对比

| 对比维度 | 传统直接读写文件系统 | 官方 CLI 调用 |
| :--- | :--- | :--- |
| **交互目标** | 本地磁盘 Markdown 文件 | 正在运行的 Obsidian 进程 |
| **Token 消耗** | 极高（需扫描数百万字符建立上下文） | 极低（约 100 Token 即可完成内置索引查询） |
| **状态感知度** | 极弱（只能读取纯文本内容） | 极强（能读取图谱关系、反向链接、插件运行状态） |
| **元数据更新** | 整体覆写（必须加载全量文件以修改 YAML） | 原子化更新（发送单条指令仅修改目标属性） |
| **数据一致性** | 差（移动文件极易导致双向链接断链） | 极佳（自动更新所有相关引用的内部链接） |


## 开启与基础配置

1. 确认系统环境，保证 Obsidian 客户端版本在 1.12 以上。
2. 进入 Obsidian 界面，打开“设置 -> 常规 (General)”。
3. 找到“命令行界面 (Command line interface)”开关并打开。
4. 在弹出的窗口中确认注册到系统 Path。
5. 保证 Obsidian 客户端处于运行状态（如果在未运行状态下执行命令，系统会自动启动客户端）。

验证配置成功的方法是打开操作系统的终端工具（Mac 使用 Terminal，Windows 使用 PowerShell），输入下面这个基础命令：

```bash
obsidian daily
```

如果配置正确，Obsidian 会直接自动应用日记模版并在界面中生成今天的日记文件。

## AI 智能体集成方案

为了让智能体工具掌握使用命令行的能力，我们需要为它们配置专门的 Agent Skill。这里以 Obsidian CEO (Steph Ango) 开发的官方 Skill 仓库为例。

### 配置 Agent Skill 目录

工具链需要严格的目录层级支持。针对不同的智能体工具，配置路径有严格的区别，必须保证 `SKILL.md` 文件在规定的层级内：

| 智能体工具 | Skill 存放路径 | 目录结构要求 |
| :--- | :--- | :--- |
| **OpenCode** | `~/.opencode/skills/` | `skills/<skill-name>/SKILL.md` |
| **Claude Code** | 项目根目录的 `.claude/` 文件夹 | 同上 |
| **Codex CLI** | `~/.codex/skills/` | 同上 |

完成目录配置后，智能体就具备了直接向 Obsidian 进程发送指令的能力。

## 场景案例与代码实现

### 案例一：让 Gemini CLI 抓取文献并生成笔记

在这个场景里，我们让智能体抓取外部数据，再用 Obsidian CLI 把数据写入笔记。

**执行提示词：**

```markdown
任务：获取 arXiv 最新 AI 论文并写入 Obsidian 今日日记。

请按以下步骤执行：

1. 获取论文数据
   从以下 RSS feed 获取论文列表：
   https://export.arxiv.org/rss/cs.AI

解析 RSS 内容，并 **按发布时间排序，选取最新发布的 10 篇论文**。

2. 提取并处理字段
   对每篇论文保留以下字段：

* title
* abstract
* link
* published date

然后执行以下处理：

* 将 **title 翻译为中文**
* 将 **abstract 翻译为中文**
* 保留原始 link
* 保留 published date

3. 整理为 Markdown 表格

生成如下格式的 Markdown 表格：

| 标题（中文） | 摘要（中文） | 原文链接 | 发布日期 |
| ------ | ------ | ---- | ---- |
| ...    | ...    | ...  | ...  |

要求：

* 每篇论文一行
* 摘要不要截断

4. 写入 Obsidian 日记

使用 **obsidian-cli skill** 完成以下操作：

* 创建或打开 **今天的日记**
* 在日记末尾追加以下内容：

## 今日AI论文

（在这里插入生成的 Markdown 表格）

5. 写入规则
* 必须使用 `obsidian-cli` skill 完成 Obsidian 操作，不要直接操作文件系统。

```

### 案例二：通过 Python 脚本调用

使用代码调用 CLI 命令适合每日定时触发的确定性任务。让 AI 编写代码时，要把 Obsidian CLI 的官方文档发送给 AI 提供上下文。

**生成代码的提示词：**

```markdown
**角色设定**：你是一位精通 Python 和自动化办公的专家，为我编写一个 Python 自动化脚本。
**任务目标**：我需要从 [输入源，例如：ArXiv API] 获取最新的 [内容类型，例如：AI 相关论文]，并将这些内容整理后通过Obsidian-CLI发送到我的Obsidian。
**详细需求**：
1. **数据获取**：从这个接口 [粘贴 URL] 获取前 10 条数据。我需要提取论文的“标题”、“发布日期”、“摘要（限制 200 字）”和“原文链接”。
2. **数据格式化**：将这些数据整理成 Markdown 表格形式，表头为：序号 | 论文名称 | 发布日期 | 简介 | 链接。
3. **与软件交互**：使用命令行方式调用Obsidian-CLI来创建并写入这些内容。

    - 使用模版 [模版名] 创建名为 [笔记名] 的笔记。
        
    - 然后将表格内容逐行追加到笔记中。
        
    - 最后自动在软件中打开这个笔记。
        
4. **稳定性要求**：
    
    - 考虑 Windows 系统的兼容性，确保代码在输出中文或特殊符号时不会报错（强制使用 UTF-8 编码）。
        
    - 因为是自动化脚本，如果操作失败（比如软件没响应或命令执行错误），务必在终端里清晰地打印出错误原因，不要静默崩溃。
        
    - 代码结构要清晰，方便我修改里面的配置参数（如笔记名称、搜索关键词等）。
```

### 案例三：在N8N工作流中调用

- 需要在本地部署N8N，以便于N8N能够直接访问本地文件系统。在Docker中部署的N8N无法做到这一点。
- 启动N8N的时候，设置参数来保证所有节点都可用：`set NODES_EXCLUDE=[] && n8n start`。（n8n 2.x 为了安全，默认禁用了涉及本地文件系统操作和 Shell 命令的节点。）
- 添加Execute Command节点，设置执行命令：`python C:\Users\jason/obsidian-cli-diary-code.py`。
- 点击Execute Step按钮测试。
- 注意事项：如果遇到utf-8编码问题，启动n8n的时候添加参数：`set PYTHONIOENCODING=utf-8 && n8n start`。

## 注意事项

* Obsidian CLI 的所有命令执行都依赖 Obsidian 桌面端程序的运行状态。
* 在本地运行 OpenClaw 这类高频自主智能体时，需要严格监控 Token 消耗。确定的日常操作建议全部转交给 n8n 或 Python 脚本。
* 浏览器内容抓取可以配合 `defuddle` 这个 Skill 工具，把网页内容清洗成干净的 Markdown 格式后直接写入笔记库。


## 官方理念与隐私边界

Obsidian 联合创始人是 Erica Xu 和 Shida Li。现任 CEO 是 Steph Ango（网络 ID 是 kepano）。

官方坚守本地优先和数据隐私底线。官方决不在软件内部强制集成任何云端 AI 模块。CLI 工具充当了一个开放的外部操作手脚。用户全权决定把笔记库接入哪种 AI 框架。

有极高隐私要求的用户可以使用 NAS 进行多端数据同步。配合本地部署的大语言模型处理数据。根据2026年的前沿模型能力测试，70B 级别的本地开源模型在执行多步骤、重度依赖工具调用的智能体任务时，表现一般。长周期任务规划能力明显弱于前沿闭源模型。智能体操作具有不可控风险。必须通过 Git 定时提交做好知识库版本备份。




# Obsidian CLI 命令列表
### Obsidian 官方 CLI 命令全景速查表 (版本要求: v1.12+)

**核心执行逻辑说明：**
- 基础格式：`obsidian <命令> 参数名=参数值 标记参数`
- 含有空格的值必须加双引号，例如：`content="Hello world"`。
- **标记参数**（如 `open`, `inline`, `total`）不需要赋值，写上就代表启用。
- 以下表格中 `file=Recipe` 代表对库中名为 Recipe 的文件执行操作，实际使用时需要替换为你库中真实存在的文件名。

| 所属模块      | 命令                             | 功能解释                              | 完整样例 (直接在终端运行)                                                        |
| :-------- | :----------------------------- | :-------------------------------- | :-------------------------------------------------------------------- |
| **基础操作**  | `help`                         | 显示帮助。加上具体命令就是查看这个命令的帮助。           | `obsidian help search`                                                |
|           | `version`                      | 显示当前 Obsidian 软件版本号。              | `obsidian version`                                                    |
|           | `reload`                       | 重新加载应用窗口。                         | `obsidian reload`                                                     |
|           | `restart`                      | 重启整个 Obsidian 应用程序。               | `obsidian restart`                                                    |
| **数据库**   | `bases`                        | 列出仓库中所有的 `.base` 数据库文件。           | `obsidian bases`                                                      |
|           | `base:views`                   | 列出当前活动数据库文件中的视图。                  | `obsidian base:views file=Contacts`                                   |
|           | `base:create`                  | 在数据库中创建新记录，支持指定字段内容。              | `obsidian base:create file=Contacts name="John Doe"`                  |
|           | `base:query`                   | 查询数据库并返回 JSON 或 CSV 结果。           | `obsidian base:query file=Contacts view=Active format=json`           |
| **书签**    | `bookmarks`                    | 列出书签。                             | `obsidian bookmarks format=json`                                      |
|           | `bookmark`                     | 将指定文件或查询条件保存为书签。                  | `obsidian bookmark file="Project A" title="当前项目"`                     |
| **命令面板**  | `commands`                     | 获取所有内置或插件命令的 ID。                  | `obsidian commands filter=workspace`                                  |
|           | `command`                      | 强制执行一个内部命令。                       | `obsidian command id=workspace:close`                                 |
|           | `hotkeys`                      | 列出所有快捷键映射。                        | `obsidian hotkeys verbose`                                            |
|           | `hotkey`                       | 获取单个命令的具体快捷键。                     | `obsidian hotkey id=workspace:close`                                  |
| **日记**    | `daily`                        | 打开当天的每日笔记。                        | `obsidian daily paneType=tab`                                         |
|           | `daily:path`                   | 输出每日笔记的物理路径。                      | `obsidian daily:path`                                                 |
|           | `daily:read`                   | 打印当天每日笔记的文本内容。                    | `obsidian daily:read`                                                 |
|           | `daily:append`                 | 向每日笔记末尾追加文本，适合快速记录。               | `obsidian daily:append content="- [ ] 记得回复邮件"`                        |
|           | `daily:prepend`                | 向每日笔记开头插入文本。                      | `obsidian daily:prepend content="# 今日重点"`                             |
| **文件历史**  | `diff`                         | 对比不同历史版本。                         | `obsidian diff file=Recipe from=2 to=1`                               |
|           | `history` / `history:list`     | 显示有本地历史记录的文件列表。                   | `obsidian history file=Recipe`                                        |
|           | `history:read`                 | 读取某个历史版本的内容。                      | `obsidian history:read file=Recipe version=1`                         |
|           | `history:restore`              | 将文件回滚到指定历史版本。                     | `obsidian history:restore file=Recipe version=2`                      |
|           | `history:open`                 | 在界面中打开文件恢复面板。                     | `obsidian history:open file=Recipe`                                   |
| **文件与目录** | `file` / `folder`              | 显示文件或文件夹的元数据（大小、时间）。              | `obsidian file path="Notes/Recipe.md"`                                |
|           | `files` / `folders`            | 遍历列表，支持后缀过滤并返回总数。                 | `obsidian files ext=md total`                                         |
|           | `open`                         | 打开文件。                             | `obsidian open file=Recipe newtab`                                    |
|           | `create`                       | 静默创建文件，支持预设内容或应用模板。               | `obsidian create name=Meeting content="# 会议记录" overwrite`             |
|           | `read`                         | 打印文件内容，Agent 接入必用命令。              | `obsidian read file=Recipe`                                           |
|           | `append` / `prepend`           | 在文件末尾或头部插入内容。                     | `obsidian append file=Recipe content="追加的文本"`                         |
|           | `move` / `rename`              | 移动或重命名文件（自动更新双链）。                 | `obsidian rename file=Recipe name=NewRecipe`                          |
|           | `delete`                       | 删除文件，可附加 `permanent` 彻底删除。        | `obsidian delete file=Recipe permanent`                               |
| **链接网络**  | `backlinks`                    | 列出指向这个文件的反向链接。                    | `obsidian backlinks file=Index format=json`                           |
|           | `links`                        | 列出这个文件包含的出站链接。                    | `obsidian links file=Index total`                                     |
|           | `unresolved`                   | 提取未创建实体文件的死链接节点。                  | `obsidian unresolved format=json`                                     |
|           | `orphans`                      | 列出没有被引用的孤立文件。                     | `obsidian orphans total`                                              |
|           | `deadends`                     | 列出没有向外发出引用的死胡同笔记。                 | `obsidian deadends total`                                             |
| **大纲**    | `outline`                      | 提取文件的标题树状结构。                      | `obsidian outline file=Recipe format=tree`                            |
| **插件管理**  | `plugins` / `enabled`          | 列出所有插件或已开启的插件。                    | `obsidian plugins filter=community`                                   |
|           | `plugins:restrict`             | 开关安全模式。                           | `obsidian plugins:restrict off`                                       |
|           | `plugin` / `plugin:enable`     | 查询插件信息或开启插件。                      | `obsidian plugin:enable id=dataview`                                  |
|           | `plugin:disable`               | 禁用插件。                             | `obsidian plugin:disable id=dataview`                                 |
|           | `plugin:install` / `uninstall` | 静默安装或卸载社区插件。                      | `obsidian plugin:install id=dataview enable`                          |
|           | `plugin:reload`                | 热重载插件（适合开发调试）。                    | `obsidian plugin:reload id=my-plugin`                                 |
| **属性元数据** | `aliases`                      | 提取别名列表。                           | `obsidian aliases active`                                             |
|           | `properties`                   | 提取 YAML 属性，支持排序。                  | `obsidian properties sort=count`                                      |
|           | `property:set`                 | 修改属性值，规范化文本、日期等类型。                | `obsidian property:set name=status value=draft type=text file=Recipe` |
|           | `property:remove` / `read`     | 删除属性或提取特定属性值。                     | `obsidian property:read name=status file=Recipe`                      |
| **发布**    | `publish:site` / `list`        | 获取 Publish 站点信息或已发布清单。            | `obsidian publish:list`                                               |
|           | `publish:status` / `add`       | 检查变更或推送到云端。                       | `obsidian publish:add changed`                                        |
|           | `publish:remove` / `open`      | 撤销发布或在浏览器中查看线上页面。                 | `obsidian publish:open file=Recipe`                                   |
| **随机笔记**  | `random` / `random:read`       | 打开随机笔记或直接打印其内容。                   | `obsidian random folder="Zettelkasten" newtab`                        |
| **全局搜索**  | `search`                       | 全文检索，返回文件路径列表。                    | `obsidian search query="TODO" format=json`                            |
|           | `search:context`               | 提供包含上下文的检索结果。                     | `obsidian search:context query="重要" limit=5`                          |
|           | `search:open`                  | 在图形界面中唤出搜索面板。                     | `obsidian search:open query="会议记录"`                                   |
| **官方同步**  | `sync` / `sync:status`         | 控制同步进程开关，查看状态。                    | `obsidian sync on`                                                    |
|           | `sync:history` / `read`        | 查阅云端版本历史记录或读取内容。                  | `obsidian sync:read file=Recipe version=1`                            |
|           | `sync:restore`                 | 强制回滚到云端版本。                        | `obsidian sync:restore file=Recipe version=2`                         |
|           | `sync:open` / `deleted`        | 打开界面查看历史或已删除文件。                   | `obsidian sync:deleted`                                               |
| **标签**    | `tags`                         | 提取标签网络，统计频次。                      | `obsidian tags sort=count format=json`                                |
|           | `tag`                          | 查询单个标签的分布和出现次数。                   | `obsidian tag name="#important" verbose`                              |
| **任务管理**  | `tasks`                        | 检索全库或指定日记的任务状态。                   | `obsidian tasks todo daily`                                           |
|           | `task`                         | 终端直连修改具体任务的勾选状态。                  | `obsidian task ref="Recipe.md:8" toggle`                              |
| **模板**    | `templates` / `template:read`  | 查看模板库，或解析带变量的模板内容。                | `obsidian template:read name=Meeting resolve`                         |
|           | `template:insert`              | 将模板注入到活动笔记中。                      | `obsidian template:insert name=Meeting`                               |
| **外观与样式** | `themes` / `theme`             | 查看安装的主题或查看当前主题详情。                 | `obsidian themes versions`                                            |
|           | `theme:set` / `install`        | 切换主题，或从终端安装并启用新主题。                | `obsidian theme:install name="Minimal" enable`                        |
|           | `theme:uninstall`              | 卸载主题。                             | `obsidian theme:uninstall name="Minimal"`                             |
|           | `snippets` 相关命令                | 开关 CSS 片段。                        | `obsidian snippet:enable name=custom-font`                            |
| **卡片盒模式** | `unique`                       | 按照 Zettelkasten 时间戳生成唯一笔记。        | `obsidian unique name="Idea" open`                                    |
| **仓库管理**  | `vault` / `vaults`             | 获取当前仓库信息或列出所有本地仓库。                | `obsidian vaults verbose`                                             |
|           | `vault:open`                   | 强制软件跳转打开另一个仓库。                    | `obsidian vault:open name="My Vault"`                                 |
| **内置浏览器** | `web`                          | 在 Obsidian 内直接打开网页。               | `obsidian web url="https://google.com" newtab`                        |
| **字数统计**  | `wordcount`                    | 统计字数或字符数。                         | `obsidian wordcount file=Recipe words`                                |
| **工作区布局** | `workspace` 系列命令               | 保存、载入、删除窗口布局配置。                   | `obsidian workspace:load name=Writing`                                |
|           | `tabs` / `tab:open`            | 管理标签页组，或者在新标签打开文件。                | `obsidian tab:open file=Recipe`                                       |
|           | `recents`                      | 返回最近打开文件的记录。                      | `obsidian recents total`                                              |
| **开发者模式** | `devtools` / `dev:debug`       | 调出底层控制台或挂载 Chrome 调试器。            | `obsidian dev:debug on`                                               |
|           | `dev:cdp`                      | 顶级权限，调用 Chrome DevTools Protocol。 | `obsidian dev:cdp method="Network.enable"`                            |
|           | `dev:screenshot`               | 生成软件当前界面的 base64 图片数据流。           | `obsidian dev:screenshot path=screenshot.png`                         |
|           | `dev:console` / `css`          | 读取控制台日志，或抓取 CSS 渲染数据。             | `obsidian dev:console level=error`                                    |
|           | `dev:dom`                      | 用 CSS 选择器直接抓取界面 DOM 元素。           | `obsidian dev:dom selector=".cm-content" text`                        |
|           | `dev:mobile`                   | 开启移动端布局模拟。                        | `obsidian dev:mobile on`                                              |
|           | `eval`                         | 注入 JavaScript 代码到底层执行并返回结果。       | `obsidian eval code="app.vault.getFiles().length"`                    |


# Obsidian CLI 典型自动化应用场景与工作流

| 工作流名称                   | 功能简介                                                                                                                                                                                | 涉及的 CLI 命令                                                                                                                                                |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. 全局极速闪记 **          | **痛点**：记录一闪而过的灵感时，打开软件、等插件加载、找文件太慢。<br>**方案**：在 Raycast、Alfred 甚至手机捷径中绑定一段终端脚本。输入文字后，脚本在后台直接调用 CLI，将文字无感追加到今天的日记末尾。完全不需要唤醒 Obsidian 界面。                                             | `obsidian daily:append content="灵感内容"`                                                                                                                    |
| **2. 播客/视频沉浸式知识榨取**     | **痛点**：看完 YouTube 视频后，手动整理笔记并建立待办事项费时费力。<br>**方案**：把链接丢给 OpenClaw 或 Telegram 机器人。AI 提取字幕并总结后，调用 CLI 直接使用你的“媒体笔记模板”创建新文件，并把提取出的行动项自动打上标签，插入到当天的日记中。                                  | `obsidian create name="视频名" template="Media"`<br>`obsidian daily:append content="- [ ] 待办项"`                                                              |
| **3. AI 收件箱自动分拣员 **     | **痛点**：平时用 Web Clipper 随手剪藏的网页堆积在 Inbox 文件夹，变成“赛博垃圾场”。<br>**方案**：利用 n8n 建立定时任务，让大模型批量阅读 Inbox 里的文件。理解内容后，通过 CLI 规范化注入 YAML 属性（如作者、分类），最后安全地将文件重命名并移动到对应的归档文件夹。CLI 会自动更新全库的双链，绝不断链。  | `obsidian files folder="Inbox"`<br>`obsidian read file="未命名"`<br>`obsidian property:set name="category" value="AI"`<br>`obsidian move file="旧名" to="新路径"` |
| **4. 绝对隐私的本地 RAG 对话助理** | **痛点**：搭建向量数据库（Chroma/Milvus）太繁琐，且每次笔记更新都要重新 Embedding（向量化）。<br>**方案**：在本地运行 Claude Code 或本地大模型，赋予其 CLI 执行权限。AI 会根据你的提问，自主使用带有上下文的全局搜索指令，并通过提取反向链接顺藤摸瓜，构建准确的背景知识库后再回答，完全零配置。        | `obsidian search:context query="关键词"`<br>`obsidian backlinks file="检索到的文件"`<br>`obsidian read file="目标笔记"`                                                |
| **5. 跨平台数据库级联录入**       | **痛点**：外部数据（如记账、习惯打卡）很难干净地录入到 Obsidian 的表格或 Dataview 中。<br>**方案**：结合 Obsidian 1.12 最新的 Bases（数据库）功能。通过 n8n 接收外部 Webhook（比如银行消费短信），直接让 CLI 在指定的 Base 文件中创建一条新记录，并严格按数据类型（数字、日期）注入字段。 | `obsidian base:create file="财务库" name="打车"`<br>`obsidian property:set type="number" value="30"`                                                           |
| **6. 历史知识自动唤醒与破冰**      | **痛点**：记录了大量笔记但从不回顾，知识变成死水。<br>**方案**：每天早晨执行一个自动化脚本，利用 CLI 提取一篇早于 1 年前的随机笔记，交给 AI 提炼核心观点，并与你最近一周关注的标签（如 `#Agent`）进行强行跨界联想，将联想结果作为“每日思考”追加到今天日记中。                                    | `obsidian random:read folder="卡片盒"`<br>`obsidian tags sort=count limit=5`<br>`obsidian daily:prepend content="AI的跨界联想"`                                   |
| **7. 批量元数据重构与清洗**       | **痛点**：笔记库用久了，属性极其混乱（比如状态标签混用了 `doing`、`in-progress`、`进行中`），导致 Dataview 列表报错。<br>**方案**：让 AI 脚本遍历你的核心文件夹，读取现有的属性值，统一转换为标准格式，然后用 CLI 进行批量覆写。这种方式强制符合 YAML 语法，绝不会多一个空格或少一个引号。         | `obsidian properties`<br>`obsidian property:read name="status"`<br>`obsidian property:set name="status" value="标准值"`                                      |

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
