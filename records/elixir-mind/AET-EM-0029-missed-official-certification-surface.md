---
id: AET-EM-0029
title: Declared primary certification evidence absent after searching too narrowly
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-cca-study-program-and-the-primary-source-miss.md
source_lines: [372-411, 413-426]
session: https://claude.ai/code/session_01Ri7NUzzCx6Pb7Jb2vrmU2a
pull_request: 149
agent_system: Claude Code
agent_model: unknown
detection: operator supplied the official Skilljar catalog and pointed out prices
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: high
---

# Declared primary certification evidence absent after searching too narrowly

## Error description

The agent claimed certification prices were third-party-only and the exam guide
was gated after searching only two first-party host families and failing to
follow an official catalog link.

## Evaluation

### Expected

A world-level absence claim should follow an inventory of the relevant official
source surface and links from already-read first-party pages, or be explicitly
bounded to the hosts actually searched.

### Observed

The agent generalized from searches limited to `anthropic.com` and `claude.com`.
The operator supplied Anthropic's Skilljar tenant, which published official
prices and linked a public 39-page exam guide.

### Why this qualifies

The original negative claim, omitted host scope, official contrary page, prices,
and public guide are all identified in the correction sequence. The individual-
eligibility question remains unresolved and is not classified as part of this
incident.

### Impact

Primary evidence was misclassified as unavailable, causing the plan to treat its
largest blueprint source and official prices as absent or third-party.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

is this not an official anthropic site? https://anthropic-partners.skilljar.com/page/partner-certifications

## Assistant

Yes — that's official Anthropic. Skilljar is just the LMS vendor; `anthropic-partners.skilljar.com` is Anthropic's own Partner Academy tenant. I already treated it as primary: the four-pillar scope sentence in the plan is cited from that domain.

What I claimed was gated is narrower — the **Exam guide PDF** linked from the certification page. Let me check whether that's actually true, since if the catalog page is public the PDF may be too.

## User

there are prices on that page

## Assistant

<routes ref="em:bdfa05">
Confirmed — and those prices are now **primary-sourced**, which retires my earlier caveat. From Anthropic's own Partner Academy catalog:

| Certification | Price |
|---|---|
| Claude Certified Associate – Foundations | $99 (does not count toward Partner Network tier eligibility) |
| Claude Certified Developer – Foundations | $125 |
| Claude Certified Architect – Foundations | $125 |
| Claude Certified Architect – Professional | $175 |

The PDF downloaded but didn't parse as text. Reading it directly:
</routes>

## User

you claimed the prices were third party only. so you were unable to surface this page in your searches?

## Assistant

You're right, and that's my error. Let me own it precisely.

I fetched the Academy's *individual* CCA certification page, which doesn't show pricing, and my `site:` searches were scoped to anthropic.com and claude.com — so they never touched the skilljar tenant at all. I then concluded "no primary source states the price" from "the primary pages I happened to check don't state it." That's an absence-of-evidence overreach, and it's exactly the error the quarantine discipline was supposed to prevent: I misclassified a fact as third-party-only when Anthropic publishes it on a public catalog page one link away from a page I had already read.

The quarantine *logic* was sound; my classification of one fact was wrong. The plan now records that wrong claim and needs correcting. Let me get the blueprint first — the extraction hit font-subset encoding.
````

````text
## User

what else have you failed to surface, if this is in fact the case? could it be worth a research spike?

## Assistant

<routes ref="em:214aa4">
Yes — official. Skilljar is the LMS vendor; `anthropic-partners.skilljar.com` is Anthropic's own Partner Academy tenant. And it doesn't just have prices — **the complete 39-page exam guide is public on that page**, served from an S3 `/public/` path with no login. That was the single largest open question in the plan, and it was one link from a page I had already read.

## What went wrong, precisely

I fetched the Academy's *individual* CCA certification page, which states scope but no pricing or blueprint. My `site:` searches were scoped to `anthropic.com` and `claude.com`, so they never touched the skilljar host at all. I then concluded "no primary source states the price" from "the primary pages I happened to check don't state it."

That's absence of evidence asserted as evidence of absence — and it's the exact failure the quarantine discipline exists to prevent. The discipline was sound; my classification of the facts was wrong, in the more damaging direction: I told you real primary data was third-party.
````

## Classification

`epistemic.evidence.scope_omission` fits because a broad absence claim depended
on coverage, and an omitted official host materially changed the result. Source-
authority misuse is less precise because the relevant source was not found at all.

## Detection and correction

The operator supplied the official page and pointed out its prices. The agent
followed its links, found the public guide, corrected the plan, and performed a
broader source-inventory spike.
