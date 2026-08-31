---
id: AET-EM-0050
title: Used a compaction summary as authority for transcript asks
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-31-survey-batch-intakes-and-review-pr-skill-audit.md
source_lines: [1050-1068, 1070-1084]
session: https://claude.ai/code/session_01YGagV9xodMZvjYarRVhmX6
pull_request: 210
agent_system: Claude Code
agent_model: unknown
detection: transcript inspection and grep during dedup-row backfill
primary_type: epistemic.source.authority_misuse
secondary_types: []
confidence: high
---

# Used a compaction summary as authority for transcript asks

## Error description

The agent derived operator asks and phrasing from its own context-compaction
summary instead of authoritative user turns in the transcript.

## Evaluation

### Expected

The review workflow should enumerate asks from transcript user turns. Dedup gold
rows must use actual operator phrasing and must never synthesize a paraphrase
when none exists.

### Observed

The agent recommended backfilling three gold queries because it assumed operator
phrasing remained in the session. Transcript inspection found no such phrasing.
The same check recovered an entire intake request absent from both the initial
audit and implementation, and the agent disclosed that it had built the asks
column from its own compaction summary.

### Why this qualifies

Transcript grep supplies the authoritative comparator for both manifestations:
one ask omitted by the summary and three bare intakes lacking the assumed query
phrasing. They belong to one incident because both arose in the same
audit/correction sequence from using the same weaker source as authority.

### Impact

One requested intake was silently dropped and the agent nearly contaminated the
dedup gold set with three synthetic queries. No synthetic rows were written.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

Working tree is clean, everything is pushed, nothing is mid-flight — so none of these block a running task. They all gate what I do next, and one of them is a live defect sitting on an open PR.

| # | Decision | My recommendation |
|---|---|---|
| 1 | The fabricated excerpt block in `em:712e01` — a `### 2026-07-31-agent-says-done-reconciliation-patterns` heading citing a thread doc that was never captured, currently on the branch in commit `ddde2ea` | **Fix now**, independent of the verifier work — rewrite it as ordinary body prose. It's a false citation in a bundle document, and it's the kind of thing that gets read and trusted. |
| 2 | Execute the verifier repair this session, or leave the plan `proposed` | **Execute now.** It's a one-expression fix plus two tests, I have the context, and per plan-vs-capture a fully-solved task handed to a fresh session adds re-derivation risk rather than removing it. If you'd rather review the plan first, it stands on its own. |
| 3 | The three `/intake` runs that skipped step 8 (gold row + `mix brain.dedup_probe --update-baseline`) | **Backfill all three**, since the operator phrasings are still in this session and are exactly what the gold set wants. They're unrecoverable once the session ends. |
| 4 | The three hand-assigned ids (`em:2f847a`, `em:b4e21d`, `em:7c4f3e`) | **Accept them.** They're unique and verify clean; re-minting would churn the registry and break the links I already wrote for no gain. Worth deciding rather than leaving implicit. |
| 5 | PR #210 | **Hold the merge until 1 lands.** Merging now puts the false citation on `main`, where it becomes something a future session has to notice rather than something we're already looking at. |

Ordering by severity: #1 is a correctness problem in the knowledge base and I'd do it first whatever you decide about the rest. #3 is time-sensitive for a different reason — the material expires with the session. #2 is ordinary work. #4 and #5 are ratifications.

The narrow version, if you want to answer once: **"do 1, 2, 3, accept 4, hold 5"** and I'll run the four in that order and report back before touching the PR.

## User

agree with all, proceed
````

````text
## Assistant

Items 1, 2, and 4 are done. Item 3 came out differently than I recommended, and doing it surfaced a dropped ask.

**The verifier repair (items 1–2).** The regression test failed first — `log fidelity :ok` over a fabricated block. The sentinel binding turned it green and simultaneously turned `mix brain.route_tags` **red on the live bundle**: `em:712e01: block for 2026-07-31-agent-says-done-reconciliation-patterns but no such thread`. That is the check firing for the first time since it was written. The block's substance moved into the concept body as a new section — the operational route to the same distinction, with the three refinements (the verifier can be testimony too; absence of error is not evidence; `pending` must be easier to earn than `done`). Suite green at 189 tests. Plan marked `done` with the outcome recorded; its open question about the same pattern elsewhere in `lib/` was not swept and stays open.

**Item 3 — I was wrong to recommend it.** I checked the transcript rather than reconstructing: all three intakes were `/intake <url>` plus a pasted transcript, with no operator phrasing describing the subject. The skill's own rule covers this — use the operator's actual phrasing, "never a synthetic paraphrase," and skip silently when there is none. Writing three rows would have meant inventing the queries the gold set exists to measure against. I refreshed the baseline instead: plain 8/25, expanded 22/25, unchanged, so no diff to commit. No regression.

**What that check turned up.** Grepping the transcript for the intake asks found one I never listed in the audit and never did:

> `/intake https://www.reddit.com/r/LLMDevs/comments/1v549i8/i_ripped_out_my_vector_db_and_a_folder_of/` + transcript

It appears nowhere in the bundle and nowhere in git history. It was asked earlier in this session, before the context compaction, and it was dropped.

The audit missed it for a specific reason. I built the delivered column from git, as the skill requires — but I built the **asks** column by reading the compaction summary, which is my own prior account of the session. The skill fixed one column and left the other on testimony, and the untrusted column is exactly where the loss occurred. Enumerating asks from the transcript is mechanical and cheap, as the grep just showed.
````

## Classification

`epistemic.source.authority_misuse` fits because the agent treated an
agent-authored summary as authoritative for exact user asks and phrasing when
the primary transcript remained available. The omitted intake and synthetic-row
recommendation are impacts of that shared source-selection error, not separate
incidents.

## Detection and correction

After the operator approved the proposed backfill, the agent inspected and
grepped the transcript. It declined to invent gold queries, recovered the
dropped intake, and proposed changing the review skill to derive asks from user
turns.

