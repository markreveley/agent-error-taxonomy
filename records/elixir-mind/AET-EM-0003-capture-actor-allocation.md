---
id: AET-EM-0003
title: Assigned agent-owned capture work to the operator
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-08-adopt-session-capture-routing-and-route-tags.md
source_lines: [470-502, 575-590]
session: https://claude.ai/code/session_018uKND3Ycc71z55zPUqU86M
pull_request: 13
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator compared runbook actor assignments with the skill
primary_type: control.contract.semantic_drift
secondary_types: []
confidence: high
---

# Assigned agent-owned capture work to the operator

## Error description

The agent wrote an operator-facing processing flow that cast concept creation,
ledger updates, route tagging, materialization, and verification as operator
chores even though the `/capture` skill assigned those steps to the agent.

## Evaluation

### Expected

The runbook should preserve the skill's actor boundary: the operator invokes the
skill and answers ratification questions; the agent performs the capture,
routing, filing, tagging, materialization, and checks.

### Observed

The runbook imperatively told its reader to carry out the substantive workflow.
When challenged, the agent inspected the skill and confirmed that every step was
agent-directed.

### Why this qualifies

The pre-incident skill is preserved in git at commit
`38d13b2900601704c1e418eaa8ac1388be5e5083` and independently establishes the
actor contract. The runbook's allocation differs from that contract.

### Impact

The operator could be burdened with repository work the automation was meant to
perform, and future captures could be skipped or inconsistently executed.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

Good plan. Here's the runbook for driving each existing thread through the new flow, and exactly what to check afterward.

## First, pick the right skill

Two skills write to `meta/threads/` — they are *different tools*, and for "process via the new workflow" you want **`/capture`**, not `/persist-thread`:

| | `/capture` (the new one) | `/persist-thread` (old) |
|---|---|---|
| Body | **distilled** — substantive responses only | **verbatim** — every exchange |
| Extras | `## Routing` ledger **+ route tags + excerpt logs** | none |
| Use when | you want the session routed into concepts | you want a faithful archive |

They collide on filename (one doc per session, update-in-place), so run **one**. If a thread was already persisted verbatim and you now want it routed, `/capture` will regenerate that same file as the distilled+routed version.

## The processing flow, per thread

Resume the session on its branch (so the agent holds the conversation — `/capture` renders from context), confirm `main` is merged in, then:

1. **Invoke `/capture`.** It renders the distilled `## User`/`## Assistant` body, writes frontmatter + a narrative section, and drafts the `## Routing` ledger.
2. **Route each topic to a concept** — this is the substantive step, and it's where content actually lands. For each ledger row that should route somewhere:
   - **Existing concept** → note its `sb:` id (grep the file's frontmatter, or `meta/registry.md`).
   - **New concept** → file it (`/intake` is ideal for this, or create the doc), then `mix brain.id` to mint its id and `mix brain.registry` to refresh the registry.
   - Set the row's **State** (`open`/`paused`/`closed`) and **Routed to** link (or `unrouted`).
3. **Tag the frozen body** — wrap each feeding paragraph in `<routes ref="sb:… path/…">`, using the concept's `sb:` id (sink) and any code/file **path** back-links.
4. **Materialize + verify** (the skill does this, or run it yourself):
   ```
   mix brain.route_tags --materialize   # writes each concept's excerpt log from the tags
   mix brain.route_tags                 # verify
   ```

Order matters: the concept must exist with a minted `sb:` id **before** you tag with it, or ref-resolution fails.
````

````text
## User

Commit, then lets continue

In orocessing flow item 2, you describe things that should be done by an agent as if i the operator should do them. Is this a mistake? What does the skill say?
Regarding verification, once we settle the above, we should create a folder in meta/verification-flows for walkthroughs exactly like you just specified, and place what you just wrote (corrected if necessary) there

## Assistant

Tree is clean — both commits are in. Now to your questions.

## Was the operator/agent framing a mistake? Yes.

My chat runbook's item 2 ("note its id", "file it", "set the row's state"…) wrongly cast **agent** work as **operator** to-dos. The skill is unambiguous — every step is agent-directed. Reading `.claude/skills/capture/SKILL.md`:

- §1 "**Render** the conversation…", §3 "A `## Routing` table…", §4 "**mark** each region…", §5 "**generate it** — `mix brain.route_tags --materialize`", "After writing → **Run the gates**".
````

## Classification

`control.contract.semantic_drift` fits because the runbook changed who the
procedure required to perform its steps. It is narrower than a general
instruction-following label: the failure is a semantic mismatch between two
representations of the same workflow contract.

## Detection and correction

The operator noticed the actor mismatch and asked what the skill said. The agent
confirmed the error, restated the operator/agent division, and incorporated it
into the walkthrough.
