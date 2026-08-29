---
type: matrix
domain: skills
page_kind: skill-evidence-matrix
status: reference
created: 2026-08-24
updated: 2026-08-24
review_after: 2026-09-24
related:
  - "[[Skill-Index]]"
  - "[[Role-Skill-Matrix]]"
  - "[[Job-Sample-Index]]"
---

# Skill Evidence Matrix

> 这张表只汇总 Job Sample 中的 `Skill Extraction`。`explicit` 可作为岗位明确要求证据；`inferred` 只能支持责任上下文，不能增加 required frequency。它不是关键词统计。

| Skill | Role | Job Samples | Evidence Type | Confidence |
| --- | --- | --- | --- | --- |
| [[Python]] | Research / ML / Application | [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]], [[Apple-Machine-Learning-Engineer-Search-Cupertino-2026-06]] | explicit | high |
| [[SQL]] | Data / ML | [[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] | explicit | high |
| [[Git]] | Engineering roles | [[Huawei-AI-Bottom-Software-Shanghai-2026-08]] | inferred | medium |
| [[Linux]] | Infra | [[Huawei-AI-Bottom-Software-Shanghai-2026-08]] | explicit | high |
| [[Testing]] | Research / Application / Safety | [[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]], [[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] | explicit + inferred | high |
| [[HTTP-API]] | Application / PM | [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]], [[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]] | explicit | high |
| [[Docker-Containers]] | Application / ML | [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]], [[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]] | explicit + inferred | high |
| [[Data-Quality-and-Lineage]] | Data / ML | [[Apple-Machine-Learning-Engineer-Data-Curation-Cupertino-2026-06]], [[Anthropic-Software-Engineer-RL-Data-San-Francisco-2026-08]] | explicit + inferred | high |
| [[ML-Experimentation]] | Research / ML / Evals | [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]], [[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] | explicit | high |
| [[Model-Evaluation]] | Research / Evals | [[Anthropic-Research-Engineer-Model-Evaluations-San-Francisco-2026-08]], [[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] | explicit + inferred | high |
| [[Transformer-LLM-Fundamentals]] | ML / Research | [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]], [[Huawei-Algorithm-Expert-Multimodal-Beijing-2026-08]] | explicit + inferred | medium |
| [[PyTorch]] | ML / Research | [[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]], [[Apple-Machine-Learning-Engineer-Video-Cupertino-2026-06]] | explicit + inferred | high |
| [[Distributed-Training]] | Research / Infra | [[Apple-Machine-Learning-Engineer-SIML-Cupertino-2026-07]], [[Huawei-Algorithm-Expert-Multimodal-Beijing-2026-08]] | explicit + inferred | medium |
| [[RAG]] | Application / FDE | [[Apple-Machine-Learning-Engineer-LLM-Cupertino-2026-02]], [[Apple-Machine-Learning-Engineer-NLU-Proactive-Santa-Clara-2026-07]] | explicit + inferred | medium |
| [[Tool-Calling-Agent-Workflow]] | Application / PM | [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]], [[Anthropic-Research-Engineer-Computer-Use-San-Francisco-2026-08]] | explicit | high |
| [[Model-Serving]] | Infra / FDE | [[OpenAI-Software-Engineer-Model-Inference-San-Francisco-2026-08]], [[Huawei-AI-Architect-Training-Inference-Beijing-2026-08]] | explicit + inferred | high |
| [[Distributed-Systems]] | Infra / Research | [[OpenAI-Software-Engineer-GPT-Infrastructure-San-Francisco-2026-08]], [[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]] | explicit | high |
| [[CUDA-GPU-Basics]] | Infra / Research | [[OpenAI-Software-Engineer-Inference-Performance-San-Francisco-2026-08]], [[Huawei-AI-Bottom-Software-Shanghai-2026-08]] | explicit + inferred | high |
| [[Observability]] | Infra / Application | [[Anthropic-Performance-Engineer-Inference-Systems-San-Francisco-2026-08]], [[OpenAI-Software-Engineer-API-Agents-San-Francisco-2026-08]] | explicit + inferred | high |
| [[LLM-Evals]] | Evals / Application | [[OpenAI-Research-Engineer-Frontier-Evals-San-Francisco-2026-08]], [[Apple-Machine-Learning-Engineer-Eval-Insights-London-2026-06]] | explicit + inferred | high |
| [[AI-Safety-Measurement]] | Safety / PM | [[OpenAI-Product-Manager-Safety-Measurement-San-Francisco-2026-08]], [[Anthropic-ML-Infrastructure-Engineer-Safeguards-San-Francisco-2026-08]] | explicit + inferred | high |
| [[API-Product-Delivery]] | PM / Application | [[OpenAI-Software-Engineer-API-SDK-Seattle-2026-08]], [[OpenAI-Product-Manager-API-Agents-San-Francisco-2026-08]] | explicit + inferred | high |
| [[Technical-Communication]] | PM / FDE | [[Huawei-AI-Solutions-Architect-Shanghai-2026-08]], [[OpenAI-Product-Manager-Safety-Measurement-San-Francisco-2026-08]] | explicit + inferred | high |

## Reading rule

样本链接是追溯入口；具体职责、明确要求、推断标记和局限必须回到 Job Sample 的原文卡片和 `Evidence Trace`，不能只依据本表的计数。

## Prerequisite layer

[[Prerequisite-Foundation-Map]] 中的六个基础 Skill 是为学习顺序补齐的综合层。它们没有被当前 Job Sample 独立抽取，因此不在上表伪造 `explicit / inferred` 计数；完成后仍应通过 [[Evidence-Index]] 形成个人能力证据。
