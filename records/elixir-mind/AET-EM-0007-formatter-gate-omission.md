---
id: AET-EM-0007
title: Reported all gates green without running the formatter
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-11-session-init-digest-and-priorities.md
source_lines: [113-121, 129-137]
session: https://claude.ai/code/session_013Zoqs81apKu8AmPkUk7dW2
pull_request: 39
agent_system: Claude Code
agent_model: Claude Fable 5
detection: pull-request CI failure
primary_type: verification.completion.incomplete_check
secondary_types: []
confidence: high
---

# Reported all gates green without running the formatter

## Error description

The agent reported that all gates were green after running contract, registry,
verification, route-tag, and test checks, but omitted the formatter gate that CI
then failed.

## Evaluation

### Expected

A completion report claiming all gates passed should cover the repository's full
required gate suite, including `mix format --check-formatted`.

### Observed

The report enumerated its checks and called them “all gates green.” The first CI
run failed formatting, and the agent acknowledged that its local suite had not
included the formatter.

### Why this qualifies

The CI result directly establishes the omitted required check and falsifies the
completion report's scope. The agent's correction supplies the causal account.

### Impact

The pull request entered CI in a known-invalid repository state, requiring a
follow-up formatting commit and delaying the merge.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

PR opened: **https://github.com/ob6to8/second-brain/pull/39**

The full `/create-pull-request` flow ran to completion:

1. **Captured** the session as `meta/threads/2026-07-11-session-init-digest-and-priorities.md` — verbatim render (two kept assistant blocks plus your messages), a routing ledger with three closed strands, and one dangling note carried forward: *soften the open-every-session agent note if the appraisal proves noisy*. Route tags are path back-links to the new tooling files (no concept sinks, so no excerpt logs to materialize).
2. **Glossaried** the thread: one new term, [session-init digest](/glossary/session-init-digest.md) (`em:6f2442`), and the existing **SessionStart hook** entry extended with the context-injection nuance (hook stdout briefs the agent) plus a third citation. Registry, glossary index, and both logs updated.
3. **Committed and pushed** to `claude/session-init-log-priorities-vuvzo6` (two commits: the feature, then capture + glossary), with all gates green — contract, registry, verify, route-tags, and 81/81 tests.
````

````text
## User

Merge

## Assistant

Merged — PR #39 is squash-merged to `main` as `524c95e`.

One bump along the way: the first CI run failed on `mix format --check-formatted` (a gate my local check suite didn't include — I'd run verify/route-tags/tests but not the formatter). I formatted the two new files, confirmed 81/81 tests still pass, pushed the fix, waited for CI to go green, then merged.
````

## Classification

`verification.completion.incomplete_check` fits because the agent made a broad
completion claim after executing only a subset of the required verification
suite. The error is not merely that formatting was wrong; it is the incomplete
check behind the green report.

## Detection and correction

CI detected the formatting failure. The agent formatted the files, reran tests,
pushed the fix, waited for green CI, and then merged.
