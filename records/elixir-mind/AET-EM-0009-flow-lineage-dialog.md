---
id: AET-EM-0009
title: Built flow-lineage defaults after losing dialog answers
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-12-fuzzy-search-spike-and-flow-lineage.md
source_lines: [106-134, 136-149]
session: https://claude.ai/code/session_01RiBxtQQbyiWPW39PkhByij
pull_request: 56
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator supplied screenshot of the dialog answers
primary_type: control.input.channel_misinterpretation
secondary_types: []
confidence: high
---

# Built flow-lineage defaults after losing dialog answers

## Error description

The agent proceeded with its own flow-lineage defaults instead of the operator's
submitted dialog answers, choosing prose-only encoding, omitting the thread from
the chain, and deferring the retrofit differently.

## Evaluation

### Expected

The implementation should have followed the operator's answers: canonical
frontmatter, a derived registry/flowchart, inclusion of the thread, and a
persisted retrofit plan after the reference instance.

### Observed

The agent proposed and began from prose-blockquote defaults. After the operator
provided a screenshot, the agent recovered the actual answers, stated that it
had gotten both wrong, and documented three concrete divergences.

### Why this qualifies

The persisted screenshot notation contains the answer content, while the
assistant's correction table preserves its different defaults and the corrected
implementation. This directly establishes the input mismatch.

### Impact

The lineage feature was initially shaped around the wrong source of truth and an
incomplete chain, requiring a correction to its schema, derived output, and plan.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="/meta/plans/flow-lineage-index.md">
## The proposal: a standardized "Lineage" header on flow docs

A flow doc gets a short, consistently-placed blockquote right under the title — a one-line walk of the arc from problem-identified to running-system, with each hop a link.

Why this shape fits the bundle's grain:

- **It closes the loop.** The backward links already exist (flow→plan→analysis); this adds the one missing edge — the analysis/plan gaining a *forward* pointer to what they became — and puts the whole chain in one glance instead of three hops.
- **Points, doesn't restate** — the discipline the flows genre already follows. It's four links and a clause, not a retelling.
- **Heterogeneous by design.** Not every flow has the full chain. `session-capture` and `render-contract` predate the analysis→plan discipline; the flows genre *itself* came from the flows-genre plan with no upstream analysis. So the header omits absent hops and can note "no originating analysis — emerged directly as a plan." Honest gaps beat forced ones.
- **It's a genre-convention change**, so it belongs codified in `meta/flows/index.md` (the genre definition) and noted in the flows-genre plan — and, per the contract, that's a change to the *shape* of the brain that you ratify, which is exactly what you're doing here.

One connection worth flagging: this is a lightweight, prose version of what the epistemic-overlay plan (`proposed`) wants to make a first-class typed graph (analysis *inspires* plan, plan *implemented-by* PR). I'd treat this flow-header convention as the pragmatic now-move and let it inform that plan later, rather than building the graph machinery for this.
</routes>

## User

_[operator attached a screenshot of their in-app answers to the two design questions]_ You can See what my responses actually were here, and they were different from your recommended

## Assistant

Thank you — that's an important correction. Your actual answers were **not** my defaults. Let me read them precisely:

- **Encoding:** *"What if we do frontmatter, and then a registry/index can be derived which acts as a flowchart of sorts? Also we need to include the thread"* → **frontmatter as canonical**, a **derived index/flowchart** generated from it, and the **thread** included in the chain.
- **Scope:** *"Begin with this step, then make a plan to retrofit all flow docs"* → do the reference instance now, then **persist a plan** for the full retrofit + the derived index.

So I got both wrong. Let me correct: convert the reference instance to frontmatter, include the thread, and write the retrofit plan.
````

````text
## Assistant

<routes ref="/meta/plans/flow-lineage-index.md">
Corrected and pushed. Here's what changed once I could read your actual answers.

## What your answers changed

| Fork | My wrong default | Your answer | Now built |
|---|---|---|---|
| **Encoding** | prose blockquote only | **frontmatter canonical + a derived registry/index acting as a flowchart** | `lineage:` frontmatter is the source of truth; the blockquote and a cross-flow flowchart are *derived* from it |
| **The chain** | analysis → plan → PR | *"also include the thread"* | analysis → plan → **thread** → PR → flow |
| **Scope** | dedup instance + convention, backfill later | *"begin with this step, then make a plan to retrofit all"* | dedup instance done + a persisted `type: plan` for the full retrofit |

The reference instance (`meta/flows/dedup-recall-probe.md`) now carries the canonical `lineage:` block, the plan (`meta/plans/flow-lineage-index.md`, `status: in-progress`) captures the frontmatter schema + the derived flowchart tooling + the retrofit, and four open questions remained for you to ratify before I built the tooling.
````

## Classification

`control.input.channel_misinterpretation` fits because the agent substituted its
defaults for answers submitted through an interaction channel it failed to
recover. The design itself is not classified as an error; the input-channel
mismatch is.

## Detection and correction

The operator supplied a screenshot. The agent extracted the answers, enumerated
the divergences, and rebuilt the reference instance around canonical frontmatter,
the expanded chain, a derived index, and a persisted retrofit plan.
