# Agent Error Taxonomy

An evidence-first taxonomy of errors made by LLM agents during real tasks.

This repository starts from observed incidents rather than a predetermined list
of failure labels. Each incident record preserves the transcript evidence,
evaluates why the behavior qualifies as an error, and links it to a defined
taxonomy type. New types are added only when existing definitions do not fit.

The initial corpus is the persisted development threads from
[`markreveley/elixir-mind`](https://github.com/markreveley/elixir-mind).

## Repository layout

- [`taxonomy/`](taxonomy/) defines reusable error types and their boundaries.
- [`records/`](records/) contains one evidence-backed incident per file.
- [`corpora/`](corpora/) records the source corpus, revision, and review coverage.
- [`docs/methodology.md`](docs/methodology.md) defines the evaluation and
  classification protocol.

## Core rule

An agent behavior is not filed merely because it looks awkward or produced a
bad outcome. A record must identify:

1. the behavior that is alleged to be erroneous;
2. the applicable expectation or comparator;
3. evidence of the mismatch, quoted verbatim where it occurred; and
4. the error type that best explains the behavior.

If the evidence does not establish the mismatch, the record must say so and use
`status: probable` or `status: contested` rather than presenting the error as
fact.

## Status

Version 0.1 is complete for the initial `elixir-mind` corpus. All 143 persisted
thread documents at revision
`e7eb8ed37b09afdf1c6ba156f70d6655d72778df` were reviewed, producing 51 retained
incident records: 40 confirmed, 10 probable, and 1 contested, classified across
14 evidence-induced taxonomy types.

- [Browse all incident records](records/index.md)
- [Review per-thread corpus coverage](corpora/elixir-mind-coverage.md)
- [Read the accepted taxonomy](taxonomy/index.md)

The source taxonomy was empty at initialization; no pre-existing types were
available to preserve.

## Validate

From this repository, with the pinned `elixir-mind` checkout beside it:

```sh
python3 scripts/validate.py --source-root ../elixir-mind
```

The validator checks record IDs and statuses, taxonomy references, source
revision, declared line ranges, exact transcript bytes, and source role headers.
