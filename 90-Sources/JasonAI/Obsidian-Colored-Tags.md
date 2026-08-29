---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian美化！让你拥有像Notion一样的彩色标签列表 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-colored-tags-like-notion/"
source_url: "https://jasonai.me/download/Obsidian美化-让你拥有像Notion一样的彩色标签列表.md"
published: 2025-07-23
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
---

### 使用方法：
新建一个css文件，比如metadata.css，用记事本打开，然后将下面的css代码，复制到这个文件中并保存。
将css文件放到你的obsidian库的这个文件夹下：.obsidian\snippets

然后在设置 - 外观中，滚动条拉到最底下有一个CSS代码片段，点击刷新按钮，然后把这个css文件的开关打开即可。

如果想自定义颜色，打开这个css文件，然后更改这个文件开头的颜色定义即可，（只更改十六进制颜色的值）

`````css
@charset "UTF-8";
/* 
  优化版：Obsidian Metadata 多彩标签样式
  - 只需修改下面的 --pill-bg-N 和 --pill-hover-N 变量即可定制你的调色板。
*/

/* 在所有非tags的metadata属性上统一定义颜色变量 */
.metadata-property:not([data-property-key="tags"]) {
    /* --- 色板3: 大地色系 / Earth Tones --- */
    /* AA=33 表示20%透明度, AA=40 表示25%透明度 */
    --pill-bg-1: #a98c7833; --pill-hover-1: #a98c7840; /* Clay Brown */
    --pill-bg-2: #d8c3a533; --pill-hover-2: #d8c3a540; /* Almond */
    --pill-bg-3: #8e8d8a33; --pill-hover-3: #8e8d8a40; /* Stone Grey */
    --pill-bg-4: #e9807433; --pill-hover-4: #e9807440; /* Terracotta */
    --pill-bg-5: #e85a4f33; --pill-hover-5: #e85a4f40; /* Rust Red */
    --pill-bg-6: #d8ae4733; --pill-hover-6: #d8ae4740; /* Ochre */
    --pill-bg-7: #a49e8d33; --pill-hover-7: #a49e8d40; /* Khaki Grey */
    --pill-bg-8: #e6b47c33; --pill-hover-8: #e6b47c40; /* Sandy Brown */
}

/* 基础样式：确保内边距和背景填充正确 */
.metadata-property:not([data-property-key="tags"]) .multi-select-pill {
    --pill-padding-x: var(--tag-padding-x);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill::after {
    width: 100% !important;
    left: 0 !important;
}

/* 颜色循环：现在只需引用变量，代码非常整洁 */
.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+1) {
    --pill-background: var(--pill-bg-1);
    --pill-background-hover: var(--pill-hover-1);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+2) {
    --pill-background: var(--pill-bg-2);
    --pill-background-hover: var(--pill-hover-2);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+3) {
    --pill-background: var(--pill-bg-3);
    --pill-background-hover: var(--pill-hover-3);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+4) {
    --pill-background: var(--pill-bg-4);
    --pill-background-hover: var(--pill-hover-4);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+5) {
    --pill-background: var(--pill-bg-5);
    --pill-background-hover: var(--pill-hover-5);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+6) {
    --pill-background: var(--pill-bg-6);
    --pill-background-hover: var(--pill-hover-6);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+7) {
    --pill-background: var(--pill-bg-7);
    --pill-background-hover: var(--pill-hover-7);
}

.metadata-property:not([data-property-key="tags"]) .multi-select-pill:nth-child(8n+8) {
    --pill-background: var(--pill-bg-8);
    --pill-background-hover: var(--pill-hover-8);
}

`````

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
