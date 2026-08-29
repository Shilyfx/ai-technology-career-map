---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian美化：像Notion一样拥有动态小组件 (时间/电量/日历) | 插件+DataviewJS两种方法 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-widgets-time-battery-calendar/"
source_url: "https://jasonai.me/download/Obsidian美化-像Notion一样拥有动态小组件-时间-电量-日历-插件-DataviewJS两种方法.md"
published: 2025-07-13
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

### Dataview时间进度条

#### 样例代码：

```dataviewjs
// --- 最终版代码 ---

const { DateTime } = dv.luxon;

const now = DateTime.now();
const startOfDay = now.startOf('day');
const passedMinutesInDay = now.diff(startOfDay, 'minutes').minutes;
const dayPercent = (passedMinutesInDay / (24 * 60)) * 100;

const startOfWeek = now.startOf('week');
const passedHoursInWeek = now.diff(startOfWeek, 'hours').hours;
const weekPercent = (passedHoursInWeek / (7 * 24)) * 100;

const monthPercent = (now.day / now.daysInMonth) * 100;

const passedDaysInYear = now.ordinal;
const totalDaysInYear = now.isInLeapYear ? 366 : 365;
const yearPercent = (passedDaysInYear / totalDaysInYear) * 100;

const progressBars = [
    { label: "今日进度", value: passedMinutesInDay, max: 24 * 60, percent: dayPercent },
    { label: "本周进度", value: passedHoursInWeek, max: 7 * 24, percent: weekPercent },
    { label: "本月进度", value: now.day, max: now.daysInMonth, percent: monthPercent },
    { label: "本年进度", value: passedDaysInYear, max: totalDaysInYear, percent: yearPercent }
];

function createProgressBar(data) {
    const container = dv.el("div", "");
    container.style.display = "flex";
    container.style.alignItems = "center";
    container.style.marginBottom = "8px";

    const label = dv.el("span", `${data.label}：`);
    label.style.minWidth = "75px";
    label.style.flexShrink = "0";

    const progress = dv.el("progress", "");
    progress.setAttribute("value", data.value);
    progress.setAttribute("max", data.max);
    progress.style.flexGrow = "1";
    progress.style.width = "100%";
    progress.style.height = "14px";

    const percentage = dv.el("span", ` ${data.percent.toFixed(2)}%`);
    percentage.style.marginLeft = "10px";

    container.append(label, progress, percentage);
    dv.paragraph(container);
}

progressBars.forEach(bar => createProgressBar(bar));
```


### Dataview年倒计时

#### 样例代码：

```dataviewjs
const year = dv.current().year || new Date().getFullYear();

let rawCssClasses = dv.current().cssclasses;
let classesArray = [];

if (rawCssClasses) {
    if (Array.isArray(rawCssClasses)) {
        classesArray = rawCssClasses;
    } else {
        classesArray = [String(rawCssClasses)];
    }
}

// --- End of Enhanced Code ---

const titleAlignClass = classesArray.find(c => c.startsWith("align-")) ?? "align-left";

// 使用 div 显示为块级元素，字体大小和颜色由配套CSS控制
dv.el("div", `${year} 年倒计时`, { cls: `year-title ${titleAlignClass}` });


const startDate = moment(`${year}-01-01`);
const endDate = moment(`${year}-12-31`);
const today = moment();


const container = dv.el("div", "", { cls: "year-calendar" });


for (let d = startDate.clone(); d.isSameOrBefore(endDate); d.add(1, "day")) {
    const dayBox = document.createElement("div");
    dayBox.classList.add("day-box");
    dayBox.setAttribute("title", d.format("YYYY-MM-DD"));


    if (d.isBefore(today, 'day')) {
        dayBox.classList.add("past");
    } else if (d.isSame(today, 'day')) {
        dayBox.classList.add("today");
    } else {
        dayBox.classList.add("future");
    }


    container.appendChild(dayBox);
}
```

#### CSS代码（添加到.obsidian/snippets文件夹下）：

```css
.year-title {
    margin-bottom: 0.5em;
    font-size: 1.2em;
    color: var(--text-muted);
}


.align-left .year-title {
    text-align: left;
}


.align-center .year-title {
    text-align: center;
}


.align-right .year-title {
    text-align: right;
}


.year-calendar {
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
    gap: 0.5px;
}


.day-box {
    width: 10px;
    height: 10px;
    border-radius: 1px;
    margin: 1px;
    background-color: white;
    transition: transform 0.2s;
}


.day-box.past {
    background-color: #3A353F;
}


.day-box.today {
    background-color: #A6D676;
}


.day-box.future {
    background-color: #EEE7DF;
    border: 0.5px solid #ddd;
}


.day-box:hover {
    transform: scale(1.4);
    cursor: pointer;
}


@media (max-width: 600px) {
    .year-calendar {
        justify-content: center;
        gap: 1px;
    }


    .day-box {
        width: 8px;
        height: 8px;
        margin: 0.5px;
    }
}
```


### Dataview彩色时钟

#### 样例代码

```dataviewjs
// --- 1. 使用 Dataview API 构建一个与原始文件完全相同的扁平化 HTML 结构 ---

// 创建最外层的容器
const clock = dv.container.createEl('div', { 
    cls: 'progress-clock', 
    attr: { id: 'clock' } 
});

// 定义一个对象来存放需要更新的元素引用
const elements = {};

// 将所有元素直接创建为 clock 的子元素
const dateButton = clock.createEl('button', { cls: 'progress-clock__time-date', attr: { 'data-group': 'd', type: 'button' } });
elements.week = dateButton.createEl('small', { attr: { 'data-unit': 'w' } });
dateButton.createEl('br');
elements.month = dateButton.createEl('span', { attr: { 'data-unit': 'mo' } });
elements.day = dateButton.createEl('span', { attr: { 'data-unit': 'd' } });

elements.hour = clock.createEl('button', { cls: 'progress-clock__time-digit', attr: { 'data-unit': 'h', 'data-group': 'h' } });
clock.createEl('span', { cls: 'progress-clock__time-colon', text: ':' });
elements.minute = clock.createEl('button', { cls: 'progress-clock__time-digit', attr: { 'data-unit': 'm', 'data-group': 'm' } });
clock.createEl('span', { cls: 'progress-clock__time-colon', text: ':' });
elements.second = clock.createEl('button', { cls: 'progress-clock__time-digit', attr: { 'data-unit': 's', 'data-group': 's' } });
elements.ampm = clock.createEl('span', { cls: 'progress-clock__time-ampm', attr: { 'data-unit': 'ap' } });

// SVG 仍然作为 clock 的直接子元素
const svgHTML = `
<svg class="progress-clock__rings" width="256" height="256" viewBox="0 0 256 256">
    <g data-units="d"><circle class="progress-clock__ring" cx="128" cy="128" r="74" fill="none" opacity="0.1" stroke="#e13e78" stroke-width="12"></circle><circle class="progress-clock__ring-fill" data-ring="mo" cx="128" cy="128" r="74" fill="none" stroke="#e13e78" stroke-width="12" stroke-dasharray="465 465" stroke-linecap="round" transform="rotate(-90,128,128)"></circle></g>
    <g data-units="h"><circle class="progress-clock__ring" cx="128" cy="128" r="90" fill="none" opacity="0.1" stroke="#e79742" stroke-width="12"></circle><circle class="progress-clock__ring-fill" data-ring="d" cx="128" cy="128" r="90" fill="none" stroke="#e79742" stroke-width="12" stroke-dasharray="565.5 565.5" stroke-linecap="round" transform="rotate(-90,128,128)"></circle></g>
    <g data-units="m"><circle class="progress-clock__ring" cx="128" cy="128" r="106" fill="none" opacity="0.1" stroke="#4483ec" stroke-width="12"></circle><circle class="progress-clock__ring-fill" data-ring="h" cx="128" cy="128" r="106" fill="none" stroke="#4483ec" stroke-width="12" stroke-dasharray="666 666" stroke-linecap="round" transform="rotate(-90,128,128)"></circle></g>
    <g data-units="s"><circle class="progress-clock__ring" cx="128" cy="128" r="122" fill="none" opacity="0.1" stroke="#8f30eb" stroke-width="12"></circle><circle class="progress-clock__ring-fill" data-ring="m" cx="128" cy="128" r="122" fill="none" stroke="#8f30eb" stroke-width="12" stroke-dasharray="766.5 766.5" stroke-linecap="round" transform="rotate(-90,128,128)"></circle></g>
</svg>
`;
clock.innerHTML += svgHTML;

const ringFills = {
    day: clock.querySelector('[data-ring="mo"]'),
    hour: clock.querySelector('[data-ring="d"]'),
    minute: clock.querySelector('[data-ring="h"]'),
    second: clock.querySelector('[data-ring="m"]'),
};

// --- 更新逻辑部分保持不变 ---
function updateClock() {
    moment.locale('zh-cn');
    const now = moment();
    const formatDate = now.format("dddd-MMMM-D-H-mm-ss-a").split("-");
    const [week, month, day, hour, minute, second, ampm] = formatDate;
    elements.week.textContent = week;
    elements.month.textContent = month;
    elements.day.textContent = day;
    elements.hour.textContent = hour;
    elements.minute.textContent = minute;
    elements.second.textContent = second;
    elements.ampm.textContent = ampm;
    const daysInMonth = now.daysInMonth(); 
    const secProgress = second / 60;
    const minProgress = (parseInt(minute) + secProgress) / 60;
    const hourProgress = (parseInt(hour) + minProgress) / 24;
    const dayProgress = (parseInt(day) - 1 + hourProgress) / daysInMonth;
    const circumferences = { day: 465, hour: 565.5, minute: 666, second: 766.5 };
    if (ringFills.second) ringFills.second.setAttribute('stroke-dashoffset', (1 - secProgress) * circumferences.second);
    if (ringFills.minute) ringFills.minute.setAttribute('stroke-dashoffset', (1 - minProgress) * circumferences.minute);
    if (ringFills.hour) ringFills.hour.setAttribute('stroke-dashoffset', (1 - hourProgress) * circumferences.hour);
    if (ringFills.day) ringFills.day.setAttribute('stroke-dashoffset', (1 - dayProgress) * circumferences.day);
}
updateClock();
const intervalId = window.setInterval(updateClock, 1000);
dv.container.onunload = () => { window.clearInterval(intervalId); }
```

#### CSS代码（添加到.obsidian/snippets文件夹下）：

```css
/*

  Colorful Clock CSS Snippet for Obsidian

  Version 2 - Corrected Selector

*/


/*

  我们直接选择 .progress-clock 类。

  这个类应该足够独特，不会与主题冲突。

  同时，我们使用 margin: auto 来将整个时钟在 Dataview 块中居中。

*/

.progress-clock {
    display: grid;
    justify-content: center;
    align-content: center;
    position: relative;
    text-align: center;
    height: 15em;
    width: 15em;
    margin: 2em auto;
}


/* --- 以下的规则保持不变，但现在会因为父级规则生效而正常工作 --- */


.progress-clock button {
    padding: 0;
    border: none;
    box-shadow: none;
    background-color: transparent;
    display: block;
    color: var(--text-normal);
}


.progress-clock button:hover {
    background-color: transparent;
}


.progress-clock__time-date,
.progress-clock__time-digit,
.progress-clock__time-colon,
.progress-clock__time-ampm {
    font: 1em/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    transition: color 0.2s linear;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
}


.progress-clock__time-date,
.progress-clock__time-digit {
    background: transparent;
}


.progress-clock__time-date,
.progress-clock__time-ampm {
    grid-column: 1 / 6;
}


.progress-clock__time-date {
    font-size: 0.75em;
    line-height: 1.33;
}


.progress-clock__time-digit,
.progress-clock__time-colon {
    font-size: 1.6em;
    font-weight: 400;
    grid-row: 2;
    margin: 0;
}


.progress-clock__time-colon {
    line-height: 1.5em;
}


.progress-clock__time-ampm {
    cursor: default;
    grid-row: 3;
}


.progress-clock__rings {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    opacity: 0.6;
}


.progress-clock__ring {
    opacity: 0.1;
}


.progress-clock__ring-fill {
    transition:
        opacity 0s 0.3s linear,
        stroke-dashoffset 0.3s ease-in-out;
}


[data-group]:focus {
    outline: transparent;
}


[data-units] {
    transition: opacity 0.2s linear;
}


[data-group="d"]:focus,
[data-group="d"]:hover {
    color: hsl(333,90%,55%);
}


[data-group="h"]:focus,
[data-group="h"]:hover {
    color: hsl(33,90%,55%);
}


[data-group="m"]:focus,
[data-group="m"]:hover {
    color: hsl(213,90%,55%);
}


[data-group="s"]:focus,
[data-group="s"]:hover {
    color: hsl(273,90%,55%);
}


[data-group]:focus ~ .progress-clock__rings [data-units],
[data-group]:hover ~ .progress-clock__rings [data-units] {
    opacity: 0.2;
}


[data-group="d"]:focus ~ .progress-clock__rings [data-units="d"],
[data-group="d"]:hover ~ .progress-clock__rings [data-units="d"],
[data-group="h"]:focus ~ .progress-clock__rings [data-units="h"],
[data-group="h"]:hover ~ .progress-clock__rings [data-units="h"],
[data-group="m"]:focus ~ .progress-clock__rings [data-units="m"],
[data-group="m"]:hover ~ .progress-clock__rings [data-units="m"],
[data-group="s"]:focus ~ .progress-clock__rings [data-units="s"],
[data-group="s"]:hover ~ .progress-clock__rings [data-units="s"] {
    opacity: 1;
}
```


### Obsidian电池电量

#### 样例代码

```dataviewjs
// --- 电池小组件 (DataviewJS 版) ---

// 1. 获取当前代码块的容器，我们将在这里渲染所有内容
const container = dv.container;
container.classList.add("battery-real-widget-container"); // 添加自定义CSS类

// 2. 检查浏览器是否支持电池API
if (!('getBattery' in navigator)) {
    container.setText("❌ 您的设备或浏览器不支持电池状态API。");
} else {
    // 3. 创建UI元素 (先创建骨架，再填充内容)
    const iconEl = dv.el("span", "", { cls: "battery-real-icon" });
    const textEl = dv.el("span", "", { cls: "battery-real-text" });
    
    // 4. 定义一个异步函数来获取并更新UI
    async function updateBatteryDisplay() {
        try {
            // @ts-ignore
            const battery = await navigator.getBattery();
            const level = Math.floor(battery.level * 100);
            
            // 更新电量文本
            textEl.setText(`${level}%`);

            // 更新图标和颜色
            if (battery.charging) {
                iconEl.setText("⚡️"); // 充电中用闪电Emoji
                container.style.color = "var(--color-green)"; // 使用主题颜色
            } else {
                iconEl.setText("🔋"); // 未充电用电池Emoji
                // 根据电量设置颜色
                if (level > 50) {
                    container.style.color = "var(--text-normal)";
                } else if (level > 20) {
                    container.style.color = "var(--color-yellow)";
                } else {
                    container.style.color = "var(--color-red)";
                }
            }
        } catch (error) {
            console.error("获取电池状态失败:", error);
            container.setText("❌ 获取电池状态失败");
        }
    }

    // 5. 首次立即执行
    updateBatteryDisplay();

    // 6. 设置定时器，每分钟更新一次
    // 警告：这个定时器在离开页面后不会被自动清理，这是DataviewJS的局限性。
    // 它会持续运行直到你关闭或重载Obsidian。
    const intervalID = setInterval(updateBatteryDisplay, 60000); // 60000毫秒 = 1分钟
    
    // (一个不完美的清理尝试) 当代码块被重新渲染时，Obsidian会清空旧容器。
    // 我们可以将intervalID附加到容器上，但这并不能保证在所有情况下都能被清理。
    container.intervalID = intervalID;
}
```

#### CSS代码（添加到.obsidian/snippets文件夹下）：
```css
/* file: .obsidian/snippets/battery-real-widget.css (大尺寸版本) */


.battery-real-widget-container {
    display: inline-flex;
    align-items: center;


    /* --- 以下是主要修改区域 --- */


    /* 1. 增大图标和文字的间距 */
    gap: 10px;
    /* 原来是 6px */


    /* 2. 增大字体大小 */
    font-size: 20px;
    /* 原来是 var(--font-ui-small)，这里直接指定一个较大的像素值 */


    font-weight: 500;


    /* 3. 增大内部空间，让整个框更大 */
    padding: 10px 16px;
    /* 原来是 4px 8px */


    /* 4. 加粗边框 */
    border: 2px solid var(--background-modifier-border);
    /* 原来是 1px */


    /* 5. 增大圆角，以匹配更大的尺寸 */
    border-radius: 12px;
    /* 原来是 6px */


    /* --- 其他属性保持不变 --- */
    transition: color 0.5s ease;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}


.battery-real-icon {
    /* 6. 再次微调图标大小，使其比文字稍大一点 */
    font-size: 1.3em;
    /* 原来是 1.2em */
}
```

#### 代码逻辑
1. **环境**: 在Obsidian的浏览器环境中运行。
2. **请求**: 通过 navigator.getBattery() 向浏览器发起获取电池信息的异步请求。
3. **等待**: 使用 await 等待请求完成并返回 BatteryManager 对象。
4. **解析**: 从返回的对象中读取 level 和 charging 属性。
5. **渲染**: 使用Dataview的 dv.el() 函数将这些信息格式化（如level * 100 + '%'），并创建HTML元素（图标和文本）显示在笔记中。
6. **刷新**: 使用 setInterval 定期重复2-5步，以实现数据的实时更新。

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
