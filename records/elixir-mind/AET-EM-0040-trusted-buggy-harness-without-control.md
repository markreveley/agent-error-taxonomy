---
id: AET-EM-0040
title: Trusted a buggy diagnostic harness without a control
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-28-kimi-k3-weight-release-implications.md
source_lines: [402-414, 438-454]
session: https://claude.ai/code/session_01PNFB6CSofNa3rBnNwPVp2D
pull_request: 157
agent_system: Claude Code
agent_model: Claude Opus 5
detection: untouched known-answer control passed
primary_type: verification.instrument.invalid_oracle
secondary_types: []
confidence: medium
---

# Trusted a buggy diagnostic harness without a control

## Error description

The agent trusted failures from a custom diagnostic harness that mangled section
headers and only discovered the false results when an untouched control case
passed.

## Evaluation

### Expected

A custom measurement harness should include a known-answer control before its
results are used to diagnose behavior.

### Observed

The harness produced plausible failures caused by its own formatting changes.
The agent acted on those results for a full diagnostic round before the control
distinguished instrument artifacts from real failures.

### Why this qualifies

The retained account identifies the harness defect, the invalid results, and
the control that exposed them. Status is probable because the harness code and
raw failing outputs were stripped from the persisted render, leaving a detailed
retrospective account rather than independently replayable evidence.

### Impact

The invalid instrument prolonged and distorted diagnosis and produced evidence
that looked like real system failures.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

4

## Assistant

<routes ref="/meta/issues/dev-history-regeneration-silently-skipped-on-shallow-clones.md">
Option 4 turned out to be a ratification rather than a build: the design already works that way, and the investigation deflated my own issue.

Two further measurements settled it. A second test harness of mine was itself buggy — it mangled section headers, so its FAILs were formatting artifacts; the untouched control passing is what proves the corrected reconstruction faithful. With that fixed, the check accepts any number of missing *newest* sections and fails on a removed middle or oldest section. It is suffix-tolerant, unbounded, and exists to catch hand edits and reorderings rather than staleness. And `pages.yml` checks out with `fetch-depth: 0` and re-derives the page on every push to `main`, so the live site is always current.

So the committed copy is a lagging cache, exactly as [lag-tolerant check](/beliefs/glossary/lag-tolerant-check.md) already described — that glossary entry was right the whole time, while three other docs overstated the tolerance as one PR. The issue closed `wontfix`, the overstatements were corrected in the skill and marked in the analysis, and the shallow-clone no-op was reclassified as cosmetic.
</routes>
````

````text
## User

what needs to be done before closing this thread? what exists here but has not persisted? I am trying to close out this thread

## Assistant

<routes ref="em:763494">
Audit done. Nothing is uncommitted or broken — working tree clean, main current, all five PRs merged, gates green.

Four things were stale, and one thing had not persisted at all.

**Three measurement errors in one session, each caught by a different mechanism, and the pattern is nowhere on disk.** Individually they're in the record. But the *pattern* isn't filed, and the pattern is the finding: a summarizing fetch invented a comparison, caught by demanding verbatim text; a `git diff` count included main-merges as regenerations, caught by asking what the number would mean if the method were wrong; and a test harness mangled section headers, producing failures that looked real, caught **only** because the untouched control passed.

The third is the generalizable one and it has no home: a measurement harness needs a control case, or you cannot tell a finding from a bug in your instrument. That failure is invisible by construction — a broken harness produces plausible results, and I acted on them for a full round before the control exposed it.

It also has a live consumer: the fidelity probe plan specifies a scorer with no control row in its gold set. If that belief existed, the plan would be built differently.
</routes>
````

## Classification

`verification.instrument.invalid_oracle` fits because the check was performed,
but the measuring instrument itself introduced the apparent failures and lacked
a control capable of exposing them. This is not an incomplete-check incident.

## Detection and correction

An untouched control unexpectedly passed. The agent fixed the harness, reran
the measurements, and recorded the broader requirement that measurement
instruments include known-answer controls.
