---
id: AET-EM-0012
title: Made optional Jido reconstruction sound required
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-13-advisor-pattern-and-rolling-your-own-harness.md
source_lines: [85-113, 156-176]
session: https://claude.ai/code/session_011No6T6tQoaV17R76v38UZ9
pull_request: 79
agent_system: Claude Code
agent_model: unknown
detection: operator challenged the inconsistency between reconstruction and native parity
primary_type: reasoning.distinction.collapse
secondary_types: []
confidence: high
---

# Made optional Jido reconstruction sound required

## Error description

The agent collapsed two distinct integration choices and presented a client-side
reconstruction as what Jido users would have to build, although Jido could call
the native Anthropic tool over HTTP.

## Evaluation

### Expected

The answer should have separated native raw-HTTP access from an optional
two-call approximation and stated that Elixir framework choice does not remove
API capabilities.

### Observed

The answer led with reconstruction and enumerated lost conveniences as though
they followed from using Jido. After the operator challenged it, the agent said
native raw HTTP provides full feature parity and that reconstruction is only a
deliberate alternative.

### Why this qualifies

The initial characterization and corrected capability account are directly
inconsistent. The correction explains the distinction using the same endpoint
and response behavior, so the error does not depend on the apology alone.

### Impact

The claim overstated the cost and limitations of an Elixir integration and could
have prompted unnecessary orchestration work.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="/meta/analysis/when-to-roll-your-own-advisor-harness.md">
Good — I have the actual advisor-tool docs now. Here's the breakdown, addressing each question.

## 1. Is this only for Claude Managed Agents (CMA)?

No — and this is worth separating into two different things that got conflated in the Instagram post:

- **The advisor pattern** (Sonnet executes, Fable advises) is a **native Messages API tool**: `type: "advisor_20260301"`. You add it to the `tools` array of an ordinary `/v1/messages` call with a beta header (`advisor-tool-2026-03-01`). It is **not** a Claude Managed Agents feature — CMA just happens to be one place it gets demonstrated. The advisor sub-inference runs **server-side, inside the same request** — Anthropic calls Fable for you and hands the advice back to Sonnet. You don't build a multi-agent harness for this one; you just add a tool definition.
- **The orchestrator pattern** ("plan big, execute small" — Fable dispatching parallel Sonnet workers) is a genuinely different, heavier thing. That one does live under Claude Managed Agents / the Agent SDK, because it involves spinning up multiple concurrent sub-agents, not a single in-request tool call.

So: yes, you need API access either way (an API key, code-level requests) — this isn't available through a no-code UI. But the *advisor* pattern specifically is close to turnkey (one tool entry, one request); the *orchestrator* pattern is the one that actually requires building/using a multi-agent harness.

## 2. Can you do this from the Claude consumer app or cloud Claude Code agents?

Correct, you can't — not as a user-facing toggle. The advisor tool is a beta **API** feature gated behind an `anthropic-beta` header on raw Messages API calls. The consumer chat app (claude.ai) doesn't expose tool configuration to end users, and cloud-hosted Claude Code sessions (like this one) don't let you inject custom `tools` arrays into the underlying model calls either — that's controlled by the harness, not you. To use it you need to be the one writing code against `api.anthropic.com` (or a Claude Agent SDK integration that exposes tool configuration), with your own API key.

## 3. Could you replicate this with a different framework, e.g. Jido (Elixir)?

Yes, but with a caveat: what you'd build in Jido is a **client-side reimplementation** of the pattern, not the native tool.

The native `advisor_20260301` tool only exists inside Anthropic's own API surface — a Jido agent (or any other framework) can't invoke it directly unless the code underneath is literally making Anthropic Messages API calls with that tool type. But nothing stops you from implementing the *pattern* yourself in Jido:

- Your Jido executor agent runs normally (say, on Sonnet).
- At a decision point, it pauses and your own orchestration code fires a **separate** API call to Fable, passing the transcript so far, asking for a plan/critique.
- You inject Fable's response back into the executor's context and let it continue.

That's functionally the advisor pattern, just done as two ordinary API calls stitched together by your own control flow instead of one request where Anthropic does the stitching server-side. You'd lose some native conveniences: the `pause_turn`/resume mechanics, the encrypted `advisor_redacted_result` handling, the `usage.iterations` cost breakdown, and Anthropic's own optimized prompt caching for the advisor's view of the transcript — you'd have to build equivalents of all of that yourself. But the core idea (cheap model executes, strong model periodically advises) is framework-agnostic and works fine as a hand-rolled Jido action/agent.
````

````text
## User

So why then were you saying that with jido that the option was to actually rebuild the functionality from scratch, missing some convenience features. It sounds like now you're saying that, actually, there's a hundred percent parity

## Assistant

Fair catch — I conflated two different approaches in my two answers. Let me untangle it properly, because you get genuinely different outcomes depending on which one you build.

**Approach A: Jido makes raw HTTP calls that include the actual `advisor_20260301` tool type.**

This is what I described in my last message. Here, you *are* invoking Anthropic's real server-side feature — your Elixir code is just the HTTP client; Anthropic's servers do the actual work (running the Fable sub-inference, producing the `advisor_tool_result`, handling `pause_turn`, returning `usage.iterations`, doing the encryption on `advisor_redacted_result`). Since it's the same API endpoint responding with the same JSON regardless of what language sent the request, this gets you **100% feature parity** with the Python/TS SDK. The only thing missing is *SDK convenience* — typed request/response structs, a helper method that automatically resends on `pause_turn`, etc. That's boilerplate you write once in Elixir (parse JSON, check `stop_reason`, loop if `pause_turn`) — real work, but not lost capability. Nothing about the feature itself degrades.

**Approach B: Jido doesn't touch the advisor tool at all — it just makes two independent ordinary Messages API calls** (call Sonnet, separately call Fable with the transcript, splice the advice back in as a message) to mimic the *concept*.

This is what my earlier answer was actually describing, and here the losses are real, because you're not using Anthropic's feature — you're rebuilding an approximation of it yourself:
- No single-request efficiency — two round trips instead of one server-side sub-call.
- No native `advisor_redacted_result` encryption semantics (moot anyway if you're calling Fable yourself, since you'd just see its raw output).
- No `usage.iterations` breakdown — you'd track cost bookkeeping yourself.
- No built-in `pause_turn`/resume protocol — you'd design your own loop control.

So the accurate statement is: **if you're willing to speak raw HTTP/JSON to `api.anthropic.com` with the correct `advisor_20260301` tool block, Jido gets you the real thing, full parity, modulo SDK sugar.** The degraded, "rebuilt from scratch" version only applies if you skip the native tool type entirely and hand-roll the two-call pattern instead — which you might still choose to do for simplicity, or if you want visibility into the advisor's raw reasoning rather than treating it as an opaque tool call, but it's a deliberate simplification, not a forced one.
````

## Classification

`reasoning.distinction.collapse` fits because the answer treated native API use
and a client-side approximation as one framework-imposed path. A factual
capability misstatement is the symptom; the supported cause is failure to keep
the two approaches distinct.

## Detection and correction

The operator challenged the apparent contradiction. The agent separated the two
approaches and corrected native Jido access to full parity apart from SDK sugar.
