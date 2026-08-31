---
id: AET-EM-0025
title: Drafted a doctrine without applying the governing type definition
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-26-living-text-present-tense-policy.md
source_lines: [68-118, 209-234]
session: https://claude.ai/code/session_016HqEGUGboxBj3A9FKcvkjz
pull_request: 140
agent_system: Claude Code
agent_model: Claude Opus 4.8 then Claude Opus 5
detection: operator challenged the inconsistent type recommendation
primary_type: control.contract.nonapplication
secondary_types: []
confidence: high
---

# Drafted a doctrine without applying the governing type definition

## Error description

The agent recommended and shaped a doctrine for a concrete behavioral rule even
though the always-loaded controlled vocabulary defined that artifact as policy.

## Evaluation

### Expected

The agent should have applied the policy/doctrine discriminator before drafting:
an enforceable operating rule is policy, while doctrine guides judgment without
prescribing an enforceable action.

### Observed

The agent anchored on its earlier “doctrine” wording, drafted in that mold, and
only afterward applied the discriminator and recommended policy.

### Why this qualifies

The governing definitions are quoted in the correction and the agent states they
were already present in its context. The mismatch was caught before persistence,
but the chat-stage recommendation and shaped draft had already contradicted the
available rule.

### Impact

If ratified unchanged, the rule would have landed in an artifact surface not
compiled into the operating contract and would not reliably govern later agents.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

You're right on both counts — the instinct is sound, and there *is* an established principle that speaks to it. But it's worth being precise about what exists, because there isn't a policy that directly names this case.

<routes ref="em:1b3c79 meta/policy/living-text-is-present-tense.md">
### What the brain already ratified

The closest ratified rule is **[retire-hand-kept-logs](/meta/plans/retire-hand-kept-logs.md)** (done, 2026-07-11) resting on **[merge-strategy](/meta/policy/merge-strategy.md)**: *the true-merge commit graph is the single provenance layer; the change narrative belongs in commit messages.* The operator's own ratifying argument was exactly yours:

> *"the only true guarantee is one source of truth… why is git history not enough? If we can't define [the log's unique value] discretely, better to remove the liability."*

And its "Demonstrated failure avenue" is precisely the risk here:

> *Stale-but-greppable prose gets retrieved and trusted as current state.*

That's the whole hazard of a comment like *"This hook used to also emit the digest…"* — it's a miniature hand-kept changelog embedded in a comment, the same liability the log purge removed, just at a smaller scale and in a spot the purge didn't sweep.

So: **the principle is ratified, but it was scoped to `log.md` files, not to retrospective narration living inside code comments and doc prose.** There is no dedicated policy or doctrine saying "don't narrate deprecated behavior in living text." What you're noticing is that principle's logic reaching past the specific artifacts it was written against.
</routes>

<routes ref="em:1b3c79">
### One caveat before a blanket sweep

Not all "used to" wording is pure history. There's a real distinction:

- **Retrospective narration** — "This hook *used to also emit* the session-init digest." This is the changelog fragment. Git owns it; drop it.
- **Present-tense pointer** — "the appraisal *now lives behind* `/priorities`." This tells a present reader *where the functionality went*, which git history does *not* surface at a glance. That's load-bearing and worth keeping.

The hook comment mixes both. Trimmed, it stays useful without the archaeology:

```bash
# Provision the session's toolchain — nothing more. The session-init appraisal
# (open work + heuristic top-3) is not emitted here; it lives behind the
# on-demand `/priorities` skill (.claude/skills/priorities/SKILL.md). This
# hook's sole job is to ensure the Elixir/OTP toolchain is present and warm...
```

Same information a reader needs, minus the "used to."
</routes>

### My recommendation

Since you say you've seen **several** examples, this is past a one-off edit — it's a candidate for a small **doctrine** (the standing direction: *living text states present tense; git narrates the past*) that policies/reviews can cite, or at minimum a documented cleanup pass. Per the contract, adding a doctrine/policy is a change to the shape of the brain that you ratify, so I won't create one unilaterally.

How would you like to proceed? A few options:

1. **Sweep first** — I grep the living surfaces (`.claude/`, `lib/`, `meta/policy`, `meta/flows`, doc bodies) for retrospective-narration instances, show you the list, and we decide per-instance. Good if you want to see the actual scope before committing to a rule.
2. **Ratify a doctrine** — I draft a `type: doctrine` (something like *"living text is present-tense; git carries the past"*) under `meta/doctrine/`, you ratify, then the sweep executes against it as the citing authority.
3. **Both** — sweep to size the problem, then ratify the doctrine so it doesn't recur, then clean up.

I'd lean toward **3**, since the branch name (`deprecated-wording-docs`) suggests you already intend this as real work rather than just a question. Which do you want?
````

````text
## User

if you lean policy over doctrine, then why did you create a doctrine?
what is the formal definition of each, and did you consider that before making the decision?
was the formal definition of each successfully surfaced to you while deciding, or is that something we need to investigate?

## Assistant

You've caught a real inconsistency, and the honest answers aren't flattering to my process. Let me take them in order.

**Why did I draft a doctrine while recommending policy?**

Because the two decisions happened in the wrong order. In my earlier message I offered option 3 with the words "I draft a `type: doctrine`," and when I sat down to write the draft I anchored on that phrasing and produced it in the doctrine mold. Only *after* drafting did I actually think about the discriminator that matters (doctrine isn't compiled into `CLAUDE.md`) — and that thought pointed at policy. So the recommendation formed *after* the artifact and contradicted it. I should have flagged that and not handed you a draft whose type my own reasoning disagreed with. (To be precise about state: I didn't *persist* a doctrine — nothing was written to disk; it's chat-only text pending your ratification. But drafting it in that shape and headlining it "doctrine" is the error you're pointing at, and "I didn't write a file" doesn't excuse it.)

<routes ref="em:6a9e78 em:fa15e7">
**The formal definitions.** Both are in the controlled-type-vocabulary, verbatim:

- **`policy`** — "a governance rule for how the brain operates; the source from which `CLAUDE.md` is compiled (lives under `meta/policy/`)."
- **`doctrine`** — "a persisted **intention statement**: a guiding principle or direction that shapes how the brain and its agents are designed and prioritized — the 'why' that informs judgment **without prescribing a specific enforceable action**. Doctrine sits *above* policy: a `policy` **implements** doctrine as a concrete, machine- or operator-enforceable rule…"

The discriminator is right there: **prescribes a specific enforceable action → policy; informs judgment without prescribing one → doctrine.** My draft's core ("rewrite living text to the new present; do not append a note about what it used to be") *is* a concrete, operator-enforceable-in-review action. By the definition, that's a policy. It also shares a parent lineage (merge-strategy, retire-hand-kept-logs) that is entirely policy. So applying the definition, policy is the correct fit — and notably, the "agents see it in the contract" argument I led with earlier is the *weaker* reason; the definitional one is the real one.
</routes>

**Did I consider the definitions before deciding, and were they surfaced?**

Surfaced: yes. They were in my context the whole time — the full `CLAUDE.md`, including that vocabulary, is in the operating contract I was given. So there's **no surfacing gap to investigate**; this isn't a tooling failure. Considered at decision time: no — not rigorously. I defaulted to my earlier "doctrine" phrasing instead of deriving the type from the definition. That's a reasoning lapse on my part, not a missing input. The fix is procedural and entirely on me: derive the type from the definition *before* drafting, not after.
````

## Classification

`control.contract.nonapplication` fits because the applicable controlled type
definition was available but not applied at the decision point. Semantic drift
does not fit as well: the agent did not restate the rule incorrectly; it failed
to use the correct rule until challenged.

## Detection and correction

The operator asked why the draft and recommendation conflicted. The agent applied
the formal discriminator, changed the artifact choice to policy, and did not
persist the wrong draft.
