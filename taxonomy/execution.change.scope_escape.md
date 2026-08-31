---
id: execution.change.scope_escape
name: Change-scope escape
family: execution
status: accepted
version: "0.1"
---

# Change-scope escape

## Definition

A mutation or remediation affects files, sections, or fields outside the
intended target set because its selector, guard, or boundary classification is
wrong.

## Inclusion criteria

- An intended mutation boundary exists.
- The operation crosses that boundary unintentionally.
- A diff, gate, or readback demonstrates the scope escape.

## Exclusions and contrast cases

- Use `provenance.record.fidelity_violation` for deliberate paraphrase,
  omission, fabrication, or rewriting of a record whose fidelity is the
  violated invariant.
- Use `control.authority.unwarranted_scope_inference` when the agent knowingly
  broadens what it believes it is authorized to change.
- A proposed broad change that is corrected before mutation is not an execution
  error.

## Examples

- `AET-EM-0018` — probable
- `AET-EM-0021` — confirmed
- `AET-EM-0045` — confirmed
