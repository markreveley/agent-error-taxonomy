---
id: AET-EM-0046
title: Overlooked an existing model-attribution trail
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-31-agent-substrate-talks-intake-analysis-and-ratifications.md
source_lines: [159-188]
session: https://claude.ai/code/session_01WJibsfQCCpNJHkGY5NPrVz
pull_request: 200
agent_system: Claude Code
agent_model: Claude Opus 5
detection: implementation-time audit of commit trailers
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: medium
---

# Overlooked an existing model-attribution trail

## Error description

The agent's analysis claimed that nothing recorded model identity without first
auditing commit provenance, where model-bearing `Co-Authored-By` trailers were
already common.

## Evaluation

### Expected

A repository-wide absence claim and policy rationale should account for
existing commit-level provenance mechanisms before proposing a new mechanism.

### Observed

During implementation, the agent reported that 257 of the last 400 commits
contained model-attribution trailers, retracted “nothing currently records it,”
and narrowed the policy to document-level attribution.

### Why this qualifies

The retained report identifies both the initial claim and a substantial
contradictory population. Status is probable because the original analysis
wording and raw `git log` output are summarized rather than reproduced in the
transcript evidence.

### Impact

The overbroad absence claim inflated the policy rationale and risked duplicating
an existing attribution mechanism.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="/meta/policy/model-attribution.md /meta/plans/matter-disjointness-check-for-parallel-filing.md /meta/evals/dedup-probe.md /meta/analysis/agent-substrate-talks-read-against-this-brain.md">
All three items are built and verified. I've halted before opening the PR — three things need your call first, per the rule that a closing flow ends clean or not at all.

In plain terms: the two commits I already pushed are missing the tags that link a commit back to the session that made it, and I only noticed because I went looking at how this repo records which model wrote what — which was the subject of the policy you ratified. Fixing that requires rewriting two commits, which is a call you should make, not me. Separately, I added one clause to the policy that you didn't literally ratify, and the policy itself grew the contract right after I criticized unmeasured contract growth.

**What I created**

| type | doc | why this type |
|---|---|---|
| `policy` | [model-attribution](https://github.com/ob6to8/elixir-mind/blob/claude/intake-7gfpj8/meta/policy/model-attribution.md) | a standing enforceable rule; compiled into the contract |
| `plan` | [matter-disjointness-check-for-parallel-filing](https://github.com/ob6to8/elixir-mind/blob/claude/intake-7gfpj8/meta/plans/matter-disjointness-check-for-parallel-filing.md) | deferred work whose approach needed deciding; structured body per `structured-plan-bodies` |

**What I modified**

| file | thrust of the change |
|---|---|
| `meta/evals/dedup-probe.md` | removed the stale figures rather than refreshing them — the prose no longer restates a regenerating table, with a fence explaining why |
| `CLAUDE.md` | recompiled; the new policy renders under *Identity & verification* |
| `meta/analysis/…-read-against-this-brain.md` | corrected a factual claim (below) and stamped `provenance` under the new rule |
| `meta/issues/parallel-sessions-file-duplicate-artifacts.md` | linked the plan adopting its candidate resolution 3 |
| `meta/policy/index.md`, `meta/plans/index.md` | listings |

**Actions I have taken**

| action | result |
|---|---|
| Checked whether commit trailers already record the model | They do — `Co-Authored-By: Claude <Name> <Version>`, on 257 of the last 400 commits. My analysis had claimed "nothing currently records it"; that was overstated, and I rewrote the passage and rescoped the policy to the per-*document* gap the trailer genuinely leaves |
| Surveyed existing `provenance` practice | Less established than the doctrine assumes: 35 agent-authored governance docs name no model, and the rest split across three incompatible forms. The policy therefore fixes one form — the trailer's — so the two records join |
````

## Classification

`epistemic.evidence.scope_omission` fits because a repository-wide absence claim
was made without searching the commit-history surface. This is not source
authority misuse: the problem was an omitted evidence surface, not selection of
a weaker source over an inspected stronger one.

## Detection and correction

An implementation-time audit counted existing trailers. The agent rewrote the
analysis and narrowed the policy to the document-level gap that commit trailers
did not fill.
