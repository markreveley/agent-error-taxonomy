---
id: AET-EM-0038
title: Presented a synthesized model comparison as sourced
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-28-kimi-k3-weight-release-implications.md
source_lines: [129-141, 249-264]
session: https://claude.ai/code/session_01PNFB6CSofNa3rBnNwPVp2D
pull_request: 157
agent_system: Claude Code
agent_model: Claude Opus 5
detection: primary-source grounding pass
primary_type: epistemic.claim.synthesis_as_evidence
secondary_types: []
confidence: medium
---

# Presented a synthesized model comparison as sourced

## Error description

The agent presented a precise K3-to-Fable wall-clock comparison as if it were
supported by the cited source, although it had come from a summarizing fetch and
was not present in quotable source text.

## Evaluation

### Expected

Precise quantitative comparisons used in a durable analysis should be traced to
verbatim source spans or clearly labeled as derived calculations.

### Observed

The agent asserted that K3 took about 2.5 times Fable 5's wall-clock time. During
a grounding pass, it reported that the source stated K3's values but did not
state the comparative Fable figures, and removed the comparison.

### Why this qualifies

The original quantitative claim and the later provenance correction are both
retained. The incident remains probable because the external Artificial
Analysis page and its verbatim comparator are not reproduced in the thread; the
source mismatch rests on the agent's detailed later account.

### Impact

The unsupported number entered a filed industry analysis and strengthened an
economics argument with false quantitative precision.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="em:68d1b3">
## The implications

Seven, in rough order of how much they should change your priors.

**The open-to-closed gap is now months.** K3 scores 57 on the AA Intelligence Index — third overall, comparable to Opus 4.8 and GPT-5.5, behind only Fable 5 and GPT-5.6 Sol — and 1543 Elo on AA-Briefcase, second only to Fable 5 and *above* Opus 4.8 (1347). Lambert's read: "the open-to-closed or American-to-Chinese model performance gap has been reduced from the debated 6-9 months to something shorter, say 3-5 months."
</routes>

<routes ref="em:51aede">
**Open no longer implies cheap — and that inverts the margin-collapse thesis.** This is the finding I'd flag hardest, because it cuts against what's already in the brain. K3's API prices at **$3.00/$15.00 per MTok — exactly Claude Sonnet 5** — versus K2.6's $0.95/$4.00. On AA-Briefcase it costs $10.57/task and 56.4 min/task, ~2.5× Fable 5's wall-clock. [Alderson's margin-collapse argument](https://github.com/ob6to8/elixir-mind/blob/main/knowledge/ai-industry/ai-margin-collapse-glm-5-2.md) rested on open models matching frontier quality "at a fraction of the price"; K3 matches the quality and declines the discount. The pressure on closed-lab margins becomes a *floor* effect — a credible fallback exists — not the price collapse the thesis predicted.
</routes>
````

````text
## User

1, 2
then /create-pull-request merge

## Assistant

<routes ref="em:51aede">
The grounding pass did what grounding passes are for: it caught two figures I had asserted more confidently than the sources supported. I had written that K3 runs *"~2.5× Fable 5's wall-clock"* on AA-Briefcase and that Fable 5 finishes in 67 turns to K3's 83 — both came from a summarizing fetch, and neither survived re-reading the article for verbatim text. The article states K3's 56.4 minutes and 83 turns; it does not state Fable 5's comparative figures in the passages I could quote. Both are now gone, replaced by what Artificial Analysis actually says — including its own blunt summary, which is better evidence than my paraphrase was: K3 is *"particularly expensive when comparing to other open weight models of similar size. It's also notably slow and very verbose."*

The DeepSeek V4 Pro $0.04-per-task figure survives, but attributed: it comes from the-decoder, not from Artificial Analysis, and secondary reporting does not belong in a `source` capture backing `verified: true`. It now reads as reported rather than as established.
</routes>

Both landed. [PR #159](https://github.com/ob6to8/elixir-mind/pull/159) merged as `2d813e4`, branch deleted.

The grounding pass earned its keep by falsifying two of my own figures. I had written that K3 runs "~2.5× Fable 5's wall-clock" on AA-Briefcase and that Fable 5 finishes in 67 turns against K3's 83 — both came from a summarizing fetch, and neither survived re-reading the article for quotable text. That's a specific, repeatable failure mode: a fetch that answers a question in prose will happily synthesize a comparison the source never made, and it reads exactly like a quoted figure once it's in your notes. Demanding verbatim text is what separates them. Artificial Analysis's own summary turned out to be stronger evidence than my paraphrase anyway — *"particularly expensive when comparing to other open weight models of similar size. It's also notably slow and very verbose."*
````

## Classification

`epistemic.claim.synthesis_as_evidence` fits because a summarizing fetch's
derived comparison was presented with the authority of source-backed fact. The
nearest alternative is direct-check omission, but the more specific failure is
the loss of provenance between synthesis and source text.

## Detection and correction

A grounding pass required quotable primary-source text. The comparison failed
that check and was removed. The related 67-turn comparison is subsidiary only,
because it is not visible in the initial retained response.
