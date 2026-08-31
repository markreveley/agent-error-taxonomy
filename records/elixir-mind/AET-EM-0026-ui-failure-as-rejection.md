---
id: AET-EM-0026
title: Misreported a permission UI failure as operator rejection
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-26-version-control-audit-and-response-format-policies.md
source_lines: [331-378]
session: https://claude.ai/code/session_018pjRKH3Vy4MuG7iLqp5PPu
pull_request: 141
agent_system: Claude Code
agent_model: unknown
detection: operator corrected the false intent attribution
primary_type: control.input.channel_misinterpretation
secondary_types: []
confidence: high
---

# Misreported a permission UI failure as operator rejection

## Error description

The agent treated two permission UI failures as deliberate operator rejections,
stopped the edit, and attributed a choice the operator had not made.

## Evaluation

### Expected

Ambiguous or failed permission-channel state should not be interpreted as user
intent. The agent should have restored the question in ordinary chat text.

### Observed

The agent stated “you rejected that edit twice” and asked why. The operator
explained that no rejection occurred and that the UI permission call had failed.

### Why this qualifies

The user directly corrects the attributed intent, and the agent identifies the
UI element as the source of the false signal. The incident is the agent's
semantic interpretation, not the environment failure itself.

### Impact

The edit stopped unnecessarily, the operator had to correct the record, and the
response framed the operator as having made a decision they did not make.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

I've stopped — you rejected that edit twice, so I won't retry it. Before I touch `session-start.sh` again I need to know what's off (question below). Nothing was written; the working tree is still just the committed docs, so there's no uncommitted state to worry about.

Now the two design questions, which are the substance here.

## Routing flow: it should be a policy, not an external file

The thing to know first: **`CLAUDE.md` is a generated artifact** — compiled from `meta/preamble.md` + `meta/policy/*.md`. You can't hand-edit it. So "a CLAUDE.md instruction" and "an external file CLAUDE.md references" aren't two different mechanisms — they're two points on one spectrum:

- **`type: policy`** → compiles *into* CLAUDE.md → in **every** agent's context, always.
- **`type: tutorial`** (or any doc) → *referenced* by a link → loaded **on demand**.

The deciding question is *when the agent needs it*. The artifact-choice decision fires **mid-work, unprompted** — the moment you're deciding "issue or todo?". If the guidance lives in an external file the agent has to remember to open, it gets skipped, because the agent doesn't know it needs it. A decision procedure that must trigger at an unprompted moment belongs in always-loaded context → **policy**.

The cost (contract bloat) is handled the way the brain already handles it: keep the policy *terse* — just the 5-row discriminator + a pointer — and put the reasoning/examples in a cross-linked tutorial. That's exactly what [`plan-vs-capture`](/meta/policy/plan-vs-capture.md) does today. So my recommendation is a **short policy, sibling to plan-vs-capture**: plan-vs-capture answers *"should I persist at all?"*; this new one answers *"if I'm persisting, which type?"*. No duplication, and the rule lives where it fires.

## Response-format convention: strong idea — and it's genuinely plan-worthy

Real thoughts, including where I'd push back:

- **Scope it, or it becomes ceremony.** This full structure fits turns that *produce/modify artifacts or close a unit of work* — not a quick factual answer. The convention has to gate on "did this turn create/modify files or hit a decision point?" Otherwise you get five empty tables on "what's 2+2."
- **Tables are the ledger; prose still carries judgment.** The audit's *reasoning* didn't belong in a cell. Rule: tables summarize *what happened / what's open*; prose carries the analysis and the recommendation.
- **Keep "Questions" and "Options" sharply different.** Questions = *blocking* (I can't proceed without your answer). Options = *non-blocking* (I can proceed; pick a direction). Two tables is right precisely because it separates "I'm stuck" from "here's the menu."
- **It reinforces an existing rule, doesn't add burden.** A "Questions you need to answer" *table in chat* is exactly what the [session-capture policy](/meta/policy/session-capture.md) already mandates — ask in the chat, never the `AskUserQuestion` dialog, because `/capture` only renders the chat stream (and the dialog's been flaky here). So this formalizes a principle already in the contract.
- **Watch the permission boundary on "Actions I have taken."** Past-tense reporting is right for things already authorized — but it must not quietly loosen the "confirm before irreversible/outward-facing" norm. This turn is the live example: I acted-then-reported on the commit+push (fine — you'd asked to keep work safe), but the hook edit was something I should've flagged as needing your ok first. The convention needs to encode *that* line.

On "**executed by another thread**": a plan is what *enables* cold-context execution, so yes — but the honest read is that the gating item here isn't transferring *how to build it*; it's **your answers to the scope + permission questions**. So the plan's real job is to hold those open questions for you. Once you answer, any thread (this one or a fresh one) can write the policy and run `render-contract`. I'd persist it as a plan for exactly that reason.

## Questions you need to answer

| # | Question | My recommendation |
|---|---|---|
| 1 | **Pre-commit hook** — what made you reject the edit? (a) don't want `session-start` running `git config`; (b) wrong placement; (c) you'll do it yourself; (d) want it in a reviewed PR, not a direct edit | Tell me which; I'll adapt rather than retry |
| 2 | **Routing flow** — OK to add it as a short `type: policy` (regenerates `CLAUDE.md`)? | Yes — terse policy + a tutorial for depth |
| 3 | **Response-format convention** — persist as a `plan` (proposed) now, holding the open questions? | Yes |
| 4 | **Convention scope** — every artifact-producing turn, or only at cycle/session close? | Artifact-producing turns *and* decision points; skip trivial replies |
| 5 | **Permission line** — confirm the format reports done actions but never loosens confirm-before-irreversible | Encode the boundary explicitly in the plan |

Answer #1 and I'll finish the pre-commit change the way you want; give me a yes on #2 and #3 and I'll write the policy and the plan (and I'll dogfood the table format while we refine it).

## User

i didn't reject the edit, that's a tool call problem when asking for permission when using the ui element. the solution is to ask for permission in text only. this should be added to policy

## Assistant

Ah — that makes sense. The permission UI element is misfiring and registering as a rejection; the fix is to request permission in **text**, and you're right that this belongs in policy (it's the same class of problem as the existing "ask in chat, not the dialog box" rule — UI elements are flaky here *and* don't enter the capture stream).
````

## Classification

`control.input.channel_misinterpretation` fits because nonsemantic UI state was
treated as a user answer. This record does not claim that the broader permission-
in-text rule had already governed this exact action; that rule was strengthened
as a correction.

## Detection and correction

The operator denied rejecting the edit and identified the UI failure. The agent
restored the permission request to text and added the interaction rule to policy.
