---
id: AET-EM-0042
title: Reported generated excerpts as live broken links
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-29-repo-evaluation-against-the-second-brain-field.md
source_lines: [165-177]
session: https://claude.ai/code/session_01XGMF8Zw3DbevFk46hHvCBH
pull_request: 188
agent_system: Claude Code
agent_model: Claude Opus 5
detection: targeted inspection after operator selected the repair option
primary_type: verification.instrument.invalid_oracle
secondary_types: []
confidence: high
---

# Reported generated excerpts as live broken links

## Error description

The agent's link audit classified twelve strings in generated transcript
excerpts or illustrative code as broken links on live, hand-authored surfaces
and offered to repair them.

## Evaluation

### Expected

The link-health measurement should exempt generated frozen excerpts and
illustrative code spans before reporting actionable live-surface failures.

### Observed

The agent offered to fix approximately twelve live-surface broken links. Direct
inspection after the option was selected showed that every candidate was
generated or illustrative and that the hand-authored live count was zero.

### Why this qualifies

The inspected population directly contradicts the audit's classification. The
verification instrument measured strings outside the population to which its
“live broken link” conclusion applied.

### Impact

The false-positive result understated repository link hygiene and proposed
unnecessary edits to frozen or illustrative material.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

4, then 1

## Assistant

<routes ref="meta/analysis/second-brain-field-re-evaluation-at-615-documents.md">
Confirmed — every one of those twelve sits inside a `## Thread excerpts` block (generated verbatim from frozen threads) or an illustrative code span. My earlier figure was wrong in kind: hand-authored broken links on live surfaces is **zero**, not twelve. Let me check the README, which is a real live surface.
</routes>

## Orientation

Option 4 turned out smaller than advertised and option 1 is filed. The twelve "broken links" I reported last turn were not broken links — every one sits inside a generated block that quotes frozen session transcripts verbatim, or inside a code-formatted example. The repo's real count of hand-authored dead links on live pages is **zero**. That's a better result than I gave it, and it moves the link-hygiene evidence behind dimension 6.
````

## Classification

`verification.instrument.invalid_oracle` fits because the audit's population
and exemption logic could not support its live-surface result. A direct-check
omission occurred during reporting, but the narrower cause is a verifier that
included non-actionable generated and illustrative text.

## Detection and correction

After the operator selected the repair option, the agent inspected all twelve
candidates, corrected the live count to zero, and repaired a genuinely stale
README description instead.
