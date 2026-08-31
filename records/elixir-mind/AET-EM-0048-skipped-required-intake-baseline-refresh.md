---
id: AET-EM-0048
title: Skipped the required intake baseline refresh
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-31-survey-batch-intakes-and-review-pr-skill-audit.md
source_lines: [974-982, 1070-1076]
session: https://claude.ai/code/session_01YGagV9xodMZvjYarRVhmX6
pull_request: 210
agent_system: Claude Code
agent_model: unknown
detection: review-pr comparison of the diff with the intake procedure
primary_type: execution.procedure.required_step_omission
secondary_types: []
confidence: high
---

# Skipped the required intake baseline refresh

## Error description

Three intake runs omitted the procedure's dedup-probe baseline-refresh step.

## Evaluation

### Expected

Each intake should execute step 8: use an operator-authored query for a gold row
when one exists, skip the row when it does not, and run
`mix brain.dedup_probe --update-baseline`.

### Observed

The review found that none of three intakes touched the dedup-probe artifacts or
ran step 8. Later transcript inspection correctly found no operator phrasing
from which to harvest gold rows, but the baseline was not refreshed until that
audit.

### Why this qualifies

The absence of harvestable rows changes what step 8 produces, not whether the
procedure must be executed. The audit and later baseline result establish that
the required refresh had been omitted from all three intake runs.

### Impact

The intakes bypassed a required procedure control. In this instance the delayed
refresh found no regression and produced no diff.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

were these gaps surfaced by asking you to do the work outlined in the new /review-pr skill?

## Assistant

Partly, and the split matters.

**Genuinely surfaced by the skill's procedure:** the skipped dedup-probe step and the fabricated route-tag block. Both came out of the instruction to build the delivered column from `git diff --stat` rather than from what I remembered doing. Diffing the file set against the `/intake` procedure is what made the *absence* of `meta/evals/dedup-probe.md` legible — an absence is invisible to recollection, because nothing in my memory of the session is shaped like "the file I didn't touch." Same for the route-tag block: walking ask-by-ask forced me back to commit `ddde2ea` in isolation, and `ls meta/threads/` answered a question I had not thought to ask when I wrote it.
````

````text
## Assistant

Items 1, 2, and 4 are done. Item 3 came out differently than I recommended, and doing it surfaced a dropped ask.

**The verifier repair (items 1–2).** The regression test failed first — `log fidelity :ok` over a fabricated block. The sentinel binding turned it green and simultaneously turned `mix brain.route_tags` **red on the live bundle**: `em:712e01: block for 2026-07-31-agent-says-done-reconciliation-patterns but no such thread`. That is the check firing for the first time since it was written. The block's substance moved into the concept body as a new section — the operational route to the same distinction, with the three refinements (the verifier can be testimony too; absence of error is not evidence; `pending` must be easier to earn than `done`). Suite green at 189 tests. Plan marked `done` with the outcome recorded; its open question about the same pattern elsewhere in `lib/` was not swept and stays open.

**Item 3 — I was wrong to recommend it.** I checked the transcript rather than reconstructing: all three intakes were `/intake <url>` plus a pasted transcript, with no operator phrasing describing the subject. The skill's own rule covers this — use the operator's actual phrasing, "never a synthetic paraphrase," and skip silently when there is none. Writing three rows would have meant inventing the queries the gold set exists to measure against. I refreshed the baseline instead: plain 8/25, expanded 22/25, unchanged, so no diff to commit. No regression.
````

## Classification

`execution.procedure.required_step_omission` fits because an explicitly required
intake step was not executed. This record does not classify the earlier “all
gates passing” statement as false: the available gates passed, while the
omitted procedure step lay outside their coverage.

## Detection and correction

The new review workflow compared delivered files with the intake procedure and
found no dedup-probe activity. The agent then checked the transcript, correctly
skipped synthetic gold rows, and refreshed the baseline.
