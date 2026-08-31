---
id: AET-EM-0033
title: Assumed the Elixir base image was fixed before checking provisioning
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md
source_lines: [337-356, 457-499]
session: https://claude.ai/code/session_01VDZ4JhC3FsNTwkcs1ci5uo
pull_request: 145
agent_system: Claude Code
agent_model: Claude Opus 5
detection: operator challenged the fixed-image premise
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Assumed the Elixir base image was fixed before checking provisioning

## Error description

The agent strongly recommended against raising the repository's Elixir pin based
on an unchecked premise that future Claude Code images were fixed and outside
the operator's control.

## Evaluation

### Expected

Before making an infrastructure recommendation, the agent should inspect package
origin and environment setup mechanics and distinguish active-session state from
new-session provisioning.

### Observed

The agent said raising the pin would leave every future web session broken until
the image caught up. Subsequent inspection showed that operator-controlled cached
setup scripts provision packages for new sessions, making an ordered upgrade
feasible.

### Why this qualifies

The initial mechanism claim and the directly inspected package/setup comparator
are both preserved. The corrected answer retains a real ordering risk but rejects
the fixed-image premise that drove the original recommendation.

### Impact

The agent incorrectly discouraged an overdue toolchain upgrade and misdiagnosed
why the existing pin matched the environment.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

## The pin: don't raise it, and you don't need to

Two separate things got tangled here.

**Speccing this system in the repo requires zero Elixir changes.** Specs are markdown. The pin gates *running* Jido code here, not documenting it. So your actual goal — "keep the speccing of this system here as long as possible" — is unblocked today.

**And raising it right now would actively break things.** I checked what this container ships:

```
Erlang/OTP 25 [erts-13.2.2.5]
Elixir 1.14.0 (compiled with Erlang/OTP 24)
```

`mix.exs` declares `elixir: "~> 1.14"`, and both `ci.yml` and `pages.yml` pin `otp-version: "25"` / `elixir-version: "1.14"`. Raise the requirement to `~> 1.17` and `mix` refuses to run *in this sandbox* — which means every Claude Code web session loses `brain.verify`, `brain.contract`, the pre-commit hook, and the SessionStart hook, until the image catches up. You'd break the working environment to enable something you're not doing yet.

Worth being clear about what the pin was never blocking, either: even at 1.17+, Jido still can't come into this repo, because the **zero-dependency constraint** is the real blocker and it's load-bearing (`mix.exs` says why — the toolchain "runs offline in any sandbox"). Jido would pull `req_llm` → `Req` → the HTTP stack into a project whose entire design premise is that it has no deps. The pin was the least of the three blockers.

**Raise it when something concrete needs it, and check the runner image first.** 1.14 is from Sept 2022 and is genuinely old, so this isn't "never" — it's "not for this reason."
````

````text
## User

ok sounds good, but why exactly does elixir need to be pinned to 1.14? wouldn't it just break active images, but new images would be built fine with 1.17?

1. 

2. I guess i would assume we just start with the latest Qwen? what workstation would have the recommended specs? how do you handle updates backups and data transfer with an air gapped machine?

5. what do you think led to the conflation? what is meant by "Revisit only if you later want the dev loop itself air-gapped."?


re: questions:

1. yes
2. yes

## Assistant

All gates green. Here are your answers.

## The pin — you were right, my reasoning was wrong

I assumed the base image was fixed and outside your control. It isn't. Here's what's actually true:

```
elixir  1.14.0.dfsg-2   from  archive.ubuntu.com/ubuntu noble/universe
erlang-base  1:25.3.2.8+dfsg-1ubuntu4.6
Ubuntu 24.04.4 LTS (Noble Numbat)
```

**The pin is at 1.14 because that is exactly what `apt install elixir` yields on Ubuntu 24.04.** It was never a decision — it's a distro default that `mix.exs` and both workflows were written to match. Elixir isn't even in Claude Code's [documented pre-installed tools](https://code.claude.com/docs/en/claude-code-on-the-web) (Python, Node, Ruby, PHP, Java, Go, Rust, C/C++, Docker, Postgres, Redis — no BEAM), so it's arriving via a setup script on this environment.

And setup scripts are yours: *"To add packages that aren't pre-installed, use a setup script. The script's output is cached, so packages you install there are available at the start of every session without reinstalling."*

So your model is correct — new sessions would pick up 1.17 fine. The one refinement: it doesn't happen automatically from a repo edit, because the setup script lives in **environment config, not the repo**. Which makes this an ordered change, not a one-liner:

1. Update the environment setup script to install Elixir 1.17+/OTP 26 (Erlang Solutions repo, or asdf/mise — not `apt`, which will keep handing you 1.14).
2. Start a session, confirm `elixir --version`.
3. *Then* bump `mix.exs` and the `elixir-version`/`otp-version` pins in `ci.yml` and `pages.yml`.

Order matters: reverse it and a session starts, `mix` refuses the version, and every brain task is dead until you fix the script. That was the real content of my warning — I just attributed it to the wrong cause.

Worth noting it still doesn't unblock Jido *here* — the zero-dependency constraint is the binding one, and this sandbox is capped at 4 vCPU / 16 GB RAM / 30 GB disk, so it could never run a local model regardless. Spec here, run on the workstation. But raising the pin is cheap, overdue (1.14 is from Sept 2022), and worth doing on its own merits.
````

## Classification

`epistemic.claim.direct_check_omission` fits because the provisioning mechanism
was concrete and directly checkable before the recommendation. The later setup-
script inspection materially disproved the fixed-image claim.

## Detection and correction

The operator challenged the active-image/new-image assumption. The agent checked
package provenance and setup documentation, reversed its recommendation, and
specified the safe upgrade order.
