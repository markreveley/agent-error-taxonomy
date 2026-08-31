---
id: AET-EM-0008
title: Used a historical log as the current priority hierarchy
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-11-deprecated-directory-triage-and-machinery-deletion.md
source_lines: [180-194, 196-215]
session: https://claude.ai/code/session_01K9HNVqSG97XiQb2qVPRduE
pull_request: 43
agent_system: Claude Code
agent_model: unknown
detection: operator questioned whether the log was authoritative
primary_type: epistemic.source.authority_misuse
secondary_types: []
confidence: high
---

# Used a historical log as the current priority hierarchy

## Error description

The agent read a timestamped change log as current policy and reported an
incomplete priority hierarchy from it instead of checking the executable weights
map.

## Evaluation

### Expected

Current behavior should be read from the canonical implementation or current
policy. At the pinned revision, `lib/elixir_mind/session_init.ex:47-57` orders
issues, in-progress plans, todos, accepted plans, open strands, paused strands,
dangling strands, and proposed plans.

### Observed

The agent cited the log for a shorter order that omitted accepted plans, paused
strands, and dangling questions. When asked whether the log was the best source,
it inspected the implementation and found the log entry stale.

### Why this qualifies

The executable artifact directly contradicts the initial current-state claim.
The transcript also identifies the authority error: a historical record was
treated as current state.

### Impact

The operator received an incorrect account of prioritization and could make
workflow decisions based on missing priority classes.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

The todo is created, why does it need to be "mirrored" to be picked up by the digest?

## Assistant

Because they're two different storage layers, and the digest only reads one of them.

The todo I created earlier (Task #1) lives in the **Claude Code harness task system** — session state managed by the app, not files in your repository. It's great for tracking work while a session (or its continuations) is alive, but it isn't a repo artifact: nothing under version control changed when I created it, and `mix brain.session_init` — which is plain Elixir tooling that scans the repo — has no access to it. The digest's four sources are all files: open issues under `meta/issues/`, open todos under `meta/todos/`, active plans under `meta/plans/`, and dangling routing-ledger strands in `meta/threads/`. A harness task is invisible to all four.

That said, "mirrored" was overstating the gap, because the work is *already* partially visible to the digest through a different door: the captured thread doc's routing ledger has an **open row** ("Is `deprecated/` safe to delete? — triage of what remains") with a dangling question listing the 13 sources, 9 assertions, URL backlog, and old plans. Open strands are one of the digest's four sources, so a fresh session's session-init digest will surface the deprecated work from that row even if nothing else is done.

The practical difference a `meta/todos/` entry would make: in the digest's priority heuristic, an explicitly recorded todo ranks *above* open strands (the ranking is issues > in-progress plans > todos > open strands > proposed plans, per the log), and it's a durable, self-contained statement of the task rather than a question hanging off a thread. The harness task also dies with this session's environment, while a filed todo survives anywhere the repo goes.

So: nothing is broken — the next session will see the work either way via the ledger strand. Filing a `/todo` would just promote it in the ranking and make the inventory self-contained. Happy to file it if you want that.
````

````text
## User

/add-to-glossary strand, ledger

Is the log the best place to find that hierarchy?

## Assistant

Done — committed and pushed (`ccaf6a0`; the branch was restarted from the latest `main` first, since PR #43 had merged).

<routes ref="em:bb2968">
**Glossary results:**
- **Added** [strand](/glossary/strand.md) (`em:bb2968`) — one topic's line of work through a session: the unit the routing ledger tracks one row per, with a state (`open`/`paused`/`closed`) orthogonal to where its content routed, and "dangling strand" defined as the form the session-init digest harvests.
- **Merged, not duplicated:** *ledger* is the same concept as the existing [routing ledger](/glossary/routing-ledger.md) entry, so per the one-term-one-file rule that entry got the short-form note ("often shortened to just 'the ledger'") and a prose cross-link to *strand*, rather than a second file.
- All gates green; registry refreshed; root `log.md` updated. Glossary at 86 terms.
</routes>

<routes ref="lib/elixir_mind/session_init.ex beliefs/glossary/session-init-digest.md">
**Is the log the best place to find that hierarchy? No** — and your question caught a real weakness. The log entry I quoted was just a change record, and it was already stale: it described the ranking *before* todos were added as a source. The canonical definition is the `@weights` map in `lib/second_brain/session_init.ex:35` (with the moduledoc stating it in prose at line 17): **issues → in-progress plans → todos → accepted plans → open strands → paused strands → leftover dangling questions → proposed plans**, newer first within a class. Since code isn't where you'd naturally look it up, I also stated the full order in the [session-init digest](/glossary/session-init-digest.md) glossary definition with a pointer to the module — so the glossary is now the best *prose* place to find it, and it cites where the truth lives.
</routes>
````

## Classification

`epistemic.source.authority_misuse` fits because the agent selected a historical
change record as authority for current executable state. A direct-check omission
occurred, but the narrower repeated pattern is misuse of a noncanonical source.

## Detection and correction

The operator questioned the log's authority. The agent checked the weights map,
reported the full order, added a discoverable prose pointer, and later recommended
that logs be explicitly treated as history rather than current state.
