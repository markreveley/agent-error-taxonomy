---
id: AET-EM-0010
title: Gave the wrong location for the Routines interface
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-12-rename-news-skill-to-research.md
source_lines: [155-198, 276-288]
session: https://claude.ai/code/session_01BQa7yjzobSxRgCUskEx2fC
pull_request: 59
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator could not find the stated interface
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Gave the wrong location for the Routines interface

## Error description

The agent told the operator to open a scheduled-triggers view at
`claude.ai/code`, but the actual interface was the dedicated
`claude.ai/code/routines` page.

## Evaluation

### Expected

Before giving actionable navigation instructions, the agent should have checked
the current documented URL and named the dedicated Routines page.

### Observed

The agent confidently supplied a nonexistent navigation location. When the
operator could not find it, the agent checked the documentation and corrected
the URL.

### Why this qualifies

The initial instruction and corrected documented location are both explicit in
the transcript. The mismatch is factual and directly resolved.

### Impact

The operator could not carry out the requested Routine deletion and had to spend
an additional turn diagnosing the bad navigation instruction.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

I lean toward 3, Priority prioritizing consistency (#3) unless there's a reason I should consider otherwise. what is the cost? Is it time and effort, or does it introduce Other issues?

Ratify file name changes

Can you clarify what you're talking about with the external routine? Not exactly sure what the action you're looking for from me is.

## Assistant

That trigger-list call hit the same approval gate that's noted in your open issue — so I can't read the Routine's current state directly. I'll explain it conceptually. Here are all three:

## 1. Cost of option 3 (full consistency)

**Mostly effort/churn, not architectural risk — but two real, manageable hazards:**

- **It lightly rewrites point-in-time records.** Analyses, plans, and issues are dated write-ups describing the system *as it was when written*. Swapping `/news` → `/research` in their bodies makes them read as if it was always `/research` — a minor historical-fidelity smudge. It's *allowed* (those bodies aren't formally frozen the way thread conversation prose, dated digests, `sb:` ids, and `provenance:` frontmatter are — I won't touch those in any option), but it does blur "what did we call it back then." For most it's harmless; the one that gives me pause is the open issue `daily-news-routine-runs-not-landing.md`, whose whole subject is a Routine that literally fires `/news`.

- **A technical trap: generated route-tag log blocks.** Several of those ~35 files carry `## Thread excerpts — route-tagged log` sections that `mix brain.route_tags` regenerates from frozen thread tags. Those frozen threads still say `/news`, so the log blocks must *stay* `/news` — if I edit `/news` inside one, the fidelity check fails CI. It's handleable (edit only the prose around the blocks), just requires per-file care rather than a blind sweep.

Net: reversible via git, no design consequences. **My recommendation is to proceed with #3** — the consistency win outweighs the smudge, and I'll keep the frozen/generated regions intact.

## 2. Filenames

Worth a precise distinction before I rename anything: the three files I flagged use "news" as a **noun** (the content), not as the `/news` **command**:
- `meta/flows/news-inbox.md` — "the inbox of news"
- `meta/plans/auto-intake-featured-news.md` — "featured news items"
- `meta/plans/news-daily-read-synthesis.md` — "the daily read of news"

The feed still surfaces *news* — I'm only renaming the command that invokes it. So strictly these could stay. If your goal is **zero "news" residue anywhere**, I'll rename them to `research-inbox.md`, `auto-intake-featured-research.md`, `research-daily-read-synthesis.md` (and fix every link). I'd **not** rename the dated thread docs (`2026-07-09-daily-news-inbox-routine.md`, etc.) — those are frozen provenance and renaming breaks their "Seen in" citations and PR anchors.

Quick check: do you want the command renamed (keep "news" the noun, files stay) — or "news" scrubbed entirely (files rename too)? Your "ratify filename changes" reads like the latter; I just want to confirm before churning links, since the noun is arguably still accurate.

## 3. The external Routine — what it is and what I need from you

In an earlier session, a **scheduled Routine** was set up (via the Claude Code web scheduling UI / the `claude-code-remote` trigger system) to run the feed automatically once a day. It's a saved job stored **server-side, outside this git repo** — its saved prompt literally starts with `/news …`. Because it lives outside the repo, nothing I commit can change it.

So after this rename: the daily automated fire will still invoke `/news`, which no longer resolves to a skill → that run will do nothing useful.

**The action:** edit that Routine's saved prompt to say `/research` instead of `/news`. Two ways:
- **You, in the UI** — open the scheduled-triggers view at claude.ai/code and edit the daily feed Routine's prompt. (This is also where the separate "runs not landing" approval-gate issue lives.)
- **Me** — I *can* do it via the trigger tools, but it requires deleting and recreating the Routine (the update tool can't edit a saved prompt), and the trigger tools are behind the same approval gate that just blocked my `list_triggers` call. If you approve those calls, I'll recreate it pointed at `/research`.

Want me to take the Routine, or will you? And confirm the filename question above and I'll execute #3 in the same pass.
````

````text
## User

"claude.ai/code → scheduled triggers" - Not seeing this at this location.

## Assistant

That's my error — the correct location is **`claude.ai/code/routines`** (a dedicated Routines page), not "claude.ai/code → scheduled triggers." Here's the accurate path from the docs:

## To delete the Routine

1. Go to **[claude.ai/code/routines](https://claude.ai/code/routines)** — this lists all your routines.
2. **Click the routine** (the daily feed one — it'll be the one whose prompt starts with `/news …`) to open its **detail page**.
3. Click the **delete icon (trash)** to remove it. Per the docs: *"Past sessions created by the routine remain in your session list"* — so your history stays, only the schedule goes.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the current UI location was
a directly checkable factual claim, and the agent only consulted the docs after
the instruction failed. This is not an interaction-tool failure; the erroneous
content was the unchecked URL.

## Detection and correction

The operator reported that the named view was absent. The agent checked the
documentation and supplied the correct dedicated URL and deletion steps.
