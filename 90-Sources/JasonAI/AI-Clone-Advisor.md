---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "用AI克隆顶级博主的大脑，打造你的专属AI顾问，【吞噬】一个顶级博主的全部思想。 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/clone-top-creator-ai-advisor/"
source_url: "https://jasonai.me/download/用AI克隆顶级博主的大脑-打造你的专属AI顾问-吞噬一个顶级博主的全部思想.md"
published: 2025-09-04
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
---

欢迎来到这份终极指南。
本笔记为你提供一个完整的、可操作的、全自动化的工作流，将任何一位顶尖知识博主的思想体系，转化为您个人的、可交互的AI顾问和私有知识库。

我们的宗旨是：**克隆他的大脑，继承他的智慧，吞噬他的思想。**

本工作流遵循三大原则：

1. **全程自动化**：尽可能减少手动操作，实现批量处理。
    
2. **工具免费化**：核心工具均为开源免费。
    
3. **流程简单化**：无需深厚的编程背景，普通学习者也能上手。
    

## 工作流总览

本工作流分为三个核心步骤：

1. **【知识获取】**：批量抓取博主所有视频的原始字幕文件。
    
2. **【知识精炼】**：通过本地AI大模型，将原始字幕自动化处理为高质量的Markdown知识文档。
    
3. **【知识内化与创造】**：使用NotebookLM和Obsidian等工具，打造AI分身并融入个人知识体系，最终实现价值创造。
    

---

## 第一步：知识获取 

**目标**：全自动、批量化地获取目标博主所有视频的原始字幕文件（.srt或.vtt格式）。

### 核心工具箱


| 工具        | 类型             | 优点                       | 缺点                                   | 推荐用户                             |
| ----------- | ---------------- | -------------------------- | -------------------------------------- | ------------------------------------ |
| **TarTube** | 图形化界面 (GUI) | 操作直观，无需命令行       | 稳定性稍弱，批量处理大量视频时可能卡顿 | 新手、不熟悉命令行的用户             |
| **yt-dlp**  | 命令行 (CLI)     | 极致灵活、速度快、稳定可靠 | 需要使用终端，有一定学习门槛           | 进阶用户、追求极致效率和自动化的用户 |

### 关键前置步骤：获取Cookie文件

> **为什么要Cookie？**  
> Cookie文件相当于您登录视频网站的“数字身份证”。在批量下载时携带Cookie，可以向服务器证明您是真实用户，从而避免被反爬虫机制拦截，这是确保任务成功的关键。

1. **安装浏览器插件**：在您的浏览器（Chrome/Edge/Firefox）中，搜索并安装插件 **Get cookies.txt LOCALLY**。
    
2. **登录网站**：确保您已在该浏览器中登录了目标视频网站（如YouTube）。
    
3. **导出Cookie**：点击浏览器右上角的插件图标，然后点击Export按钮，浏览器将自动下载一个名为cookies.txt的文件。
    
4. **妥善保管**：将这个cookies.txt文件保存在您即将进行操作的工作文件夹中。
    

### 方案A：使用 TarTube (图形化界面)

1. **下载与安装**：
    
    - 前往TarTube的GitHub官方页面。
        
    - 在页面右侧找到并点击 **Releases**。
        
    - 根据您的操作系统（Windows/macOS）下载对应的安装包（推荐选择带ffmpeg的版本），并像安装普通软件一样完成安装。
        
2. **初始化设置**：
    
    - 首次打开时，按提示选择一个用于存放下载文件的默认文件夹。
        
    - 根据引导完成yt-dlp核心组件的安装。
        
3. **配置Cookie**：
    
    - 在TarTube主界面，点击左上角的 **编辑** -> **全局下载选项**。
        
    - 在弹出的窗口中，切换到 **文件** -> **cookies**。
        
    - 勾选“使用Cookie文件”，并点击浏览按钮，选择您之前导出的cookies.txt文件。
        
4. **下载字幕**：
    
    - 回到主页面，点击顶部第二个按钮 **添加新频道**，粘贴目标博主的频道URL。
        
    - 在左侧频道列表中，右键点击新添加的频道，选择 **检查频道**，等待软件获取所有视频列表。
        
    - 再次进入 **编辑** -> **全局下载选项**，在 **名称** 选项卡的输入框中，粘贴以下参数。这会告诉TarTube只下载中英文字幕，并跳过视频本身：
        
        codeCode
        
        ```
        --write-sub --skip-download --sub-lang en,zh-CN
        ```
        
    - 切换到 **字幕** 选项卡，勾选 **下载所有可用的字幕文件**。
        
    - 点击确认保存设置。
        
    - 在右侧视频列表中，分批次（建议一次5-10个）选中视频，右键点击 **下载**。
        

### 方案B：使用 yt-dlp (命令行)

1. **环境搭建**：
    
    - **安装Python**：前往Python官网 (python.org) 下载并安装最新稳定版。**在安装过程中，务必勾选 Add Python to PATH 选项。**
        
    - **安装yt-dlp**：打开终端（Windows下为CMD或PowerShell，macOS下为Terminal），输入以下命令并回车：
        
        codeBash
        
        ```
        pip install yt-dlp
        ```
        
    - **（可选）保持更新**：为确保最佳兼容性，可以随时运行以下命令升级yt-dlp：
        
        codeBash
        
        ```
        pip install --upgrade yt-dlp
        ```
        
2. **核心命令**：
    
    - **第一步：获取所有视频链接（侦察）**  
        在一个新建的空文件夹中，打开终端，运行以下命令，它会快速抓取频道内所有视频的URL并存入一个文本文件：
        
        codeBash
        
        ```
        yt-dlp --flat-playlist --print url "YOUTUBE_CHANNEL_URL" > video_links.txt
        ```
        
        > **注意**：请将 YOUTUBE_CHANNEL_URL 替换为真实的频道链接。
        
    - **第二步：批量下载所有字幕（总攻）**  
        确保cookies.txt和上一步生成的video_links.txt都在当前文件夹中。然后运行以下“终极指令”：
        
        codeBash
        
        ```
        yt-dlp --cookies cookies.txt --write-auto-sub --sub-lang en --skip-download --batch-file video_links.txt      
        ```

		> **参数解析**：
        > - `--cookies cookies.txt`: 使用Cookie文件进行认证。
        > - `--write-auto-sub`: 下载自动生成的字幕。
        > - `--sub-lang en`: 指定下载英文字幕。
        > - `--skip-download`: 跳过视频和音频的下载，只取字幕。
        > - `--batch-file video_links.txt`: 从指定文件中读取链接列表并批量处理。
---

## 第二步：知识精炼 

**目标**：利用本地AI大模型，将第一步获取的原始字幕文件，自动化地翻译、润色，并处理成干净的Markdown格式知识文档。

### 核心工具：LM Studio + Python脚本

**优势**：数据完全私有，无API调用费用，可深度定制处理逻辑。

1. **部署本地大模型 (LM Studio)**：
    
    - 前往LM Studio官网 (lmstudio.ai) 下载并安装软件。
        
    - 打开软件，点击左侧的放大镜图标进入搜索页。
        
    - 搜索推荐模型，例如 qwen3-8b-instruct-GGUF，选择一个版本点击下载。
        
    - 下载完成后，点击左侧第三个“本地服务器”图标。
        
    - 在顶部选择刚刚下载的模型，服务器设置保持默认即可。
        
    - 点击 **Start Server** 启动本地API服务器。
        
    - **关键设置**：点击右侧的Settings，确保 **CORS (Cross-Origin Resource Sharing)** 选项是**开启**的，这样我们的Python脚本才能访问它。
        
    - **性能配置**：在Load选项卡下的Context Length中，根据你电脑的显存进行设置（例如8G显存可设置为8000）。
        
2. **运行自动化脚本**：
    
    - **准备脚本**：获取我们提供的Python脚本文件。
        
    - **配置脚本**：用任何文本编辑器打开脚本，修改开头的三个参数：
        
        1. input_folder: 设置为第一步存放原始字幕文件的文件夹路径。
            
        2. output_folder: 设置为你希望保存Markdown文档的目标文件夹路径。
            
        3. api_url: 保持默认的 `http://localhost:1234/v1/chat/completions` 即可，除非你修改了LM Studio的默认端口。
            
    - **执行脚本**：在存放脚本的文件夹中打开终端，运行以下命令：
        
        codeBash
        
        ```
        python your_script_name.py
        ```
        
        > **注意**：请将 your_script_name.py 替换为真实的脚本文件名。
        
    
    脚本将自动开始处理，你可以看到终端中会打印出每个文件的处理进度。
    

---

## 第三步：知识内化与价值创造 

**目标**：将精炼后的知识文档转化为可交互的AI顾问和个人知识体系的一部分，并探索其价值变现的可能。

### 核心工具：Obsidian + NotebookLM

#### 1. Obsidian：构建你的知识网络

- **用途**：作为知识的最终沉淀地和“第二大脑”。
    
- **操作**：将第二步生成的所有Markdown文档导入到你的Obsidian仓库中。
    
- **价值**：
    
    - **深度学习**：利用Obsidian强大的双向链接功能，将博主的知识点与你已有的知识体系进行关联，形成知识网络。
        
    - **本地AI对话**：通过Copilot等AI插件，连接到我们之前部署的本地LM Studio模型，直接在Obsidian内与你的笔记进行对话。
        

#### 2. NotebookLM：召唤你的AI私人顾问

- **用途**：打造一个只基于博主知识回答问题的、绝对忠诚的AI分身。
    
- **操作**：
    
    1. 打开Google NotebookLM官网。
        
    2. 创建一个新的“空间”（Space），例如命名为“Dan Koe AI顾问”。
        
    3. 点击 **添加来源 (Add Source)**，将第二步生成的整个Markdown文件夹上传上去。
        
    4. 等待AI完成索引和消化。
        
- **核心功能与价值**：
    
    - **引用溯源**：所有回答都会标注原文出处，彻底杜绝AI幻觉。
        
    - **全局洞察**：可以跨越上百个文档进行宏观问题的分析、比较和总结。
        
    - **自动学习工具**：一键生成**研读指南**、**FAQ**、**思维导图**等，加速学习进程。
        
    - **语音摘要 (Audio Overview)**：将知识库内容生成类似播客的语音摘要，实现通勤路上的“听学”。
        

### 价值延伸：从学习到创造

拥有了这套高质量的知识库后，其价值远不止于学习：

- **二次创作**：可作为你自媒体频道的“无限选题库”和素材来源。
    
- **价值变现**：可深度加工成精读笔记、思维导图、付费专栏等虚拟产品进行售卖。
    

---

## 备选方案：Notion MCP + Notion AI

如果你的主力工具是Notion，第二步和第三步可以被完美整合：

1. 使用 **Notion MCP** 插件，通过与AI对话的方式，批量清理、处理并导入第一步的字幕文件到Notion数据库。
    
2. 利用 **Notion AI** 的“AI属性”功能，自动对英文原文进行翻译和润色。
    
3. 直接在Notion内，使用其强大的数据库和AI问答功能，实现知识管理和AI顾问的雙重目标。
    

---

**恭喜你！** 至此，你已经完整掌握了这套“克隆顶级大脑”的终极工作流。现在，就开始选择你的第一个目标，开启全新的认知升级之旅吧！


附代码，新建.py文件，把代码复制进去然后保存，然后在命令行中，运行`python xxx.py`即可。

下载YouTube视频的代码：`run_channel_downloader.py`

`````python
import yt_dlp
import os

# ==================== 配置区 (请在这里修改) ====================

# 1. 填入你想要下载的 YouTube 频道的 "Videos" 页面 URL
CHANNEL_URL = "https://www.youtube.com/@DanKoeTalks/videos"

# 2. 定义存放最终字幕文件的输出文件夹名
OUTPUT_DIR = 'output_result'

# 3. 定义 Cookies 文件名 (用于登录验证)
COOKIE_FILE = 'youtube.com_cookies.txt'

# 4. 定义临时存放 URL 列表的文件名 (脚本会自动创建和覆盖)
URLS_FILE = 'urls.txt'

# =============================================================

def get_channel_video_urls(channel_url):
    """
    使用 yt-dlp 获取一个频道下的所有视频 URL。
    这相当于命令: yt-dlp --flat-playlist --print url "channel_url"
    """
    ydl_opts = {
        'extract_flat': True,  # 等同于 --flat-playlist，只提取链接，不访问视频详情
        'quiet': True,         # 不在控制台打印过多信息
    }
    
    video_urls = []
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # extract_info 会返回一个包含所有信息的字典
            result = ydl.extract_info(channel_url, download=False)
            
            if 'entries' in result:
                # 从返回结果中提取每个视频的 URL
                video_urls = [entry['url'] for entry in result['entries']]
    except Exception as e:
        print(f"错误：获取频道视频列表失败。请检查 URL 是否正确以及网络连接。")
        print(f"详细错误: {e}")
        return None
        
    return video_urls

def download_subtitles_from_list(urls):
    """
    根据给定的 URL 列表，下载所有视频的字幕。
    """
    # 配置 yt-dlp 的下载选项
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en', 'zh-CN', 'zh-Hant'],
        'skip_download': True,
        'ignoreerrors': True,
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'cookiefile': COOKIE_FILE,
        
        # 添加禁止写入额外文件的选项，保持输出目录干净
        'writedescription': False,
        'writeinfojson': False,
        'writethumbnail': False,
    }

    # 使用 yt-dlp 的 Python API 开始下载
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        total_urls = len(urls)
        for i, url in enumerate(urls, 1):
            print(f"--- [进度: {i}/{total_urls}] 正在处理URL: {url} ---")
            try:
                ydl.download([url])
                print("字幕下载成功。")
            except Exception as e:
                print(f"处理过程中发生错误: {e}")

def main():
    """
    主函数：集成所有步骤，实现完全自动化。
    """
    print("============================================")
    print("YouTube 频道字幕下载器")
    print("============================================")

    # 步骤 1: 获取频道下的所有视频 URL
    print(f"\n[步骤 1/3] 正在从频道获取所有视频的 URL 列表...\n频道: {CHANNEL_URL}")
    video_urls = get_channel_video_urls(CHANNEL_URL)

    if not video_urls:
        print("\n无法获取视频列表，脚本已终止。")
        return

    print(f"成功获取到 {len(video_urls)} 个视频 URL。")

    # 步骤 2: 将获取到的 URL 写入 urls.txt 文件
    try:
        with open(URLS_FILE, 'w', encoding='utf-8') as f:
            for url in video_urls:
                f.write(f"{url}\n")
        print(f"\n[步骤 2/3] 已将所有 URL 成功写入文件 '{URLS_FILE}'。")
    except Exception as e:
        print(f"\n错误：无法写入 URL 文件。详细错误: {e}")
        return

    # 步骤 3: 创建输出文件夹并开始下载字幕
    if not os.path.exists(OUTPUT_DIR):
        print(f"输出文件夹 '{OUTPUT_DIR}' 不存在，正在创建...")
        os.makedirs(OUTPUT_DIR)
        
    print(f"\n[步骤 3/3] 开始根据 '{URLS_FILE}' 中的列表下载字幕...")
    download_subtitles_from_list(video_urls)

    print(f"\n所有任务处理完毕！下载的字幕文件已全部保存在 '{OUTPUT_DIR}' 文件夹中。")

# 当直接运行此脚本文件时，执行 main() 函数
if __name__ == '__main__':
    main()
`````

**调用本地大模型**对字幕进行翻译润色的代码：`call_ai_translate_vtt_to_md.py`

`````python
import os
import requests
import json
import webvtt
import tiktoken
import time
import re

# --- 1. 配置区 ---

VTT_FOLDER_PATH = r'C:\Users\wwd_m\Downloads\test-vtt'
OUTPUT_FOLDER_PATH = r'C:\Users\wwd_m\Downloads\output-vtt-md'
API_URL = 'http://127.0.0.1:1234/v1/chat/completions'

# 【优化点1】: 尝试一个更大的分片值，您可以根据测试结果调整这个数字
MAX_TOKENS_PER_CHUNK = 2500  # 建议从 2500 开始测试

# 【优化点2】: 使用能合并段落的新版Prompt
SYSTEM_PROMPT = """
你是一位顶级的翻译家和内容编辑。
你的任务是：将用户提供的英文视频口播稿，完整地翻译成一篇流畅、自然、连贯的简体中文文章。

请严格遵守以下核心原则：
1. **全文翻译与合并**：
   - 必须逐句翻译所有内容，不能省略或总结。
   - **关键指令**：请智能地将原文中语义连贯的多行短句，合并成符合中文阅读习惯的自然段落。不要原文每行都换行。

2. **保持逻辑**：在合并段落时，要尊重原文的逻辑停顿。如果原文有明显的空行或意群转换，可以在译文中也进行分段。

3. **Markdown输出**：使用 Markdown 格式，可以对关键词进行 **加粗** 以提高可读性。

4. **直接输出文章**：请直接开始输出最终翻译好的中文文章，不要包含任何解释或类似 <think> 的标签。
"""

# --- 2. 核心功能区 (与上一版相同) ---

def get_tokenizer():
    try:
        return tiktoken.get_encoding("cl100k_base")
    except Exception as e:
        print(f"获取 tokenizer 失败: {e}")
        return None

def parse_vtt_file(file_path):
    try:
        captions = webvtt.read(file_path)
        full_text = "\n".join([caption.text.strip() for caption in captions])
        return full_text
    except Exception as e:
        print(f"解析VTT文件 {os.path.basename(file_path)} 时出错: {e}")
        return None

def split_text_into_chunks(text, tokenizer):
    if not tokenizer:
        print("Tokenizer 不可用，无法进行分片。将尝试一次性处理。")
        return [text]
    tokens = tokenizer.encode(text)
    if len(tokens) <= MAX_TOKENS_PER_CHUNK:
        return [text]

    print(f"文本过长 ({len(tokens)} tokens)，正在分片处理...")
    chunks = []
    current_chunk_tokens = []
    paragraphs = text.split('\n')
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
        paragraph_tokens = tokenizer.encode(paragraph + "\n")
        if len(current_chunk_tokens) + len(paragraph_tokens) > MAX_TOKENS_PER_CHUNK:
            if current_chunk_tokens:
                chunks.append(tokenizer.decode(current_chunk_tokens))
                current_chunk_tokens = []
        current_chunk_tokens.extend(paragraph_tokens)
    if current_chunk_tokens:
        chunks.append(tokenizer.decode(current_chunk_tokens))
    
    print(f"文本成功被分成了 {len(chunks)} 个片段。")
    return chunks

def clean_model_output(raw_text):
    cleaned_text = re.sub(r'^\s*<think>.*?</think>\s*', '', raw_text, flags=re.DOTALL)
    return cleaned_text

def process_chunk_with_llm(text_chunk):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text_chunk}
        ],
        "temperature": 0.7,
        "stream": False
    }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload), timeout=300)
        response.raise_for_status()
        response_json = response.json()
        raw_output_text = response_json['choices'][0]['message']['content']
        cleaned_output_text = clean_model_output(raw_output_text)
        return cleaned_output_text
    except requests.exceptions.Timeout:
        print(f"调用API时超时！(超过300秒)")
        return None
    except requests.exceptions.RequestException as e:
        print(f"调用API时出错: {e}")
        return None

def process_single_file(vtt_file_path, tokenizer):
    filename = os.path.basename(vtt_file_path)
    print(f"\n--- 正在处理文件: {filename} ---")
    
    english_text = parse_vtt_file(vtt_file_path)
    if not english_text:
        return

    chunks = split_text_into_chunks(english_text, tokenizer)
    
    processed_chunks = []
    for i, chunk in enumerate(chunks):
        print(f"正在翻译片段 {i+1}/{len(chunks)}...")
        translated_chunk = process_chunk_with_llm(chunk)
        if not translated_chunk:
            print(f"片段 {i+1} 翻译失败，已跳过整个文件 {filename}。")
            return
        processed_chunks.append(translated_chunk)
        time.sleep(1)
        
    final_text = "\n\n".join(processed_chunks)
    output_filename = f"{os.path.splitext(filename)[0]}.md"
    output_file_path = os.path.join(OUTPUT_FOLDER_PATH, output_filename)
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(final_text.strip())
        print(f"处理完成！翻译稿已保存至: {output_file_path}\n" + "-"*40)
    except IOError as e:
        print(f"保存文件 {output_filename} 时出错: {e}")

# --- 3. 主程序入口 ---
def main():
    if not os.path.isdir(VTT_FOLDER_PATH):
        print(f"错误：输入文件夹路径不存在 -> {VTT_FOLDER_PATH}")
        return
    if not os.path.isdir(OUTPUT_FOLDER_PATH):
        try:
            os.makedirs(OUTPUT_FOLDER_PATH)
            print(f"已自动创建输出文件夹: {OUTPUT_FOLDER_PATH}")
        except OSError as e:
            print(f"错误：无法创建输出文件夹 {OUTPUT_FOLDER_PATH}。错误信息: {e}")
            return
    tokenizer = get_tokenizer()
    for filename in sorted(os.listdir(VTT_FOLDER_PATH)):
        if filename.lower().endswith(".vtt"):
            vtt_file_path = os.path.join(VTT_FOLDER_PATH, filename)
            process_single_file(vtt_file_path, tokenizer)

if __name__ == '__main__':
    main()
`````

如果因为一些原因（电脑性能不行，或者嫌麻烦，或者用着很卡很慢）不想使用本地大模型，可以使用api key。下面是使用api key来对vtt字幕文件进行翻译润色的python代码，要注意把其中的api key换成自己的key，大部分api key都会收费，比如你使用deepseek的api key，就需要收费。但是也有一些api key会有每日的免费额度，比如gemini，比如qwen。
你需要设置这几个值：1. api key 2. url 3. MODEL_NAME
这些信息一般都会在官方页面找到
代码`call_api_key_translate_vtt_to_md.py`

`````python
import os
import requests
import json
import webvtt
import tiktoken
import time
import re

# --- 1. 配置区 ---

VTT_FOLDER_PATH = r'C:\Users\wwd_m\Downloads\test-vtt'
OUTPUT_FOLDER_PATH = r'C:\Users\wwd_m\Downloads\output-vtt-md'

# --- 【请在这里修改为您的API配置】 ---

# 1. API URL (请根据您使用的服务商取消注释并使用)
# OpenAI (GPT系列)
# API_URL = 'https://api.openai.com/v1/chat/completions'
# DeepSeek (与OpenAI格式兼容)
# API_URL = 'https://api.deepseek.com/chat/completions'
# Google (Gemini系列) - 注意：URL中需要包含模型名称和 :generateContent
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'


# 2. API KEY
# 【重要】请将 "..." 替换为您的真实 API Key
API_KEY = '' # 替换为您的 Gemini API Key

# 3. 模型名称 (Model Name)
# OpenAI Models
# MODEL_NAME = 'gpt-4o'
# DeepSeek Models
# MODEL_NAME = 'deepseek-chat'
# Google Gemini Models - 在Gemini中，此变量仅作参考，实际模型在URL中指定
MODEL_NAME = 'gemini-2.0-flash' 

# --- 【API配置结束】 ---

MAX_TOKENS_PER_CHUNK = 16000 

SYSTEM_PROMPT = """
你是一位顶级的翻译家和内容编辑。
你的任务是：将用户提供的英文视频口播稿，完整地翻译成一篇流畅、自然、连贯的简体中文文章。

请严格遵守以下核心原则：
1. **全文翻译与合并**：
   - 必须逐句翻译所有内容，不能省略或总结。
   - **关键指令**：请智能地将原文中语义连贯的多行短句，合并成符合中文阅读习惯的自然段落。不要原文每行都换行。

2. **保持逻辑**：在合并段落时，要尊重原文的逻辑停顿。如果原文有明显的空行或意群转换，可以在译文中也进行分段。

3. **Markdown输出**：使用 Markdown 格式，可以对关键词进行 **加粗** 以提高可读性。

4. **直接输出文章**：请直接开始输出最终翻译好的中文文章，不要包含任何解释或类似 <think> 的标签。
"""

# --- 2. 核心功能区 (其余函数不变) ---

def get_tokenizer():
    try:
        return tiktoken.get_encoding("cl100k_base")
    except Exception as e:
        print(f"获取 tokenizer 失败: {e}")
        return None

def parse_vtt_file(file_path):
    try:
        captions = webvtt.read(file_path)
        full_text = "\n".join([caption.text.strip() for caption in captions])
        return full_text
    except Exception as e:
        print(f"解析VTT文件 {os.path.basename(file_path)} 时出错: {e}")
        return None

def split_text_into_chunks(text, tokenizer):
    if not tokenizer:
        print("Tokenizer 不可用，无法进行分片。将尝试一次性处理。")
        return [text]
    tokens = tokenizer.encode(text)
    if len(tokens) <= MAX_TOKENS_PER_CHUNK:
        print(f"文本长度为 {len(tokens)} tokens，小于阈值 {MAX_TOKENS_PER_CHUNK}，将一次性处理。")
        return [text]
    print(f"文本过长 ({len(tokens)} tokens)，正在分片处理...")
    chunks = []
    current_chunk_tokens = []
    paragraphs = text.split('\n')
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
        paragraph_tokens = tokenizer.encode(paragraph + "\n")
        if len(current_chunk_tokens) + len(paragraph_tokens) > MAX_TOKENS_PER_CHUNK:
            if current_chunk_tokens:
                chunks.append(tokenizer.decode(current_chunk_tokens))
                current_chunk_tokens = []
        current_chunk_tokens.extend(paragraph_tokens)
    if current_chunk_tokens:
        chunks.append(tokenizer.decode(current_chunk_tokens))
    print(f"文本成功被分成了 {len(chunks)} 个片段。")
    return chunks

def clean_model_output(raw_text):
    cleaned_text = re.sub(r'^\s*<think>.*?</think>\s*', '', raw_text, flags=re.DOTALL)
    return cleaned_text

# --- 【重大修改】支持多服务商API的函数 ---
def process_chunk_with_llm(text_chunk):
    headers = {"Content-Type": "application/json"}
    payload = {}
    url = API_URL
    
    # --- 根据API_URL判断是哪个服务商 ---
    
    # 1. 如果是 Google Gemini API
    if "generativelanguage.googleapis.com" in API_URL:
        # Gemini 的 URL 需要拼接 API Key
        url = f"{API_URL}?key={API_KEY}"
        # Gemini 的 Payload 结构
        # 注意: Gemini 没有明确的 "system" role, 通常将系统指令作为对话的第一个 "user" message
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
                {"role": "model", "parts": [{"text": "好的，我明白了。请给我需要翻译的英文口播稿。"}]}, # 模拟一个对话轮次，让模型进入角色
                {"role": "user", "parts": [{"text": text_chunk}]}
            ]
        }
        
    # 2. 如果是 OpenAI 或 兼容OpenAI 的 API (如 DeepSeek)
    else:
        # OpenAI 的认证信息在请求头
        headers["Authorization"] = f"Bearer {API_KEY}"
        # OpenAI 的 Payload 结构
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text_chunk}
            ],
            "temperature": 0.7,
            "stream": False
        }

    # --- 发送请求并处理响应 ---
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=300)
        response.raise_for_status()
        response_json = response.json()
        
        raw_output_text = ""
        # 根据不同服务商的响应格式提取内容
        if "generativelanguage.googleapis.com" in API_URL:
            # Gemini 的响应路径
            raw_output_text = response_json['candidates'][0]['content']['parts'][0]['text']
        else:
            # OpenAI 的响应路径
            raw_output_text = response_json['choices'][0]['message']['content']
            
        cleaned_output_text = clean_model_output(raw_output_text)
        return cleaned_output_text
        
    except requests.exceptions.Timeout:
        print(f"调用API时超时！(超过300秒)")
        return None
    except requests.exceptions.RequestException as e:
        error_message = f"调用API时出错: {e}"
        if e.response is not None:
            error_message += f"\n服务器响应状态码: {e.response.status_code}"
            try:
                error_message += f"\n服务器响应内容: {e.response.text}"
            except Exception:
                error_message += "\n(无法解析服务器响应内容)"
        print(error_message)
        return None

def process_single_file(vtt_file_path, tokenizer):
    filename = os.path.basename(vtt_file_path)
    print(f"\n--- 正在处理文件: {filename} ---")
    
    english_text = parse_vtt_file(vtt_file_path)
    if not english_text:
        return

    chunks = split_text_into_chunks(english_text, tokenizer)
    
    processed_chunks = []
    for i, chunk in enumerate(chunks):
        if len(chunks) > 1:
            print(f"正在翻译片段 {i+1}/{len(chunks)}...")
        
        translated_chunk = process_chunk_with_llm(chunk)
        if not translated_chunk:
            print(f"翻译失败，已跳过整个文件 {filename}。")
            return
        processed_chunks.append(translated_chunk)
        if len(chunks) > 1:
            time.sleep(1)
        
    final_text = "\n\n".join(processed_chunks)
    output_filename = f"{os.path.splitext(filename)[0]}.md"
    output_file_path = os.path.join(OUTPUT_FOLDER_PATH, output_filename)
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(final_text.strip())
        print(f"处理完成！翻译稿已保存至: {output_file_path}\n" + "-"*40)
    except IOError as e:
        print(f"保存文件 {output_filename} 时出错: {e}")

# --- 3. 主程序入口 ---
def main():
    if not API_KEY or API_KEY == '...':
        print("错误：请在代码的配置区填写您的 API_KEY。")
        return
        
    if not os.path.isdir(VTT_FOLDER_PATH):
        print(f"错误：输入文件夹路径不存在 -> {VTT_FOLDER_PATH}")
        return
    if not os.path.isdir(OUTPUT_FOLDER_PATH):
        try:
            os.makedirs(OUTPUT_FOLDER_PATH)
            print(f"已自动创建输出文件夹: {OUTPUT_FOLDER_PATH}")
        except OSError as e:
            print(f"错误：无法创建输出文件夹 {OUTPUT_FOLDER_PATH}。错误信息: {e}")
            return
            
    tokenizer = get_tokenizer()
    for filename in sorted(os.listdir(VTT_FOLDER_PATH)):
        if filename.lower().endswith(".vtt"):
            vtt_file_path = os.path.join(VTT_FOLDER_PATH, filename)
            process_single_file(vtt_file_path, tokenizer)

if __name__ == '__main__':
    main()
`````

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
