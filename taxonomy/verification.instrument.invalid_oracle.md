---
id: verification.instrument.invalid_oracle
name: Invalid verification oracle
family: verification
status: accepted
version: "0.1"
---

# Invalid verification oracle

## Definition

A test, audit, or readback cannot support its claimed inference because its
implementation or population is defective, a known-answer control is absent,
or it shares the producer's failure boundary.

## Inclusion criteria

- A verification mechanism, rather than an omitted check, is the central failed
  control.
- The mechanism can produce plausible but invalid results.
- A later control or inspection establishes false positives, false negatives, or
  self-confirmation.

## Exclusions and contrast cases

- Use `verification.completion.incomplete_check` when a valid oracle simply was
  not run.
- Use `epistemic.claim.direct_check_omission` when implementation behavior was
  guessed before inspection rather than relied on as a verifier.
- A failing test is not an invalid oracle merely because its result is
  inconvenient.

## Examples

- `AET-EM-0040` — probable
- `AET-EM-0042` — confirmed
