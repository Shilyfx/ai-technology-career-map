---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian彩虹文件夹-边框版 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-rainbow-folder-border/"
source_url: "https://jasonai.me/download/Obsidian彩虹文件夹-边框版.md"
published: 2025-07-11
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

### 使用方法：
新建一个css文件，比如rainbow.css，用记事本打开，然后将下面的css代码，复制到这个文件中并保存。
将css文件放到你的obsidian库的这个文件夹下：.obsidian\snippets

然后在设置 - 外观中，滚动条拉到最底下有一个CSS代码片段，点击刷新按钮，然后把这个css文件的开关打开即可。

`````css
@charset "UTF-8";
/* @settings
name: 【杰森的效率工坊】文件夹多彩边框
id: folder-color-border-icon-style
settings:
    - 
        id: folder-color-scheme-class
        title: 配色方案
        description: "为文件夹边框、文字和图标选择一套循环配色方案。"
        type: class-select
        allowEmpty: false
        default: folder-scheme-neon-jewel
        options:
            - 
                label: 霓虹宝石 (Neon Jewel)
                value: folder-scheme-neon-jewel
            - 
                label: 北境极光 (Nord Aurora)
                value: folder-scheme-nord-aurora
            - 
                label: 秋日森语 (Autumn Forest)
                value: folder-scheme-autumn-forest
            - 
                label: 深海远山 (Deep Ocean)
                value: folder-scheme-deep-ocean
            - 
                label: 蔷薇之梦 (Rose Dream)
                value: folder-scheme-rose-dream
*/

/* --- 1. 配色方案定义区 --- */
/* Style Settings 插件会根据你的选择，应用下面的其中一个类来定义颜色 */

/* 方案一：霓虹宝石 (Neon Jewel) - 默认 */
.folder-scheme-neon-jewel {
    --folder-color-1: #6ab5d6;
    /* Sky Blue */
    --folder-color-2: #d6a760;
    /* Vibrant Yellow */
    --folder-color-3: #b569d6;
    /* Lilac Purple */
    --folder-color-4: #d66087;
    /* Coral Pink */
    --folder-color-5: #55c4a7;
    /* Mint Green */
    --folder-color-6: #6086d6;
    /* Jewel Blue */
}

/* 方案二：北境极光 (Nord Aurora) */
.folder-scheme-nord-aurora {
    --folder-color-1: #d08770;
    --folder-color-2: #ebcb8b;
    --folder-color-3: #a3be8c;
    --folder-color-4: #88c0d0;
    --folder-color-5: #81a1c1;
    --folder-color-6: #b48ead;
}

/* 方案三：秋日森语 (Autumn Forest) */
.folder-scheme-autumn-forest {
    --folder-color-1: #b06a4b;
    /* Terracotta */
    --folder-color-2: #c89258;
    /* Mustard */
    --folder-color-3: #6f7c3f;
    /* Olive Green */
    --folder-color-4: #a47c48;
    /* Oak */
    --folder-color-5: #8c5a47;
    /* Russet */
    --folder-color-6: #5e6145;
    /* Forest Green */
}

/* 方案四：深海远山 (Deep Ocean) */
.folder-scheme-deep-ocean {
    --folder-color-1: #526D82;
    --folder-color-2: #738a9a;
    --folder-color-3: #9DB2BF;
    --folder-color-4: #b8c4ce;
    --folder-color-5: #7c909e;
    --folder-color-6: #5e7686;
}

/* 方案五：蔷薇之梦 (Rose Dream) */
.folder-scheme-rose-dream {
    --folder-color-1: #f6c8d7;
    --folder-color-2: #e8b3c5;
    --folder-color-3: #d89eb6;
    --folder-color-4: #c68ba8;
    --folder-color-5: #b27a97;
    --folder-color-6: #d4a7c0;
}


/* --- 2. 核心样式逻辑 (无需修改) --- */

/* 为顶级文件夹标题设置相对定位，作为伪元素的锚点 */
.nav-files-container>div>.tree-item.nav-folder>.nav-folder-title {
    position: relative;
    margin-bottom: 4px;
}

/* 使用 ::before 伪元素创建背景/边框盒子 */
.nav-files-container>div>.tree-item.nav-folder>.nav-folder-title::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-style: solid;
    border-width: 1px 1px 1px 3px;
    border-radius: 5px;
    z-index: -1;
    /* 将伪元素置于实际内容之后 */
}


/* --- 3. 循环应用颜色到边框、文字和图标 (无需修改) --- */

/* 第1个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 1)>.nav-folder-title::before {
    border-color: var(--folder-color-1);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 1)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-1);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 1)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-1);
}

/* 第2个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 2)>.nav-folder-title::before {
    border-color: var(--folder-color-2);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 2)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-2);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 2)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-2);
}

/* 第3个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 3)>.nav-folder-title::before {
    border-color: var(--folder-color-3);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 3)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-3);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 3)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-3);
}

/* 第4个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 4)>.nav-folder-title::before {
    border-color: var(--folder-color-4);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 4)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-4);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 4)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-4);
}

/* 第5个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 5)>.nav-folder-title::before {
    border-color: var(--folder-color-5);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 5)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-5);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 5)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-5);
}

/* 第6个文件夹 */
.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 6)>.nav-folder-title::before {
    border-color: var(--folder-color-6);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 6)>.nav-folder-title .nav-folder-title-content {
    color: var(--folder-color-6);
}

.nav-files-container>div>.tree-item.nav-folder:nth-child(6n + 6)>.nav-folder-title .iconize-icon svg {
    stroke: var(--folder-color-6);
}

`````


### 如何自己改变配色：

目前提供了几种配色方案，在Style Settings插件中，可以自行选择：

### 如果想自己选择其他颜色搭配，可以直接改变现有颜色里的值，也就是#xxxxxx的值，可以搜索【RGB颜色表】来选择配色，也可以搜索【高级感颜色搭配】这种关键词，来选择喜欢的颜色搭配。

目前是使用6系配色，也就是6个颜色。

颜色命名要严格遵循从1到6。—folder-color-**1**

**如果颜色数量有变化，比如7个颜色，5个颜色，那么命名就是从1到5，或者从1到7。**

同时，下面的公式（n+几的那部分）也要更改：

如果是5，则是5n+2一直到5n+6。

如果是7，则是7n+2一直到7n+8。

也就是说：Xn+Y的这个公式中，

X：就是你颜色的总数。 Y：这是起始位置的偏移量。由于你的文件夹列表是从第2个元素开始的，所以第一个颜色的 Y 总是 2，第二个颜色是 3，以此类推。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
