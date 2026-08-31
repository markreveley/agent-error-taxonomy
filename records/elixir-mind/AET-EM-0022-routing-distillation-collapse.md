---
id: AET-EM-0022
title: Classified verbatim provenance routing as distillation
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-22-qiju-thread-storage-and-fit-each-layer-doctrine.md
source_lines: [70-95]
session: https://claude.ai/code/session_016sMoc9k6FSwoQgjtmuKS8K
pull_request: 127
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator challenged whether verbatim excerpt layering was distillation
primary_type: reasoning.distinction.collapse
secondary_types: []
confidence: high
---

# Classified verbatim provenance routing as distillation

## Error description

The agent called the lifting of thread content into topic documents a
distillation step even though route tagging copies passages verbatim and serves
provenance rather than condensation.

## Evaluation

### Expected

The answer should have kept archival retention, provenance routing, and knowledge
distillation distinct and classified each operation by what it actually does.

### Observed

The agent said distillation occurs when routing lifts content into topic docs. It
later explained that the excerpts are lifted whole and that routing is provenance
wiring, not distillation.

### Why this qualifies

The mechanism stated in the correction directly contradicts the earlier
classification. The error is established by the verbatim-copy behavior, not only
by the agent's concession.

### Impact

The collapse produced a misleading architectural account and distorted whether
the repository's stated doctrine described its actual layers.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

Is there a capability in Qiju that enables for cross agent work (clauee and codex reviewing eachother's responses for example)
If Qiju persists entire jsonl threads, how is that "distill don't dump"?

## Assistant

Both grounded now.

**1. Cross-agent work — no, not in the sense you mean.** The docs state flatly: *"Qiju is not an agent framework and does not orchestrate hosts."* There is no mechanism for one agent to review, critique, or respond to another's output. What it *does* provide is a shared passive substrate plus an `--agent` filter: all supported agents read/write the same store, and `qiju search --agent codex` slices records by author. So the capability is **handoff/continuity, not mutual review** — a filing cabinet both agents share, not a room where they talk. You could build "Claude reviews Codex's work" on top, but Qiju supplies only the shared memory and the author filter, not the orchestration.

**2. The JSONL is not "entire threads" — my earlier framing was loose, and you caught it.** Qiju does not persist threads at all. JSONL here is just the container encoding — one authored structured record per line, not a conversation dump. *"Qiju does not capture sessions silently and does not ingest raw transcripts."* The distillation happens at `qiju log` time. So Qiju is genuinely distill-don't-dump — arguably *more* aggressively than elixir-mind, which is the point worth owning: elixir-mind is actually the one that keeps verbatim (our `/capture` retains every substantive exchange word-for-word; the distillation in our model happens one layer later, when routing lifts content into topic docs). So to correct the table I gave you earlier: where I wrote Qiju stores "threads," it stores **records**; the "no raw transcript" bet is one Qiju holds more strictly than we do. My "distill don't dump" label was right about Qiju — I just muddied it by calling the JSONL a thread store, which it isn't.

## User

How is Elixir mind distilled out dump in that we're persisting verbatim content threads, which is essentially dump, and then extracting elements of those to inform and create provenance for analyses, which is, I guess, a form of distillation, but not really. Um, I don't think you could come to any conclusions whatsoever if you consider all expository pros layered over the threads to be distillation. And, meanwhile, we are clearly persisting these threads verbatim, which seems to be dumping. So, uh, please, if you could explain how we came to that conclusion and if it's still accurate. that this repo embodies distilled don't dump.

## Assistant

<routes ref="em:bec37f em:1b3c79">
You're right to push, and part of what I told you earlier was sloppy. First, the correction: routing is *not* distillation. The thread body is verbatim; the doc-side route-tagged excerpt log *lifts the tagged regions whole* — verbatim excerpts, headers demoted. So the entire routing/route-tagging apparatus is **provenance wiring, not distillation**. If anyone claimed "the tags/ledger over the threads *are* the distillation," that claim is false — and I effectively made it. You cannot call expository/provenance layering over a verbatim record "distillation." Conceded.

What's actually going on: two artifacts, two policies, two senses of one word. **Knowledge documents** (governed by distill-dont-dump) genuinely distill — raw material goes to citations. **Thread docs** (governed by session-capture) are deliberately verbatim; the policy *explicitly narrows* the word: *"'Distilled' here means the noise is dropped, not that the kept text is condensed."* So the thread doc is a dump minus the noise — that's not a bug, it's the archive layer doing its job. The two layers serve opposite masters: knowledge wants concision + queryability; provenance wants fidelity (you cannot reconstruct "what did we decide and why" from a lossy summary — a condensed record is a *worse* record).
</routes>

Verdict on "does elixir-mind embody distill-don't-dump?": **Yes, at the layer the policy governs** — the knowledge base a reader queries. **No, it does not distill its session archive — and never claimed to.** Where I misled you was collapsing those two layers and implying the provenance machinery over the threads counts as distillation. It doesn't. One honest smell falls out of this: "distilled" is overloaded in the contract (condensed-to-knowledge vs. noise-stripped), and that overload is exactly what tripped me. That's arguably a `type: issue` worth filing. Want me to write that up, or is the clarification enough?
````

## Classification

`reasoning.distinction.collapse` fits because the agent collapsed provenance
routing and content distillation despite their different operations and purposes.
The doctrine conclusion was downstream of that lost distinction.

## Detection and correction

The operator challenged the characterization. The agent separated the record and
knowledge layers and corrected route tagging to provenance wiring.
