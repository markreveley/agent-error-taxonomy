---
id: AET-EM-0047
title: Omitted required provenance trailers from pushed commits
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-31-agent-substrate-talks-intake-analysis-and-ratifications.md
source_lines: [159-195, 230-234]
session: https://claude.ai/code/session_01WJibsfQCCpNJHkGY5NPrVz
pull_request: 200
agent_system: Claude Code
agent_model: Claude Opus 5
detection: attribution-policy implementation audit
primary_type: execution.procedure.required_step_omission
secondary_types: []
confidence: high
---

# Omitted required provenance trailers from pushed commits

## Error description

The agent created and pushed two commits without the `Co-Authored-By` and
`Claude-Session` trailers that the harness required it to append.

## Evaluation

### Expected

The required provenance trailers should be added when commits are created, so
each commit remains attributable to the model and session that produced it.

### Observed

The agent discovered after pushing that commits `ecca88e` and `165dc01` lacked
both trailers. Because the branch was not merged, it requested authorization to
rewrite the commits and backfill the metadata.

### Why this qualifies

The transcript names the two pushed commits, the missing fields, and the harness
instruction requiring them. The later history rewrite is remediation of this
single omission, not a separate incident.

### Impact

Without repair, two commits would have entered `main` without their required
model and session provenance. Repair added force-push and history-rewrite risk.

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
| Gates | `brain.verify`, `contract --check`, `orphans` all clean; the two `from` warnings resolve when `/create-pull-request` stamps the thread |

**Questions you need to answer**

| # | question | my recommendation |
|---|---|---|
| 1 | Both pushed commits (`ecca88e`, `165dc01`) carry **no** `Co-Authored-By` or `Claude-Session:` trailer, though the harness directs me to append them. After a true merge those objects enter `main`'s ancestry permanently, and the contract documents legitimate reasons a trailer can be absent — so an auditor would read these as ordinary, not defective. Add the trailers by non-interactive rebase and force-push-with-lease, or leave them? | **Add them.** The branch is unmerged and solely this session's, so `merge-strategy`'s never-rewrite-shared-history rule isn't engaged; and session traceability is the exact property that policy exists to protect. `git rebase <base> --exec 'git commit --amend --no-edit --trailer …'` does it without interactive mode |
````

````text
## User

1 - add them
2 - ratify
3 - proced
````

## Classification

`execution.procedure.required_step_omission` fits because the commits were
authorized and successfully pushed, but a mandatory non-validation step was
skipped. The incident is not an authorization error; authorization was needed
only for the later rewrite.

## Detection and correction

The model-attribution implementation audit exposed the omission. The operator
authorized a noninteractive rebase and force-push-with-lease to backfill the
trailers before merge.
