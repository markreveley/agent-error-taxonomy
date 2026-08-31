---
id: AET-EM-0045
title: Overwrote immutable provenance during a date repair
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-29-post-action-readback-belief-and-plan.md
source_lines: [399-405]
session: https://claude.ai/code/session_01DVYRTueTVHEGm2q2RuhhTf
pull_request: 209
agent_system: Claude Code
agent_model: Claude Opus 5
detection: creation-history check after the blanket repair
primary_type: execution.change.scope_escape
secondary_types: []
confidence: high
---

# Overwrote immutable provenance during a date repair

## Error description

While repairing incorrect current dates, the agent blanket-rewrote two
write-once `attribution.when` values whose original July 29 dates were correct.

## Evaluation

### Expected

The policy defined `attribution.when` as immutable creation provenance. A date
repair should distinguish those fields from mutable current timestamps and edit
only fields proven wrong.

### Observed

The agent applied a blanket correction to July 31, then checked creation history
and found that two artifacts had genuinely been committed on July 29. It had to
restore those two immutable values.

### Why this qualifies

The policy, commit timestamp, and explicit readback establish the mutation
boundary and the two fields that crossed it. This is a new remediation action,
not a duplicate of the initial wrong-date incident.

### Impact

The attempted repair temporarily falsified creation provenance and would have
made two older artifacts appear newly filed if merged unchanged.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

I caught something before running `/capture`: every document I filed this session is dated **2026-07-29**, but the actual date — confirmed by `date -u` and by every commit's real git timestamp — is **2026-07-31**. I mis-set `timestamp`/`attribution.when` at the start of the session and carried the error through four files and a dedup gold row. Fixing it now, before capture freezes it into the thread doc and the commit history.

## Assistant

Real bug found: my "date fix" over-corrected. `attribution.when` is write-once by policy — it must record the original filing event, not the latest edit. The session log proves `em:674c8f` and the plan were genuinely first committed **2026-07-29T20:24:35Z**; only `em:01abda` and the source capture were genuinely minted on 07-31. My blanket fix wrongly rewrote two immutable `attribution.when` fields. Reverting those precisely.
````

## Classification

`execution.change.scope_escape` fits because an authorized repair crossed its
intended field boundary and mutated correct immutable provenance. The initiating
date mistake is separately classified as a direct-check omission.

## Detection and correction

After the blanket fix, the agent compared session and commit timestamps with the
write-once policy, identified the two correct July 29 values, and reverted them
before capture and merge.

