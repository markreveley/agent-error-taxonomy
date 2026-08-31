---
id: AET-EM-0021
title: Edited a frozen excerpt log as if it were live documentation
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-21-docs-audit-link-and-content-drift.md
source_lines: [86-112]
session: https://claude.ai/code/session_01TKU4LdfJv9r7j9ZnH1WDhQ
pull_request: 125
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: route-tag fidelity gate failed after the edits
primary_type: execution.change.scope_escape
secondary_types: []
confidence: high
---

# Edited a frozen excerpt log as if it were live documentation

## Error description

The agent's content scan did not exclude a generated frozen excerpt section, so
it edited historical transcript quotes as stale live prose.

## Evaluation

### Expected

The content audit should have applied the same live-content boundary as the link
scan and inspected the enclosing section before editing matches.

### Observed

The agent changed three strings inside a frozen route-tag excerpt log. The
fidelity gate failed, while inspection showed that the live body was already
current.

### Why this qualifies

The gate failure and section inspection directly establish both the protected
boundary and the scope escape. This is not an ordinary tool failure: the agent's
scan and edit selection caused the violation.

### Impact

The edit temporarily corrupted materialized historical evidence and required
reversion and a rebuilt audit scan.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

ok great. now what about a doc audit related to actual content? i assume they must have drifted from recent features

## Assistant

Good — that's a different and harder audit: **content drift**, where a doc's *prose* describes tooling/skills/policies that have since changed, even though its links resolve. Let me first establish ground truth (what tooling/skills/modules actually exist now) and reuse the framework from the last content audit, then find where docs describe the system in stale terms.

The enumerating tutorials (gate-suite, three-scanners) are current and internally consistent — the strong gating culture kept them fresh. Drift concentrated in **ungated inline prose** (glossary concept bodies, index descriptions) where facts were hardcoded. Let me sweep for other stated-count/stated-path facts that could have drifted the same way.

Wait — critical catch. The `## Thread excerpts — route-tagged log` heading in `compiled-contract.md` is at **line 26**, so my edits at lines 36 and 54 landed **inside the frozen excerpt-log**, not the live body. Those "twenty-one policies" / `lib/second_brain` / `SecondBrain.Contract` strings are **frozen thread quotes — history, not live drift**. My content grep didn't exclude excerpt logs (my *link* scan did). Let me confirm the fidelity gate now fails and revert.

Confirmed my error: the **live body** (lines 17–25) is already **correct and current** — it says `lib/elixir_mind/contract.ex`, states no policy count, and has no `SecondBrain.Contract`. The stale strings I edited were frozen thread quotes in the excerpt log — history that must stay verbatim, and `mix brain.route_tags` now **FAILS** fidelity because I corrupted the materialized block. Reverting immediately.

With proper excerpt-log stripping, the live content-drift picture is now clean and honest:

- **`second_brain` (134 hits): all legitimate** — filenames (`rename-second-brain-to-elixir-mind.md`, `comparison-with-the-2026-second-brain-field.md`), prose *documenting* the rename, or discussion of the external "second-brain" product genre. No drift.
- **`SecondBrain.` module (7 hits): all in the rename plan** documenting `SecondBrain.X → ElixirMind.X`. No drift.
- **`sb:` id (1), stated count (1): both point-in-time plan content.** Not drift.
- **3 glossary entries reference not-yet-built commands** (`brain.decisions`, `brain.graph`, `brain.summarize`) — need to confirm they're framed as *proposed*.

Committed and pushed. Here's the content-drift audit result.

## Method
I checked whether docs' *prose* describes tooling/skills/policies that have since changed — the harder audit, since these links all resolve. I established ground truth (16 mix tasks, 13 skills, 25 policies, actual module names) and swept live docs for stale identifiers from the recent structural features (the `elixir-mind` lib separation #100/#118, `sb:`→`em:` id migration, the retired auto-injected SessionStart digest, policy growth).

**Crucial correction mid-audit:** my first content grep flagged `beliefs/glossary/compiled-contract.md` as having 3 stale facts ("twenty-one policies", `lib/second_brain/contract.ex`, `SecondBrain.Contract`) and I edited them — but those strings live in that doc's **frozen route-tag excerpt log** (materialized thread quotes, history that must stay verbatim). `mix brain.route_tags` fidelity **failed**, catching the mistake; I reverted, then rebuilt the scan to strip excerpt logs *and* frozen threads (matching how the link scan already worked). The doc's live body was already current.
````

## Classification

`execution.change.scope_escape` fits because the edit crossed from live prose
into a protected generated evidence section. The missed artifact boundary is the
mechanism by which the change escaped scope.

## Detection and correction

The route-tag fidelity gate failed. The agent inspected the section, reverted the
changes, and rebuilt the scan to exclude excerpt logs and frozen threads.
