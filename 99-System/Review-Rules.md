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
| stable concepts | 180–365 days or on a source change | definitions, dependencies, links and examples |
| current techniques | 60–90 days | API/model behavior, best practices, cost and known failure modes |
| emerging techniques and Term Radar | 30–90 days | whether the term still matters, moved to Build/Deepen, or should be removed |
| job roles and skill matrix | 90 days | deliverables, skill depth, interfaces and sampled postings |
| market snapshots | 90 days | source availability, geography, sample and date limits |

Dates are guidance, not evidence of truth. `review_after` is the next action date; `updated` is only the edit date.

QA 会在 `today >= review_after` 时发出 review due 警告（模板除外）。完成复查后同时更新 `updated` 与 `review_after`，并在变更记录或页面历史中写明保留、升级、降级或移除的理由。

## Stale handling

1. At or after `review_after`, run `python scripts/check_vault.py` and inspect the page’s sources.
2. If still valid, update `updated`, set a new `review_after`, and record the reason in the change log or page history.
3. If uncertain, set `status: developing` and add a visible “待复核” note; do not silently present it as stable.
4. If contradicted or no longer useful, keep the evidence trail, set `status: deprecated`, and link a replacement when one exists.

## Snapshots and job signals

Keep `snapshot_date`, `retrieved`, publisher, region, sample and limitations. A job posting is evidence of one employer’s request at one time; it is not a universal definition of a role. Preserve the extracted signal even when the URL expires.

## Radar updates

Every radar revision must include “Changes since last radar” with Added, Promoted, Demoted, Removed and Why. The first edition explicitly says there is no previous radar; never invent a delta.
