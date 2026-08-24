---
type: system
page_kind: review-rules
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Metadata-Schema]]"
  - "[[Technology-Radar-2026-08]]"
  - "[[Term-Radar]]"
---

# Review Rules

## 默认间隔

| Content | Review interval | What to check |
| --- | --- | --- |
| Job Sample | 30–60 days | URL/status, title, location, explicit vs inferred extraction |
| Role Profile | 60–90 days | sample coverage, priority, seniority and deliverables |
| current tools / Skill notes | 60–90 days | API/model behavior, practice and sources |
| stable concepts / prerequisites | 180–365 days | definitions, dependencies and links |
| market snapshots | 90 days | source availability, region, sample and limits |

`review_after` 是下一次动作日期，`updated` 只是编辑日期。QA 在 today >= review_after 时提示，模板除外。

## Job evidence rules

保留 `snapshot_date`、`retrieved`、发布方、区域、样本和 limitations。职位页是某公司某时间的需求证据，不是普遍门槛；URL 失效时保留提炼结果并标记 `source_status: expired`。

## Stale handling

仍有效：更新 `updated`/`review_after` 并记录理由；不确定：标为 `developing` 并显式待复核；失效：保留证据轨迹并标 `deprecated`，链接替代页。

## Radar updates

每次 Radar 修订必须有 Changes since last radar 的 Added、Promoted、Demoted、Removed、Why。第一版不得编造历史变化。
