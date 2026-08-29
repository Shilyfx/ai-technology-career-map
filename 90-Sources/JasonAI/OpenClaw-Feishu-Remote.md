---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "从 0 开始用 OpenClaw：Windows / Mac 安装 + 飞书联动，手机远程操控 AI | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/install-openclaw-feishu-remote-ai/"
source_url: "https://jasonai.me/download/从-0-开始用-OpenClaw-Windows-Mac-安装-飞书联动-手机远程操控-AI.md"
published: 2026-02-14
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

## 1. 准备工作

### 环境依赖
无论是 Windows 还是 macOS，必须预先安装以下工具：

1.  **Node.js**: 版本需 **> 22** 。
    *   [Node.js 官网下载](https://nodejs.org/)
2.  **Git**: 用于拉取 GitHub 资源。
    *   [Git 官网下载](https://git-scm.com/)

> **验证环境命令** (终端/CMD):
> ```bash
> node -v  # 检查 Node 版本
> npm -v   # 检查 NPM 版本
> git -v   # 检查 Git 版本
> ```

---

## 2. 快速安装与初始化 (本机运行)

### 安装步骤

1.  **配置 NPM 国内镜像** (防止网络超时，如果在国外则不用。):
    ```bash
    npm config set registry https://registry.npmmirror.com
    ```

2.  **全局安装 OpenClaw**:
    ```bash
    npm install -g openclaw@latest
    ```

3.  **初始化**:
    ```bash
    openclaw onboard --install-daemon
    ```

### 初始化配置向导

| 步骤 | 选项/输入 | 说明 |
| :--- | :--- | :--- |
| **Risk Warning** | `Yes` | 确认知晓 AI 操作风险 |
| **Setup Mode** | `Quickstart` | 快速开始模式 |
| **LLM Provider** | `Zhipu AI` (或其他) | 推荐先用智谱 GLM 等有免费额度的模型测试 |
| **API Key** | `粘贴你的 Key` | 终端中粘贴不显示，直接回车 |
| **Model** | `GLM 4.7` | 或 MiniMax, Kimi 等高性价比模型 |
| **Skills/Channels** | `Skip` / `No` | 后续在 WebUI 中配置 |
| **Interface** | `Open the Web UI` | 启动网页版图形界面 (默认端口 18789) |

> **测试指令**: 
> *   对话框输入: "你好" (验证 LLM 连接)
> *   对话框输入: "在我的用户主目录下，创建一个名为 Jason-OpenClaw 的文件夹" (验证系统操作权限)

---

## 3. 插件与技能 (Skills) 管理

OpenClaw 的强大在于 Skills。除了内置技能，还可以从社区安装。

*   **官方市场**: [ClawHub](https://clawhub.openclaw.ai) (官网链接进入)
*   **GitHub仓库**: `awesome-openclaw-skills`

### 必装技能

1.  **find-skills**: 核心技能。允许 AI 根据你的自然语言需求，自动去寻找并安装其他所需的 Skills。
2.  **Web Search / Browsing**: 增强联网搜索能力。

### 安装方式
*   **安装插件：命令行方式**: `openclaw plugins install 插件名`
*   **安装Skill：对话安装**: 直接把 GitHub 仓库链接发给机器人，指令："请帮我安装这个 skill"。

---

## 4. 集成即时通讯APP（WhatsApp，飞书等）

这是实现“手机遥控数字员工”的关键步骤。

### WhatsApp 集成
在 OpenClaw 的配置文件里（通常是 `~/.openclaw/openclaw.json`），添加如下最基本的 WhatsApp 配置：
```json
{
  "channels": {
    "whatsapp": {
      "dmPolicy": "allowlist",
      "allowFrom": ["+15551234567"]
    }
  }
}
```
然后在终端执行：
```bash
openclaw channels login
```
这个命令会打印一个专用的 QR 码，打开 WhatsApp 手机应用扫码即可。

### 飞书集成
#### 第一步：安装飞书插件
在终端执行：
```bash
openclaw plugins install @m1heng-clawd/feishu
# 注：插件名可能随社区更新变动，具体以 github 仓库为准
```

#### 第二步：飞书开放平台配置
登录 [飞书开放平台](https://open.feishu.cn/) -> 开发者后台。

1.  **创建应用**: 点击“创建企业自建应用”，填写名称（如 `JasonBot`），选择图标。
2.  **添加能力**: 左侧菜单“添加应用能力” -> “机器人” -> 点击添加。
3.  **权限管理 (关键)**:
    *   进入“权限管理”。
    *   搜索并开通 `im:message` 相关权限 (收发消息)，如表格所示。
    *   **也可批量导入**: 点击“批量导入”，粘贴以下 JSON 配置 (参考模板):

| 必要权限                               | 范围  | 说明            |
| ---------------------------------- | --- | ------------- |
| `im:message`                       | 消息  | 发送和接收消息       |
| `im:message.p2p_msg:readonly`      | 私聊  | 读取发给机器人的私聊消息  |
| `im:message.group_at_msg:readonly` | 群聊  | 接收群内 @机器人 的消息 |
| `im:message:send_as_bot`           | 发送  | 以机器人身份发送消息    |
| `im:resource`                      | 媒体  | 上传和下载图片/文件    |

```json
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "docs:document.content:read",
      "event:ip_list",
      "im:chat",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.group_msg",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource",
      "sheets:spreadsheet",
      "wiki:wiki:readonly"
    ],
    "user": [
      "aily:file:read",
      "aily:file:write",
      "im:chat.access_event.bot_p2p_chat:read"
    ]
  }
}
```

4.  **版本发布**: 左侧“版本管理与发布” -> 创建版本 (v1.0.0) -> 发布。
5.  **获取凭证**: 左侧“凭证与基础信息” -> 复制 `App ID` 和 `App Secret`。

#### 第三步：OpenClaw 连接配置
回到 OpenClaw Web UI -> `Channels` -> `Feishu` (配置界面)：

*   **App ID**: 粘贴飞书 App ID。
*   **App Secret**: 粘贴飞书 App Secret。
*   **Connection Mode**: 选择 `WebSocket` (无需公网 IP，无需内网穿透)。
*   **Domain**:  `feishu`。
*   **Policies**: `DM Policy` 和 `Group Policy` 建议选 `Open` (或按需设置 Allowlist)。
*   点击 **Save** 保存。

#### 第四步：开启事件订阅
*OpenClaw 配置保存后，守护进程会启动 WebSocket 连接，此时才能去飞书配置长连接。*

1.  回到飞书开发者后台 -> “事件与回调”。
2.  **配置订阅方式**: 选择 **长连接**。
3.  **添加事件**: 点击“添加事件” -> 搜索 `receive` -> 勾选 `im.message.receive_v1` (接收消息) -> 确认。
4.  **重新发布**: 修改配置后，**必须**再次去“版本管理”发布一个新版本才能生效。

> **手机APP测试**: 打开飞书 App -> 搜索机器人名称 -> 发送 "你好" 或 "在我的用户主目录下创建一个名字叫 jason-feishu 的文件夹"。（飞书桌面APP同理）

---

## 5. Docker 隔离环境部署 (进阶)

为了安全（隔离主系统文件）和 24h 运行，建议使用 Docker 部署。

### 部署流程
1.  **安装 Docker**: 下载并安装 Docker Desktop。
2.  **下载仓库**:
    ```bash
    git clone https://github.com/openclaw/openclaw
    cd openclaw
    ```
3.  **运行安装脚本**:
    *   **Mac/Linux**:
        ```bash
        ./docker-setup.sh
        ```
    *   **Windows**: 需在 Git Bash 中运行上述命令。
4.  **注意事项**:
    *   脚本会自动拉取镜像并启动容器。
    *   初始化步骤与本机安装一致。
    *   **Token 成本**: 建议使用 Coding Plan 或包月类 API (如GLM, MiniMax) 防止 Token 消耗过快。

---

## 安全与隐私警告

1.  **数据隐私**: 避免让 AI 访问存有敏感数据（私钥、密码表、个人相册等）的目录。
2.  **操作权限**: OpenClaw 具有系统级操作权限（删除文件、运行脚本），请谨慎授予 `sudo` 权限或在非隔离环境运行高风险指令。
3.  **Token 监控**: 智能体自主运行时会消耗大量 Token，务必设置额度上限。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
