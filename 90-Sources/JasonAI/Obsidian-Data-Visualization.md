---
type: source
page_kind: imported-source
status: reference
source_kind: external-markdown
title: "Obsidian数据可视化 | 如何制作饼图，柱状图，曲线图。从0打造你的个人数据仪表盘 | 杰森的效率工坊"
article_url: "https://jasonai.me/blog/obsidian-data-visualization-guide/"
source_url: "https://jasonai.me/download/Obsidian数据可视化-如何制作饼图-柱状图-曲线图从0打造你的个人数据仪表盘.md"
published: 2025-07-31
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

## 核心对比


| 插件/方式  | 核心理念 | 易用性 | 数据源 | 动态更新能力 | 外观与交互 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mermaid (内置)** | 快速的文本到图表转换器 | **极高** | 静态文本 | ❌ 不支持 | 基础，无交互 |
| **Charts** | 简洁的静态报告图表生成器 | **高 (静态) / 低 (动态)** | 静态YAML数据<br>(动态需`DataviewJS`辅助) | ⚠️ **需 `DataviewJS` 辅助** | 简洁，有基础交互 |
| **Charts View** | 功能强大的动态仪表盘构建器 | **中等** | 静态, CSV, **原生Dataview查询** | ✅ **原生支持** | 现代美观，交互丰富 |
| **Tracker** | 自动化的个人数据追踪器 | **中等** | **自动扫描笔记内容/元数据** | ✅ **完全自动化** | 功能性，特有日历热力图 |

---

## 核心图表支持度/难度评估


> **难度等级说明**:
> *   **极简**: 语法极其简单，几乎没有学习成本。
> *   **简单**: 语法直观，通过少量配置即可完成。
> *   **中等**: 需要理解插件的工作逻辑（如数据源、查询语法），配置步骤更多。

| 插件/方式 (Plugin/Method) | 饼图 (Pie Chart) | 柱状图 (Bar Chart)  | 折线图 (Line Chart) | 核心优势 (Pros)        | 核心劣势 (Cons)   |
| :-------------------- | :------------- | :--------------- | :--------------- | :----------------- | :------------ |
| **Mermaid (内置)**      | ✅ **极简**       | ✅ **xychart 内测** | ✅ **xychart 内测** | **开箱即用**，无需安装      | 功能简陋，图表类型极少   |
| **Charts**            | ✅ **简单**       | ✅ **简单**         | ✅ **简单**         | **创建静态报告的最佳选择**    | 动态能力依赖编程，配置复杂 |
| **Charts View**       | ✅ **中等**       | ✅ **中等**         | ✅ **中等**         | **原生动态数据能力**，功能强大  | 学习曲线稍高，配置略繁琐  |
| **Tracker**           | ✅ **中等**       | ✅ **中等**         | ✅ **中等**         | **“一劳永逸”的自动化习惯追踪** | 不适合做报告，只适合追踪  |

---

## 决策指南：如何选择？


### 场景一：“我只想快速示意一下，不关心精确数据。”
*   **➡️ 最佳选择：Mermaid**
*   **理由**：内置功能，无需安装。用几行简单的文本就能生成一个示意饼图，非常高效。

### 场景二：“我有一份整理好的数据，想为它做一份干净、正式的图表报告。”
*   **➡️ 最佳选择：Charts 插件**
*   **理由**：这是 `Charts` 插件最核心的用途。它的 YAML 语法非常直观，专门为这种“数据已知，需要展示”的静态报告场景而设计。

### 场景三：“我希望图表能‘活’起来，自动从我的笔记里抓取数据并更新。”
*   **➡️ 最佳选择：Charts View 插件**
*   **理由**：它的王牌功能是**原生支持 Dataview 查询**。您可以轻松构建一个动态仪表盘，例如按月统计您读过的书籍数量，而无需编写复杂的 `DataviewJS` 代码。

### 场景四：“我需要追踪一个日常习惯，并在日历上看到我的坚持情况。”
*   **➡️ 最佳选择：Tracker 插件**
*   **理由**：`Tracker` 的设计理念就是**自动化追踪**。它会自动扫描您每日笔记中的特定标记（如任务完成状态、标签），并生成直观的日历热力图，是习惯养成的绝佳工具。


## Obsidian数据图表案例-Charts

## 饼图

```chart
type: pie
labels: [Monday,Tuesday,Wednesday,Thursday,Friday]
series:
  - title: Title 1
    data: [1, 3, 3, 4, 5]
width: 50%
labelColors: true
```



## 柱状图
```chart
type: bar
labels: [Monday, Tuesday, Wednesday, Thursday, Friday]
series:
  - title: Title 1
    data: [2, 2, 3, 4, 5]
  - title: Title 2
    data: [5, 4, 3, 2, 1]
width: 60%
labelColors: true
```


## 折线图


```chart
type: line
labels: [Monday,Tuesday,Wednesday,Thursday,Friday]
series:
  - title: Title 1
    data: [1, 5, 3, 2, 5]
  - title: Title 2
    data: [3, 4, 2, 4, 1]
```










## Fitness习惯完成比例（集成Dataview，读取日记中的数据）

```dataviewjs
// 1. 数据查询与计算逻辑修改
const habitToTrack = 'fitness';
const allTasks = dv.pages('"diary"').file.tasks;

const counts = {
    '已完成 (Done)': 0,
    '未完成 (Not Done)': 0
};

for (let task of allTasks) {
    // 只关心包含指定习惯关键词的任务
    if (task.text.includes(habitToTrack)) {
        if (task.completed) {
            counts['已完成 (Done)']++;
        } else {
            counts['未完成 (Not Done)']++;
        }
    }
}

// 2. 构建图表数据
const chartData = {
    type: 'pie',
    data: {
        labels: Object.keys(counts),
        datasets: [{
            label: 'Fitness 打卡状态',
            data: Object.values(counts),
            backgroundColor: [
                'rgba(75, 192, 192, 0.7)',  // 'Done' 的颜色 (绿色系)
                'rgba(255, 99, 132, 0.7)'   // 'Not Done' 的颜色 (红色系)
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        // 【需求1】设置宽度是通过外层容器的样式实现的
        // Charts 插件本身没有直接的 width 参数，但我们可以控制它的容器
        responsive: true,
        maintainAspectRatio: false, // 允许图表自由调整以适应容器
        plugins: {
            title: {
                display: true,
                text: `'${habitToTrack}' 习惯完成状态`
            }
        }
    }
};

// 3. 渲染图表，并设置容器宽度
// 我们给 this.container 这个 div 元素设置一个 style 属性
this.container.style.width = '40%';
this.container.style.height = '400px'; // 建议同时设置一个高度
window.renderChart(chartData, this.container);
```


```chart
type: pie
labels: [a,b,c]
series:
  - title: test
    data: [1,2,3]
tension: 0.2
width: 80%
labelColors: false
fill: false
beginAtZero: false
bestFit: false
bestFitTitle: undefined
bestFitNumber: 0
```

## Obsidian数据图表案例-ChartsView

## 饼图

```chartsview

type: Pie


data:
  - type: "Wage income per capita (¥)"
    value: 17917
  - type: "Operating net income per capita (¥)"
    value: 5307
  - type: "Property Per Capita Net Income (¥)"
    value: 2791
  - type: "Transfer of net income per capita (¥)"
    value: 6173


options:
  angleField: "value"
  colorField: "type"
  radius: 0.5
  label:
    type: "spider"
    content: "{percentage}\n{name}"
  legend:
    layout: "horizontal"
    position: "bottom"
```



## 柱状图

```chartsview
#-----------------#
#- chart type    -#
#-----------------#
type: Bar

#-----------------#
#- chart data    -#
#-----------------#
data:
  - action: "Browse the website"
    pv: 50000
  - action: "Add to cart"
    pv: 35000
  - action: "Generate orders"
    pv: 25000
  - action: "Pay order"
    pv: 15000
  - action: "Seal the deal"
    pv: 8500

#-----------------#
#- chart options -#
#-----------------#
options:
  xField: "pv"
  yField: "action"
  conversionTag: {}
```


## 折线图

```chartsview
#-----------------#
#- chart type    -#
#-----------------#
type: TinyLine

#-----------------#
#- chart data    -#
#-----------------#
data: [264, 417, 438, 887, 309, 397, 550, 575, 563, 430, 525, 592, 492, 467, 513, 546, 983, 340, 539, 243, 226, 192]

#-----------------#
#- chart options -#
#-----------------#
options:
  height: 60
  autoFit: false
  smooth: true
  tooltip: false
  annotations:
    - type: "line"
      start: ["min", "mean"]
      end: ["max", "mean"]
      style:
        stroke: "rgba(0, 0, 0, 0.45)"
      text:
        content: "Average"
        offsetY: -2
        style:
          textAlign: "left"
          fontSize: 10
          fill: "rgba(44, 53, 66, 0.45)"
          textBaseline: "bottom"
    - type: "line"
      start: ["min", 800]
      end: ["max", 800]
      style:
        stroke: "rgba(200, 0, 0, 0.55)"
      text:
        content: "Target"
        offsetY: -2
        style:
          textAlign: "left"
          fontSize: 10
          fill: "rgba(44, 53, 66, 0.45)"
          textBaseline: "bottom"
```


## 与dataview集成

```chartsview
# 1. 定义图表类型为饼图
type: Pie

# 2. 动态生成数据
data: |
  dataviewjs:
  // 使用 dataviewjs 查询数据
  return dv.pages('"diary"').file.tasks
           // 步骤 a: 只筛选出文本中包含 "fitness" 的任务
           .where(t => t.text.includes('fitness'))
           // 步骤 b: 按任务是否完成进行分组
           .groupBy(t => t.completed ? '已完成' : '未完成')
           // 步骤 c: 将分组结果映射成图表所需的格式
           .map(g => ({ type: g.key, value: g.rows.length }))
           // 步骤 d: 确保返回的是一个标准的数组
           .array();

# 3. 配置图表外观和选项
options:
  # 告诉图表，用数据中的 'value' 字段来决定扇区大小
  angleField: "value"
  
  # 告诉图表，用数据中的 'type' 字段来区分颜色和标签
  colorField: "type"
  
  # 设置饼图的半径大小
  radius: 0.8
  
  # 设置标签样式
  label:
    type: "spider" # 蜘蛛网样式的引导线
    content: "{name}: {value} ({percentage})" # 标签内容格式
    
  # 设置图例
  legend:
    layout: "horizontal"
    position: "bottom"
```












```chartsview
#-----------------#
#- chart type    -#
#-----------------#
type: Mix

#-----------------#
#- chart data    -#
#-----------------#
data.area:
  - time: 1246406400000
    temperature: [14.3, 27.7]
  - time: 1246492800000
    temperature: [14.5, 27.8]
  - time: 1246579200000
    temperature: [15.5, 29.6]
  - time: 1246665600000
    temperature: [16.7, 30.7]
  - time: 1246752000000
    temperature: [16.5, 25.0]
  - time: 1246838400000
    temperature: [17.8, 25.7]

data.line:
  - time: 1246406400000
    temperature: 21.5
  - time: 1246492800000
    temperature: 22.1
  - time: 1246579200000
    temperature: 23
  - time: 1246665600000
    temperature: 23.8
  - time: 1246752000000
    temperature: 21.4
  - time: 1246838400000
    temperature: 21.3

#-----------------#
#- chart options -#
#-----------------#
options:
  appendPadding: 8
  syncViewPadding: true
  tooltip:
    shared: true
    showMarkers: false
    showCrosshairs: true
    offsetY: -50

options.area:
  axes: {}
  meta:
    time:
      type: 'time'
      mask: 'MM-DD'
      nice: true
      tickInterval: 172800000
      range: [0, 1]
    temperature:
      nice: true
      sync: true
      alias: '温度范围'
  geometries:
    - type: 'area'
      xField: 'time'
      yField: 'temperature'
      mapping: {}

options.line:
  axes: false
  meta:
    time:
      type: 'time'
      mask: 'MM-DD'
      nice: true
      tickInterval: 172800000
      range: [0, 1]
    temperature:
      sync: 'temperature'
      alias: '温度'
  geometries:
    - type: 'line'
      xField: 'time'
      yField: 'temperature'
      mapping: {}
    - type: 'point'
      xField: 'time'
      yField: 'temperature'
      mapping:
        shape: 'circle'
        style:
          fillOpacity: 1
```



## Obsidian数据图表案例-Tracker


## 饼状图

``` tracker
searchType: task.done, task.notdone
searchTarget: fitness, fitness
folder: diary
endDate: 2025-07-31
pie:
    title: 已完成任务分布
    data: '{{sum(dataset(0))}},{{sum(dataset(1))}}'
    dataColor: '#4daf4a,#377eb8'
    label: 健身了,偷懒了
    ratioInnerRadius: 0.3
    extLabel: '健身了, 偷懒了'
    dataName: 健身了, 偷懒了
	showLegend: true
    legendPosition: right
    legendOrientation: vertical
```




## 柱状图

```tracker
searchType: dvField
searchTarget: 喝水
folder: diary
bar:
    title: 每日饮水量追踪
    yAxisLabel: 饮水量
    yAxisUnit: ml
    barColor: #377eb8
    xAxisTickInterval: 1w
```










```tracker
searchType: task.done
searchTarget: fitness,reading,meditation
folder: diary
stack: true
bar:
    title: 每日完成习惯统计
    yAxisLabel: 完成数量
    barColor: '#4daf4a,#377eb8,#ff7f00'
```










## 折线图

```tracker
searchType: dvField
searchTarget: 喝水
folder: diary
endDate: 2025-07-31
line:
    title: 本月饮水量走势
    yAxisLabel: 饮水量
    yAxisUnit: ml
    lineColor: dodgerblue
    showPoint: true
    xAxisTickInterval: 7d
    xAxisTickLabelFormat: MM-DD
```








```text
    extLabel: '健身了, 偷懒了'
    dataName: 健身了, 偷懒了
	showLegend: true
    legendPosition: right
    legendOrientation: vertical
```

> **专注 AI 与个人知识管理**
> 本文属于 [杰森的效率工坊](https://jasonai.me)原创。未经允许禁止商用。
> 
> **订阅杰森的频道：**
> [YouTube](https://www.youtube.com/@JasonEfficiencyLab) · [Twitter(X)](https://x.com/JasonEffiLab) · [小红书](https://www.xiaohongshu.com/user/profile/60935957000000000101fbf7) · [B站](https://space.bilibili.com/3546884870244925)
