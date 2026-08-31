---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "用N8N给你的Obsidian植入AI大脑，将你的知识库打造成真正的 AI 神器 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/n8n-obsidian-ai-rss-automation/"
source_url: "https://jasonai.me/download/用N8N给你的Obsidian植入AI大脑-将你的知识库打造成真正的-AI-神器.md"
published: 2025-10-02
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
---

# n8n 与 Obsidian 集成指南



## 1. n8n 的安装与启动

n8n 提供了多种安装方式，此处介绍两种最常用的方法：通过 Node.js 和通过 Docker。

### 1.1 通过 Node.js 安装 (推荐新手)

**前置条件**: 安装 Node.js。访问 [Node.js 官网](https://nodejs.org/) 下载并安装最新 LTS 版本。

1.  **验证安装**: 打开命令行终端 (CMD, PowerShell, or Terminal)，执行以下命令验证 Node.js 和 npm 是否安装成功。
    ```bash
    node -v
    npm -v
    ```
    如果能正常显示版本号，则说明安装成功。

2.  **安装 n8n**: 在命令行终端中执行以下命令来全局安装 n8n。
    ```bash
    npm install -g n8n
    ```

3.  **启动 n8n**: 安装完成后，执行以下命令启动 n8n 服务。
    ```bash
    n8n
    ```
    当终端显示服务已启动后，在浏览器中访问 `http://localhost:5678` 即可进入 n8n 界面。

### 1.2 通过 Docker 安装

**前置条件**: 安装 Docker Desktop。

1.  **拉取并运行 n8n 容器**: 打开命令行终端，执行以下 Docker 命令。
    ```bash
    docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
    ```
2.  **访问 n8n**: 容器运行后，同样在浏览器中访问 `http://localhost:5678`。

**初次设置**: 首次访问 n8n 需要设置一个管理员账户。完成注册后即可进入 n8n 主界面。

---

## 2. 在 n8n 中集成 Obsidian

集成的核心是利用 Obsidian 的社区插件 `Local REST API` 对外暴露接口，然后在 n8n 中使用 `HTTP Request` 节点来调用这些接口。

### 2.1 Obsidian 配置

1.  **安装插件**: 在 Obsidian 中，进入 `设置` -> `第三方插件` -> `社区插件市场`，搜索并安装 `Local REST API` 插件。
2.  **启用并配置**:
    *   安装后启用该插件。
    *   进入插件的设置页面。
    *   **开启 HTTP 服务**: 找到并打开 `Enable Non-encrypted (HTTP) Server` 这个开关。
    *   **获取 API Key**: 复制页面上显示的 `Your API Key`。这是一个长字符串，是后续操作的身份凭证。
    *   **确认 API 地址**: 记下 `Non-encrypted (HTTP) API URL`，默认为 `http://127.0.0.1:27123/`。

### 2.2 n8n 节点配置：读取 Vault 列表

1.  **创建工作流**: 在 n8n 主页，点击 `Create Workflow` 创建一个新的工作流。
2.  **添加 HTTP 节点**: 添加一个 `HTTP Request` 节点。
3.  **配置节点**:
    *   **Method**: `GET`
    *   **URL**: `http://127.0.0.1:27123/vault/` (此地址用于获取 Vault 内所有文件和文件夹列表)。
    *   **Authentication**: `Generic Credential Type`
    *   **Generic Auth Type**: `Bearer Auth`
    *   **Bearer Auth account**: 点击 `Create New` 创建新凭证。
        *   **Name**: `Obsidian API Key`
        *   **Bearer Token**: 粘贴上一步从 Obsidian 复制的 `API Key`。
        *   保存凭证。
4.  **执行测试**: 点击节点右上角的 `Execute step`。如果配置正确，右侧的 `OUTPUT` 区域将显示一个包含您 Vault 内所有笔记和文件夹列表的 JSON 对象。

> [!note] Docker容器访问宿主机服务的网络问题
> 当n8n通过Docker部署时，其HTTP Request节点可能会无法访问宿主机（Host Machine）上运行的服务（如Obsidian Local REST API）。这是因为在Docker容器内部，`localhost` 或 `127.0.0.1` 指向的是容器本身，而非宿主机。正确的解决方法是将URL中的 `127.0.0.1` 替换为Docker提供的特殊DNS名称 `host.docker.internal`，它能正确解析到宿主机的IP地址。例如，应将 `http://127.0.0.1:27123/vault/` 修改为 `http://host.docker.internal:27123/vault/` 以确保连接成功。



### 2.3 n8n 节点配置：创建一篇新笔记

接下来，我们将修改上述节点以实现创建笔记的功能。

1.  **修改 Method**: 将 `GET` 修改为 `POST`。
2.  **修改 URL**: 指定要创建的文件名，例如: `http://127.0.0.1:27123/vault/我的第一篇n8n知识笔记.md`。
3.  **配置 Headers**:
    *   **开启 `Send Headers` 开关**。
    *   添加一个 Header:
        *   **Name**: `Content-Type`
        *   **Value**: `text/plain`
4.  **配置 Body**:
    *   **开启 `Send Body` 开关**。
    *   **Body Content Type**: `Raw`。
    *   **Body**: **必须将输入模式切换为 `Expression`**，以保留 Markdown 的换行格式。然后输入Markdown 内容。
    ```markdown
    # 这是笔记的标题

    这篇笔记是通过 n8n 自动创建的。

    ## 待办事项
    - [ ] 完成自动化工作流
    - [ ] 学习更多 n8n 技巧

    当前创建时间：{{ $now }}
    ```
5.  **执行测试**: 点击 `Execute step`。成功后，在您的 Obsidian Vault 中即可看到这篇新创建的笔记。

> **API 文档**: `Local REST API` 插件提供了完整的 API 接口文档，您可以在插件设置页面找到 `the online docs` 链接进行查阅，以实现更多高级操作（如更新、删除、搜索笔记等）。

---

## 3. 构建自动化工作流：RSS -> AI -> Obsidian

这是一个简单的实例，用于演示如何将多个节点串联起来，形成自动化生产线。

### 3.1 步骤一：添加 RSS 读取节点

1.  在工作流中添加一个 `RSS Read` 节点。
2.  在 `URL` 字段中，输入您想订阅的 RSS 源地址。例如 IT之家的 RSS 地址。
3.  执行节点，您将获取到最新的10篇文章列表。

### 3.2 步骤二：添加 AI 处理节点 (以智谱 GLM 为例)

1.  添加一个 `OpenAI` 节点。
2.  **配置凭证**:
    *   点击 `Credential` -> `Create New`。
    *   **Name**: `Zhipu GLM Key`
    *   **API Key**: 粘贴您的智谱 AI API Key。
    *   **添加 Base URL**: 点击 `Add Option` -> `Base URL`，填入智谱的 OpenAI 兼容接口地址: `https://open.bigmodel.cn/api/paas/v1beta/`
    *   保存凭证 (忽略可能出现的连接错误)。
3.  **配置模型**:
    *   **Resource**: `Chat`。
    *   **Model**: 将输入模式切换为 `Expression`，并输入模型ID，例如 `"glm-4-flash"`。
4.  **配置提示词 (Prompt)**:
    *   在 `Messages` -> `Content` 中编写您的提示词。
    *   **关键操作**: 从左侧 `INPUT` 面板中，将上一步 RSS 节点的文章内容 (如 `description` 字段) 拖拽到提示词中，以实现数据的动态传递。
    *   示例 Prompt: 
    ```markdown
    对以下文案进行归纳总结，并将总结出的摘要生成markdown格式的知识笔记。请直接输出markdown格式的文本，不需要放置在markdown代码块中。
	文案内容： {{ $json.contentSnippet }}
    ```

### 3.3 步骤三：连接到 Obsidian 节点

1.  回到我们之前配置好的用于创建 Obsidian 笔记的 `HTTP Request` 节点。
2.  **修改 URL**: 将 URL 中的文件名部分修改为表达式，动态获取 RSS 文章的标题。(额外添加正则表达式，来过滤掉不能用在文件名中的特殊字符)
    *   例如: `http://127.0.0.1:27123/vault/新闻文件夹/{{ $('RSS Read').item.json.title.replace(/[\/\\:*?"<>|%]/g, '-') }}.md`
3.  **修改 Body**: 将 Body 的内容修改为表达式，动态获取上一步 AI 节点的输出结果。
    *   例如: `{{ $json.message.content }}`
4.  **保存并执行**: 保存工作流，点击下方的 `Execute Workflow` 按钮。工作流将自动为每一条 RSS 信息生成一篇 AI 总结笔记并存入 Obsidian。

---

## 4. n8n 工作流的导入与导出

### 4.1 导出工作流

在工作流编辑页面，点击右上角的三个点 `...` 菜单，选择 `Download`。n8n 会将当前工作流下载为一个 `.json` 文件。您可以将此文件分享给他人。

**安全性**: 导出的 JSON 文件中不包含您的凭证（如 API Key）的实际内容，而是包含一个指向凭证的内部 ID。因此分享工作流是安全的。

### 4.2 导入工作流

1.  创建一个新的空白工作流。
2.  点击右上角的三个点 `...` 菜单，选择 `Import from File`。
3.  选择您获取到的 `.json` 文件进行导入。
4.  **重新配置**: 导入后，工作流中所有需要凭证的节点（如 OpenAI, HTTP Request 等）会显示错误。您需要逐个点击这些节点，并在 `Credential` 处选择或创建您自己的凭证，以使其正常工作。


# Obsidian Local REST API 核心接口功能详解

本文档基于 [官方 API 文档](https://coddingtonbear.github.io/obsidian-local-rest-api/)，将各主要接口的功能、参数及调用方式整理成表，以便于快速查阅和集成。

**通用说明**:
*   **`{path}`**: 表示从 Vault 根目录开始的**相对路径**，例如 `My Notes/My First Note.md`。
*   **认证**: 所有示例中的 `YOUR_API_KEY` 都需要替换为您在插件中获取的实际 API Key。

---

### Vault (文件与目录操作)

| Method | Endpoint | Description | Parameters | Example Call |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/vault/` | 获取 Vault 中所有的文件和文件夹列表。 | **无** | `curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/vault/` |
| `GET` | `/vault/{path}` | 读取指定路径的文件内容。 | **Path**: `{path}` - 文件的完整相对路径。 | `curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/vault/My%20Folder/My%20Note.md` |
| `POST` | `/vault/{path}` | 创建一个新文件或完全覆盖一个已存在的文件。 | **Path**: `{path}`<br>**Body**: 文件的原始文本内容 (Raw Text)。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: text/plain" -d "# New Note" http://127.0.0.1:27123/vault/NewNote.md` |
| `PATCH` | `/vault/{path}` | 在现有文件内容的开头或结尾追加文本。 | **Path**: `{path}`<br>**Body**: JSON 对象，包含 `action` (`"append"` 或 `"prepend"`) 和 `data` (要添加的文本)。 | `curl -X PATCH -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"action": "append", "data": "\n\n## Appended Content"}' http://127.0.0.1:27123/vault/ExistingNote.md` |
| `DELETE` | `/vault/{path}` | 删除指定路径的文件或空的文件夹。 | **Path**: `{path}` - 要删除的文件或文件夹的相对路径。 | `curl -X DELETE -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/vault/NoteToDelete.md` |

---

### Commands (命令面板操作)

| Method | Endpoint | Description | Parameters | Example Call |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/commands/` | 获取 Obsidian 中所有可用的命令及其 ID。 | **无** | `curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/commands/` |
| `POST` | `/commands/{command-id}` | 执行一个指定的命令。 | **Path**: `{command-id}` - 从 `/commands/` 接口获取的命令 ID。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/commands/app%3Aopen-settings` |

---

### Periodic Notes (周期性笔记)

此功能需要您已安装并配置 `Periodic Notes` 插件。

| Method | Endpoint | Description | Parameters | Example Call |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/periodic/` | 获取所有类型的周期性笔记列表。 | **Query**: `?type=` 可选值为 `daily`, `weekly`, `monthly`, `quarterly`, `yearly`。 | `curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/periodic/?type=daily` |
| `POST` | `/periodic/daily/` | 创建或打开今天的日报。 | **Body** (可选): JSON 对象，如 `{"data": "# My Content"}`，用于写入内容。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/periodic/daily/` |
| `GET` | `/periodic/daily/{date}` | 获取指定日期的日报内容。 | **Path**: `{date}` - 日期，格式为 `YYYY-MM-DD`。 | `curl -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/periodic/daily/2025-10-01` |
| `POST` | `/periodic/weekly/` | 创建或打开本周的周报。 | **Body** (可选): JSON 对象，用于写入内容。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" http://127.0.0.1:27123/periodic/weekly/` |

*(注：`monthly`, `quarterly`, `yearly` 的操作与 `daily` 和 `weekly` 类似，此处不再赘述。)*

---

### Search (搜索)

| Method | Endpoint | Description | Parameters | Example Call |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/search/` | 在 Vault 中执行一次搜索查询。 | **Body**: JSON 对象，至少包含 `query` 字段。其他可选字段如 `tag`, `path` 等。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"query": "n8n integration"}' http://127.0.0.1:27123/search/` |

---

### Dataview (Dataview 插件交互)

此功能需要您已安装并配置 `Dataview` 插件。

| Method | Endpoint | Description | Parameters | Example Call |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/dataview/` | 执行一次 Dataview 查询。 | **Body**: JSON 对象，包含 `query` 字段，内容为 Dataview 查询语句。 | `curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"query": "LIST FROM #project"}' http://127.0.0.1:27123/dataview/` |

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
