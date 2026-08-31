---
id: AET-EM-0023
title: Returned a dead Pages link for a branch-only document
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-22-qiju-thread-storage-and-fit-each-layer-doctrine.md
source_lines: [141-149, 165-176]
session: https://claude.ai/code/session_016sMoc9k6FSwoQgjtmuKS8K
pull_request: 127
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator compared the working branch URL with the dead Pages URL
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Returned a dead Pages link for a branch-only document

## Error description

The agent presented a resource link that resolved to a Pages URL for a document
available only on an unmerged branch, so the link did not work.

## Evaluation

### Expected

Before presenting the link as a usable resource, the agent should have checked
whether the document was published from `main` or used the branch blob URL.

### Observed

The operator showed that the branch blob URL worked and the Pages URL did not.
The agent then confirmed that Pages deploys only from `main` and that branch-only
documents require branch URLs.

### Why this qualifies

The working/dead URL comparison and deployment configuration directly establish
the mismatch. The record does not assert whether the agent hand-built the URL or
received it from the old URL tool because the transcript gives inconsistent
accounts of that narrower cause.

### Impact

The operator received an unusable resource link and had to locate and supply the
working branch URL.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

Done — committed and pushed. Here's the answer to "fitness for purpose."

<routes ref="lib/elixir_mind/site_config.ex">
**"Fitness for purpose"** = each layer is shaped and judged against the *function it must serve*, not against one global standard. The mistake in "distill, don't dump" was treating retention as a single virtue applied everywhere. But the brain runs two layers whose jobs pull in opposite directions: the **knowledge layer** (understanding on demand) is fit when concise and queryable → distill hard and cite the raw; the **provenance/record layer** (reconstructing what was decided and why) is fit only when faithful → a condensed record is a *worse* record. "Distill" and "dump" aren't competing virtues on one dial — they're the right tools for two different jobs, and the verbatim record is what *licenses* aggressive distillation elsewhere.
</routes>

I built the full scope: the [fit each layer to its purpose](/meta/doctrine/fit-each-layer-to-its-purpose.md) doctrine, the reworded/renamed [capture-knowledge-cite-the-source](/meta/policy/capture-knowledge-cite-the-source.md) policy (functionality preserved, characterization fixed), the [is-to-ought analysis](/meta/analysis/is-to-ought-belief-grounds-doctrine.md), and the glossary terms [normative conclusion](/beliefs/glossary/normative-conclusion.md) and [descriptive premise](/beliefs/glossary/descriptive-premise.md). One decision worth your veto: I kept a *policy* (reworded) rather than folding everything into the doctrine, because removing the filing rule from the contract would be a functionality change — and policy-implements-doctrine is the structure the repo already teaches. Bundle verifies, 177 tests pass.
````

````text
## User

https://github.com/ob6to8/elixir-mind/blob/claude/qiju-thread-storage-59ur3l/meta/policy/capture-knowledge-cite-the-source.md is working

https://ob6to8.github.io/elixir-mind/meta/doctrine/fit-each-layer-to-its-purpose.html is not

how can we get you to consistently present links as active working urls

## Assistant

<routes ref="lib/mix/tasks/brain.url.ex">
Root cause confirmed: **Pages deploys only on push to `main`** (`pages.yml` → `branches: [main]`). So any doc created or changed on a feature branch has no live Pages page until the PR merges — the Pages URL 404s meanwhile, while the GitHub blob URL at the branch ref resolves immediately. My mistake was citing the canonical Pages URL for docs that only exist on this unmerged branch. The durable answer to "consistently" is mechanical: make `mix brain.url` liveness-aware so I run the tool instead of hand-building URLs (hand-behavior is exactly what fails intermittently). It now emits the live Pages URL when a doc is rendered *and* unchanged vs `origin/main`, and the GitHub branch blob URL otherwise (new, modified, or non-rendered dir), with `--pages` to force canonical. Backed by `SiteConfig.blob_url/2`, git-based liveness detection, 3 new tests, and an amended `response-resource-links` policy that says: route every response link through `mix brain.url`.
````

## Classification

`epistemic.claim.direct_check_omission` fits because link usability and branch
publication state were directly checkable before the resource was presented.
No unsupported tool-misuse subtype is assigned.

## Detection and correction

The operator supplied the working and dead URLs. The agent confirmed the deploy
boundary and implemented branch-aware URL selection.
