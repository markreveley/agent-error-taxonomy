---
id: AET-EM-0043
title: Claimed thousands of lookups without inspecting usage
status: confirmed
corpus: elixir-mind
source_repository: https://github.com/markreveley/elixir-mind.git
source_revision: e7eb8ed37b09afdf1c6ba156f70d6655d72778df
source_path: meta/threads/2026-07-29-elixir-comprehension-tutorial.md
source_lines: [57-101, 119-128]
session: https://claude.ai/code/session_01CX6rEN67aHag6T1UN1UcVo
pull_request: 186
agent_system: Claude Code
agent_model: Claude Opus 5
detection: source inspection while creating the durable tutorial
primary_type: epistemic.claim.direct_check_omission
secondary_types: []
confidence: high
---

# Claimed thousands of lookups without inspecting usage

## Error description

The agent justified a map-building comprehension by claiming the map was looked
up thousands of times, without checking call sites or the data population.

## Evaluation

### Expected

Before teaching a quantitative performance rationale, the agent should inspect
the relevant usage and data volume or state the rationale without invented
scale.

### Observed

The agent confidently said the map was looked up thousands of times. Source
inspection while filing the tutorial found only three documents with seven
edges, so a full build performed seven relevant lookups; the actual design
rationale was API shape.

### Why this qualifies

The later count directly contradicts the quantitative assertion, and the agent
states that the earlier number was recalled rather than checked.

### Impact

The response mis-taught a beginner and supplied a false performance explanation
for an otherwise reasonable data-structure choice.

## Verbatim evidence

The following text is reproduced exactly from the source cited in frontmatter.

````text
## Assistant

<routes ref="meta/tutorials/elixir/comprehensions-that-build-maps.md lib/elixir_mind/site.ex">
This is `lib/elixir_mind/site.ex:169-171` — the site builder's lookup table for `em:` ids.

### What it does, in one sentence

It takes a list of pages and returns a map that lets you look a page up by its id: `%{"em:4c9e1f" => page, "em:a96688" => page, …}`.

### Line by line

```elixir
defp build_id_index(pages) do
  for %{fm: %{"id" => id}} = p <- pages, is_binary(id), into: %{}, do: {id, p}
end
```

**`defp`** — define a *private* function. `def` would make it callable from other modules; `defp` keeps it internal to `ElixirMind.Site`.

**`for … do …`** — a **comprehension**. Think of it as "for each thing in this list, produce a thing". By default it produces a list, but here `into:` changes that (see below). It's Elixir's version of a `map` + `filter` combined into one readable line.

A comprehension has three kinds of parts, and this one uses all three:

**1. The generator: `%{fm: %{"id" => id}} = p <- pages`**

`x <- pages` means "take each element of `pages`, one at a time". The unusual bit is what's on the left of the arrow — instead of a plain variable name, there's a **pattern**:

- `%{fm: %{"id" => id}}` says: *this element must be a map that has an `:fm` key, whose value is itself a map that has an `"id"` key* — and when it does, bind that inner value to the variable `id`.
- `= p` on the end additionally binds the whole element to `p`. This is a *match on a match*: destructure the piece I want (`id`) **and** keep a handle on the whole thing (`p`).

Note the two key styles: `fm:` is an **atom** key (the page struct is built in Elixir, `site.ex:109`), while `"id"` is a **string** key (frontmatter is parsed from YAML, so its keys stay strings). They aren't interchangeable in Elixir.

The crucial beginner-surprising behavior: **in a comprehension generator, an element that doesn't match the pattern is silently skipped.** A page with no `id` in its frontmatter just doesn't appear in the output — no error, no `nil`. That's the pattern doing filtering work as a side effect of destructuring. (In a `case` or a function head, a failed match would raise.)

**2. The filter: `is_binary(id)`**

Any expression after the generator that isn't itself a generator acts as a filter — keep the element only if it's truthy. `is_binary/1` is Elixir's "is this a string?" check (strings are binaries under the hood). So this guards against frontmatter like `id: 12345`, which YAML would parse as an integer. Belt and braces on top of the pattern.

**3. The body and `into:`**

`do: {id, p}` — for each surviving page, produce the two-element tuple `{id, p}`.

`into: %{}` — instead of collecting those results into a list, pour them into an empty map. Maps know how to absorb `{key, value}` tuples, so each tuple becomes one map entry. Without `into:` you'd get `[{"em:4c9e1f", page}, …]`, a list of tuples; with it you get a real map with O(1) lookup, which is the point — `render_page/4` at `site.ex:56` resolves id references while rendering each page, so this is looked up thousands of times.

One consequence worth knowing: if two pages somehow carried the same id, **the last one wins** — maps can't hold duplicate keys. (The bundle's `mix brain.verify` is what prevents duplicate ids upstream, so this function doesn't need to.)
````

````text
## User

create an "elixir" directory in tutorials, and commit this to a tutorial

## Assistant

<routes ref="meta/tutorials/elixir/comprehensions-that-build-maps.md">
The explanation is now a durable tutorial rather than a chat answer. I created a new `elixir/` subdirectory under the existing tutorials folder — that's a subdirectory under an already-established area, so it's an autonomous filing under the taxonomy protocol, not a shape change needing your ratification. The tutorial expands the chat explanation with the parts that only surfaced once I read the surrounding source: what the index is actually *for*, why the page map has atom keys while the frontmatter map has string ones, and why the very next function in the file deliberately doesn't use a comprehension.

One correction to what I told you in chat: I said the id map is "looked up thousands of times", offering constant-time lookup as the reason for `into: %{}`. That was recalled, not checked. Three documents in the bundle carry `verified_by`, seven edges total — so a full site build performs seven of these lookups. The real justification is shape: `Map.get(id_index, id)` returning `nil` at `site.ex:485` is exactly the branch `edge_item/3` needs. The tutorial says it that way.
````

## Classification

`epistemic.claim.direct_check_omission` fits because a concrete quantitative
claim was made despite readily inspectable call sites and data. This is not
primarily a reasoning error: the false scale came from failing to check the
repository.

## Detection and correction

The agent inspected the surrounding implementation and data while converting
the explanation into a tutorial. It replaced the performance story with the
actual shape-based rationale and disclosed the corrected count.
