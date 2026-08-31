---
title: Agent Error Taxonomy
status: accepted
version: "0.1"
---

# Agent Error Taxonomy v0.1

This taxonomy classifies the closest evidence-supported causal behavior, not the
surface symptom. False claims, bad edits, red CI, rework, and user burden are
consequences or impact tags rather than error types.

## Hierarchy

```text
epistemic
├── epistemic.source.authority_misuse
├── epistemic.evidence.scope_omission
├── epistemic.claim.direct_check_omission
└── epistemic.claim.synthesis_as_evidence

reasoning
└── reasoning.distinction.collapse

control
├── control.input.channel_misinterpretation
├── control.authority.unwarranted_scope_inference
├── control.contract.semantic_drift
└── control.contract.nonapplication

execution
├── execution.change.scope_escape
└── execution.procedure.required_step_omission

verification
├── verification.completion.incomplete_check
└── verification.instrument.invalid_oracle

provenance
└── provenance.record.fidelity_violation
```

## Assignment rules

1. Assign one primary leaf per incident. Record impact, detection, confidence,
   and recovery separately.
2. Use `epistemic.*` when the failure is selecting, finding, labeling, or
   checking evidence.
3. Use `reasoning.*` when relevant facts are present but materially different
   mechanisms, units, criteria, or consequences are collapsed.
4. Use `control.*` when the agent mishandles user input, action authority, or an
   operative instruction.
5. Use `execution.*` when authorized work is performed against the wrong scope
   or with a required operational step missing.
6. Use `verification.*` when the agent makes a terminal-state claim without the
   necessary checks or relies on an invalid verification instrument.
7. Use `provenance.*` when preserving what a source, session, or history
   actually said or did is itself the violated invariant.
8. Do not create separate types for factual domain, artifact genre, severity,
   impact, or detection source.
9. Add a new leaf only when the causal behavior requires a distinct prevention
   or evaluation mechanism and accepted evidence does not fit an existing leaf.

## Family boundaries

- **Epistemic** errors are prevented primarily by better evidence acquisition,
  source selection, direct inspection, or provenance labeling.
- **Reasoning** errors arise after relevant facts are available but are combined
  or distinguished incorrectly.
- **Control** errors concern received intent, authorization, or governing rules.
- **Execution** errors occur while carrying out otherwise authorized work.
- **Verification** errors concern claims about completed state or the validity
  of the checking instrument.
- **Provenance** errors damage the fidelity or reachability of historical and
  source records.

