---
id: AET-EM-0039
title: Propagated wrong checker semantics into a filed issue
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-28-kimi-k3-weight-release-implications.md
source_lines: [386-400]
session: https://claude.ai/code/session_01PNFB6CSofNa3rBnNwPVp2D
pull_request: 157
agent_system: Claude Code
agent_model: Claude Opus 5
detection: empirical deletion test of the checker
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Propagated wrong checker semantics into a filed issue

## Error description

The agent repeated documentation claiming that the development-history checker
tolerated exactly one missing pull request without inspecting or testing its
implementation, then filed an issue using that premise.

## Evaluation

### Expected

Before diagnosing a gate failure and persisting remedies, the agent should
inspect or empirically test what the checker enforces.

### Observed

The agent said the design tolerated one missing pull request while the actual
lag was six. A deletion test then passed after all six newest sections were
removed, demonstrating that the checker tolerated an unbounded missing suffix.

### Why this qualifies

The empirical test directly disproves the claimed behavior. The agent also
states that it copied the prose claim into a durable issue without checking the
code's actual bound.

### Impact

The filed issue contained a false defect diagnosis and its options omitted the
more important fact that CI could not detect any amount of newest-history lag.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

what are the options for 1?

## Assistant

<routes ref="/meta/issues/dev-history-regeneration-silently-skipped-on-shallow-clones.md">
I need to correct something before answering — the premise in my filed issue is wrong, and I just proved it.

**CI does have full history and does run the check.** So the six-PR gap should have failed CI. It didn't. I tested why: I deleted the six newest sections from the file and ran the check. It passed clean, exit 0.

The check tolerates *any* amount of missing history, not one PR's worth. It only verifies that what's in the file is correct — anything missing off the top is fine by it. The skill doc says "lag-tolerant by exactly one PR" and that's what I repeated into the issue, but the code enforces no bound at all. That's the third time this session I've asserted something the evidence didn't support, and this time I propagated it into a filed document.

So there are **two separate holes**, not one: sessions don't regenerate (the shallow clone, silent), and nothing detects it (CI checks with full history and passes anyway). The second is the more important, and my earlier options list didn't address it at all.
</routes>
````

## Classification

`epistemic.claim.direct_check_omission` fits because this was a precise claim
about executable checker behavior that code inspection or a cheap deletion test
could resolve. The incorrect durable issue is impact, not a separate provenance
incident.

## Detection and correction

The agent tested the checker after the operator requested options. It corrected
the issue premise, separated the two actual gaps, and later closed the original
issue as `wontfix` after further investigation.
