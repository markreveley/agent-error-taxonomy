---
id: AET-EM-0018
title: Let a bulk substitution escape into frozen thread prose
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-14-execute-second-brain-to-elixir-mind-rename.md
source_lines: [50-88, 273-279]
session: https://claude.ai/code/session_01Ecg4gRC7V3vPM3YHJjkpNu
pull_request: 88
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: agent inspected a changed frozen line and diagnosed the Perl guard
primary_type: execution.change.scope_escape
secondary_types: []
confidence: medium
---

# Let a bulk substitution escape into frozen thread prose

## Error description

A Perl statement modifier guarded only the final substitution, allowing an
earlier replacement to modify frozen transcript prose outside the permitted
route-tag attributes.

## Evaluation

### Expected

The authoritative plan allowed changes only to route-tag path attributes inside
frozen thread bodies; all other prose had to remain verbatim.

### Observed

The agent reported that its substitution ran on every line and changed a named
frozen prose occurrence before it reverted the thread edits.

### Why this qualifies

The diagnosis is immediate, mechanically specific, and tied to an explicit
scope boundary. Status is probable because the persisted transcript does not
retain the actual command, tool output, or reverted diff.

### Impact

The operation temporarily corrupted historical transcript text across the
thread corpus and required a full revert and corrected rerun.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

Evaluate the prompt below - ask questions if you have and confirm assumptions if needed before running

Execute the accepted "second-brain → elixir-mind" rename, following the plan at
meta/plans/rename-second-brain-to-elixir-mind.md on main. Read that plan in full
first — it is the authoritative spec (six decisions, scope boundaries, build
order). This prompt only frames execution; the plan governs.

Run on Claude Opus 4.8 at effort high/xhigh. Work on your designated feature
branch cut from the latest main.

## What you're doing
Two workstreams, each its own atomic PR, executed IN SEQUENCE:
- Phase 1a — the NAME rename (SecondBrain → ElixirMind, :second_brain →
  :elixir_mind, lib/second_brain/ → lib/elixir_mind/, hook, docs).
- Phase 1b — the ID migration (sb: → em:, tail-preserving), only AFTER 1a
  has merged.
Do NOT combine them. Do NOT start 1b until 1a is merged to main (1b's corpus
sweep must run on the renamed tree).

## Before you touch anything — re-measure
The plan's counts (200 ids / ~940 tokens / 37 doc files) are STALE: a main-merge
roughly doubled the corpus (363 files carried sb: ids at last check). Re-run the
inventory greps from the plan's Decision 6 and Workstream B tables to get current
numbers before sweeping. The migration regex is unchanged; only the scale is.

## Phase 1a — name rename (one PR)
Follow build-order steps 1a.1–1a.10. The load-bearing parts:
- The sweep is DEFINED BY GREP, not a file list (Decision 6). Update every live
  code identifier — `SecondBrain.`, `lib/second_brain/…`, `test/second_brain/…`,
  `:second_brain` — across ALL non-frozen, non-deprecated/ surfaces (not just the
  maintained-docs list: also beliefs/glossary/, knowledge/ bodies, meta/analysis/
  code links, meta/issues/, meta/evals/, meta/elaborations/, meta/plans/).
- Name-prose vs. code identifiers are DIFFERENT (Decisions 5 & 6): rename
  proper-noun "Second Brain" → "Elixir Mind"; KEEP the "second brain" category
  term; in meta/analysis/ keep the prose but move the code links.
- Frozen thread BODIES: leave prose (incl. stale code mentions) verbatim; update
  only the <routes ref="…"> path-ref attributes (Decision 3).
````

````text
## Assistant

I need to update only the **real `<routes>` tag openers** (lines starting with `<routes`), not the two prose mentions where `<routes` appears mid-sentence backticked (frozen body — stays verbatim per Decision 6). The two prose mentions are at `elixir-mind-rename-plan...:111` and `adopt-session-capture...:372` (both start with `**`, not `<routes`). Targeted sed on real tag lines only:

## Assistant

I found a **bug in my perl command**: the statement modifier `if /^<routes/` only guards the *last* substitution — the `lib/second_brain` sub ran on **every line**, wrongly rewriting frozen prose mentions (e.g. line 115 of the branch-deletion thread now shows `lib/elixir_mind/contract.ex` in prose). This violates Decision 6. Since threads were pristine before this task, I'll revert all threads and redo correctly with a proper block guard.
````

## Classification

`execution.change.scope_escape` fits because a bulk operation crossed the
explicitly permitted edit boundary and changed frozen prose. The Perl semantics
explain how the scope escape happened but do not require a separate type.

## Detection and correction

The agent inspected a frozen prose line, diagnosed the guard placement, reverted
all thread changes, and stated it would rerun with a block guard.
