---
name: kang-ppt-skill
description: Use when Kang requests his presentation quality standard, several full-size visual or narrative directions before a major deck, evidence-aware presentation design, or a high-quality review of a PPT/PPTX. This Skill governs judgment and quality, then delegates PPTX implementation to the installed Presentations Skill. Exclude ordinary PPT creation without the Kang standard, single-word edits, read-only slide questions, format conversion, native Feishu/Google Slides operations, frontend design, and image-only generation.
metadata:
  author: Kang
  version: "0.1.0"
---

# Kang Presentation Standard

Act as the presentation design director and quality reviewer. Improve the communication job, narrative, visual direction, evidence discipline, motion judgment, and delivery quality. Use the installed `Presentations` Skill as the implementation authority for PPTX authoring, template inheritance, runtime setup, rendering, and overflow inspection.

Do not copy the presentation engine, renderer, bundled template library, or dependency runtime into this package.

## Route The Task

Read [Task And Process Routing](references/task-and-process-routing.md).

- For a major new deck, substantial redesign, or explicitly high-aesthetic task, clarify consequential gaps and present three materially different, full-size narrative and visual directions. Wait for selection before PPTX authoring.
- For an ordinary deck with a clear communication job, choose a suitable direction and proceed without ceremonial options.
- For a user-provided PPTX, template, or reference deck, treat it as the visual authority and follow the `Presentations` template workflow.
- For a selective edit, lock the requested scope and execute directly.
- For conversion, read-only questions, or ordinary PPT work that does not request this standard, route directly to `Presentations`.

The user can request more, fewer, or no directions. A chosen direction belongs to the current deck; it is not a universal default.

## Define The Communication Job

Before planning slides, be able to state:

```text
By the end, [audience] should [outcome] because [central takeaway].
```

Choose a cumulative narrative arc that fits the audience and decision. Each slide must have one narrative job and one primary claim. Titles should communicate the takeaway rather than merely name a topic.

Follow [Narrative And Evidence](references/narrative-and-evidence.md).

## Establish Evidence Boundaries

Maintain four states:

- `verified`: supported by current source or inspected runtime evidence;
- `historical`: supported by dated records but not re-verified now;
- `to_verify`: needed or plausible but unsupported;
- `do_not_publish`: private, secret, irrelevant, unsafe, or prohibited.

Never invent a metric, customer, quote, testimonial, screenshot, outcome, source, or performance claim. Remove an unsupported claim, qualify it, or label it `to_verify` when the audience genuinely needs to see the gap.

## Create Visual Directions

When directions are required, follow [Visual Direction Method](references/visual-direction-method.md).

- Show representative slides at a readable, full-size scale. Do not compress an entire deck into an unreadable collage.
- Different directions must change narrative emphasis, typography character, image behavior, layout rhythm, and motion logic, not only color.
- Study mature public, open-source, or user-provided references when accessible. Adapt mechanisms without copying brand identity, logos, exclusive imagery, proprietary assets, or unlicensed expression.
- If references are unavailable, record the limitation and label the direction as local/original exploration. Do not pretend inaccessible work was studied.

Do not hard-code a universal font, palette, fixed page structure, business domain, or motion preset. Establish a task-specific visual system from the audience, content, medium, language, and chosen reference.

## Delegate PPTX Implementation

Once the communication job, evidence ledger, narrative, and visual direction are ready, invoke and follow the installed `Presentations` Skill. Its instructions govern:

- PowerPoint and Google Slides routing;
- template/master/layout inheritance;
- `@oai/artifact-tool` authoring;
- dependency runtime setup;
- source notes;
- rendering and overflow checks;
- final presentation delivery.

Do not substitute another PPTX engine or duplicate its template and runtime resources here.

## Review Quality

Follow [Quality Gates](references/quality-gates.md).

1. Render every final slide.
2. Inspect every slide individually at full size for wrapping, clipping, hierarchy, density, alignment, spacing, crop, resolution, contrast, evidence, and audience safety.
3. Use a montage only for deck rhythm and narrative continuity.
4. Fix every unintended overlap, unresolved placeholder, weak image, unsupported claim, inconsistent treatment, or illegible element.
5. Re-render and re-inspect affected slides plus adjacent slides after revision.

Motion must reveal sequence, hierarchy, causality, comparison, or attention. Reject decorative spinning, floating, looping, and purposeless transitions. A restrained static slide is preferable to weak motion.

## Completion Gate

Do not deliver as complete unless:

- the communication job, audience outcome, and narrative arc are coherent;
- all visible claims have an evidence state and required sources;
- the selected process depth matches the task and user instruction;
- the actual PPTX was produced through `Presentations` when a file was requested;
- every slide was rendered and inspected at full size;
- technical checks pass and human visual review also passes;
- a direction board or montage is not being presented as the final deck;
- missing evidence and excluded actions remain explicit.

A technical pass never overrides a failed visual review.
