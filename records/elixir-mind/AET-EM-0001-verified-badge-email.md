---
id: AET-EM-0001
title: Equated GitHub's Verified badge with committer email
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-08-adopt-session-capture-routing-and-route-tags.md
source_lines: [757-779]
session: https://claude.ai/code/session_018uKND3Ycc71z55zPUqU86M
pull_request: 13
agent_system: Claude Code
agent_model: Claude Opus 4.8
detection: operator-requested tutorial prompted factual reinspection
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Equated GitHub's Verified badge with committer email

## Error description

The agent said that setting the author and committer email would make GitHub show
a commit as Verified, conflating identity metadata with cryptographic signature
verification.

## Evaluation

### Expected

Before explaining the badge, the agent should have checked GitHub's verification
semantics and distinguished commit identity fields from signature validation.

### Observed

When asked to turn its earlier explanation into a tutorial, the agent recognized
that its claim was an oversimplification: the badge represents a validated
cryptographic signature, and email alone never produces it. The original claim
appears in the earlier bootstrap thread at the same revision,
`meta/threads/2026-07-05-greenfield-okf-bootstrap-and-verification-layer.md:704-712`.

### Why this qualifies

The correction states the factual comparator and identifies the precise mismatch.
The error is confirmed because both the earlier claim and its factual correction
are preserved at the pinned revision.

### Impact

The explanation could teach the operator to treat email rewriting as sufficient
for commit verification and obscure the actual role of signing configuration.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## User

Retrofit
Then - create a tutorial explaining what's occurring with "The tip commit is now b4c6c67 with both author and committer set to noreply@anthropic.com, so GitHub will show it as verified"

## Assistant

The bootstrap thread is fundamentally a **governance/tooling** session — its content is homed in `meta/` (policies, the contract compiler, the registry/verifier), none of which are `sb:`-id concept sinks. The one genuine knowledge concept it touches is **OKF** (`em:24bd1e`). Let me read the OKF-discussing turns to find an honest region to tag, and glance at the OKF concept.

This bootstrap session mostly built the brain's **governance/tooling** (policies, the contract compiler, the registry/verifier) — homed in `meta/`, not `concept` sinks — so honestly most strands are `unrouted`. The one genuine knowledge feed is turn 2's definition of *what an OKF bundle is* → the OKF concept (`em:24bd1e`). Retrofitting the ledger and that one route tag over the frozen body:

Task 1 committed (`6cb9110`). Now **task 2 — the tutorial.** This is a chance to be precise: my earlier one-liner ("set committer email → GitHub shows verified") was actually an oversimplification worth correcting, since GitHub's "Verified" fundamentally means a cryptographic *signature*, not an email. Let me check the existing tutorial format first.

Both done — all three unpushed commits are correctly authored (`noreply@anthropic.com` for author and committer), so the stop-hook won't flag them.

## 1. Retrofit — `6cb9110`
Added a `## Routing` ledger + a route tag over the **frozen body** of the 2026-07-05 bootstrap thread (no re-render — it's a verbatim `/persist-thread` archive). Honest outcome: that session mostly built governance/tooling homed in `meta/` (not `concept` sinks), so 11 of 12 ledger rows are `unrouted`; the one genuine knowledge feed — turn 2's definition of *what an OKF bundle is* — is tagged to the OKF concept (`em:24bd1e`), whose excerpt log I materialized. All five `mix brain.route_tags` checks green. This demonstrated the retrofit motion (tag an existing frozen body, don't rewrite it) and honestly showed that not every thread has rich concept sinks.

## 2. Tutorial — `8d7b806`
`meta/tutorials/what-makes-a-commit-verified-on-github.md`. It deliberately **corrects** my earlier shorthand rather than repeating it:
- **Author vs committer** — every commit carries two identities, and they diverge on rebase/amend/merge/agent commits.
- **"Verified" is a signature check, not an email** — the badge means a cryptographic signature GitHub can validate against a key bound to the committer identity; an email alone never produces it.
- **Why the email fix still worked here** — this environment signs on behalf of the `noreply@anthropic.com` bot identity, and the stop-hook is a local proxy for that; re-authoring *enabled* the signature, it didn't *become* it. (Also notes the `noreply@github.com` merge commits are GitHub's own web-flow signed commits — which is why they're left alone.)
````

## Classification

`epistemic.claim.direct_check_omission` fits because a readily checkable factual
claim was made without checking the authoritative semantics. This is not merely
source-authority misuse: the central failure was failing to verify the direct
claim, not choosing between conflicting repository sources.

## Detection and correction

The operator asked for a tutorial about the claim. During that task the agent
rechecked the semantics, corrected the explanation, and documented the
signature-versus-email distinction.
