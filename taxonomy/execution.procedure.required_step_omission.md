---
id: execution.procedure.required_step_omission
name: Required procedure-step omission
family: execution
status: accepted
version: "0.1"
---

# Required procedure-step omission

## Definition

A required non-validation step in an applicable skill or workflow is skipped,
leaving the output or artifact incomplete.

## Inclusion criteria

- The procedure explicitly requires the step.
- The agent is executing that procedure.
- The required output or action is absent.

## Exclusions and contrast cases

- Use `verification.completion.incomplete_check` when omitted checks are paired
  with a terminal completion claim.
- Use `control.contract.nonapplication` when the failure occurs while deciding
  or recommending what to do rather than executing a known procedure.
- An optional or advisory step does not qualify.

## Examples

- `AET-EM-0011` — confirmed
- `AET-EM-0047` — confirmed
- `AET-EM-0048` — confirmed
