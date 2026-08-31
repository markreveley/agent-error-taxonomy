---
id: AET-EM-0004
title: Paraphrased transcript text required to remain verbatim
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-08-adopt-session-capture-routing-and-route-tags.md
source_lines: [891-908]
session: https://claude.ai/code/session_018uKND3Ycc71z55zPUqU86M
pull_request: 13
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator inspection of the captured thread
primary_type: provenance.record.fidelity_violation
secondary_types: []
confidence: high
---

# Paraphrased transcript text required to remain verbatim

## Error description

The agent interpreted “distilled” as permission to summarize retained responses,
producing a session record that paraphrased text whose provenance contract
required byte-faithful retention after noise removal.

## Evaluation

### Expected

Tool calls, reasoning, and qualifying short pre-tool narration could be removed,
but every retained operator message and agent response had to remain verbatim.

### Observed

The capture policy and implementation licensed paraphrase. The pre-recapture
artifact is preserved at git commit
`f47f5ac890a5371a48c69968a393a802cc616fb8`; its 99-line thread compresses the
operator prompt and assistant response that the corrected 919-line capture
preserves.

### Why this qualifies

This is not merely misleading documentation: the stored provenance record was
actually rewritten as summaries. The historical artifact, operator report, and
agent correction jointly establish the behavior and comparator.

### Impact

The capture ceased to be reliable transcript evidence. Exact wording, omissions,
and the temporal form of the interaction could no longer be audited from it.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

There is a problem. The thread has a note that agent responses are distilled. They should be verbatim. Tool calls etc still stripped, but all substantive retained agent responses should be verbatim. Change the policy and skill and recapture

## Assistant

You're right — that's a real semantics bug. "Distilled" should mean *the noise is stripped*, not that the kept responses are summarized. The cb hook keeps retained assistant text **verbatim**; my wording ("distilled render… delivered substance, not word-for-word") wrongly licensed paraphrase. Let me fix the policy, skill, and guide, then recapture the thread doc with verbatim responses.

First, find every place that implies summarization:

Most uses of "distill" are fine shorthand for "noise-stripped," but the retained-text-is-verbatim requirement is missing and the "delivered substance, not word-for-word" license is wrong. Before rewriting docs, let me check whether the host session log is available — parsing it gives a truly verbatim render instead of relying on memory:

The core idea + 4 mechanisms is a clean self-contained unit to tag. No line-anchored tags exist anywhere in the render, so insertion is safe. Let me assemble the thread doc via a script — reusing the existing header (narrative + ledger) with verbatim wording, then the parsed verbatim body with the route tag, truncating my in-progress turn:

Committed as `9b18905` (authored correctly). Here's what this fixed and did:

## The bug
"Distilled" had leaked into meaning *summarize the substance* — the policy/skill/guide literally licensed paraphrase ("delivered substance, not word-for-word"). That's wrong: the cb rule keeps retained assistant text **verbatim**; only the *noise* is dropped.
````

## Classification

`provenance.record.fidelity_violation` fits because the agent altered the content
of a record whose value depended on faithful reproduction. Contract semantic
drift is causal context, but the narrower evidenced failure is the corrupted
record itself.

## Detection and correction

The operator inspected the thread and identified the paraphrase. The agent
changed the policy and skill, preferred parsing the host log over memory, and
recaptured all retained exchanges verbatim.
