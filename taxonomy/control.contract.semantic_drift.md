---
id: control.contract.semantic_drift
name: Operative-contract semantic drift
family: control
status: accepted
version: "0.1"
---

# Operative-contract semantic drift

## Definition

While restating a skill, policy, or runbook, the agent changes what the rule
means, who acts, or the conditions under which it applies.

## Inclusion criteria

- An authoritative operative contract exists.
- The agent's guidance purports to represent that contract.
- The guidance weakens, broadens, narrows, or reassigns its semantics.

## Exclusions and contrast cases

- Use `control.contract.nonapplication` when the correct rule is available but
  not applied at the decision point.
- Use `execution.procedure.required_step_omission` when the agent understands the
  rule but skips a required operational step while executing it.
- A clearer paraphrase that preserves semantics is not drift.

## Examples

- `AET-EM-0002` — probable
- `AET-EM-0003` — confirmed
