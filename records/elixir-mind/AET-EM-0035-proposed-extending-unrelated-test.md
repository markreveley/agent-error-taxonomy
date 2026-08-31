---
id: AET-EM-0035
title: Proposed extending a test for code that did not exist
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md
source_lines: [1255-1276]
session: https://claude.ai/code/session_01VDZ4JhC3FsNTwkcs1ci5uo
pull_request: 145
agent_system: Claude Code
agent_model: Claude Opus 5
detection: operator asked whether the proposed options were inadvisable
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Proposed extending a test for code that did not exist

## Error description

The agent proposed extending `capture_scenario_test.exs` without first checking
what the file tested or whether capture rendering existed in executable code.

## Evaluation

### Expected

Before presenting an implementation option as a modest extension, the agent
should inspect the named test and the implementation surface it purportedly
covered.

### Observed

The agent offered “extend the capture scenario test” as an option. Inspection
then showed that the file tested route-tag materialization, while capture
rendering was agent-performed and had no implementation in `lib/` to extend.

### Why this qualifies

The repository inspection directly falsified the filename-based assumption.
The agent acknowledged that the proposed option was incoherent and that the
file name had misled it.

### Impact

The operator was offered an implementation path that understated the actual
work and could not be performed as described.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

what about adding 3 and 4? inadvised?

## Assistant

Checking changed my answer on both, in opposite directions.

## 3 — as I described it, it doesn't work

`capture_scenario_test.exs` tests **`route_tags --materialize`**, not the capture render:

```
test "materialize writes the expected log and the bundle then checks clean"
test "re-materializing is idempotent"
test "materialize removes the section of a sink no longer fed"
test "a still-fed sink drops the block of a thread that stopped tagging it"
```

And there is **no capture code in `lib/`** — no module parses a session log, applies the drop rule, or computes a boundary. The entire render is agent-performed from a markdown skill. I was misled by the file's name into assuming it covered the render half; it covers the materialize half, which is the only part that *is* code.

So "extend the capture scenario test" was not a modest option — it was incoherent. There is nothing there to extend. My apologies for proposing it as though it were shelf-ready.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the error was a concrete
claim about an existing test and implementation that a cheap code inspection
would have resolved. It is not a design-disagreement case: inspection showed
that the proposed extension target did not exist.

## Detection and correction

The operator asked whether adding the proposed tests was inadvisable. The agent
inspected the file and `lib/`, retracted the option, and proposed a new
`thread_tail` mechanism instead.
