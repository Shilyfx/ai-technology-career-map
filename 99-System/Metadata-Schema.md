---
type: system
page_kind: metadata-schema
status: reference
created: 2026-08-24
updated: 2026-08-24
related:
  - "[[Review-Rules]]"
  - "[[Vault-Design]]"
  - "[[Job-Skill-Extraction-Rules]]"
---

# Metadata Schema

## Common fields

`type`, `status`, `created`, `updated` are required on formal notes. Use `snapshot_date` for a represented snapshot, `retrieved` for capture time, and `review_after` for time-sensitive pages. `stability` is `stable | current | emerging`.

Allowed `type`: `home`, `moc`, `path`, `concept`, `assessment`, `radar`, `role`, `matrix`, `source-index`, `snapshot`, `inbox`, `job-sample`, `skill`, `evidence`, `lab`, `project`, `review`, `system`, `term`.

## Job Sample contract

Required: `type: job-sample`, `company`, `role_title`, `role_family`, `seniority`, `location`, `region`, `source_url`, `source_kind`, `source_status`, `snapshot_date`, `retrieved`, `created`, `updated`, `review_after`. `source_kind` must be one of `official-job-posting`, `official-career-page`, `official-role-description`, `secondary-source`. Recommended: `posted`, `source_access`.

Body headings: `Source Scope`, `Role Summary`, `Responsibilities`, `Explicit Requirements`, `Preferred/Nice-to-have`, `Skill Extraction`, `Non-skill Gates`, `Role Mapping`, `Limitations`, `Evidence Trace`.

Explicit requirements and inferred skills must be separated. Do not copy a full JD; preserve only concise, evidence-bounded extraction.

## Role contract

Required: `type: role`, `role_family`, `sample_count`, `snapshot_date`, `review_after`. Body headings: `Sample Basis`, `Main Deliverables`, `Responsibility Clusters`, `Skill Profile`, `Non-skill Gates`, `Seniority/Subtrack Differences`, `Portfolio Evidence`, `Adjacent Roles`, `Source Limitations`, `Refresh`.

Role priority values are `Core | Common | Specialized | Company-specific | Prerequisite`; target depth belongs in the Role–Skill table, not a global role claim.

## Skill contract

Required: `type: skill`, `skill_category`, `roles`, `prerequisites`, `related_concepts`. Body headings: `为什么岗位需要它`, `Role Demand`, `Job Evidence`, `在岗位中怎么使用`, `Role-specific Target Depth`, `前置 Skills`, `学习范围`, `核心知识`, `Practice`, `Pass Evidence`, `常见失败 / 误区`, `不需要深挖到什么程度`, `Related Knowledge`, `Actual Evidence`, `Sources`.

Skills do not carry a global `depth`; depth is role-specific. A Skill must be a reusable learnable unit, not merely a framework name.

## Other contracts

- `page_kind: current-state` is the single `type: home` page with one `current` and one `next`.
- `page_kind: evidence-index` is `type: moc`, `domain: evidence`; it is not an Evidence record.
- Technology and Term radars retain `snapshot_date`, `review_after` and their own body bands.
- Evidence records link `skills`, `role_targets`, and optionally `job_samples`; they must include Problem, Action, Result, Failure and Judgment.

## Link and privacy rules

Use stable descriptive filenames and explicit paths where ambiguity matters. Do not create concept pages just for product names. Public notes must not contain API keys, private skill gaps, proprietary data or identifiable internal project details.
