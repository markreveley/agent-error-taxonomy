---
id: AET-EM-0024
title: Treated file history as complete recent-PR state
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-22-survey-tier-and-bookmarks-register.md
source_lines: [119-140, 253-288]
session: https://claude.ai/code/session_01Vvd7J5SUbSgg5cP8MayE85
pull_request: 128
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: merge-time main update exposed PR 127's doctrine retirement
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: medium
---

# Treated file history as complete recent-PR state

## Error description

Asked whether a recent PR amended a doctrine, the agent checked the current
file's commits, answered no, and treated the doctrine as stable without covering
concurrent open-PR state.

## Evaluation

### Expected

The explicit recent-PR question called for checking open and recent PRs or
qualifying the answer as limited to the current branch and reachable history.

### Observed

The agent gave an unqualified negative based on three file commits. At merge
time, PR #127 had retired the exact doctrine, leaving the branch with broken and
stale references.

### Why this qualifies

The evidence strongly supports a scope omission, but status is probable because
the transcript does not timestamp PR #127's creation. It proves the later
collision, not conclusively that PR #127 was discoverable at the earlier turn.

### Impact

The work was built on a doctrine that disappeared during the PR, requiring a
late conceptual reframe and reference repair before merge.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

agree with your suggestions, let's proceed
I imagine a "bookmarks-registe.md" doc that I add to, then run a /bookmarks skill which then proceses them
are you imagining them being one per flie, or listed in a doc?
where are you seeing "distill, don't dump"? do you see a recent pr where that doctrine was amended?

## Assistant

### "Distill, don't dump" — where it is, and no, it hasn't been amended

It's a real, foundational policy: `meta/policy/distill-dont-dump.md`, `section: filing`, `order: 1` — literally the first filing rule. Full text is just that one paragraph I quoted.

On whether it was recently amended: **no.** Its entire history is three commits, and none touched the doctrine's substance:

- `2113193` — the concept→document terminology sweep (mechanical, bundle-wide)
- `cb2d837` — attribution backfill (added the frontmatter block, not the body)
- `4960c48` — its arrival

The body text is untouched since it was written. Recent policy churn has all been elsewhere — `session-capture`, `merge-strategy`, `plan-vs-capture`. So it's stable ground, and good instinct to check.

The important nuance: what we're building **doesn't amend `distill-dont-dump` at all.** That doctrine governs *documents* — things that have earned a place in the tree. Our bookmark tier sits *before* distillation, so the honest move is a narrow carve-out in its sibling `link-processing` ("no bookmark type" → "one explicit staging tier, which does not enter the taxonomy"), leaving `distill-dont-dump` fully intact and still the rule the moment a bookmark is *promoted*.
````

````text
## Assistant

Done — captured, glossaried, committed, pushed, and the PR is open. PR #128 carries the survey tier, the `/bookmarks` skill (with the date-added and Hacker News refinements), the captured thread doc, the new glossary term **survey tier**, and the `attribution.from` stamping. No merge — the open PR is handed back for you to merge. Want me to watch it, or leave it as pushed?

## User

merge

## Assistant

Merge aborted — the tree is clean and nothing is half-merged. I need to surface this before touching anything, because it's a **doctrine collision**, not a mechanical conflict.

## What happened

While this PR was open, **PR #127 merged to `main`** (the "qiju-thread-storage" session) and **retired "distill, don't dump"** — the exact doctrine my survey-tier work is built on. Specifically, main:

- **Deleted** `meta/policy/distill-dont-dump.md`, replacing it with **`capture-knowledge-cite-the-source.md`** (same filing injunction, new name).
- Added a new doctrine, **`fit each layer to its purpose`**: retention is judged per-layer — the knowledge layer distills hard, the record layer keeps verbatim — rather than by one global "distill" dial.
- Turned the `distill-dont-dump` glossary entry into a retired-slogan stub.

My branch references the old doctrine everywhere — the `link-processing` carve-out, the `survey-tier` glossary entry, the plan, and the thread all link `/meta/policy/distill-dont-dump.md`, which **no longer exists**. Merging as-is would land broken links and cite a retired slogan. Three files conflict directly (`distill-dont-dump.md`, `graduation.md`, `threads/index.md`); the rest are stale-by-reference.

## The good news

The new doctrine **fits the survey tier better than the old one did**. "Fit each layer to its purpose" is *exactly* the survey tier's argument — it's a new staging layer with its own retention purpose (light metadata, enough to surface), distinct from the knowledge layer. And the rule that re-engages on promotion is now precisely `capture-knowledge-cite-the-source` (the knowledge-layer half).

## My recommended resolution

Merge `main` in and reframe my work onto the new doctrine:

1. **Conflicts:** take main's retired-slogan stub for `distill-dont-dump.md`; keep both citation sets in `graduation.md` (main's + my sense 4) and `threads/index.md`.
2. **Reframe references** in `link-processing` (carve-out), `survey-tier`, and the plan: `distill, don't dump` → `capture the knowledge, cite the source`, positioned under the `fit each layer to its purpose` doctrine — and repoint the one route-tag ref off the deleted policy path so `route_tags` stays green.
3. Leave the **thread body verbatim** (it's the frozen record of what was actually said, when the old doctrine was live) — only fix its route-tag ref resolution.
4. Re-run every gate, then true-merge.

This is doctrine-adjacent and you authored the new doctrine hours ago, so I don't want to silently reframe it. **Shall I proceed with that resolution** (reframe onto `fit each layer to its purpose` + `capture-knowledge-cite-the-source`), or do you want the survey tier to cite the new doctrine differently?
````

## Classification

`epistemic.evidence.scope_omission` fits because the answer used file history as
the evidence scope for a question explicitly about recent PRs. The missing
temporal premise prevents confirmed status.

## Detection and correction

The merge attempt exposed PR #127's changes. The agent aborted the merge,
described the collision, and proposed reframing the work onto the new doctrine.
