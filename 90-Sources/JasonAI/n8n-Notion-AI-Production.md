---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "用N8N把Notion升级成AI生产线 | n8n自动化工作流全流程教学 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/n8n-notion-ai-production-tutorial/"
source_url: "https://jasonai.me/download/用N8N把Notion升级成AI生产线-n8n自动化工作流全流程教学.md"
published: 2025-09-18
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[Enterprise-Integrations-and-Connectors]]"
  - "[[Workflow-Automation-and-Business-Process-Design]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
---

## 摘要

本笔记旨在提供一个从零开始部署、配置并使用自托管 n8n 的完整指南。内容涵盖了两种主流的安装方式（Node.js 与 Docker）、首次启动设置、一个从 RSS 订阅同步数据至 Notion 的实战工作流，并最终解决了在中国大陆环境下使用 AI 节点时最关键的网络代理配置问题。

---

## 1. n8n 的安装：两种核心方式

选择合适的安装方式是稳定使用 n8n 的第一步。

### 方式一：使用 Node.js (npm) 安装 (适合快速体验)

这种方式最直接，适合想快速在本地电脑上体验 n8n 功能的场景。

- **前置要求**:
    - 已安装 [Node.js](https://nodejs.org/) (建议使用 LTS 版本)。

- **安装命令**:
  打开您的终端 (Terminal / CMD / PowerShell)，运行以下命令进行全局安装：
  ```bash
  npm install -g n8n
  ```

- **启动命令**:
  安装完成后，直接在终端中运行：
  ```bash
  n8n
  ```

> [!NOTE]
> **优点**: 安装简单快捷，无需额外软件。
> **缺点**: n8n 进程会与您的本地环境耦合，且关闭终端窗口通常会中止 n8n 服务。不适合作为长期运行的生产服务。

### 方式二：使用 Docker 安装 (推荐用于长期稳定运行)

Docker 提供了一个隔离、可移植的环境，是自托管 n8n 的最佳实践。它能确保 n8n 及其依赖项独立运行，并且便于管理和数据持久化。

- **前置要求**:
    - 已安装 [Docker](https://www.docker.com/products/docker-desktop/) 和 Docker Compose。

### 方法一：使用 Docker Run 命令
1. **打开命令提示符或 PowerShell**：  
    您可以在开始菜单中搜索 "Command Prompt" 或 "PowerShell" 并打开它。
    
2. **执行以下命令来启动 n8n 容器**：
```bash
docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n
```
3. **访问 n8n**：  
当您在命令行中看到类似 "Editor is now accessible" 的消息时，说明 n8n 已经成功启动。打开您的浏览器并访问 http://localhost:5678 即可开始使用。

### 方法二：使用 Docker Compose

- **配置 `docker-compose.yml`**:
  1. 在您希望存放 n8n 数据的文件夹中，创建一个名为 `docker-compose.yml` 的文件。
  2. 将以下内容粘贴到文件中：

  ```yaml
  version: '3.7'

  services:
    n8n:
      image: docker.n8n.io/n8nio/n8n
      restart: always
      ports:
        # 将 n8n 的 5678 端口映射到您电脑的 5678 端口
        - "127.0.0.1:5678:5678"
      volumes:
        # 将 n8n 的数据持久化到本地，防止容器重启后数据丢失
        - n8n_data:/home/node/.n8n
      environment:
        # 设置时区，避免时间错乱问题
        - GENERIC_TIMEZONE=Asia/Shanghai

  volumes:
    n8n_data:
  ```

- **启动命令**:
  在存放 `docker-compose.yml` 文件的目录下，打开终端并运行：
  ```bash
  docker-compose up -d
  ```
  n8n 将会在后台稳定运行。

> [!TIP]
> **数据持久化**: `volumes` 的配置至关重要，它将 n8n 的所有工作流、凭证等数据保存在您电脑的一个 Docker 数据卷中，名为 `n8n_data`。

---

## 2. 首次启动与设置

无论使用哪种方式启动，后续步骤都是相同的。

1.  **访问 n8n**: 打开浏览器，访问 `http://localhost:5678`。
2.  **创建所有者账户**: 您会看到一个欢迎页面，引导您创建第一个用户。这个用户是该 n8n 实例的**所有者 (Owner)**，拥有最高权限。
3.  **填写信息**: 按照提示填写您的姓名、邮箱和密码。
4.  **登录**: 完成注册后，系统将自动登录，您会进入 n8n 的主仪表盘，准备好创建您的第一个工作流。

---

## 3. 创建第一个工作流：RSS 订阅同步至 Notion

这是一个经典的自动化场景，我们将从 RSS 源获取文章，并将其关键信息存入一个 Notion 数据库。

- **准备工作**:
    1.  一个 RSS 订阅链接 (例如：`http://arxiv.org/rss/cs.AI`)。
    2.  在 Notion 中创建一个数据库，并包含以下属性：
        - `Title` (标题)
        - `Link` (URL)
        - `Published Date` (日期)

### 步骤一：创建工作流与 RSS 读取节点

1.  在 n8n 仪表盘，点击 "Add workflow"，创建一个空白画布。
2.  点击 **+** 号，搜索并添加 **RSS Read** 节点。
3.  在右侧配置面板的 **URL** 字段中，粘贴您的 RSS 订阅链接。
4.  点击右下角的 **Test workflow**，n8n 会抓取最新的几条 RSS 条目，您可以在输出中看到数据。

### 步骤二：数据处理 (Set 节点)

RSS 返回的数据字段可能不规整，我们需要用 Set 节点进行格式化和映射。

1.  点击 RSS Read 节点右侧的 **+** 号，添加 **Set** 节点。
2.  **开启 "Keep Only Set"** 选项，以保持数据流的干净。
3.  点击 **Add Value** 添加以下值：
    - **Value 1**:
        - Name: `notion_title`
        - Value (表达式): `{{ $json.title }}`
    - **Value 2**:
        - Name: `notion_link`
        - Value (表达式): `{{ $json.link }}`
    - **Value 3 (日期格式化)**:
        - Name: `notion_date`
        - Value (表达式): `{{ DateTime.fromRFC2822($json.pubDate).toISO() }}`

> [!NOTE]
> `pubDate` 的原始格式 Notion 不识别，`DateTime.fromRFC2822(...).toISO()` 表达式使用 n8n 内置的 Luxon 库将其转换为 Notion 接受的标准 ISO 格式。

### 步骤三：写入 Notion (Notion 节点)

1.  点击 Set 节点后的 **+** 号，添加 **Notion** 节点。
2.  **配置凭证**: 首次使用需点击 "Credential" > "Create New"，按照指引完成对 Notion 的授权。
3.  **配置节点**:
    - **Resource**: `Database/Page`
    - **Operation**: `Append`
    - **Database ID**: 填入您 Notion 数据库的 ID。
    - **Properties**: 点击 **Add Property**，将数据库属性与 Set 节点的输出进行映射：
        - `Title` -> `{{ $json.notion_title }}`
        - `Link` -> `{{ $json.notion_link }}`
        - `Published Date` -> `{{ $json.notion_date }}`

### 步骤四：测试与激活

1.  再次点击 **Test workflow**，整个流程会完整运行一遍。
2.  检查您的 Notion 数据库，确认新条目已成功写入。
3.  点击右上角的开关将其从 **Inactive** 切换为 **Active**，工作流将根据您的触发器设置自动运行。

---

## 4. 关键技巧：为 n8n 配置网络代理

当您的工作流需要访问如 OpenAI、Gemini 等在中国大陆无法直接访问的 API 时，必须为 n8n 本身配置网络代理。

### 为什么需要配置代理？

n8n 是一个**后端服务**，它独立于您的浏览器运行。您为浏览器或系统设置的“科学上网”代理，n8n 默认是无法使用的。因此，我们会收到 `timeout` (连接超时) 错误。解决方案是通过**环境变量**，明确告知 n8n 使用您的代理服务。

### 核心：找到你的代理地址

首先，在您的代理软件 (Clash, V2RayN 等) 中找到其提供的 HTTP 代理端口。

- **常见地址**: `127.0.0.1`
- **常见端口**: `7890`, `10809`, `1080` 等。

**本文假设您的代理地址为 `http://127.0.0.1:7890`**。

### 配置方法：根据你的安装方式选择

#### 针对 Node.js / npm 安装

您需要在**启动 n8n 的同一个终端窗口**中，先设置环境变量，再启动服务。

**Windows (PowerShell)**:
```powershell
# 在 PowerShell 中
$env:HTTPS_PROXY="http://127.0.0.1:7890"
$env:HTTP_PROXY="http://127.0.0.1:7890"

# 或者在 CMD 中
set HTTPS_PROXY=http://127.0.0.1:7897
set HTTP_PROXY=http://127.0.0.1:7897
```
**macOS / Linux**:
```bash
export HTTPS_PROXY="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"

```

> [!WARNING]
> 这种方式设置的环境变量仅对当前终端会话有效。关闭窗口后需重新设置。

#### 针对 Docker 安装

这是更稳定、一劳永逸的方法。我们需要修改 `docker-compose.yml` 文件。

1.  打开 `docker-compose.yml` 文件。
2.  在 `n8n` 服务的 `environment` 部分添加代理变量。

```yaml
version: '3.7'

services:
  n8n:
    image: docker.n8n.io/n8nio/n8n
    restart: always
    ports:
      - "127.0.0.1:5678:5678"
    environment:
      # --- 在这里添加代理配置 ---
      - HTTPS_PROXY=http://host.docker.internal:7890
      - HTTP_PROXY=http://host.docker.internal:7890
      # --- 其他环境变量 ---
      - GENERIC_TIMEZONE=Asia/Shanghai
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
```

> [!IMPORTANT]
> **为什么使用 `host.docker.internal`？**
> 在 Docker 容器内部，`127.0.0.1` 指的是容器自身，而不是您的宿主机（电脑）。`host.docker.internal` 是一个特殊的 DNS 名称，它会正确地指向您的电脑 IP，从而让容器内的 n8n 能够找到并使用您在电脑上运行的代理服务。

3.  保存文件后，在终端中**重启 n8n 容器**以使配置生效：
    ```bash
    docker-compose down && docker-compose up -d
    ```

完成代理配置后，您的 n8n 工作流中的 AI 节点或其他需要代理的节点就能正常工作了。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
