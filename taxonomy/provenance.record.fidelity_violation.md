---
id: provenance.record.fidelity_violation
name: Record-fidelity violation
family: provenance
status: accepted
version: "0.1"
---

# Record-fidelity violation

## Definition

The agent paraphrases, omits, rewrites, fabricates, or severs content or links
that must faithfully preserve a source, session, or commit history.

## Inclusion criteria

- Fidelity, immutability, or source reachability is a load-bearing purpose of
  the record.
- The agent's action changes historical or source meaning, attribution, or
  reconstructability.
- Correction restores fidelity or establishes the loss.

## Exclusions and contrast cases

- Use `epistemic.claim.synthesis_as_evidence` for unlabeled synthesis in an
  answer when the underlying record itself is not altered.
- Use `execution.change.scope_escape` when a selector accidentally mutates
  frozen content despite the agent understanding the fidelity boundary.
- Intentional summarization is not a violation when the artifact is explicitly
  designated as a summary and does not claim verbatim fidelity.

## Examples

- `AET-EM-0004` — confirmed
- `AET-EM-0014` — contested
- `AET-EM-0049` — confirmed
