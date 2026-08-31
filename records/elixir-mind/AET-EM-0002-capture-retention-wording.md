---
id: AET-EM-0002
title: Documented the capture retention rule too narrowly
status: probable
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-08-adopt-session-capture-routing-and-route-tags.md
source_lines: [543-549]
session: https://claude.ai/code/session_018uKND3Ycc71z55zPUqU86M
pull_request: 13
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator comparison with the source workflow
primary_type: control.contract.semantic_drift
secondary_types: []
confidence: medium
---

# Documented the capture retention rule too narrowly

## Error description

The agent described `/capture` as retaining only “substantive” responses instead
of preserving every text block except the specifically defined noise classes.

## Evaluation

### Expected

The ported workflow's contract retained a short assistant text block unless it
was both under the threshold and followed by a tool call; tool-less turns and
isolated short replies remained intact.

### Observed

The agent's documentation used a broad “substantive responses only” shorthand.
After the operator supplied the inherited behavior, the agent checked the source
hook and acknowledged that its wording understated the contract.

### Why this qualifies

The wording could direct later agents to drop allowed material. The status is
probable because the decisive external `transcript_hook.py` comparator is
reported in the retained exchange but is not independently present in this
source repository.

### Impact

Agents following the wording could produce incomplete session records by
discarding short but substantive standalone responses.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

Ok lets take this one by one. First, lets remove /persist-thread in favor of capture. Second; capture, according to the workflow this was borrowed from in the cb repo, should capture all thread exchanges except tool calls, statements less than 300 characters UNLESS its in isolation, thinking, etc

## Assistant

I've confirmed the cb rule against `transcript_hook.py` (lines 110–129): an assistant text block is dropped **only** when it's *both* under 300 chars *and* followed by a tool call in the same turn; a short block in isolation (nothing after it calls a tool — a closing reply or standalone remark) is kept, thinking/tool calls are always dropped, and no-tool turns keep everything. My current wording ("keep only the substantive response") undersells that, so I'll reframe it in Task 2.
````

## Classification

`control.contract.semantic_drift` fits because the agent's prose representation
of an inherited behavioral contract narrowed the contract's semantics. This is
not yet a record-fidelity violation: the evidenced behavior is the misleading
rule, not a demonstrated corrupt capture.

## Detection and correction

The operator compared the new workflow with its source. The agent inspected the
hook, restated the conjunction precisely, and revised the policy, skill, guide,
and frontmatter descriptions.
