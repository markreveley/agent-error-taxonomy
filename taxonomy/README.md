# Taxonomy

This directory defines the reusable error types referenced by incident records.
The taxonomy is evidence-led: a type is added when at least one evaluated
incident needs it, not to make a theoretically complete tree.

The accepted v0.1 hierarchy and assignment rules are in [`index.md`](index.md).
Each type definition includes:

- a stable type ID and concise name;
- a behavior-focused definition;
- inclusion and exclusion criteria;
- contrast cases against neighboring types; and
- accepted incident IDs classified under it, once those IDs are assigned.

The filenames are the stable dotted type IDs. Definitions are intended to
remain domain-independent; incident status, confidence, impact, detection, and
recovery belong to the evidence records rather than the type hierarchy.

The current v0.1 taxonomy contains 14 leaf types in six families. Rejected scan
candidates do not support type definitions or examples. Retained contested
records appear in example lists with their status, but are not counted as
confirmed support.
