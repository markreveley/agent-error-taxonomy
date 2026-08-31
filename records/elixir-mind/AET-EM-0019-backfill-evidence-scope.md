---
id: AET-EM-0019
title: Declared session URL backfill unrecoverable without inspecting provenance
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-19-session-url-persistence-and-plan-vs-capture-policy.md
source_lines: [173-210, 237-251]
session: https://claude.ai/code/session_01FBDre38cUCeGRfbiBTsDfw
pull_request: 111
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator suggested PR provenance and agent ran the derivation
primary_type: epistemic.evidence.scope_omission
secondary_types: []
confidence: high
---

# Declared session URL backfill unrecoverable without inspecting provenance

## Error description

The agent encoded a no-backfill decision on the claim that historical session
URLs would require guessing without checking capture commits and PR bodies.

## Evaluation

### Expected

Before declaring provenance unrecoverable, the agent should have inspected the
recorded mapping from thread files to their first-add commits, session trailers,
and PR bodies.

### Observed

After the operator challenged the claim, the agent found a mechanical derivation
and successfully backfilled 70 thread documents from recorded evidence.

### Why this qualifies

The completed backfill is a direct comparator that disproves the blanket
unrecoverability claim. The independent unchecked count is recorded separately
as AET-EM-0020.

### Impact

Without correction, the policy would have left recoverable provenance links
unstamped and preserved a false rationale for doing so.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

implement the change to stamp the session url into the thread-doc frontmatter

## Assistant

Done — the session-stamp change is implemented, verified, and pushed as `cb520bd` on `claude/session-transcript-persistence-ouwnp7` (two commits on the branch now, this and the earlier merge-strategy edit).

What changed:

- **`meta/policy/session-capture.md`** gained a bullet beside the `pr:` rule: `/capture` stamps `session: <url>` into the thread doc's frontmatter, derived from `CLAUDE_CODE_REMOTE_SESSION_ID` with the `cse_` → `session_` prefix conversion. The policy frames it explicitly as the full-fidelity escape hatch to the raw transcript and the *weaker* anchor — account-bound, agent-unreadable, deletable — complementing `pr:`, never substituting for it.
- **`.claude/skills/capture/SKILL.md`** got the `session:` line in its frontmatter template plus the stamping procedure, including the exact one-liner from the docs (`${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}`).
- **`CLAUDE.md`** regenerated via `/render-contract`.

Three decisions I baked in, all on the conservative side: **write-once** (stamped at first capture, never rewritten — matching the immutability style of `attribution`); **omit when local** (no env var → no key, never a guessed URL, consistent with the forged-trailer concern from earlier); and **no backfill** of the ~30 existing thread docs — reconstructing session URLs for past threads would mean guessing, and the trailer/PR anchors already cover them.

No Elixir tooling changes were needed: the frontmatter schema explicitly preserves extra keys, and the `pr:`-reading code (`lineage.ex`, `backfill.ex`, `orphans.ex`) is untouched. All gates pass — contract and registry checks, `mix brain.verify`, `mix brain.route_tags`, and 177 tests.

One nice consequence: when this session is eventually captured, its own thread doc becomes the first to carry a `session:` stamp — the rule takes effect on the session that ratified it. Say `/create-pull-request` whenever you want that capture and the PR opened.

## User

why would reconstructing for backfill require guessing, wouldn't you just grab the url from the associated PR's? also there are a lot more than 30 threads

## Assistant

Both points conceded — I was wrong on each, and the second error caused the first.

**The count:** there are **72** thread docs, not ~30. I low-balled it without counting.

**The "guessing" claim:** doesn't hold, and your instinct about the PRs is exactly right — in fact there's an even more direct route than the PR body. The commit that *first added* each thread doc is the capture commit, made by the very session the thread records, and that commit carries the `Claude-Session:` trailer. So the mapping is `thread doc → first-add commit → trailer value`, fully mechanical, no inference at all. I just ran it across all 72:

- **67 threads** resolve to an exact session URL from their capture commit's trailer.
- **3 threads** (all 2026-07-11) have no trailer because they landed in the squash era — the GitHub squash commit replaced the session-authored original. But these are post-v2.1.179, so their **PR bodies** should carry the session URL on its own line, recoverable through each thread's `pr:` stamp — your suggested route picks up exactly where the trailer route fails.
- **1 thread** (2026-07-05, the greenfield bootstrap) predates the trailer feature *and* the PR-body link entirely. This is the only one where "backfill" would actually mean guessing — the URL exists nowhere in the repo's history.
- **2 threads** (07-17 brain-orphans, 07-18 agent-drivable-apps) were **local-terminal sessions** — no cloud transcript exists, so an absent key is the *correct* state per the rule we just wrote, not a gap to fill.

So the honest restatement of the policy rationale: backfill from **recorded evidence** (trailers, PR bodies) is exact for 70 of 72 threads; only the pre-feature thread is unrecoverable, and the two local ones are correctly bare. My blanket "do not backfill — it would mean guessing" line in the policy is wrong as written and worth amending to something like: *backfill is permitted only when the URL is mechanically derivable from the capture commit's trailer or the PR body — never inferred otherwise.*
````

````text
## User

Do the work here
Also create a new policy document that describes this "plan vs thread" decision matrix

## Assistant

Both done, pushed as `3b790a0` on `claude/session-transcript-persistence-ouwnp7`.

**The backfill** — 70 of 73 thread docs now carry a `session:` line, sourced entirely from recorded evidence:
- **67** from each thread's own capture-commit `Claude-Session:` trailer (the capture commit *is* the session that produced the thread, so the trailer is exactly the right URL — no inference).
- **3** squash-era threads (PRs 38/39/40) recovered from their PR bodies via the `pr:` anchor — your route, and it worked.
- **3** correctly left bare: the pre-v2.1.179 greenfield bootstrap (URL exists nowhere), and the two local-terminal sessions (PRs 106/109 — I checked their bodies too; no URL, consistent with local). Bare is the *correct* state per the rule, not a gap.

I also corrected the rule I'd committed an hour earlier: the "do not backfill" line is gone, replaced with the accurate "backfill only from recorded evidence — trailer, else PR body, else bare; never inferred." You were right to push on that; the blanket claim was wrong and the data proved it (70 recoverable, only 1 genuinely lost).
````

## Classification

`epistemic.evidence.scope_omission` fits because the agent declared historical
URLs unrecoverable without examining the repository's provenance surfaces. The
later mechanical recovery demonstrates that the missing evidence was available.

## Detection and correction

The operator proposed PR-based recovery. The agent found the more direct trailer
route, used PR bodies as fallback, backfilled 70 documents, and amended the rule.
