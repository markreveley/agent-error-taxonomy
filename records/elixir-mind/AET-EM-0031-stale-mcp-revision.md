---
id: AET-EM-0031
title: Treated a live dated MCP specification URL as current
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-cca-study-program-and-the-primary-source-miss.md
source_lines: [480-515, 562-574]
session: https://claude.ai/code/session_01Ri7NUzzCx6Pb7Jb2vrmU2a
pull_request: 149
agent_system: Claude Code
agent_model: unknown
detection: specification revision inventory
primary_type: epistemic.source.authority_misuse
secondary_types: []
confidence: medium
---

# Treated a live dated MCP specification URL as current

## Error description

The agent filed two MCP documents from the 2025-06-18 revision because its dated
canonical URL remained live, without checking that 2025-11-25 was current.

## Evaluation

### Expected

A dated specification path should be compared with the protocol's current index
or revision listing before being represented in newly filed current knowledge.

### Observed

The retained correction identifies the captured and current revisions and says
both filed documents required explicit revision notes and planned re-verification.

### Why this qualifies

The account strongly identifies a source-currency error, but the underlying MCP
index result and original currentness assertion are not preserved in the
transcript. The status is therefore probable.

### Impact

New knowledge documents captured stale protocol information without initially
signaling that their source revision was not current.

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
````

## Classification

`epistemic.source.authority_misuse` fits because an older still-live revision was
treated as the current authority when a newer canonical revision existed.
Evidence-scope omission is less precise: the failure centers on source currency
and authority, not a broad absence claim.

## Detection and correction

A revision inventory found the current specification. The agent added captured-
revision notes to the two documents and put re-verification into the plan.
