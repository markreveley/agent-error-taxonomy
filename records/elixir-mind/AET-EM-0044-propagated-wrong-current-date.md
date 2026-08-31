---
id: AET-EM-0044
title: Propagated the wrong current date into new artifacts
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-29-post-action-readback-belief-and-plan.md
source_lines: [393-405]
session: https://claude.ai/code/session_01DVYRTueTVHEGm2q2RuhhTf
pull_request: 209
agent_system: Claude Code
agent_model: Claude Opus 5
detection: pre-capture date and commit-timestamp check
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: medium
---

# Propagated the wrong current date into new artifacts

## Error description

The agent resumed a session under an old date and propagated that date into
current timestamp or dated-row values on artifacts newly created on July 31.

## Evaluation

### Expected

Current filing metadata should use the execution date established by the system
clock and commit timestamps, while older write-once attribution dates should
remain unchanged.

### Observed

The agent reported using July 29 metadata although `date -u` and commit
timestamps showed July 31. Its next report narrowed the scope: two artifacts
were genuinely first filed on July 29, while `em:01abda` and the source capture
were minted on July 31.

### Why this qualifies

The retained reports establish a current-date mismatch, but they conflict about
its original scope and do not reproduce the four file diffs or every field
value. The accepted incident is therefore probable and limited to incorrect
current timestamp or dated-row values on the newly minted July 31 artifacts. It
does not treat every July 29 `attribution.when` value as erroneous.

### Impact

Incorrect dates entered new artifacts and a dedup row, weakening their temporal
metadata until the targeted repair.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

<command-message>create-pull-request</command-message>
<command-name>/create-pull-request</command-name>
<command-args>merge</command-args>

## Assistant

I caught something before running `/capture`: every document I filed this session is dated **2026-07-29**, but the actual date — confirmed by `date -u` and by every commit's real git timestamp — is **2026-07-31**. I mis-set `timestamp`/`attribution.when` at the start of the session and carried the error through four files and a dedup gold row. Fixing it now, before capture freezes it into the thread doc and the commit history.

## Assistant

Real bug found: my "date fix" over-corrected. `attribution.when` is write-once by policy — it must record the original filing event, not the latest edit. The session log proves `em:674c8f` and the plan were genuinely first committed **2026-07-29T20:24:35Z**; only `em:01abda` and the source capture were genuinely minted on 07-31. My blanket fix wrongly rewrote two immutable `attribution.when` fields. Reverting those precisely.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the current date was a
cheap, directly checkable environment fact that was used incorrectly while
filing new artifacts. The subsequent overbroad repair is a separate execution
incident recorded as `AET-EM-0045`.

## Detection and correction

Before capture, the agent compared the metadata with `date -u`, commit
timestamps, and creation history. It narrowed the repair to fields associated
with artifacts actually minted on July 31.

