# Evidence and classification methodology

## Unit of analysis

The unit is an **incident**: one temporally bounded agent behavior that departs
from a supported expectation. A correction sequence may span several user and
assistant messages and still be one incident. Conversely, a single response can
contain more than one incident when the behaviors have independent expectations
and causes.

The taxonomy classifies the agent behavior, not merely the downstream symptom.
For example, a false completion report caused by failure to inspect repository
state is primarily a state-inspection error and secondarily a completion-report
error when the evidence supports both.

## What qualifies as an error

A record needs all four elements:

1. **Agent behavior** — a claim, decision, omission, action, or report attributable
   to the agent.
2. **Comparator** — an instruction, repository rule, tool result, source, later
   inspection, or other defensible account of what should have happened.
3. **Mismatch** — an explainable difference between the behavior and comparator.
4. **Evidence** — transcript text and, when available, artifact or test evidence
   sufficient for another reviewer to evaluate the mismatch.

The following do not qualify by themselves:

- a tool, network, dependency, or environment failure the agent handled correctly;
- a user preference first disclosed after the disputed response;
- a design disagreement with no controlling requirement or factual resolution;
- harmless exploration that the agent clearly labeled as uncertain;
- an adverse outcome without evidence of an agent mistake; or
- a retrospective statement that an error occurred without enough context to
  identify the behavior.

## Status and evidence strength

- `confirmed` — the comparator and mismatch are directly established. Typical
  support is an artifact/test result, an explicit instruction violation, or a
  correction whose factual basis is shown in the transcript.
- `probable` — the evidence strongly indicates an error but a material premise
  cannot be independently established from the retained record.
- `contested` — reasonable readings differ about whether the behavior violated
  the expectation. These records are retained for analysis but must not be
  counted as confirmed errors.

An agent's admission raises confidence but is not conclusive by itself. An agent
can also over-concede.

## Evidence fidelity

Every record must preserve the decisive transcript exchange verbatim:

- retain role labels and message order;
- do not silently correct spelling, punctuation, capitalization, or formatting;
- do not use an ellipsis inside the decisive passage;
- quote enough preceding and following text to make the mismatch intelligible;
- cite source repository, immutable revision, file path, and exact line ranges;
- keep analysis outside the verbatim block; and
- never reconstruct hidden reasoning or tool output absent from the persisted
  source.

Additional excerpts may be included when the mistake, detection, and correction
occur in different parts of the thread. Line references are anchored to the
recorded source revision so later edits do not invalidate provenance.

## Classification procedure

For each incident:

1. Describe the behavior without using a taxonomy label.
2. Identify its nearest cause supported by the evidence.
3. Compare that cause against every existing type's inclusion and exclusion
   criteria.
4. Assign the narrowest matching type as `primary_type`.
5. Add `secondary_types` only for independently useful, evidenced facets; do not
   turn the taxonomy into a list of every consequence.
6. If no type fits, propose a type with a definition, inclusion rule, exclusion
   rule, and contrast cases. Check all existing records before adding it.

Types describe repeatable failure patterns. Project names, tools, model names,
and one-off symptoms belong in record metadata, not in type definitions.

## Review and deduplication

Two candidate findings are the same incident when they concern the same agent
behavior, expectation, and correction sequence. Merge them and preserve all
useful evidence. Similar mistakes in different sessions remain separate
incidents linked to the same type.

Before accepting a record, a reviewer checks:

- the quote against the source at the pinned revision;
- the line ranges and role attribution;
- the comparator and status;
- the primary type's inclusion and exclusion criteria; and
- whether another record already captures the incident.
