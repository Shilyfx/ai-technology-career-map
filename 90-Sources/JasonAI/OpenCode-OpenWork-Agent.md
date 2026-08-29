---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "OpenCode &amp; OpenWork 快速上手教程，让AI Agent接管你所有工作。 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/opencode-openwork-ai-agent-guide/"
source_url: "https://jasonai.me/download/OpenCode-OpenWork-快速上手教程-让AI-Agent接管你所有工作.md"
published: 2026-02-03
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

# OpenCode使用方法
## 1. 工具定义与竞品对比

**OpenCode** 是一个开源的 AI Agent 编程工具，本质是 **Claude Code（人送绰号Close Code）** 的社区开源替代方案。支持代码编写，还能通过加载 "Skill"（技能包）执行文件操作、数据分析等通用计算机任务。

| 维度 | OpenCode | Claude Code |
| :--- | :--- | :--- |
| **内核性质** | 开源社区驱动，代码透明 | Anthropic 闭源商业产品 |
| **扩展性** | 支持自定义 Skill，兼容 Anthropic 标准 | 官方预设能力为主 |
| **成本** | 免费（仅需支付底层 API 费用），支持本地模型 | 需订阅或按 Token 付费 |
| **数据隐私** | 数据流可控，适合敏感项目 | 数据经过 Anthropic 服务器 |

## 2. 安装部署方案

### 命令行版 (CLI)
适用于开发者，集成于终端环境，资源占用极低。
*   **源码/仓库**：[GitHub - anomalyco/opencode](https://github.com/anomalyco/opencode)
*   **安装命令**（需 Node.js 环境）：
```bash
npm install -g @anomalyco/opencode
```

安装完成后在终端输入 opencode 启动

### 桌面版 (Desktop APP)
适用于演示、非代码类任务处理，提供可视化交互界面。
*   **下载地址**：[OpenCode 官网下载](https://opencode.ai/download)
*   **支持平台**：macOS, Windows, Linux

## 3. 版本形态对比决策

| 特性 | 命令行版 (CLI) | 桌面客户端 (Desktop) |
| :--- | :--- | :--- |
| **核心优势** | 极速响应、支持管道操作、可编写 Shell 脚本联动 | 可视化预览、文件拖拽交互、适合演示录屏 |
| **适用人群** | 程序员、DevOps、自动化极客 | 不习惯命令行、编程经验少的用户 |
| **Obsidian 联动** | **强**（可通过插件或 Shell 脚本深度集成） | **弱**（仅作为独立窗口使用） |

## 4. Agent Skill 加载机制

OpenCode 遵循 Anthropic 的 `SKILL.md` 标准。要扩展 AI 的能力（如读取 PDF、操作 Excel），需要将对应的技能文件放入指定配置目录。

**Skill 文件存放路径：**

*   **macOS / Linux**:
    ```bash
    ~/.config/opencode/skills/
    ```
*   **Windows**:
    ```powershell
    C:\Users\你的用户名\.config\opencode\skills\
    ```

> **操作提示**：在上述目录下新建文件夹（如 `excel-tool`），放入 `SKILL.md` 和配套脚本（如 `analyze.py`），重启 OpenCode 即可生效。

## 5. 应用场景
除了编程开发之外，还可以做很多事情：
*   **Obsidian 知识库重构**
    *   指向 Vault 目录，执行：“扫描 `/Inbox` 文件夹，提取所有关于 'RAG' 的笔记，合并成一篇新的永久笔记放入 `/Wiki`，保留原链接。”
*   **数据报表自动化**
    *   加载 Excel Skill 后，执行：“读取这个销售 CSV，计算各季度环比增长率，并用 Python 生成一张折线图保存到桌面。”

## 6. 常用命令

| 功能分类 | Slash 命令 (输入框) | 快捷键 (CLI/Desktop) | 作用说明 |
| :--- | :--- | :--- | :--- |
| **核心流程** | `/new` 或 `/clear` | `Ctrl+x` + `n` | **新建会话**：清空当前上下文，开始新任务。 |
| | `/exit` 或 `/quit` | `Ctrl+x` + `q` | **退出程序**：安全关闭 Agent。 |
| | `/compact` | `Ctrl+x` + `c` | **压缩上下文**：将长对话总结为摘要，节省 Token 并防止遗忘。 |
| **模式切换** | `/plan` / `/build` | **`Tab`** (最常用) | **切换模式**：在“规划模式”(只读/思考)与“构建模式”(写代码/执行)间切换。 |
| **时光机** | `/undo` | `Ctrl+x` + `u` | **撤销**：回滚上一次 AI 的修改（基于 Git，非常安全）。 |
| | `/redo` | `Ctrl+x` + `r` | **重做**：恢复被撤销的操作。 |
| **上下文控制** | `@文件名` | - | **引用文件**：模糊搜索并添加文件内容到 Prompt（如 `@utils.ts`）。 |
| | `!命令` | - | **Shell 直通车**：直接执行系统命令（如 `!npm install` 或 `!ls -la`）。 |
| | `/editor` | `Ctrl+x` + `e` | **调用编辑器**：在你的默认编辑器（如 VS Code）中编写复杂的 Prompt。 |
| **系统与配置** | `/init` | `Ctrl+x` + `i` | **初始化**：在当前目录生成 `AGENTS.md`（项目规则文件）。 |
| | `/connect` | - | **连接模型**：配置 API Key（OpenAI/Anthropic/Ollama 等）。 |
| | `/models` | `Ctrl+x` + `m` | **切换模型**：在不同大模型之间无缝切换。 |
| **桌面版专属** | - | `Cmd+Esc` (Mac) | **全局唤醒**：类似于 Spotlight，快速呼出/隐藏 OpenCode 窗口。 |
| | - | `Cmd+Opt+K` | **插入引用**：在输入框中快速插入当前选中的文件路径。 |

# OpenWork使用方法

**OpenWork** 是基于 **OpenCode** 引擎构建的现代化桌面端 AI Agent 办公环境。它为非技术用户提供了直观的图形界面 (GUI)，完美对标 Anthropic 的 Claude Cowork，支持多模型切换、MCP 协议扩展及文件系统操作。
## 1. 快速安装 
OpenWork 提供了开箱即用的安装包，无需繁琐的 Python/Node 环境配置。

1.  **访问 GitHub 仓库**：[different-ai/openwork](https://github.com/different-ai/openwork)
2.  **下载安装包**：
    *   点击右侧的 **Releases** 链接。
    *   下载匹配自己操作系统的安装文件
3.  **安装与启动**：双击运行，安装完成后打开应用。

> 💡 **提示**：OpenWork 本质是 OpenCode 的图形化“外壳”。安装 OpenWork 后，它会在后台自动管理 OpenCode 的核心引擎。

## 2. 初始化配置
### 2.1 选择工作区 (Workspace)
启动后，第一步是选择**工作目录**。
*   **建议**：选择你日常办公的核心文件夹（如 `D:\Documents\Work`）或 Obsidian 知识库根目录。
*   **作用**：AI Agent 将获得该目录下文件的**读写权限**（OpenWork 默认有安全锁，修改文件前通常需要人工 Confirm）。
### 2.2 模型选择 
点击界面右上角或设置中的模型图标：
*   **免费模型**：选择 **MiniMax M2.1** 或 **GLM-4.7**（如列表提供，显示free字样）。

## 3. 核心配置：`opencode.jsonc`
这是 OpenWork 的核心配置文件。
*   **文件位置**：
    *   **Windows**: `C:\Users\你的用户名\.config\opencode\opencode.jsonc`
    *   **Mac**: `~/.config/opencode/opencode.jsonc` (需按 `Cmd+Shift+.` 显示隐藏文件)
注：.json和.jsonc本质其实都是json，而jsonc就是json with comments，带注释的json。
### 3.1 配置模板
按照下面的格式配置MCP。

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    // 1. 本地文件系统 (核心能力)
    "filesystem": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-filesystem"],
      "enabled": true
    },
    
    // 2. 网页抓取 (读取公众号/推特文章)
    "fetch": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-fetch"],
      "enabled": true
    },
    
    // 3. Notion 集成 (需获取 Internal Integration Token)
    "notion": {
      "type": "local",
      "command": ["npx", "-y", "@notionhq/notion-mcp-server"],
      "environment": {
        "NOTION_TOKEN": "secret_你的Notion密钥" 
      },
      "enabled": true
    },

    // 4. 联网搜索 (推荐 Brave Search，免费且干净)
    "brave-search": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-brave-search"],
      "environment": {
        "BRAVE_API_KEY": "你的BraveAPIKey"
      },
      "enabled": true
    }
  }
}
```

---

## 4. 插件与Skills
在 OpenWork 的左侧菜单栏中，你可以图形化地管理扩展。

### 4.1 安装 Plugins (界面功能增强)
1.  点击左侧 **Plugins** 菜单。
2.  在 **Add Plugin** 输入框中，输入 GitHub 仓库地址（推荐参考 `awesome-opencode` 列表）。

### 4.2 管理 Skills (AI 能力包)
*   **查看**：点击 **Skills** 菜单，查看当前 AI 已掌握的能力（如 `bash`, `python_interpreter` 等）。
*   **导入**：点击Import按钮导入你的Skills。

## 5. 实战案例：自动化文件整理
**场景**：将 `Downloads` 文件夹中乱七八糟的 PDF 和 TXT 整理为 Markdown 笔记。

**操作步骤**：
1.  将 OpenWork 的工作区切换到包含 `Downloads` 的父目录。
2.  在对话框输入以下 **Prompt (提示词)**：

> "请扫描 `Downloads` 目录。
> 1. 读取所有 PDF 和 TXT 文件内容。
> 2. 为每个文件生成一份 Markdown 笔记，包含‘核心摘要’和‘关键洞察’。
> 3. 将笔记保存到 `Knowledge_Base/Inbox` 目录。
> 4. 遇到无法直接读取的 PDF，请编写 Python 脚本使用 pypdf 库进行提取。"

**预期结果**：
*   OpenWork 会自动规划任务 (Plan)。
*   你会看到它编写并运行 Python 代码。
*   右侧文件管理面板中，旧文件被读取，新笔记自动生成。

## 6. 注意事项 

*   **Token 消耗**：OpenWork 是多步执行的 Agent，处理一个复杂任务可能会消耗大量 Token。建议在非生产环境使用免费模型（如 MiniMax）。
*   **权限确认**：在 **Build** 模式下，AI 修改或删除文件时，OpenWork 默认会弹出确认框。**请务必看清 AI 要删除什么文件再点 Confirm**。
*   **本地模型**：OpenWork 支持连接本地 Ollama（如 Llama 3），但这需要你的电脑显存足够（建议 16GB+），且本地模型的逻辑规划能力弱于云端模型。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
