---
type: system
page_kind: metadata-schema
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Review-Rules]]"
  - "[[Vault-Design]]"
---

# Metadata Schema

> 这是 Vault 的最小、正交元数据约定。字段用于检索和质检，不替代正文判断。

## 通用字段

| Field | Required | Allowed / meaning |
| --- | --- | --- |
| `type` | yes | `home`, `moc`, `path`, `concept`, `assessment`, `radar`, `role`, `matrix`, `source-index`, `snapshot`, `inbox`, `evidence`, `lab`, `project`, `review`, `system`; `term` is a lightweight alias for Inbox cards |
| `status` | yes for formal pages | Note maturity only: `seed`, `developing`, `validated`, `reference`, `deprecated` |
| `stability` | when relevant | `stable`, `current`, `emerging` |
| `created` / `updated` | yes for formal notes | ISO date `YYYY-MM-DD` |
| `review_after` | current/emerging or time-sensitive | Next review date; absence means the page must be stable or explicitly exempt |
| `snapshot_date` | radar/snapshot/market/role views | Date represented by the page, not the edit date |
| `related` | recommended | Wikilinks to adjacent notes; keep small and meaningful |
| `depth` | concept, term, learning or evidence when useful | `recognize`, `explain`, `use`, `implement`, `optimize`, `research` |

## Type-specific expectations

| Type | Minimum body contract |
| --- | --- |
| `home` | Entry or state page; `page_kind: current-state` must have exactly one `current` and one `next` |
| `moc` | Navigation map with links to its children |
| `path` | Learning Units with Goal, Prerequisites, Concepts, Practice, Pass Evidence, Next |
| `concept` | What it is, problem, dependencies, non-use case, verification and links |
| `assessment` | Questions, interpretation, and a route from assessment to Evidence and learning depth |
| `radar` | Core/Build/Deepen/Watch/Avoid plus `snapshot_date` and `review_after`; changes since last radar |
| `role` | Deliverables, core problems, skill depth, interfaces, failure modes, portfolio evidence, market signals and source dates |
| `matrix` | Comparable role/skill dimensions and snapshot context |
| `source-index` | Source records with publisher, scope, region, published/retrieved dates and limitations |
| `snapshot` | Scope, region, sample, `snapshot_date`, retrieved date, limitations and review date |
| `inbox` | Real pending terms only; workflow status belongs in the table, not frontmatter maturity |
| `evidence` / `lab` / `project` / `review` | Problem → action → result → failure → judgment → skill → gap; link back to a role or path |
| `system` | Rules, schemas or maintenance design; no personal secrets |

## Workflow status is not note status

Terms Inbox uses `inbox → classified → promoted|discarded`. Evidence may use a body-level outcome such as `keep|drop|next`. Neither becomes a new frontmatter enum.

## Naming and privacy

Use stable, descriptive filenames. Do not create a page solely for a trending product name. Public pages must not contain API keys, private skill-gap data, proprietary datasets or identifiable internal project details.
