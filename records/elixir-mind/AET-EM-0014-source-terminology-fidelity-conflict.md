---
id: AET-EM-0014
title: Replaced externally attributed terminology under a broad rename instruction
status: contested
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-13-second-mind-taxonomy-analysis-and-belief-plan.md
source_lines: [538-560]
session: https://claude.ai/code/session_01HJPV4LC84LSauxspwapUw9
pull_request: 80
agent_system: Claude Code
agent_model: unknown
detection: agent disclosed the source-fidelity consequence and operator requested reversion
primary_type: provenance.record.fidelity_violation
secondary_types: []
confidence: medium
---

# Replaced externally attributed terminology under a broad rename instruction

## Error description

The agent applied a blanket terminology rename inside passages describing an
external source, making those passages read as though the source used the
repository's term.

## Evaluation

### Expected

One defensible expectation is that externally attributed terminology remain
faithful, or that the conflict between fidelity and a blanket rename be surfaced
before changing it.

### Observed

The agent followed “anywhere it appears,” pushed the replacement, then disclosed
that the external dialogue actually used “second mind.” The operator called that
result incorrect and asked for a revert.

### Why this qualifies

The source-fidelity consequence is objective, but responsibility is contested.
The operator's instruction literally authorized replacement anywhere in the
documents, and no retained earlier exception for attributed language is shown.
This record therefore captures an instruction-versus-fidelity conflict, not an
unauthorized change, and must not be counted as confirmed.

### Impact

Until reverted, the documents inaccurately represented the external source's
terminology.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

Change second-mind in the title to elixir-mind, and anywhere it appears in the documents

## Assistant

Done and pushed (commit `bc694e5`). The rename covered:

- **The analysis file itself** — moved to `meta/analysis/elixir-mind-taxonomy-and-the-belief-gap.md` (filename tracks the title per the filenames policy), with its title now "Do the second-brain → elixir-mind taxonomies point anywhere this bundle should head?", plus every occurrence in its description, tags, and body — both the hyphenated compound and the spaced prose forms ("elixir mind", "elixir minds"), with article agreement fixed ("an elixir mind").
- **The plan** — its provenance line, tags, and the cross-link title/path pointing at the renamed analysis.
- **Both indexes** — entry titles, descriptions, and link paths.

All gates stay green (`brain.verify`, `brain.registry --check`).

One fidelity note worth having on record: a few of the renamed spots describe the *external ChatGPT dialogue's own* taxonomy — e.g. "the first-mind / second-brain / elixir-mind ladder" and "elixir minds push toward 'personal philosophy made executable'" — where the source conversation actually used the term "second mind." As written, the docs now read as if the source used your term. If you'd rather keep source-attribution exact, I can add a one-line terminology note to the analysis ("'elixir mind' is this bundle's name for what the source calls a 'second mind'") — say the word and I'll amend it.

## User

Ah i see, revert, that is incorrect

## Assistant

Reverted and pushed. The rename commit was undone with a proper revert commit (no history rewrite, since the branch was already on the remote), so the branch now reads: file the two docs → rename to elixir-mind → revert the rename.
````

## Classification

`provenance.record.fidelity_violation` fits the altered source attribution. The
record remains contested because a broad direct instruction supported the literal
edit, making failure to clarify the conflict a reasonable alternative reading.

## Detection and correction

The agent disclosed the fidelity problem in its completion report. The operator
rejected the result, and the agent reverted the pushed rename without rewriting
history.
