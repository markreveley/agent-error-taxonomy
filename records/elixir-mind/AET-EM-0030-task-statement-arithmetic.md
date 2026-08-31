---
id: AET-EM-0030
title: Asserted a task-statement total before summing it
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-cca-study-program-and-the-primary-source-miss.md
source_lines: [480-515, 562-576]
session: https://claude.ai/code/session_01Ri7NUzzCx6Pb7Jb2vrmU2a
pull_request: 149
agent_system: Claude Code
agent_model: unknown
detection: mechanical numbering and arithmetic sum
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: medium
---

# Asserted a task-statement total before summing it

## Error description

The agent reported 29 task statements before adding the extracted domain counts,
which sum to 30.

## Evaluation

### Expected

The agent should have performed the cheap arithmetic check `7+5+6+6+6` before
stating the total.

### Observed

The retained correction says the agent asserted 29 first and that automatic
numbering exposed the correct total of 30.

### Why this qualifies

The arithmetic and detailed correction strongly support the error, but the
original 29-count utterance is absent from the persisted render. The incident is
therefore probable rather than confirmed.

### Impact

An incorrect exam-blueprint count briefly entered the study-program work and
could have affected coverage accounting.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

Done — ready for you to invoke `/create-pull-request`.

## What the spike found

Anthropic's authoritative docs span **seven hosts**, and the split isn't intuitive:

| Host | Owns |
|---|---|
| `anthropic.com` | corporate news, research, policy, `/learn` |
| `claude.com` | product marketing, blog, `/partners`, `/resources/courses`, `/resources/certifications` |
| `platform.claude.com` | the Claude API — Messages, tool use, caching, batches, Managed Agents |
| `code.claude.com` | Claude Code **and** the Agent SDK |
| `anthropic-partners.skilljar.com` | Partner Academy — certification catalog and **all four exam guides** |
| `support.claude.com` | help center, billing, compliance |
| `modelcontextprotocol.io` | the MCP spec, SEPs, registry, governance |

Two findings I didn't expect. **The redirect chain hides the topology** — `docs.claude.com` 301s to *either* `platform.` or `code.` depending on path, so an agent following redirects lands correctly while never learning two hosts exist. The knowledge needed to search well is exactly what the redirects conceal. And **both doc hosts publish `llms.txt` indexes** — a complete machine-readable page index. Fetching one is strictly better than searching, and should be the first move against either host.

I filed this as an `analysis`, not a policy. The contract loads in full every session and should carry rules that fire unprompted; a vendor source map is consulted once you've already decided to research Anthropic. The one genuinely general rule — *report absence relative to the scope searched* — I left as an open question rather than smuggling it in under a vendor map. It's the actual lesson and deserves its own decision.

## The gaps, closed

All four exam guides recovered. They're **different roles, not tiers of one syllabus**:

| | Items | Fee | Domains | Heaviest domain |
|---|---|---|---|---|
| `CCAO-F` Associate | 60 | $99 | 7 | Output Evaluation & Validation 21% |
| `CCDV-F` Developer | 53 | $125 | 8 | Applications & Integration 33.1% |
| `CCAR-F` Architect–F | 60 | $125 | 5 | Agentic Architecture & Orchestration 27% |
| `CCAR-P` Architect–P | 63 | $175 | 7 | Integration 19% |

The sharpest contrast: **only `CCAR-F` treats Claude Code configuration as a major domain — 20%, against the Developer exam's 3.1%.** And Architect Professional trades orchestration and tool design for governance, stakeholder communication, and lifecycle management. Worth knowing before choosing a target credential.

Two corrections to my own work this session: the count is **30** task statements, not 29 — I asserted it before summing the per-domain counts (7+5+6+6+6), and the auto-numbering caught it. And the **MCP spec's current revision is 2025-11-25**; the two MCP docs I filed captured 2025-06-18. Dated revision paths stay live indefinitely without signalling staleness, so both now carry an explicit captured-revision note and re-verification is in the plan.
````

````text
## Assistant

Taking the hardest question first, because it determines the answer to the other two.

## Were any of today's errors hallucinations?

No — none of the three. That's the crux, and it's worth being precise:

| Error | What actually happened | Kind |
|---|---|---|
| "No primary source states the price" | A **true** statement about my search, generalized to a claim about the world | scoping |
| MCP spec at 2025-06-18 | A **real** revision at a **live** canonical URL | currency |
| 29 task statements | Arithmetic on data I had **correctly** extracted | computation |

Zero fabrications. Nothing was invented — every input was real and every intermediate step was sound. The failures happened at the *reporting* and *currency* boundaries, not the generation boundary.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the precise numeric claim
had an immediate arithmetic check that materially disproved it. The probable
status reflects missing original-assertion evidence, not ambiguity in the sum.

## Detection and correction

Automatic numbering exposed the mismatch. The agent summed the domain counts and
corrected the total to 30.
