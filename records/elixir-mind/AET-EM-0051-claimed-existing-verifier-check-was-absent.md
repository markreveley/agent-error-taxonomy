---
id: AET-EM-0051
title: Claimed an existing verifier check was absent
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-31-survey-batch-intakes-and-review-pr-skill-audit.md
source_lines: [978-995, 997-1019]
session: https://claude.ai/code/session_01YGagV9xodMZvjYarRVhmX6
pull_request: 210
agent_system: Claude Code
agent_model: unknown
detection: code inspection and empirical comprehension probe during planning
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Claimed an existing verifier check was absent

## Error description

The agent diagnosed a false-citation escape as a missing verifier capability and
proposed adding a check without inspecting the implementation, where the exact
orphan check already existed but was unreachable because of a comprehension
binding bug.

## Evaluation

### Expected

Before classifying a verifier gap as missing functionality and planning a new
check, the agent should inspect the existing verifier implementation.

### Observed

The agent said the verifier had nothing to say about an interloper. When the
operator requested a plan, code inspection found the orphan clause already
implemented; a bare assignment filtered out `nil` rows before the error branch
could run.

### Why this qualifies

The existing code and empirical comprehension probe directly contradict the
implementation-presence claim. The underlying dead-code defect belongs to the
repository; the agent error is confidently diagnosing absence without checking
the implementation.

### Impact

The initial plan scope and mechanism were wrong and could have duplicated logic
instead of repairing the smaller existing defect. The error was corrected
during planning before implementation.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

Partly, and the split matters.

**Genuinely surfaced by the skill's procedure:** the skipped dedup-probe step and the fabricated route-tag block. Both came out of the instruction to build the delivered column from `git diff --stat` rather than from what I remembered doing. Diffing the file set against the `/intake` procedure is what made the *absence* of `meta/evals/dedup-probe.md` legible — an absence is invisible to recollection, because nothing in my memory of the session is shaped like "the file I didn't touch." Same for the route-tag block: walking ask-by-ask forced me back to commit `ddde2ea` in isolation, and `ls meta/threads/` answered a question I had not thought to ask when I wrote it.

**Not surfaced by the skill:** the hand-assigned ids. I knew that when I did it, in view of the transcript. The enumeration made me *report* it; it didn't reveal it.

The thing the skill does not do, and cannot: it is still me auditing me. Every one of those findings is my own account of my own work, produced by the same context that did the work — the failure mode `em:7c4f3e` names ("never trust completion claims from the same context that made the claim") and the one Shape_Weird sharpens ("the verification step can be testimony too, and it is very easy to build one that is"). Git as the oracle for the file list is a real read-back and narrows the space of things I can be wrong about. The status column is not — I graded ask 5 `done` in the table and then contradicted myself in the prose beneath.

Both findings are also mechanizable, which is where they'd stop depending on my diligence:

| Gap | Mechanical check that would catch it |
|---|---|
| Hand-written route-tag block citing a nonexistent thread | `mix brain.route_tags` asserting every `### <thread-slug>` block under a materialized log resolves to a file in `meta/threads/` |
| Intake without a gold-set row | a warn-level check that a commit touching a new bundle `reference` also touched `meta/evals/dedup-probe.md` |

The first is the stronger candidate — the log section is already declared generated, so a block with no tag behind it is a well-defined defect with a clean oracle, and the gate suite already re-derives those blocks. It passed here only because it validates blocks that *derive from* tags and has nothing to say about an interloper. That's a gap in the verifier, not in the policy.
````

````text
## User

write a plan that creates the first mechanical check. pass on second for now

## Assistant

Confirmed — and it changes the plan. The check I proposed **already exists** and is silently dead.

In `check_log_fidelity`, the orphan clause binds `t = by_slug[slug]` inside a `for` comprehension. In Elixir a bare assignment in a comprehension is a **filter**, so when the slug names no thread the row is dropped before the `t == nil` test ever runs — the "no such thread" message is unreachable. The probe above shows `ghost` surviving only with a non-nil sentinel.

Let me check the plan conventions, then write it.

Investigating the fix turned the plan into something different from what you asked for. You asked me to build the first mechanical check; the check already exists and has never been able to fire.

`check_log_fidelity/2` has an orphan clause meant to catch exactly this — a block in a generated log naming a thread that isn't there. It binds `t = by_slug[slug]` inside a `for` comprehension. In Elixir a bare assignment in a comprehension is a **filter**, so when the lookup returns `nil` — precisely the no-such-thread case — the row is discarded before the `t == nil` test runs. The `else: "no such thread"` message is unreachable. The probe:

```
blocks = %{"real" => [], "ghost" => []}   # by_slug has only "real"
for {slug, _} <- blocks, t = by_slug[slug], t == nil or true, do: slug
#=> ["real"]
```

So my earlier account was wrong on the mechanism. I said the gate "validates blocks that derive from real tags and has nothing to say about an interloper." It does have something to say; a one-expression bug means it never says it. The correction matters because it changes the work from *add a check* to *repair a check*, and the second is much smaller.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the existence and structure
of a specific implementation check were directly inspectable before the agent
claimed it was absent. The repository's dead branch is the factual comparator,
not a separate agent error.

## Detection and correction

The operator requested a plan. Code inspection and a minimal Elixir probe found
the existing unreachable clause, changing the work from adding a check to
repairing and testing it.
