---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian 教程：3种方法实现习惯打卡热力图 (Tracker/Heatmap Calendar/DataviewJS) | 视觉化你的自律与进步 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-habit-heatmap-tutorial/"
source_url: "https://jasonai.me/download/Obsidian-教程-3种方法实现习惯打卡热力图-Tracker-Heatmap-Calendar-DataviewJS-视觉化你的自律与进步.md"
published: 2025-07-16
retrieved: 2026-08-29
created: 2026-08-29
updated: 2026-08-29
review_after: 2027-02-25
related:
  - "[[JasonAI-Source-Index]]"
---

### Heatmap-Dataviewjs

```
// --- 配置项 ---
// 1. 请将 "notes/diary" 替换为你的日记文件夹路径
const DIARY_FOLDER = "diary";

// 2. 请将 "阅读" 替换为你想要追踪的任务关键词
const TASK_TO_TRACK = "fitness";

// 3. 指定要显示的月份，格式为 "YYYY-MM"
const HEATMAP_MONTH = "2025-07"; 
// --- 配置结束 ---


```

```dataviewjs
// --- 配置项 ---

// 1. 文件夹路径
const DIARY_FOLDER = "diary";

// 2. 追踪的任务关键词
const TASK_TO_TRACK = "fitness";

// 3. 显示的月份
const HEATMAP_MONTH = "2025-07"; 

// 4. 颜色配置 (您可以随意修改这里的颜色代码！)
const COMPLETED_COLOR = "#006d77";    // 已完成任务的颜色 (推荐: #216e39, #006d77)
const INCOMPLETE_COLOR = "#e2f0f1";  // 未完成任务的颜色 (推荐: #d6e6d7, #e2f0f1)
const TEXT_COLOR_DARK_BG = "#ffffff"; // 深色背景上的文字颜色 (通常是白色)
const TEXT_COLOR_LIGHT_BG = "#000000"; // 浅色背景上的文字颜色 (通常是黑色)

// --- 配置结束 ---


const targetMoment = moment(HEATMAP_MONTH, "YYYY-MM");

if (!targetMoment.isValid()) {
    dv.el("p", `❌ **错误:** 无效的月份格式。`);
} else {
    // --- 1. 数据准备 ---
    const targetYear = targetMoment.year();
    const targetMonth = targetMoment.month();
    const taskCompletionData = new Map();
    const pages = dv.pages(`"${DIARY_FOLDER}"`).where(p => p.file.day);
    const processedTaskQuery = TASK_TO_TRACK.trim().toLowerCase();

    for (const page of pages) {
        const pageMoment = moment(page.file.day.toJSDate());
        if (pageMoment.year() !== targetYear || pageMoment.month() !== targetMonth) continue;
        
        const tasks = page.file.tasks;
        const specificTask = tasks.find(t => t.text.trim().toLowerCase().includes(processedTaskQuery));

        if (specificTask) {
            taskCompletionData.set(page.file.day.day, specificTask.completed);
        }
    }

    // --- 2. 样式定义 (只保留布局) ---
    dv.el("style", `
    .heatmap-calendar-container { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; width: 100%; max-width: 350px; margin: 0 auto; }
    .heatmap-calendar-grid { border-collapse: collapse; width: 100%; }
    .heatmap-calendar-grid th, .heatmap-calendar-grid td { text-align: center; padding: 0; width: 14.28%; height: 40px; line-height: 40px; font-size: 12px; }
    .heatmap-calendar-grid th { font-weight: bold; color: var(--text-muted); }
    .day-cell { border: 2px solid var(--background-primary); border-radius: 8px; background-color: var(--background-secondary); color: var(--text-normal); }
    .day-cell.empty { background-color: transparent; border: none; }
    `);

    // --- 3. 绘制日历 ---
    const daysInMonth = targetMoment.daysInMonth();
    const firstDayOfMonth = targetMoment.clone().startOf('month').day();
    
    let calendarHtml = `<div class="heatmap-calendar-container">`;
    calendarHtml += `<h2>${targetMoment.format("YYYY 年 MMMM")}</h2>`;
    calendarHtml += `<table class="heatmap-calendar-grid">`;
    calendarHtml += `<thead><tr><th>日</th><th>一</th><th>二</th><th>三</th><th>四</th><th>五</th><th>六</th></tr></thead>`;
    calendarHtml += `<tbody><tr>`;

    for (let i = 0; i < firstDayOfMonth; i++) { calendarHtml += `<td class="day-cell empty"></td>`; }

    for (let day = 1; day <= daysInMonth; day++) {
        const currentDayOfWeek = (firstDayOfMonth + day - 1) % 7;
        if (currentDayOfWeek === 0 && day !== 1) { calendarHtml += `</tr><tr>`; }

        const status = taskCompletionData.get(day);
        let styleString = ""; 

        if (status === true) {
            styleString = `style="background-color: ${COMPLETED_COLOR}; color: ${TEXT_COLOR_DARK_BG}; font-weight: bold;"`;
        } else if (status === false) {
            styleString = `style="background-color: ${INCOMPLETE_COLOR}; color: ${TEXT_COLOR_LIGHT_BG};"`;
        }
        
        calendarHtml += `<td class="day-cell" ${styleString}>${day}</td>`;
    }

    let lastDayOfWeek = (firstDayOfMonth + daysInMonth - 1) % 7;
    while (lastDayOfWeek < 6) { calendarHtml += `<td class="day-cell empty"></td>`; lastDayOfWeek++; }

    calendarHtml += `</tr></tbody></table></div>`;
    dv.el("div", calendarHtml, { raw: true });
}
```

### HeatMap-Canlendar


#### 代码


```dataviewjs
// --- 配置区 ---
// 1. 请在这里修改您的日记文件夹名称
const DIARY_FOLDER = 'diary';

// 2. 定义所有你想追踪的习惯，以及它们的配置
const habitsToTrack = {
    "fitness":    { color: "orange", icon: "🏋️" },
    "reading":    { color: "blue",   icon: "📚" },
    "meditation": { color: "purple", icon: "🧘" } 
};

// --- 代码开始 ---

if (typeof renderHeatmapCalendar !== 'function') {
    dv.el("div", "❌ **错误：** 找不到 `renderHeatmapCalendar` 函数。");
} else {
    for (const habitName in habitsToTrack) {
        const config = habitsToTrack[habitName];
        
        dv.header(3, `${config.icon} ${habitName.charAt(0).toUpperCase() + habitName.slice(1)}`);
        
        const entries = [];
        for (const page of dv.pages(`"${DIARY_FOLDER}" and #daily-note`)) {
            if (page.file.day && page.file.tasks.some(t => t.completed && t.text.toLowerCase().trim() === habitName)) {
                entries.push({
                    date: page.file.day.toISODate(),
                    intensity: 1,
                    color: config.color,
                });
            }
        }

        // 【调色板】在这里定义或修改您的颜色主题
        const calendarData = {
            colors: {
                blue:   ["#8cb9ff", "#69a3ff", "#428bff", "#1872ff", "#0058e2"],
                orange: ["#ffa244", "#fd7f00", "#dd6f00", "#bf6000", "#9b4e00"],
                pink:   ["#ff96cb", "#ff70b8", "#ff3a9d", "#ee0077", "#c30062"],
                purple: ["#d8b4fe", "#c084fc", "#a855f7", "#9333ea", "#7e22ce"],
            },
            entries: entries,
        };
        
        const container = dv.el("div", "");
        renderHeatmapCalendar(container, calendarData);
    }
}
```



```dataviewjs
// --- 喝水热力图 ---

// --- 配置区 ---
// 1. 请在这里修改您的日记文件夹名称
const DIARY_FOLDER = 'diary';

// 2. 您想追踪的行内字段的名称
const FIELD_NAME = "喝水";

// 3. 为这个热力图选择一个颜色主题
const COLOR_THEME = "red";

// --- 代码开始 ---

dv.header(3, `💧 ${FIELD_NAME}热力图`);

// 步骤 1: 检查核心函数是否存在
if (typeof renderHeatmapCalendar !== 'function') {
    dv.el("div", "❌ **错误：** 找不到 `renderHeatmapCalendar` 函数。请确保 Heatmap Calendar 插件已启用并刷新 Obsidian (Ctrl/Cmd + R)。", {
        attr: { style: "background-color: var(--background-secondary); border-left: 4px solid var(--color-red); padding: 12px;" }
    });
} else {
    // 步骤 2: 使用同步循环来安全地构建数据
    const entries = [];
    // 使用精确查询（文件夹+标签）
    for (const page of dv.pages(`"${DIARY_FOLDER}" and #daily-note`)) {
        // 检查页面是否同时拥有：有效的文件名日期 和 我们要追踪的字段
        if (page.file.day && page[FIELD_NAME]) {
            entries.push({
                // 从文件名获取正确日期
                date: page.file.day.toISODate(),
                // 【关键】将字段的数值赋值给 intensity
                intensity: page[FIELD_NAME],
                // 使用配置中定义的颜色主题
                color: COLOR_THEME,
            });
        }
    }

    // 步骤 3: 准备最终的日历数据
    const calendarData = {
        colors: {
            blue:   ["#8cb9ff", "#69a3ff", "#428bff", "#1872ff", "#0058e2"],
            green:  ["#c6e48b", "#7bc96f", "#49af5d", "#2e8840", "#196127"],
            red:    ["#ff9e82", "#ff7b55", "#ff4d1a", "#e73400", "#bd2a00"],
            orange: ["#ffa244", "#fd7f00", "#dd6f00", "#bf6000", "#9b4e00"],
            pink:   ["#ff96cb", "#ff70b8", "#ff3a9d", "#ee0077", "#c30062"],
        },
        entries: entries,
    };
    
    // 步骤 4: 渲染日历
    const container = dv.el("div", "");
    renderHeatmapCalendar(container, calendarData);
    
    dv.paragraph(`*图表已生成。共找到了 ${entries.length} 条 "${FIELD_NAME}" 记录。*`);
}
```

### HeatMap-Tracker



```tracker
searchType: task.done
searchTarget: fitness
datasetName: "健身"
folder: diary
endDate: 2025-07-31
month:
```

```tracker
searchType: task.done
searchTarget: reading
datasetName: "阅读"
folder: diary
endDate: 2025-07-31
month:
```

```tracker
searchType: task.done
searchTarget: meditation
datasetName: "冥想"
folder: diary
endDate: 2025-07-31
month:
	color: "#e06c75"
```

### Heatmap-Calendar-AllYear


```dataviewjs
// --- 全年模拟数据热力图 (精简与美化版) ---

// 步骤 1: 检查核心函数是否存在
if (typeof renderHeatmapCalendar !== 'function') {
    dv.el("div", "❌ **错误：** 找不到 `renderHeatmapCalendar` 函数。");
} else {

    // ====================================================================
    // 步骤 2: 定义一个函数，用于生成一整年的随机数据
    // ====================================================================
    /**
     * @param {number} year - 要生成的年份, 例如 2024
     * @param {string} color - 该数据集要使用的主题颜色名
     * @param {number} probability - 每一天有数据的概率 (0.0 to 1.0)
     * @param {number} minIntensity - 随机强度的最小值
     * @param {number} maxIntensity - 随机强度的最大值
     * @returns {Array} - 返回一个包含全年随机数据的 entries 数组
     */
    function generateFakeYearData(year, color, probability, minIntensity, maxIntensity) {
        const entries = [];
        let currentDate = dv.luxon.DateTime.fromObject({ year: year, month: 1, day: 1 });

        while (currentDate.year === year) {
            if (Math.random() < probability) {
                const randomIntensity = Math.floor(Math.random() * (maxIntensity - minIntensity + 1)) + minIntensity;
                entries.push({
                    date: currentDate.toISODate(),
                    intensity: randomIntensity,
                    color: color,
                });
            }
            currentDate = currentDate.plus({ days: 1 });
        }
        return entries;
    }

    // ====================================================================
    // 步骤 3: 配置您想要生成的热力图
    // ====================================================================
    const heatmapsToGenerate = [
        {
            name: "项目A贡献",
            color: "green",
            probability: 0.6,
            minIntensity: 1,
            maxIntensity: 10,
        },
        {
            name: "精力水平",
            color: "teal", // <--- 已替换为更高级的青色系
            probability: 0.8,
            minIntensity: 1,
            maxIntensity: 5,
        },
        {
            name: "学习时长(小时)",
            color: "amber", // <--- 已替换为更高级的琥珀色系
            probability: 0.5,
            minIntensity: 1,
            maxIntensity: 4,
        }
    ];

    // ====================================================================
    // 步骤 4: 循环遍历配置，生成并渲染每一个热力图
    // ====================================================================
    const currentYear = new Date().getFullYear();

    for (const config of heatmapsToGenerate) {
        // 【已修改】删除了 Emoji
        dv.header(3, config.name);

        const fakeEntries = generateFakeYearData(
            currentYear,
            config.color,
            config.probability,
            config.minIntensity,
            config.maxIntensity
        );

        // 【已修改】在调色板中加入了新的颜色主题
        const calendarData = {
            year: currentYear,
            colors: {
                green:  ["#c6e48b", "#7bc96f", "#49af5d", "#2e8840", "#196127"],
                // 新增：专业且冷静的青色系
                teal:   ["#99f6e4", "#5eead4", "#2dd4bf", "#14b8a6", "#0f766e"],
                // 新增：温暖且沉稳的琥珀色系
                amber:  ["#fde68a", "#fcd34d", "#fbbf24", "#f59e0b", "#d97706"],
            },
            entries: fakeEntries,
        };
        
        const container = dv.el("div", "");
        renderHeatmapCalendar(container, calendarData);

        // 【已修改】删除了末尾的统计文字
    }
}
```

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
