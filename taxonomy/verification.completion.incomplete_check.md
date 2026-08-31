---
id: verification.completion.incomplete_check
name: Completion claim after incomplete checking
family: verification
status: accepted
version: "0.1"
---

# Completion claim after incomplete checking

## Definition

The agent reports a ready, complete, clean, or green state without a check or
readback required to establish it.

## Inclusion criteria

- The agent makes an explicit or strong terminal-state claim.
- A relevant check or readback is available and expected.
- Later CI, hook, audit, or inspection disproves the claimed state.

## Exclusions and contrast cases

- Use `execution.procedure.required_step_omission` when a non-validation step is
  missing and no completion claim depends on it.
- Use `epistemic.claim.direct_check_omission` for precise factual claims made
  before implementation rather than terminal-state reports.
- A failed check disclosed as unresolved is not a false completion claim.

## Examples

- `AET-EM-0007` — confirmed
- `AET-EM-0015` — confirmed
- `AET-EM-0028` — confirmed
