---
type: system
page_kind: metadata-schema
status: reference
created: 2026-08-24
updated: 2026-09-01
related:
  - "[[Review-Rules]]"
  - "[[Vault-Design]]"
  - "[[Job-Skill-Extraction-Rules]]"
---

# Metadata Schema

## Common fields

`type`, `status`, `created`, `updated` are required on formal notes. Use `snapshot_date` for a represented snapshot, `retrieved` for capture time, and `review_after` for time-sensitive pages. `stability` is `stable | current | emerging`.

Allowed `type`: `home`, `moc`, `path`, `concept`, `assessment`, `radar`, `role`, `matrix`, `source-index`, `source`, `snapshot`, `inbox`, `job-sample`, `skill`, `evidence`, `lab`, `project`, `review`, `system`, `term`.

## Job Sample contract

Required: `type: job-sample`, `company`, `role_title`, `role_family`, `seniority`, `location`, `region`, `source_url`, `source_kind`, `source_status`, `snapshot_date`, `retrieved`, `created`, `updated`, `review_after`. `source_kind` must be one of `official-job-posting`, `official-career-page`, `official-role-description`, `secondary-source`. Recommended: `posted`, `source_access`. For the `enterprise-applied-ai-2026-08` Batch B audit, `source_access` and `evidence_audit_status` are required: `source_access` is one of `full | partial | dynamic-partial | page-shell-only | blocked`, and `evidence_audit_status` is one of `verified | partial | historical`. `source_status`, `source_access`, `evidence_audit_status`, and confidence must agree; a partial, blocked, page-shell-only, unavailable, redirected, or expired source cannot support high-confidence required evidence. Applied AI batches additionally record `sample_batch`, `company_segment` and `role_subtrack`; these classify the evidence set and do not imply market frequency.

For the `enterprise-applied-ai-2026-08` batch, `company_segment` is one of `enterprise-saas | fintech-platform | automation-platform | b2b-saas`; `role_subtrack` is one of `product-application | agent-platform | field-deployment | applied-ai-product`.

Body headings: `Source Scope`, `Role Summary`, `Responsibilities`, `Explicit Requirements`, `Preferred/Nice-to-have`, `Skill Extraction`, `Non-skill Gates`, `Role Mapping`, `Limitations`, `Evidence Trace`.

Explicit requirements and inferred skills must be separated. Do not copy a full JD; preserve only concise, evidence-bounded extraction.

### Batch B Evidence Trace contract

Every Batch B Evidence Trace row is one source-bound fact and must include `Source Section`, `Source Fidelity`, `Raw Evidence`, `Mapped Skill`, `Evidence Type`, `Requirement Strength`, `Alternative Group`, `Depth Signal`, `Confidence`, `Mapping Rationale`, and `Notes`. `Source Fidelity` is exactly `direct | close-paraphrase | inferred`; `inferred` rows are learning prerequisites only and cannot be marked `required` or `preferred`. `required` and `preferred` rows must cite an official Requirements/Qualifications/Preferred section, never Responsibilities; historical or unavailable cards contain no required/preferred rows. Alternative groups are one-of choices and are not summed. `Mapping Rationale` must explain the semantic fit for that exact fact; generic repeated rationales or notes are invalid. Explicit RAG/retrieval/grounding remains RAG, observability/debugging/metrics/tracing remains Observability, and MCP/A2A remains MCP-and-Agent-Interoperability unless the source separately states tool/action/execution behavior.

## Role contract

Required: `type: role`, `role_family`, `sample_count`, `snapshot_date`, `review_after`. Body headings: `Sample Basis`, `Main Deliverables`, `Responsibility Clusters`, `Skill Profile`, `Non-skill Gates`, `Seniority/Subtrack Differences`, `Portfolio Evidence`, `Adjacent Roles`, `Source Limitations`, `Refresh`.

Role priority values are `Core | Common | Specialized | Company-specific | Prerequisite`; target depth belongs in the Role–Skill table, not a global role claim.

## Skill contract

Required: `type: skill`, `skill_category`, `roles`, `prerequisites`, `related_concepts`. Body headings: `为什么岗位需要它`, `Role Demand`, `Job Evidence`, `在岗位中怎么使用`, `Role-specific Target Depth`, `前置 Skills`, `学习范围`, `核心知识`, `Practice`, `Pass Evidence`, `常见失败 / 误区`, `不需要深挖到什么程度`, `Related Knowledge`, `Actual Evidence`, `Sources`.

Skills do not carry a global `depth`; depth is role-specific. A Skill must be a reusable learnable unit, not merely a framework name.

`evidence_mode: prerequisite-synthesis` may be used for a foundational Skill that is required by a Role Profile but is not separately labeled in the current Job Sample extraction. Such a page must say so explicitly in `Job Evidence` and must not be added to the evidence-frequency matrix as if it were an explicit requirement.

Skill `Sources` should keep Official / normative, Job evidence and Practice tutorial visibly separate. A tutorial never substitutes for a Job Sample.

## Other contracts

- `page_kind: current-state` is the single `type: home` page with one `current` and one `next`.
- `page_kind: evidence-index` is `type: moc`, `domain: evidence`; it is not an Evidence record.
- Technology and Term radars retain `snapshot_date`, `review_after` and their own body bands.
- Evidence records link `skills`, `role_targets`, and optionally `job_samples`; they must include Problem, Action, Result, Failure and Judgment.

## Imported source contract

`type: source` with `page_kind: imported-source` is reserved for a preserved external Markdown artifact. Required provenance fields are `title`, `article_url`, `source_url`, `source_kind: external-markdown`, and `retrieved`; `created` and `updated` still describe when this vault captured the file. The body remains a read-only reference: do not promote product instructions into reusable Skills without testing them against official documentation and this vault's role/evidence rules.

## Link and privacy rules

Use stable descriptive filenames and explicit paths where ambiguity matters. Do not create concept pages just for product names. Public notes must not contain API keys, private skill gaps, proprietary data or identifiable internal project details.
