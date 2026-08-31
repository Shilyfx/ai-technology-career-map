---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Claude Skill快速上手教程：三个步骤就能用上。 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/claude-skill-quick-start/"
source_url: "https://jasonai.me/download/Claude-Skill快速上手教程-三个步骤就能用上.md"
published: 2026-01-14
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
  - "[[AI-Agents-and-Tool-Use]]"
  - "[[Agent-Orchestration-and-State]]"
  - "[[Tool-Calling-and-Action-Contracts]]"
  - "[[Software-Design-and-Architecture]]"
  - "[[Security-Privacy-and-Access-Control]]"
  - "[[AI-Solutions-Architect-and-FDE]]"
---

# Claude Code 安装指南

Claude Code 对于中国大陆用户，直接使用面临网络与账号双重门槛。但可以通过本地部署 + 国产大模型兼容层（GLM/DeepSeek）方案，实现无障碍安装使用。
**操作起来很简单，只需要3个步骤即可。**

## 1. 基础环境与工具安装

Claude Code 依赖 Node.js 环境运行。**请确保已安装 [Node.js](https://nodejs.org/)**。
下载Nodejs之后，双击安装即可。

打开终端（Windows 推荐 PowerShell/CMD，Mac 使用 Terminal），按顺序执行以下命令完成从检查到安装的全流程：

1. 检查 Node.js 环境（必须有版本号返回）
```bash
node -v
npm -v
```
2. 安装 Claude Code（使用 -g 进行全局安装）
```bash
npm install -g @anthropic-ai/claude-code
```
3. 验证安装
```bash
claude --version
```
看到版本号即安装成功。输出示例：2.1.2 (Claude Code) 

如果在npm install这一步遇到卡顿，建议搜索watt toolkit加速器（windows应用商店搜索然后安装），或者使用国内npm中转，具体做法是在npm install命令后面添加参数：

```bash
npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
```


## 2. Claude账号问题

安装完成后，需要解决“谁来驱动”的问题，**根据你的网络与账号情况**选择路径：

*   **路径 A：标准模式（美国、欧洲等支持地区）**
    **如果你身处海外环境且有 Anthropic 账号**，直接运行 `claude login`，系统会打开浏览器，让你登录Claude，进行 OAuth 授权。登录完成后即可顺畅使用Claude Code。那么对于你来说，现在已经安装成功了。

*   **路径 B：兼容模式（中国大陆推荐）**
    国内用户无需注册 Anthropic 账号，可直接使用**智谱 GLM**或**DeepSeek**的 API 来驱动 Claude Code。这两者均提供了官方兼容接口。具体看第三步。

## 3. 核心配置：使用兼容模型，绕过Claude登录验证

为了让 Claude Code 连接到兼容模型（智谱GLM, DeepSeek)。

- 请求 / 响应结构与 Anthropic 基本一致
- 可直接作为 Claude Code 的后端
- 不需要登录 Anthropic 官网账号

### 方案一：通过命令行设置环境变量

我们需要配置 `BASE_URL` 和 `API_KEY`
为了避免每次重启终端丢失配置，以下命令将直接写入系统**永久环境变量**。

*   **智谱 GLM Base URL**: `https://open.bigmodel.cn/api/anthropic`
*   **DeepSeek Base URL**: `https://api.deepseek.com/anthropic`

请根据你的系统，复制对应的命令块运行（只需运行一次）：

#### Windows 用户 (CMD 命令提示符)
使用 setx 命令写入用户级永久变量
```cmd
setx ANTHROPIC_BASE_URL "https://open.bigmodel.cn/api/anthropic"
setx ANTHROPIC_AUTH_TOKEN "你的_GLM_API_KEY"
setx ANTHROPIC_MODEL "glm-4.6"
```

注意：运行后需重启 CMD 窗口才会生效

#### macOS / Linux 用户 (Shell)
```bash
echo 'export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"' >> ~/.zshrc
echo 'export ANTHROPIC_AUTH_TOKEN="你的_GLM_API_KEY"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL=glm-4.6' >> ~/.zshrc

source ~/.zshrc
```

如果使用DeepSeek则使用DeepSeek的url和api key，模型名则是deepseek-chat。

### 方案二：通过配置文件修改环境变量

通过修改本地配置文件，可以强制 Claude Code (CLI) 连接到 DeepSeek 或其他兼容 Anthropic 协议的模型，并跳过官方的浏览器登录验证。

#### 1. 文件结构总览
需要修改的文件位于用户根目录下。请确保文件位置和层级完全一致：

```text
C:\Users\用户名\
│
├── 📄 .claude.json                 <-- 【状态文件】 修改这个文件内容，添加"hasCompletedOnboarding": true,
│
└── 📂 .claude\                     <-- 【配置文件夹】 这是claude全局文件夹
    └── ⚙️ settings.json            <-- 【配置文件】 新建这个settings.json文件，并添加环境变量
```

#### 2. 详细配置指南

1. 配置 API 连接 (`.claude\settings.json`)
此文件用于接管网络请求，将其重定向到第三方服务（如 GLM/DeepSeek）。
*   **路径**: `C:\Users\你的用户名\.claude\settings.json`
*   **内容**: 新建这个setting.json文件，用记事本打开，在里面添加下面这段内容：

```json
{
    "env": {
        // 将地址改为 DeepSeek 或 GLM 的 Anthropic 兼容接口
        "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
        // 填写对应的 API Key
        "ANTHROPIC_AUTH_TOKEN": "你的API Key",
        // 禁用遥测和联网检查，防止因地区问题导致的报错
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
    }
}
```

2. 绕过登录验证 (`.claude.json`)
此文件用于伪造“老用户”状态，防止 CLI 启动时弹出浏览器进行 OAuth 验证。
*   **路径**: `C:\Users\你的用户名\.claude.json` 
*   **内容**: 用记事本打开这个文件，在其中添加一项

```json
	"hasCompletedOnboarding": true,  // 核心：告诉程序已完成新手引导，直接进入对话
```



## 4. 启动与常用指令

环境变量配置完毕后，无需登录，直接启动即可。

*   **启动程序**：在命令行中输入 `claude`，然后回车。
    *   *成功标志*：出现 "Welcome to Claude Code" 欢迎语，且未弹出浏览器。
*   **退出程序**：在交互界面输入`exit`，回车。

**常用交互指令**：
*   `/clear`：清除上下文记忆（节省 Token，开启新任务时推荐）。
*   `/compact`：压缩上下文（处理长任务时使用）。
*   `/help`：查看所有可用命令。
*   `Alt + Enter` (Win) / `Opt + Enter` (Mac)：在对话框中换行。



# Claude Skill



## 1.  概念：Agent Skill

**定义**：
Agent Skill（Claude Skill）是 Anthropic 推出的一种**基于文件系统的模块化能力标准**。它本质上是一种“渐进式披露” (Progressive Disclosure)的提示词管理机制。
### 核心比喻：一本“带目录的书” 
传统的 System Prompt 往往把所有规则一次性塞给 AI，既浪费 Token 又容易让模型混淆。Agent Skill 将能力分层管理，就像一本书：
*   **第1层：元数据 (Metadata) ≈ 目录** 
    *   **内容**：技能的名称 (`name`) 和简短描述 (`description`)。
    *   **加载机制**：**始终加载**。AI 只看目录，判断“用户的问题我需不需要查这本书”。
    *   **优势**：极度节省 Token，几乎不占内存。
*   **第2层：指令 (Instructions) ≈ 正文** 
    *   **内容**：具体的 Prompt、操作步骤、约束条件。
    *   **加载机制**：**按需加载**。只有当 AI 决定调用该技能时，才会读取这部分内容进入上下文。
*   **第3层：资源 (Resources) ≈ 附录** 
    *   **内容**：辅助脚本 (`scripts/`)、模板文件 (`templates/`) 或参考数据。
    *   **加载机制**：**按需调用**。在指令执行过程中被引用时才读取。
### Agent Skill的特点
1.  **标准化**：不仅仅是 Claude，Cursor、Codex、OpenCode 等新一代 AI 编程工具均开始支持此标准。
2.  **低消耗**：解决了“随着能力增加，Context Window 爆炸”的问题。
3.  **配合 MCP**：Skill 定义“SOP（标准作业程序）”，MCP 提供“工具接口（如读写文件）”，两者结合实现复杂的 Agent 工作流。

---

## 2. Skill配置指南
假设您已安装好 `Claude Code` 并通过 `settings.json` 配置了 DeepSeek/GLM 等兼容模型，以下是加载skill的完整流程。

### 📂 第一步：建立“技能库”
Claude Code 会自动扫描用户根目录下的 `.claude/skills` 文件夹。

**标准路径结构**（请务必遵守此层级）：
```text
C:\Users\用户名\.claude\skills\        <-- skill所在目录
│
├── 📂 pdf-summary\                    <-- [技能包] 文件夹名建议用 kebab-case
│   │
│   ├── 📄 SKILL.md                    <-- [🔴 核心] 必须叫 SKILL.md (大写)
│   │
│   ├── 📂 scripts\                    <-- [手脚] 存放 Python/Bash 脚本
│   │   └── 🐍 extract.py
│   │
│   └── 📂 templates\                  <-- [素材] 存放输出模板
│       └── 📄 format.txt
│
└── 📂 git-automator\                  <-- 另一个技能包
    └── 📄 SKILL.md
```

### 📝 第二步：编写 `SKILL.md` (标准定义)
这是 Agent Skill 标准的核心。Claude 会先读取 Frontmatter (元数据) 来决定何时调用。
**你并不需要亲自撰写SKILL.md，网络上有很多官方/第三方的优质SKILL，比如GitHub上的awesome-claude-skills。**

**文件内容示例 (`C:\Users\用户名\.claude\skills\xlsx\SKILL.md`)**：
````markdown

---
# 【1. 元数据区 / Metadata】
# 作用：Claude 启动时只会读取这一小部分。description 必须准确概括功能，
# 只有当用户的问题与这段描述匹配时，下方的指令区才会被加载。

name: csv-data-summarizer
description: 使用 Python 和 pandas 分析 CSV 文件，生成统计摘要并绘制快速可视化图表。
metadata:
  version: 2.1.0
  dependencies: python>=3.8, pandas>=2.0.0
---

# CSV Data Summarizer
<!-- 【2. 指令区 / Instructions】 -->
<!-- 作用：当技能被触发后，Claude 会遵循这里的规则去执行任务 -->

## When to Use (触发时机)
当用户满足以下条件时使用此 Skill：
- 上传或引用了一个 CSV 文件
- 要求对表格数据进行摘要、分析或可视化
- 想要了解数据的结构和质量

## Critical Behavior (核心行为准则)
⚠️ **绝对准则**：
1. **禁止询问用户意图**：不要问 "你想让我做什么？" 或提供选项。
2. **立即执行全量分析**：自动运行分析、生成所有相关图表并展示结果。
3. **智能适配**：根据数据内容（销售、客户、财务等）自动决定分析方向，无需用户指定。

## Automatic Steps (自动化步骤)
1. **加载与检查**：读取 CSV 到 pandas DataFrame。
2. **识别结构**：判断列类型（日期、数值、分类）。
3. **执行分析**：根据数据类型生成统计数据（如时间序列趋势、相关性热力图等）。
4. **生成输出**：一次性展示概览、统计数据、缺失值分析和可视化图表。

---

# Files
<!-- 【3. 资源区 / Resources】 -->
<!-- 作用：列出此 Skill 需要调用的具体文件（位于同级目录中） -->

- `analyze.py` - 核心分析逻辑代码
- `requirements.txt` - Python 依赖库列表
- `resources/sample.csv` - 用于测试的示例数据

````

### 🚀 第三步：加载与触发
1.  **重启 Claude Code**：
    关闭并重新打开终端，输入 `claude` 启动。
2.  **检查加载**：
    在对话框中输入指令 `/doctor` 或者直接问它：
    > "你现在加载了哪些 skills？"
    它会列出已发现的技能，例如：`pdf-summary-pro`。
3.  **触发使用**：
    无需特殊命令，直接用自然语言：
    > "帮我读一下桌面上这个 annual_report.pdf，我要看财报摘要"
    Claude 会识别意图 -> 自动命中 `SKILL.md` -> 执行内部逻辑。

---

## 3. 补充

### 核心机制：渐进式披露
Claude 不是一次性把所有 Skill 的内容都塞进 Context (上下文) 里的。
1.  **启动时**：只加载 `SKILL.md` 顶部的 `name` 和 `description` (元数据)。这几乎不消耗 Token。
2.  **命中时**：只有当用户的问题与 `description` 匹配时，Claude 才会将该 `SKILL.md` 的正文和相关脚本加载进上下文。
*这意味着你可以安装 100 个技能，而不会让 Claude 变笨或变慢。*

### 安全提示
下载别人的 Agent Skill (比如从 GitHub 上的 `awesome-claude-skills`) 时要格外小心。
因为 Agent Skill 标准允许包含 `scripts/` 文件夹，**这意味着它可以在你的电脑上执行任意 Python/Shell 代码**。在运行陌生 Skill 之前，务必检查 `scripts/` 下的代码逻辑。

### 完全自主权
如果想给claude code完全自主权，而不是每次调用skill或更改代码都询问你是否同意，那么，可以使用这个命令来启动claude code:

```bash
claude --dangerously-skip-permissions
```

但是，就像这个命令内容一样，dangerously（危险地），开启后 Claude 拥有了**完全的自主权**。
- **风险**：它可能会直接修改你的代码、删除文件、安装依赖或执行 shell 命令，而不会再次征求你的同意。
- **建议**：仅在你信任当前任务环境，或者在版本控制（Git）已经提交了代码（方便回滚）的情况下使用此模式。

## 4. 最终文件夹层级结构 - 样例：

```text
C:\Users\用户名\.claude\skills\                  <-- 【根目录】所有 Skill 的存放位置
│
├── 📂 pptx-creation/                          <-- 【Skill 1】PPT 演示文稿生成助手
│   │                                              (参考自 anthropics/skills/pptx)
│   │
│   ├── 📄 SKILL.md                            <-- 🔴 核心：定义 "制作PPT" 的指令入口
│   │                                              (内容：指示Claude调用Python脚本生成幻灯片)
│   │
│   ├── 📂 scripts/                            <-- 执行代码库
│   │   └── 🐍 generate_slides.py              <-- 脚本：使用 python-pptx 库构建 PPT 文件
│   │
│   └── 📂 assets/                             <-- 静态资源库
│       ├── 📊 corporate_template.pptx         <-- 模板：包含公司Logo和配色方案的主母版
│       └── 📄 layout_config.json              <-- 配置：定义标题、正文在页面上的坐标位置
│
└── 📂 xlsx-analysis/                          <-- 【Skill 2】Excel 数据清洗与分析
    │                                              (参考自 anthropics/skills/xlsx)
    │
    ├── 📄 SKILL.md                            <-- 🔴 核心：定义 "分析表格" 的指令入口
    │                                              (内容：指示Claude读取Excel并生成图表)
    │
    ├── 📂 scripts/                            <-- 执行代码库
    │   ├── 🐍 clean_data.py                   <-- 脚本：使用 pandas 清洗空值和错误格式
    │   └── 🐍 create_pivot_table.py           <-- 脚本：自动生成数据透视表
    │
    └── 📂 examples/                           <-- 示例库 (用于 Few-Shot Prompting)
        ├── 📄 prompt_examples.txt             <-- 教程：教 Claude 如何写对应的 Python 代码
        └── 📉 sample_output.xlsx              <-- 样例：期望的输出格式参考文件
```

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
