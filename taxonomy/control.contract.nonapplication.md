---
id: control.contract.nonapplication
name: Governing-rule nonapplication
family: control
status: accepted
version: "0.1"
---

# Governing-rule nonapplication

## Definition

An applicable, available policy, type definition, genre rule, or skill
instruction is not applied at the decision point, producing an answer or action
the rule would have excluded.

## Inclusion criteria

- The governing rule exists and is applicable.
- The rule was available to the agent.
- The recommendation or action contradicts the rule, or the agent later
  acknowledges that it did not apply it.

## Exclusions and contrast cases

- Use `control.contract.semantic_drift` when the rule is restated with changed
  meaning.
- Use `epistemic.evidence.scope_omission` when the agent failed to find an
  existing source rather than failing to apply a known governing rule.
- A newly supplied rule does not retroactively establish nonapplication.

## Examples

- `AET-EM-0025` — confirmed
- `AET-EM-0041` — confirmed
