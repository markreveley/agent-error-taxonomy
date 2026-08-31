---
id: AET-EM-0036
title: Narrow search missed the repository's designated evidence surface
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md
source_lines: [1371-1407]
session: https://claude.ai/code/session_01VDZ4JhC3FsNTwkcs1ci5uo
pull_request: 145
agent_system: Claude Code
agent_model: Claude Opus 5
detection: later persistence audit found a prior cross-session observation
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: high
---

# Narrow search missed the repository's designated evidence surface

## Error description

The agent filed an eval as supported by three instances from one session after
searching only `meta/evals/` and `lib/`, missing a fourth cross-session instance
in the repository's observations-awaiting-formalization list.

## Evaluation

### Expected

The update-in-place workflow required searching the bundle before filing, and
`beliefs/future-beliefs.md` was a designated surface for relevant observations
awaiting formalization.

### Observed

The agent filed the eval with an understated evidence base, then found the
fourth instance and disclosed that its original search had omitted
`beliefs/future-beliefs.md`.

### Why this qualifies

The later repository search supplies the missing item and identifies the
omitted search surface. This establishes a coverage failure rather than merely
a later improvement in the analysis.

### Impact

The persisted eval understated its cross-session evidence and risked
fragmenting or discounting an already recorded observation.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

is everything in thread persisted in the pr? anything left to persist?

## Assistant

**Yes — two things, neither of them transcript.** The un-captured tail is just my merge report and this question, which is structural. But the audit turned up two real gaps.

## 1. `session-capture` cites a rule it never states

The policy contains this self-reference:

> "later turns extend the *same* thread doc in place (per the **[session-capture](/meta/policy/session-capture.md) update-in-place rule**)"

That points at itself, and the rule isn't there. The actual statement — *"if this session already has a thread file, append the un-captured exchanges to it"* — lives only in the `/capture` skill, which is where I just edited it.

The reach asymmetry matters: `CLAUDE.md` loads in **every** session; the skill loads only when `/capture` runs. So the authoritative rule for how thread docs are extended sits on the lower-reach surface, and the higher-reach surface points at it circularly. An agent reading the contract alone gets a dangling pointer.

This is the **third** instance of one family this session — a rule and its advertised location drifting apart:

| | Instance | Where it landed |
|---|---|---|
| 1 | Policy body changed, index gloss kept the old rule | filed as an issue |
| 2 | `depends_on` shipped unregistered in the frontmatter schema | recorded in `epistemic-overlay` |
| 3 | Policy cites an update-in-place rule it doesn't state | **unpersisted** |

## 2. The eval understates its own evidence — and a prior session already recorded a fourth instance

I filed `re-derivation-vs-recall` saying "three self-reported instances, one session," and flagged that as thin. `beliefs/future-beliefs.md` contains a fourth, from **2026-07-22**, recorded by a different session:

> "the contract already said 'use `mix brain.url`', yet a dead Pages URL shipped, because the *tool* was wrong (not branch-aware) and the policy also taught a hand-mapping an agent could apply instead."

That's the same signature — an authoritative source existed, a shortcut was taken — and it carries the same conclusion I reached independently: *"Asserting the rule harder in prose does not move reliability… The fix landed in the tool… never in a sterner sentence."*

Which is [the belief I filed](https://github.com/ob6to8/elixir-mind/blob/main/beliefs/remembered-surfaces-are-forgotten-surfaces.md), arrived at from a different direction, months-scale earlier. So the eval's evidence base is four instances across two sessions with one externally corroborated — meaningfully stronger than what its doc claims, and understating it is the kind of inaccuracy that makes a future reader discount the instrument.

**I also should have found this before filing.** `update-in-place` says search the bundle first; I searched `meta/evals/` and `lib/` but not `beliefs/future-beliefs.md`, which is exactly the scratch list for observations-awaiting-formalization. Scoping my search that narrowly is itself an instance of the pattern.
````

## Classification

`epistemic.evidence.scope_omission` fits because the filed evidence-count claim
depended on repository-wide coverage, but the agent omitted a known relevant
surface. The dangling self-reference mentioned nearby is a separate repository
defect and is not part of this incident.

## Detection and correction

A later persistence audit found the prior-session observation. The agent
corrected the eval's evidence base from three one-session instances to four
instances across two sessions.
