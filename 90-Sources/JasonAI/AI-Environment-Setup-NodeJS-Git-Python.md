---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "2026 AI环境配置完整指南：Node.js、Git、Python、API Key一次讲清，解决你90%的环境报错。 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/ai-environment-setup-nodejs-git-python/"
source_url: "https://jasonai.me/download/2026-AI环境配置完整指南-Node.js-Git-Python-API-Key一次讲清-解决你90-的环境报错.md"
published: 2026-03-13
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
---

## 1. 必装核心环境 (Node.js / Git / Python)

为 AI Agent 提供底层运行支持，必须优先安装。

### 为什么必须安装
- **Node.js**: 核心基石。绝大多数现代 Agent 工具（比如 **OpenClaw**, Gemini CLI, Claude Code, OpenCode）都依赖 Node 环境运行。
- **Git**: 版本控制与代码拉取工具。Agent 在获取外部 Skill（技能）、克隆插件仓库时强制依赖 Git。
- **Python**: 数据处理与脚本执行环境。大量 Agent 的底层技能（比如数据分析、文件处理）是由 Python 编写的。

以**OpenClaw**为例，不管你是通过`npm install`安装，还是通过`curl`或`iwr`安装，还是让其他智能体（Codex, Claude Code）帮你安装，**都依赖Node.js和Git环境**。
### 安装方法
**Windows 系统（方法一）： 直接下载安装文件**



| 工具 | 官方下载地址 | 验证命令 |
| :--- | :--- | :--- |
| **Node.js** | [nodejs.org](https://nodejs.org) | `node -v` / `npm -v` |
| **Git** | [git-scm.com](https://git-scm.com) | `git --version` |
| **Python** | [python.org](https://python.org) | `python --version` |

安装完成后可以在终端验证，如果命令能正常输出版本号说明安装成功。：

```
node -v
npm -v
git --version
python --version
```

**💡 安装要点：**
* 安装时请务必勾选 **`Add to PATH`**。
* 其余步骤保持默认设置即可。
* 若终端能正常输出版本号，则表示安装成功。

**Windows 系统 （方法二）：使用系统内置的 winget**
打开 PowerShell，直接运行以下命令。这会自动下载并配置所有环境变量。

```powershell
winget install OpenJS.NodeJS.LTS
winget install Git.Git
winget install Python.Python.3.13
```

**macOS 系统 (使用 Homebrew)**
打开 Terminal。如果网络受限，建议在科学上网客户端开启“增强模式 / TUN 模式”，否则会导致拉取失败。

1. 安装 Homebrew（如果提示安装 Xcode Command Line Tools，按回车确认）：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
安装过程中如果系统没有 Command Line Tools 会提示安装。Homebrew 安装完成后运行下面的命令，确认环境正常：
```
brew doctor
```

2. 随后安装基础环境：
```
brew install node
brew install git
brew install python
```
验证安装：
```
node -v
git --version
python3 --version
```

**避坑提示**：作为单纯的 AI 使用者，**绝对不要**去安装 `nvm` (Node 版本管理) 或 `uv` (Python 依赖管理)。这些是针对开发者的复杂工具，只会增加普通人的使用摩擦。

> 很多人看到 OpenClaw 的安装命令是 `curl | bash` 或 Windows 的 `iwr | iex`，会误以为这是在“直接安装软件”。其实不是。这种命令本质只是下载并运行一个安装脚本，让官方可以在脚本里做更多事情，比如检查系统环境、创建配置文件、安装后台服务（daemon）等。因此像 OpenClaw 这种需要初始化较多组件的 AI Agent 工具，就更适合用这种方式安装。
>
> 但需要注意：**OpenClaw 本身仍然依赖 Node.js 和 Git**。安装脚本通常只是检测这些依赖是否存在，**如果没有就会报错**，而不是自动帮你完整安装整个开发环境。
>
> 相比之下，Claude Code 和 OpenCode 这类工具，本质上是比较标准的 Node.js CLI 程序，所以官方仍然更推荐用 `npm install -g` 来安装。因为 npm 已经是 Node 生态最直接、最稳定的分发方式，不需要额外的安装脚本。

---
## 2. 终端 (Terminal) 基础操作与网络配置

| 操作系统        | 终端工具                     | 精准描述                                           |
| ----------- | ------------------------ | ---------------------------------------------- |
| **Windows** | **Command Prompt (CMD)** | 基于传统 DOS 指令的遗留命令行工具，主要用于执行简单的系统任务。             |
| **Windows** | **PowerShell**           | 基于 .NET 框架的现代化脚本环境，通过“对象”管理实现复杂的系统自动化。         |
| **macOS**   | **Terminal (终端)**        | 基于 Unix 内核的命令行接口，使用 Zsh/Bash Shell 进行标准化的系统交互。 |
#### 针对powershell：
PowerShell 可能会报错说“禁止运行脚本”。这对普通人来说像是个大故障，但其实只需要执行一行命令就能永久解决：
 **解决办法**：以管理员身份打开 PowerShell，输入并回车：
 
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 一、 环境变量配置

#### 1. CMD (Windows)
* **仅当前窗口有效 (临时)**：使用 `set`，关闭窗口后失效。
  ```cmd
  set OPENAI_API_KEY="你的API_KEY"
  ```
* **永久有效**：使用 `setx`，设置后需**重新打开** CMD 窗口生效。
  ```cmd
  setx OPENAI_API_KEY "你的API_KEY"
  ```

#### 2. Terminal (macOS)
*(以 macOS 默认的 zsh 为例)*
* **仅当前窗口有效 (临时)**：使用 `export` 命令。
  ```bash
  export OPENAI_API_KEY="你的API_KEY"
  ```
* **永久有效**：将配置追加到 Shell 的配置文件中，并刷新生效。
  ```bash
  echo 'export OPENAI_API_KEY="你的API_KEY"' >> ~/.zshrc
  source ~/.zshrc
  ```

#### 举例：Claude Code环境变量设置

Claude地区限制严格。用兼容模型提到Claude模型。（可回看我的Claude Skill视频）

```bash
# 1. CMD (Windows) - 使用 setx 永久设置
# 注意：setx 命令不需要等号，变量名和值之间用空格分隔
setx ANTHROPIC_BASE_URL "https://open.bigmodel.cn/api/anthropic"
setx ANTHROPIC_API_KEY "你的API Key"
setx ANTHROPIC_MODEL "glm-4.7-flash"

# 2. Terminal (macOS / Linux) - 写入 zsh 配置文件
echo 'export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"' >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY="你的API Key"' >> ~/.zshrc
echo 'export ANTHROPIC_MODEL="glm-4.7-flash"' >> ~/.zshrc
# 执行下方命令立即在当前窗口生效：
source ~/.zshrc
```

### 二、 网络代理配置（永久有效）

#### 1. CMD (Windows)
使用 `setx` 命令将代理地址写入用户环境变量，永久有效。
```cmd
setx http_proxy "http://127.0.0.1:7890"
setx https_proxy "http://127.0.0.1:7890"
```

#### 2. Terminal (macOS)
将代理的环境变量永久写入到 `~/.zshrc` 配置文件中。
```bash
echo 'export http_proxy="http://127.0.0.1:7890"' >> ~/.zshrc
echo 'export https_proxy="http://127.0.0.1:7890"' >> ~/.zshrc
source ~/.zshrc
```

### 三、 常用命令

#### 1. CMD (Windows)
* `dir` : 列出当前目录下的文件和文件夹
* `cd 文件夹名` : 进入指定文件夹 (`cd ..` 返回上一级)
* `cd /d D:\` : 跨驱动器切换目录
* `md 文件夹名` 或 `mkdir 文件夹名` : 创建新文件夹
* `rd 文件夹名` : 删除空文件夹
* `del 文件名` : 删除文件

#### 2. Terminal (macOS)
* `ls` : 列出文件 (`ls -la` 包含隐藏文件及详细信息)
* `cd 文件夹名` : 切换目录 (`cd ~` 回到用户根目录)
* `mkdir 文件夹名` : 创建新文件夹
* `rm 文件名` : 删除文件 (`rm -rf 文件夹名` 强制删除非空文件夹，慎用)
* `pwd` : 打印当前工作目录的完整路径
* `cat 文件名` : 在终端中直接查看文件内容

---
## 3. API Key 核心认知

API Key 是你调用云端大模型算力的“通行证”，它和普通网页版 AI (比如 ChatGPT) 有本质区别。

### 核心差异对比
| 维度       | 网页版 AI  (比如 ChatGPT)    | API Key 调用                                          |
| :------- | :---------------------- | :-------------------------------------------------- |
| **付费模式** | 包月制（通常 20 美元/月），有使用次数上限 | 按量计费（消耗 Token 扣费），用多少扣多少                            |
| **调用接口** | 仅限官方网页或官方 App           | 可接入任何第三方 Agent 工具（比如 OpenClaw, Claude Code）         |
| **模型选择** | 只能用官方提供的几个固定模型          | 自由切换不同厂商的模型（比如 OpenAI, Anthropic, Gemini, DeepSeek） |

### API 调用通常需要配置三个核心信息：

* **API Key**: 访问凭证，相当于你的调用密码。
* **Base URL**: API 地址，即请求发送到的服务器网关。
* **Model Name**: 模型名称，指定具体要调用的 AI 版本（如 gpt-4 或 claude-3）。

### 常见 API 类型：

* **OpenAI 兼容 API**：
  这是目前行业最通用的标准接口格式。大多数国内模型平台（如智谱 AI、通义千问）和中转服务都支持此格式，使得开发者可以无缝替换底层模型。
* **Anthropic API**：
  Claude 系列模型专用的接口协议。与 OpenAI 格式略有不同，它是 Claude Code 等 Anthropic 原生工具默认采用的通信方式。
* **自定义 API**：
  指某些特定平台独有的接口协议或私有化部署的 API。通常需要专门的 SDK 或额外的参数映射（如 API 版本号、Project ID 等）才能正常对接。

#### 举例：
```bash
# DeepSeek API (深度求索)
ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic" # Anthropic 格式 (Claude Code 专用)
OPENAI_BASE_URL="https://api.deepseek.com/v1"           # OpenAI 兼容格式 (常规插件使用)
OFFICIAL_BASE_URL="https://api.deepseek.com"            # 官方原生格式 (官方 SDK 使用)

# Zhipu AI (智谱清言 GLM)
ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic" # Anthropic 格式 (Claude Code 专用)
OPENAI_BASE_URL="https://open.bigmodel.cn/api/paas/v4"      # OpenAI 兼容格式 (常规插件使用)
OFFICIAL_BASE_URL="https://open.bigmodel.cn/api/paas/v4"    # 官方原生格式 (目前与 OpenAI 格式相同)
```

### 视觉能力与模型选择限制
如果在命令行 Agent 中发送图片却报错“无法识别”，通常不是工具的问题，而是你填写的模型名称 (Model Name) 或调用的 API 节点不支持视觉。
- 纯文本模型：例如专门用于后台代码生成的低延迟模型（比如一些专供 Coding 计划的轻量模型），为了追求速度阉割了视觉模块。
- 免费高可用模型：日常做 Agent 底座测试，推荐注册使用智谱的 `GLM-4.7-Flash` 模型，速度极快且调用完全免费。

**安全警告**：API Key 等同于你的银行卡密码，**绝对不能**截图发给别人，也不能上传到公开的 GitHub 仓库中，否则会被恶意盗刷产生巨额账单。

---

## 4. 进阶环境与 Agent 工具


### Docker 与环境隔离
- **作用**：让高权限 Agent (比如 OpenClaw) 直接在真实电脑里运行代码是极度危险的。必须把它关在 Docker 这个“沙盒”里。这样即便 Agent 执行了危险代码，也只会破坏容器内部，不会伤及你的真实电脑系统。
- **Windows 用户**：直接安装 **Docker Desktop**。安装时必须勾选 `Use WSL 2 based engine`。这个勾选动作就已经帮你完成了 WSL 的底层部署，不需要单独去折腾 WSL 命令行。
- **提示**：部署在 Docker 里的 n8n 完全可以访问本地文件。只需要在启动命令中使用 `-v /你的本地路径:/容器内部路径` 参数进行卷映射，就能打通容器内外的数据。





| 操作系统 | 推荐安装方式 | 核心操作 |
| :--- | :--- | :--- |
| Windows | 官网下载 .exe 安装包 | 安装时务必勾选 "Use WSL 2 based engine"，无需手动折腾命令行。 |
| macOS | 官网下载 .dmg 安装包 | 验证芯片类型（Apple Silicon 或 Intel），下载对应版本直接拖拽安装。 |


### 本地AI大模型部署 (LM Studio)

- **作用**：让你在不联网、不花钱的情况下，直接在自己电脑上运行 AI 模型（如 Qwen 或 Llama）。
- **优势**：全图形界面操作，且能一键开启“OpenAI 兼容接口”，让你的其他 AI 工具（如 Cursor 或翻译插件）直接调用本地模型（例如 `qwen-2.5-7b`）。


| 操作系统 | 推荐安装方式 | 核心操作 |
| :--- | :--- | :--- |
| Windows | 官网下载 .exe 安装包 | 去 lmstudio.ai 下载，安装后可一键开启兼容 OpenAI 的本地 API 服务。 |
| macOS | 官网下载 .dmg 安装包 | 对 M 系列芯片支持极佳，建议 16G 内存以上机型使用以获得流畅体验。 |


### 主流 Agent 工具横向对比 (2026 最新版)

| 工具名称        | 安装命令 (NPM)                                 | 备注                                                |
| :---------- | :----------------------------------------- | :------------------------------------------------ |
| Gemini CLI  | `npm install -g @google/gemini-cli`        | Google 官方开源，免费额度大，适合本地文件管理与问答，我最推荐Obsidian使用者用这个。 |
| Claude Code | `npm install -g @anthropic-ai/claude-code` | Anthropic 官方出品，代码理解力极强，执行高危命令需人工确认，安全稳健。          |
| OpenCode    | `npm install -g opencode-ai`               | 第三方开源工具，支持多模型自由切换，有免费模型，需注意保护配置文件中的 Key。          |
| OpenClaw    | `npm install -g openclaw`                  | 权限极大，一定要注意安全和隐私。                                  |

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
