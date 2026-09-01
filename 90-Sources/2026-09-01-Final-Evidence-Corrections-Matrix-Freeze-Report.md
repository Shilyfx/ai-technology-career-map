---
type: review
status: validated
created: 2026-09-01
updated: 2026-09-01
review_after: 2026-10-01
related:
  - "[[Skill-Evidence-Matrix]]"
  - "[[2026-08-31-Enterprise-Applied-AI-Job-Snapshot]]"
  - "[[Job-Skill-Extraction-Rules]]"
---

# Final Evidence Corrections & Matrix Freeze Report

## 1. Git

- Base branch: `refine/source-fidelity-dependency-cleanup`
- Base SHA: `6a9b0f0915956b6bb09f4b72840eb8660a3b6440`
- Final branch: `finalize/evidence-matrix-freeze`
- Commit 1: `fix: correct final applied ai evidence semantics` (pushed)
- Commit 2: `refactor: freeze applied ai matrix and role priorities` (pushed SHA `902550d6d6bb8086256957d24888a0af5adb9aee`)
- Main was not merged; the existing review branch was not rebased or force-pushed.

## 2. Corrected Evidence

### Zapier

The official Ashby posting says the team works mostly in TypeScript and Python, while experience is “not strictly required” and is a “big plus” ([official posting](https://jobs.ashbyhq.com/zapier/38434b88-086c-424b-8d18-8d006e0b71b8)). The two language rows are therefore `responsibility` implementation context, not `required` candidate gates; the old required rows and `language-1` group were removed.

### Warp

The official posting places Docker/Linux, prompt engineering, agent architectures, tool use, and evaluating non-deterministic systems under one `You may be a good fit if...` block ([official posting](https://job-boards.greenhouse.io/warp/jobs/5749183004)). The whole block is now consistently classified as `required`; only the separate `Bonus...` block remains `preferred`.

### ServiceNow AI Agent Engineer

The official `About You` section calls out API-based systems integration and LLM-based systems design with prompt/context engineering ([official posting](https://careers.servicenow.com/jobs/744000143976690/ai-agent-engineer-moveworks/)). Both rows now represent candidate qualifications (`required`) rather than responsibilities.

### ServiceNow Agent Eval Platform

The official role describes rubrics, judges, calibration against human labels, and trajectory scoring, plus scheduling/retries/high-concurrency/run isolation/versioned reports, as an evaluation platform ([official posting](https://careers.servicenow.com/jobs/744000145843394/staff-software-engineer-agent-eval-platform/)). Human-label calibration and eval-harness orchestration now map to `Agent-Evals-and-Trace-Debugging`; neither is treated as HITL approval or business workflow automation.

### Ramp

The generic “Backend systems and infrastructure that support AI-driven products” row was removed from Skill Extraction because it does not prove a reusable Distributed Systems requirement. The more specific full-stack/web/backend/cloud qualification remains mapped to `Software-Design-and-Architecture` ([official posting](https://jobs.ashbyhq.com/ramp/d204e136-2749-42de-82b4-88a0dd352090)).

### Glean

The current official posting is for `Bangalore, India` and is in-person ([official posting](https://job-boards.greenhouse.io/gleanwork/jobs/4712442005?gh_src=ai101x)). Metadata now records `location: Bangalore, India` and `region: India/APAC`. The strong-plus OR-set remains visible in `Preferred/Nice-to-have` but has no normalized Skill row.

## 3. Section Semantics Policy

- Requirements, Qualifications, Minimum Qualifications, What You Need, Skills You'll Need to Bring, About You, Who You Are, What We're Looking For, and On your first day… default to candidate qualifications.
- Preferred Qualifications, Nice to Have, Bonus, Strong Plus, and Big Plus are consistently `preferred`.
- `You may be a good fit if...` / `You’d be a great fit if...` is one soft-qualification block: it must be all `required` or all `preferred`, with a rationale; it cannot mix types.
- Responsibilities, What You’ll Do, You Will, Core Responsibilities, and About the Role produce `responsibility` only when they describe actual work content.
- `scripts/check_vault.py` warns on mixed candidate-fit evidence types, About You responsibilities, non-preferred Bonus rows, and mixed soft-fit blocks.

## 4. Matrix Before / After

| Skill | Before (Required direct / one-of / Preferred / Responsibility) | After (Required direct / one-of / Preferred / Responsibility) | Change |
| --- | --- | --- | --- |
| Python | 0 / 8 / 0 / 1 | 0 / 7 / 0 / 2 | Zapier language rows leave required and become implementation context |
| TypeScript-JavaScript | 1 / 5 / 0 / 0 | 1 / 4 / 0 / 1 | Zapier language rows leave required and become implementation context |
| HTTP-API | 2 / 1 / 2 / 3 | 3 / 1 / 2 / 2 | ServiceNow About You becomes required |
| Prompt-and-Context-Engineering | 0 / 0 / 2 / 1 | 2 / 0 / 1 / 0 | ServiceNow About You required; Warp fit block required |
| Workflow-Automation-and-Business-Process-Design | 2 / 0 / 2 / 9 | 2 / 0 / 1 / 8 | Glean OR-set unmapped; ServiceNow eval runtime leaves Workflow |
| Agent-Evals-and-Trace-Debugging | 0 / 0 / 3 / 4 | 1 / 0 / 2 / 6 | Warp required; ServiceNow calibration/orchestration moved to evals |
| Human-in-the-Loop-and-Agent-Guardrails | 0 / 0 / 1 / 4 | 0 / 0 / 1 / 3 | ServiceNow human-label calibration is not runtime HITL |
| Distributed-Systems | 2 / 2 / 0 / 1 | 1 / 2 / 0 / 1 | Generic Ramp backend/infrastructure signal removed |

Final totals are `required 41`, `preferred 20`, `responsibility 65`, `inferred-prerequisite 7` across 133 source-bound rows.

## 5. Role Priority Changes

- AI Application Engineer: Tool Calling `Common → Prerequisite`, with zero audited Batch B rows explicitly documented as an architecture/learning prerequisite rather than a hiring-frequency claim.
- AI Application Engineer language counts now reflect Zapier implementation context (`Python` and `TypeScript-JavaScript` responsibility rows, not required rows).
- AI Solutions Architect/FDE and AI Infrastructure/Inference profiles now reflect the Warp and ServiceNow Eval semantic corrections; the profiles remain evidence summaries, not market percentages.

## 6. Metadata Corrections

- Glean Software Engineer, Agents: `location: Bangalore, India`; `region: India/APAC`.
- Snapshot region summary now names Bangalore India/APAC explicitly.
- Canonical Notion FDE Japan source URL is `https://jobs.ashbyhq.com/notion/4bc0802c-b5e0-411c-be01-daaea2bc3ae0`.
- Duplicate OpenAI Agents testing/tracing entries were removed from `90-Sources/Source-Index.md`; one canonical SDK testing link and one canonical SDK tracing link remain.

## 7. QA

- `python3 scripts/rebuild_applied_evidence.py`: 22 cards, 133 rows.
- `python3 scripts/check_vault.py`: `Errors: 0`, `Warnings: 0`, `Review due: 0`.
- `git diff --check`: passed.
- `python3 -m py_compile scripts/check_vault.py`: passed.
- Rebuild/recompute reproducibility: rerun produces no semantic diff beyond the two preserved user-local files (`.obsidian/graph.json`, `01-Inbox/Term-Radar.md`).
- GitHub Actions validation for the pushed final tree: run ID `33466420718`, head SHA `902550d6d6bb8086256957d24888a0af5adb9aee`, status `completed`, conclusion `success`.

## 8. Source-bound Spot Checks

| Company | Source Section | Raw Evidence | Old | New | Reason |
| --- | --- | --- | --- | --- | --- |
| Zapier | Things You'll Do | You will work mostly in TypeScript; experience isn't strictly required, but it is a big plus. | required | responsibility | Official wording explicitly rejects a strict experience gate. |
| Zapier | Things You'll Do | You will work mostly in Python; experience isn't strictly required, but it is a big plus. | required | responsibility | Team implementation context, not a candidate qualification. |
| Warp | You may be a good fit if... | Understand evaluating non-deterministic systems | preferred | required | Entire soft-fit section is kept semantically consistent. |
| ServiceNow AI Agent Engineer | About You | Strong grasp of API-based systems integration | responsibility | required | `About You` is a candidate capability block. |
| ServiceNow AI Agent Engineer | About You | LLM-based systems design including prompt engineering and context engineering | responsibility | required | Technical Mastery is a candidate qualification. |
| ServiceNow Agent Eval Platform | The Role | Calibration against human labels | responsibility / HITL | responsibility / Agent Evals | Labels calibrate evaluators; no approval/authorization is stated. |
| ServiceNow Agent Eval Platform | Eval orchestration at scale | Scheduling, retries, high-concurrency execution, run isolation, and versioned reports | responsibility / Workflow | responsibility / Agent Evals | These are evaluation-harness runtime concerns. |
| Glean | About you | Experience building AI, agentic, workflow, automation, or developer-product experiences | preferred / Workflow | preferred text-only | OR-set is retained for study but not forced into one Skill. |

## 9. Remaining Risks

- ATS pages are dynamic and may change; active samples require 30–60 day refresh.
- Historical, redirected, and blocked URLs remain learning leads, not current requirements.
- The batch is senior-heavy and enterprise-SaaS-heavy; it is not a market census or hiring-probability estimate.
- Soft-fit interpretation is documented and warning-backed, but future source-section title variants still need review.

### Problem

Candidate-fit sections had inconsistent required/preferred semantics, and several generic signals were over-mapped to Skills.

### Action

Reclassified the six P0/P1 evidence groups, removed forced mappings, added section policy and warning checks, then rebuilt the matrix and role profiles.

### Result

All 133 retained rows are source-bound, reproducible, and linked to the corrected Job Samples; local QA is clean.

### Failure

No local QA failures remain. Dynamic ATS pages and historical URLs remain explicit external refresh risks.

### Judgment

The evidence layer is semantically coherent enough for final human review, but it must not be read as a market-frequency estimate.

## 10. Merge Recommendation

READY FOR FINAL REVIEW
