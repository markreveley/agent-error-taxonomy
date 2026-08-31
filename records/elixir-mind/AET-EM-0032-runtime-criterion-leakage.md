---
id: AET-EM-0032
title: Applied a production-runtime criterion to the development harness
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-27-secure-financial-agent-and-projects-namespace.md
source_lines: [154-240, 323-388]
session: https://claude.ai/code/session_01VDZ4JhC3FsNTwkcs1ci5uo
pull_request: 145
agent_system: Claude Code
agent_model: Claude Opus 5
detection: operator challenged why the development harness should change
primary_type: reasoning.distinction.collapse
secondary_types: []
confidence: high
---

# Applied a production-runtime criterion to the development harness

## Error description

The agent distinguished the coding harness from the production financial runtime
but then ranked `pi` as the best development harness using the runtime's minimal-
surface auditability criterion.

## Evaluation

### Expected

Development tools should be evaluated for development fluency and capability;
security constraints for sensitive financial data should govern the production
runtime that handles those data.

### Observed

The agent called `pi` the best building tool because its four-tool surface was
auditable. After the operator challenged the switch from Claude Code, the agent
acknowledged that it had collapsed the two harness categories and applied the
runtime criterion to the wrong one.

### Why this qualifies

The category boundary and the criterion leakage are both explicit in the initial
and corrected responses. The mismatch does not depend on a newly disclosed
preference for Claude Code.

### Impact

The recommendation would have imposed a development-tool migration and lost
operator fluency without improving the security of the actual financial-data
runtime.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

## First, the reframe that changes the design

<routes ref="em:7da513 em:f6de6f">
You asked for "completely secure." The honest answer is that a local model buys you **one** of the two security properties you need here, and it's not the harder one.
</routes>

| Threat | What it looks like | Does local hosting fix it? |
|---|---|---|
| **Confidentiality** — your data leaves | Tax returns, account numbers, balances sent to a third-party API and retained | **Yes.** This is exactly what self-hosting solves. |
| **Integrity** — your agent gets hijacked | A PDF contains text the model reads as instructions; the agent then does something with the tools it holds | **No.** Completely unaffected. |

The second one is the real risk in *this specific* application, and it's easy to miss. Financial documents are not trusted input. A brokerage statement, a vendor invoice, a 1099 emailed to you — these are documents **an outside party controls the contents of**. That's the textbook setup for indirect prompt injection: malicious instructions embedded in external content an agent is told to process. The 2026 track record is not reassuring — [GitHub Copilot's CVE-2025-53773](https://dev.to/waxell/the-trusted-document-problem-why-indirect-prompt-injection-is-now-your-ai-agents-1-security-risk-5c14) (CVSS 9.6) was RCE via exactly this mechanism, and CNCERT found [~21,000 exposed OpenClaw instances](https://atlan.com/know/prompt-injection-attacks-ai-agents/) silently leaking API keys and conversation logs to injected instructions.

<routes ref="em:7da513">
So: run the model locally *for confidentiality*, but understand that the security of this system is decided by **what the agent is allowed to do**, not by where the weights sit. That's the part your Jido question turns out to be the right answer to — I'll come back to it.
</routes>

---

## The models you named: all three are wrong for this, for different reasons

<routes ref="em:28fac6">
I checked each. They're real, they're recent, and none of them is what you want.

| Model | Released | Size | Why not |
|---|---|---|---|
| **Kimi K3** | July 26, 2026 | 2.8T total, 16/896 experts active, 1M ctx | **1.4TB** in MXFP4 — [~18× 80GB accelerators just to load](https://www.techi.com/kimi-k3-open-weights-inference-economics/), before any context. An 8×Blackwell node (1.5TB) "barely fits the weights with almost nothing to spare." Not personally self-hostable. |
| **TML Inkling** | July 15, 2026 | 975B total / 41B active, Apache 2.0, multimodal | The active-param count is a *speed* number, not a *memory* number — you still resident all 975B. ~500GB at 4-bit. It's explicitly positioned as [a base for fine-tuning via Tinker](https://artificialanalysis.ai/articles/thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model), debuting at 41 on the AA index — not a frontier reasoner. |
| **GLM-5.2** | June 13, 2026 | 753B / ~40B active, **MIT**, 1M ctx | The best of the three for this, and the license is the most permissive available. Still ~400GB at 4-bit. |

**Llama: don't.** Meta [ship-paused open-weight Llama](https://www.digitalapplied.com/blog/open-weight-models-h1-2026-retrospective-deepseek-qwen-llama) and pivoted frontier work to the closed Muse line. Behemoth never shipped. Building a 2026 system on Llama means building on an abandoned line.
</routes>

### The sizing mistake worth avoiding

The common error in MoE sizing is [using active params instead of total](https://www.spheron.network/blog/best-open-source-llms-self-host-2026-vram-guide/) — all experts must be resident. Every model above is a multi-node deployment.

**But look at what the workload actually is.** Processing tax documents and bank statements is: OCR → structured extraction → classification → arithmetic → summarization. That is *not* frontier reasoning. It's the workload the small-model tier has been crushing all year:

- **Document layer**: [Qwen2.5-VL-7B](https://presenc.ai/research/best-open-weight-ocr-document-ai-models-2026) is the dominant general document-AI model (OCR + layout + tables + chart extraction in one). For high-volume pure text, GOT-OCR2 does it in **580M params**. LightOnOCR if you want the smallest/fastest/cleanest.
- **Reasoning layer**: a 30–120B dense or small-MoE model for categorization and Q&A over the extracted structured data.

That whole stack fits on **one machine**, runs air-gapped, and will outperform a badly-quantized frontier model you can barely fit. Reach for GLM-5.2 later if you find a genuine reasoning ceiling — but design so the big model is optional.

---

## Infra options, as a ladder

| Tier | What | Cost | Confidentiality |
|---|---|---|---|
| **0. Workstation** ← *recommended* | [RTX PRO 6000 Blackwell, 96GB GDDR7 ECC](https://www.newegg.com/insider/nvidia-rtx-pro-6000-blackwell-workstation-96gb-gddr7-for-serious-local-ai/) (~$8.5k) · [DGX Spark, 128GB unified](https://www.blogarama.com/internet-blogs/1385826-codersera-blog/77195228-local-llm-hardware-showdown-june-2026-dgx-spark-strix-halo-rtx-6000-pro-max) ($4,699) · Mac Studio M3 Ultra (819 GB/s, largest single-machine unified memory outside enterprise) | $4k–15k one-time | **Total.** Air-gappable. |
| **1. Single-tenant bare metal** | Rented dedicated GPU box, your disk encryption, no hypervisor neighbors | $1–3/GPU-hr | High — but the host operator is in your trust boundary |
| **2. Confidential computing** | Intel TDX / AMD SEV-SNP + [H100/H200 in CC mode](https://www.spheron.network/blog/confidential-gpu-computing-nvidia-tee-encrypted-vram/): encrypted VRAM, TLS-like CPU↔GPU channel, composite attestation. [NVIDIA publishes 2–5% overhead](https://appscale.blog/en/blog/confidential-computing-ai-inference-tees-nitro-enclaves-nvidia-h100-h200-2026) | Cloud GPU + ~10% | **This is the credible way to run a 400GB+ model without owning it.** Azure Confidential GPU VMs, Phala, AWS Nitro Enclaves. |
| **3. Zero-retention API** | Enterprise API with contractual no-training/no-retention | Cheapest | Contractual, not technical |

<routes ref="em:f96824">
Tier 2 is the underrated one. It's how you'd use GLM-5.2 at full size without a $200k rack, and attestation gives you a *cryptographic* claim rather than a promise.
</routes>

<routes ref="em:f5914d">
### Serving stack

- **vLLM** — the production default. PagedAttention, continuous batching, and it takes FP8/MXFP4/NVFP4/INT4/GPTQ/AWQ/GGUF.
- **SGLang** — [lower latency than vLLM for structured JSON output, tool calls, and agent loops](https://builderai.tools/blog/state-of-open-source-llm-inference-engines-2026). Your workload is *exactly* structured extraction and tool calls, so benchmark this one seriously.
- **llama.cpp / Ollama** — laptop tier and CPU offload. `llama-server` gives an OpenAI-compatible endpoint, which matters below.

One caveat worth respecting: **FP4 is not the production default yet** — calibration tooling is still maturing and accuracy varies by model and task. Validate on your own documents before trusting a 4-bit quant with your taxes.
</routes>

---

## Harnesses — but note these are the wrong *category*

Everything you named (opencode, Warp, Zed, pi) is a **coding** harness. They're for *building* the system, not for *being* it. You do not want your tax pipeline running inside an interactive dev tool with `bash` and `write` in its tool list.

**For building it:**

| Harness | Fit |
|---|---|
| **pi** ([badlogic/pi-mono](https://www.npmjs.com/package/@mariozechner/pi-coding-agent)) | **Best fit.** Radical minimalism — [four built-in tools: read, write, edit, bash](https://explainx.ai/blog/pi-minimal-agent-harness-mario-zechner-guide-2026), everything else via TypeScript extensions. Built precisely because Claude Code's feature velocity made behavior unpredictable. A tool surface you can hold in your head is a tool surface you can audit. 62k+ stars. |
| **OpenCode** | Also strong. Go, [75+ providers including local via Ollama](https://www.firecrawl.dev/blog/best-ai-coding-agents), and explicitly **does not store your code or context** — designed for exactly the "can't send source to third parties" case. |
| **Zed** | Fast editor, GPL v3, agent interop via the open **ACP** standard (20+ agents, JetBrains). Good if you want editor-centric. |
| **Warp** | **Skip for this.** It rebranded to an "Agentic Development Environment" — cloud agents (Oz), session sharing, team knowledge in Warp Drive. Every one of those features is a data-egress path. Wrong tool for a confidential workload. |

**For the production pipeline: write your own.** Which brings us to your last question, and it's the best one you asked.
````

````text
## User

what about raising the pin of this repo to elixir 1.17+/OTP 26+? I would like to keep the speccing of this system here as long as possible. 

1. you say you'd build a workstation, but above you seemed to lean towards option 2 confidential computing, which I assume is a secure cloud option? or was that only for frontier models?
2. confirm qwen
3. greek to me, approved
4. agree - but we punt on actually writing code until everything is specced here
5. unclear why to use pi vs claude code to build as cc is what i have used to build this repo
6. noted


I think there should be a new type - projects. this would be for the development of specs, info, and research for projects/systems that will built outside of this repo. the idea is that this knowledge system could live in one place and evolve without duplication occurring across repos, or at least not until the architecture here has settled and been broken out into a standalone dev library. the idea is that all research and dev towards this project could both build out the knowledge layer as research is being done as well as draw from it. So yes, this could technically be an analysis - though it would belong to this project, which should have some sort of home as a type. Thoughts?

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

---

## 1. Confidential computing vs. workstation — I was ambiguous, here's the rule

Yes, CC is a cloud option: your workload runs in someone else's datacenter, but inside a hardware-encrypted enclave with attestation, so the host operator theoretically can't read VRAM.

I listed it at tier 2 as **the fallback for models too big to own** — and since I'm recommending the small-model stack, you don't hit that case. The decision rule:

> **Can the model fit on hardware you physically possess?** If yes → workstation, always. If no → confidential computing is how you use a bigger one without trusting a provider's promise.

For personal tax and banking documents, the workstation wins on every axis simultaneously — cheaper (one-time vs. per-hour), strictly more private (no attestation to reason about, no enclave escape research to track, air-gappable), and simpler. CC only becomes interesting if you later decide you need GLM-5.2 at full size. Treat it as a documented escape hatch, not part of the v1 design.

## 2. Qwen — confirmed, but I gave you a stale version

Correcting myself: **Qwen3-VL**, not Qwen2.5-VL. That earlier search surfaced an out-of-date article and I passed it through without catching it.

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) — dense at 2B/4B/8B/32B, MoE at 30B-A3B/235B-A22B, all **Apache 2.0**. Native 256K context, expandable to 1M. 32 languages, robust to low light/blur/tilt, improved long-document structure parsing.
- Built-in document tasks are exactly your workload: document parsing, text localization, information extraction, **table parsing**, formula recognition.
- The [flagship 235B-A22B rivals Gemini 2.5 Pro](https://qwen3-vl.com/) on OCR and document comprehension — but you want **8B or 32B**, which is the point: it fits your workstation with room to spare.
- Newer still: [Qwen3.5 (Feb 2026)](https://www.mindstudio.ai/blog/what-is-qwen-3-5-alibaba-open-weight-model) added a 0.8B–27B dense lineup plus MoE variants, Apache 2.0, with [Qwen3.5-VL](https://docs.nvidia.com/nemo/megatron-bridge/nightly/models/vlm/qwen35-vl.html) in the family.

The one thing I won't assert without evidence: which specific variant is best *on your documents*. Bank statement layouts and IRS forms are their own domain. That's a benchmark to run at build time — hold 20 real pages back as a test set — not a spec-time decision.

## 5. pi vs. Claude Code — use Claude Code, I conflated two things

Fair challenge, and you're right. I collapsed two different harnesses into one recommendation:

- **The harness that builds the system** — writes Elixir, edits specs, never touches a bank statement. Threat model: none beyond normal development. **Use Claude Code.** You know it, it built this repo, and switching costs you fluency for no security gain.
- **The runtime that processes financial documents** — that's the Jido thing you'd write, and it's not a coding harness at all.

pi's minimal 4-tool surface is an auditability argument, and auditability only matters for the *second* one. Since you're punting on code anyway (#4), this is moot for now. Revisit only if you later want the dev loop itself air-gapped.
````

## Classification

`reasoning.distinction.collapse` fits because two explicitly distinguished
criterion domains were treated as equivalent when ranking the development tool.
Restoring the development/runtime distinction reversed the recommendation.

## Detection and correction

The operator asked why `pi` was preferred over the tool already used to build the
repository. The agent retracted the recommendation and confined runtime
auditability to the production system.
