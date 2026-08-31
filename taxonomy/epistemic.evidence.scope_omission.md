---
id: epistemic.evidence.scope_omission
name: Evidence-scope omission
family: epistemic
status: accepted
version: "0.1"
---

# Evidence-scope omission

## Definition

An exhaustive, completeness, absence, duplication, or unrecoverability claim is
made without searching a relevant portion of the available evidence surface.

## Inclusion criteria

- The claim depends on evidence coverage.
- Relevant evidence was available to the agent.
- Later inventory or search demonstrates that the omitted surface mattered.

## Exclusions and contrast cases

- Use `epistemic.source.authority_misuse` when the source was found but the wrong
  source was treated as authoritative.
- Use `verification.completion.incomplete_check` when an implementation gate was
  omitted before a terminal completion claim.
- A scoped claim is not an error merely because evidence exists outside its
  stated scope.

## Examples

- `AET-EM-0013` — confirmed
- `AET-EM-0016` — confirmed
- `AET-EM-0019` — confirmed
- `AET-EM-0024` — probable
- `AET-EM-0029` — confirmed
- `AET-EM-0034` — confirmed
- `AET-EM-0036` — confirmed
- `AET-EM-0046` — probable
