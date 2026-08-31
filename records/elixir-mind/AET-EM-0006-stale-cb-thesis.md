---
id: AET-EM-0006
title: Used a stale thesis as current CB authority
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-10-field-comparison-evals-and-cb-overlay-execution-path.md
source_lines: [216-245, 260-269]
session: https://claude.ai/code/session_01L9ydexp9srawtgZT8kBKGY
pull_request: 34
agent_system: Claude Code
agent_model: Claude Fable
detection: operator noticed deprecated terminology and requested reinspection
primary_type: epistemic.source.authority_misuse
secondary_types: []
confidence: high
---

# Used a stale thesis as current CB authority

## Error description

The agent represented a stale Composable Beliefs thesis as a fresh account of
the current system, inheriting deprecated terminology and false claims about
formal edge rules and portability.

## Evaluation

### Expected

An evaluation explicitly grounded in “what CB actually is” should prefer the
current glossary and schema over an older thesis, or reconcile their versions
before making current-state claims.

### Observed

The agent said it had fetched the repository fresh but relied on the thesis's
deprecated primitive/compound/directive terms and asserted that the thesis made
no portability claims. After the operator noticed the stale vocabulary, current
glossary inspection corrected two material claims and surfaced an omitted repair
primitive.

### Why this qualifies

The transcript identifies the stale source, the original claims, and the
current-source corrections. These are factual source-authority mismatches, not a
change in design preference.

### Impact

The stale account distorted the overlay comparison, weakened its portability
analysis, and overstated the cost of dependency repair until corrected.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="/meta/analysis/cb-epistemic-overlay-as-failure-chain-stabilizer.md /meta/plans/epistemic-overlay.md">
All three tasks are done or ready — here's the Composable Beliefs assessment.

---

# Could CB's four-typed DAG, as an overlay, stabilize a knowledge base against the failure chain?

First, grounding the evaluation in what CB actually is (fetched fresh from the repo, plus the prior comparison already in this bundle): CB stores beliefs as immutable JSON nodes in a DAG with four epistemic operations — the thesis names them *primitive* (atomic claim grounded in one source), *compound* (composes assertions into something none contain alone), *inference* (a conclusion licensed to exceed its deps), and *directive* (what needs to happen); the epistemic-overlay plan's attestation/aggregation/inference/prescription is the same quartet under evolved names. Beliefs are never edited in place — they are superseded — and the load-bearing sentence for your question is this one from the thesis: **"When a primitive is superseded, every compound depending on it is flagged as potentially stale — detectable by query."** Enforcement is deterministic (six structural contracts, schema verifier, no LLM in the read path). The prior session's diagnosis stands: CB is three projects fused at one substrate, and the four-type layer is the one piece that's genuinely universal.

## Mapped against the five stages

**Stage 3 (cross-reference drift) — yes, and this is the headline.** Drift is the failure of knowing which existing pages a new or contradicting source touches — an *unbounded recall problem* in an untyped corpus, which is why Karpathy's lint pass degrades at scale. A dependency DAG with supersession converts it into *bounded graph traversal*: supersede an attestation, and the affected set is the transitive closure of its dependents — computed, not guessed. CB has exactly this mechanism. The deeper reason it works is a **timing asymmetry**: dependency edges are cheapest to create at intake, when the source is fully in context, while drift detection is needed forever afterward, when context is gone. The overlay moves the epistemically hard work to the one moment it's easy. The honest conditional: this only holds if the edges exist and are correct, and edge creation is itself probabilistically-enforced agent behavior. So the overlay doesn't eliminate the probabilistic-enforcement root cause — it *relocates* the bet from "update all affected pages, forever, from partial views" (unbounded, repeated) to "record your dependencies once, at intake, in full context" (bounded, one-time). That is a much better place to put the bet, and it's measurable — an edge-completeness eval is the fan-out eval from the eval-suitability analysis wearing graph clothes.

**Stage 5 (trust collapse) — yes, second-strongest.** Trust collapses because degradation is invisible and therefore binary: you trusted, then one bad retrieval and you don't. The DAG makes epistemic state visible *per statement*: this concept rests on a superseded attestation; this inference is ungrounded; this node has twelve dependents (blast radius). Trust becomes calibrated and local instead of global and brittle — the system tells you *exactly what* to distrust. A brain that shows its wounds doesn't lose the operator the way a brain that rots silently does.

**Stage 1 (context saturation) — partial.** The DAG gives agents *principled* partial views: instead of arbitrary retrieval, walk the grounding subtree outward from a relevant node. It changes what a partial view is, not whether you have one — and attaching new content still requires finding the attachment point, which is the recall problem again.

**Stage 2 (dedup/fragmentation) — no, arguably slightly negative.** The DAG doesn't help find the existing twin, and a missed duplicate is *worse* in a DAG: each twin accretes its own dependency subtree, and merging later means rewiring edges, not just concatenating prose. The one offset: a mandatory-grounding discipline forces a structured search for candidate dependencies at intake, which can surface the twin as a side effect — but that's the dedup search under another name. **The overlay does not defend the chain's entry gate. The dedup recall probe stays prior work no matter what happens with the overlay; they are complements attacking different stages.**

**Stage 4 (taxonomy entropy) — conditional.** The graph is an axis orthogonal to the tree and can absorb pressure that otherwise deforms the taxonomy (over-nesting to express relatedness). But CB is itself the cautionary tale here: its open `kind` axis sprawled past 40 values and atomization produced ~400 belief files — a DAG can *generate* entropy of its own kind. The overlay stabilizes stage 4 only with CB's failure modes bounded out: closed four-enum, concept-granularity nodes, no second axis — exactly the scope boundaries the epistemic-overlay plan already draws.

**Two structural conclusions.** First, the overlay extends this bundle's core move — structural enforcement — from *form* into a slice of *semantics* (groundedness, dependency-freshness), which is precisely the territory the field-comparison analysis said CI couldn't reach. It doesn't cover all semantics (dedup and filing quality stay editorial), but stages 3 and 5 are the ones it does cover, mechanically. Second, **the stabilization runs entirely through supersession**: staleness propagation is the mechanism, and it requires supersede-not-edit — the one genuine gap versus CB, since this bundle edits in place. That reframes open question 3 of the epistemic-overlay plan: if the overlay's purpose is stabilization (rather than explorability), supersession isn't a deferrable phase, it's the point — a groundedness-only v1 delivers audit but not the anti-drift machinery. And it upgrades the plan's motivation generally: from "explorability plus an integrity nicety" to "the stage-3/5 stabilizer of the failure chain." One caveat that CB itself understood: an *advisory* DAG rots like any advisory structure — edges nobody verifies go stale like prose links. The overlay stabilizes only as an enforced overlay; `mix brain.graph` in the gate suite is not an accessory, it's the mechanism.

## Language-agnostic overlay, or native integration?

Split the overlay into its three layers, because they answer differently:

**The data model — genuinely agnostic, and should be specified that way.** Epistemic role plus dependency edges as frontmatter (a role key or type-derived, deps as lists of stable ids) is exactly `verified_by`'s shape today: YAML any toolchain in any language can parse, over plain markdown. Specified as an OKF extension, the four-type overlay could sit above *any* bundle-shaped knowledge base — an Obsidian vault, a Karpathy wiki — and given the survey found nobody in the field with structural epistemics, a portable spec would be the first of its kind out there. CB's thesis makes no portability claims, but the OKF substrate both repos share is precisely the portable layer.
````

````text
## User

Yes author it. But before you do, examine cb again. You mentioned primitive, compound, directive. These are deprecated terms. The up to date terms are attestation, aggregation, and prescription. If these were antiquated, could some of the info inderlying your orher info be as well?

Also, when would it be worth taking on the beginnings of architectural sketchings, of how this move could be made, and how what of cb we would want to import into second-brain to develop this? Should that be this thread or a fresh thread, referencing your analysis doc?

## Assistant

<routes ref="/meta/analysis/cb-epistemic-overlay-as-failure-chain-stabilizer.md">
The re-examination pays off — the operator's suspicion was correct, and materially so. The current glossary corrects **two of my claims** (both traced to the stale thesis): CB *does* have formal edge rules (attestations carry no deps; aggregations/inferences require them; non-contract prescriptions "required-or-stipulated"), and CB *does* make portability claims — it explicitly positions itself as an "opt-in ceiling" layer over OKF as "portable knowledge methodology," which directly anticipates your overlay framing. The load-bearing staleness claim survives and gets sharper: staleness (active nodes depending on superseded/retracted nodes) is detected by audit, and there's a first-class repair primitive I didn't know about — the **"dep-repoint front door,"** an atomic swing of a dep from a superseded node to its successor. That also softens my stage-2 "merging duplicates means costly edge rewiring" objection. And one meta-observation worth filing: the thesis going stale *inside CB itself* — while `belief-graph.md` says "query it rather than restating it" — is a live demonstration of stage-3 drift striking prose that lives outside the enforced graph.
````

## Classification

`epistemic.source.authority_misuse` fits because the agent treated an outdated
source as authoritative for current system behavior despite fresher canonical
materials. Direct-check omission is secondary in spirit, but the shared cause of
the claims was selecting the wrong authority.

## Detection and correction

The operator recognized deprecated terminology and asked whether the underlying
analysis could also be stale. The agent re-read the current glossary, corrected
the two claims, and recorded the source-staleness check in the analysis.
