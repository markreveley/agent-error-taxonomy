---
id: AET-EM-0034
title: Added an ungoverned dependency field without finding its existing plan
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md
source_lines: [1111-1138, 1144-1146, 1149-1173]
session: https://claude.ai/code/session_01VDZ4JhC3FsNTwkcs1ci5uo
pull_request: 145
agent_system: Claude Code
agent_model: Claude Opus 5
detection: operator asked where to persist the cross-type dependency finding
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: high
---

# Added an ungoverned dependency field without finding its existing plan

## Error description

The agent committed a belief with a `depends_on` frontmatter edge without finding
the existing epistemic-overlay plan, which explicitly kept such edges in prose
until a machine consumer existed.

## Evaluation

### Expected

Before introducing a new typed edge, the agent should search the repository for
the existing matter, apply update-in-place, and check schema, semantics, and gate
support.

### Observed

The agent shipped `depends_on` and described its cross-type target as a finding.
Only after the operator asked where to persist it did the agent locate the plan
and verify that the field was absent from the schema, implementation, tests, and
specified legal type pairs.

### Why this qualifies

The committed action and the previously omitted plan are both directly preserved
in the exchange. The plan's quoted rule and the repository inventory establish
that the omitted evidence surface materially changed what action was allowed.

### Impact

The repository gained a field that looked like a typed dependency edge but
behaved as an unchecked comment; even an invalid target would pass all gates.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

PR [#158](https://github.com/ob6to8/elixir-mind/pull/158) merged as `b692feb`. Timer cleared before firing.

**Thread doc:** `meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md`

### What I created

| Type | Doc | Why this type |
|---|---|---|
| `belief` | [remembered-surfaces-are-forgotten-surfaces](https://github.com/ob6to8/elixir-mind/blob/main/beliefs/remembered-surfaces-are-forgotten-surfaces.md) `em:d1ba60` | Value-laden prior, `depends_on: [em:189d88]` |
| `issue` | [merge-commits-show-unverified](https://github.com/ob6to8/elixir-mind/blob/main/meta/issues/merge-commits-show-unverified-and-trip-the-git-hook.md) | A live concern with two independent fixes, neither chosen |

### Actions I have taken

| Step | Result |
|---|---|
| `/capture` | Six exchanges appended; ledger gains both strands; region tagged for `em:d1ba60` |
| `/add-to-glossary` | **No-op** — `true-merge` already covers the merge-commit concept |
| `attribution.from` | Stamped on the new issue at filing |
| `mix brain.dev_history` | Skipped — shallow clone |
| Commits `b7dfc87`, `efd4355` | Full gate suite green; 183 tests, 0 failures |
| CI on `efd4355` | All 19 steps green |
| Merge | True merge commit |

Two things worth flagging from the work itself.

**The belief's `depends_on` points at a concept, not another belief** — `em:189d88` is `freshness-gate`. Your proposed decomposition had both statements as beliefs with one depending on the other; what actually holds is that the analytic pair lives in the concept and only the value-laden step is a belief. The dependency edge crosses type boundaries, which the existing `em:0c4913 → em:1eebdf` precedent doesn't exercise (both are beliefs there). Worth knowing if the `/extract-belief` skill ever gets built — it needs to allow that.
````

````text
## User

re: "The belief's depends_on points at a concept, not another belief" - where to persist this?
````

````text
## Assistant

Both answers changed after checking. The first one substantially.

## 1. The `depends_on` finding — it's already tracked, and the news is worse than I framed it

I was going to recommend a new issue. Don't file one: the [`epistemic-overlay`](https://github.com/ob6to8/elixir-mind/blob/main/meta/plans/epistemic-overlay.md) plan already owns this matter, and it anticipated exactly this case:

> "**Typed dependency edges.** Generalize the evidence edge into grounding edges: a concept declares the ids it stands on. Keep `verified_by` semantics as the special case… **Open question:** widen `verified_by`, or add a broader `deps`/`grounds` beside it."

And it set a bar for introducing one:

> "*This tool is the machine consumer that earns the typed edge under our own rule.* **Until it exists, these edges stay prose.**"

So `depends_on` shipped as a *third* answer to that open question, without the machine consumer the plan said earns a typed edge. Three consequences, all verified against the tree:

| | State |
|---|---|
| Registered in [`frontmatter-schema`](https://github.com/ob6to8/elixir-mind/blob/main/meta/policy/frontmatter-schema.md)? | **No** — absent from the field table |
| Checked by any gate? | **No** — `depends_on` appears nowhere in `lib/` or `test/` |
| Semantics specified? | **No** — belief→belief was the seed; belief→concept is what I did; nothing says which pairs are legal |

The verification gap is the sharp one. `verified_by` is parsed in `registry.ex` and its targets must resolve; `depends_on: [em:deadbe]` pointing at nothing would pass every gate silently. It looks like a typed edge and behaves like a comment.

**So it goes into the existing plan**, per `update-in-place` and one-artifact-per-matter — a note that its open question was partly preempted in the wild, plus the cleanup obligation that creates. Filing a fresh issue would fragment a matter that already has a home.
````

## Classification

`epistemic.evidence.scope_omission` fits because the agent failed to find a
relevant existing plan before making a repository action; that omitted source
contained the rule that would have excluded the new field. Governing-rule
nonapplication is less precise because the plan had not been surfaced at the
decision point.

## Detection and correction

The operator asked where the finding belonged. The agent searched, found the
existing plan, documented the schema/gate gap there, and identified cleanup of
the shipped field as part of the existing matter.
