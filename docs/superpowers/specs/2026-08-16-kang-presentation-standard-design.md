# Kang Presentation Standard Design

- Date: 2026-08-16
- Owner: Kang
- Status: approved design, implementation pending
- Target mode: Production
- Runtime dependency: existing `Presentations` Skill

## 1. Objective

Create a reusable personal presentation-quality Skill that improves narrative, visual direction, evidence discipline, motion judgment, and delivery quality without duplicating the existing PowerPoint implementation engine.

The Skill receives a presentation request and available materials, determines the communication job and appropriate design process, then hands PPTX authoring, template inheritance, rendering, and technical inspection to the existing `Presentations` Skill.

It applies to initial creation, major redesign, iterative improvement, and selective editing across project proposals, customer decks, case studies, teaching decks, internal reports, product introductions, and other presentation types.

## 2. Reuse Decision

### Capabilities found

The installed `Presentations` Skill already owns:

- PowerPoint and Google Slides creation and editing;
- user-provided template inheritance;
- narrative and slide-composition guidance;
- typography minimums and content-fit rules;
- visual sourcing and source notes;
- PPTX generation through `@oai/artifact-tool`;
- full-slide rendering, overlap checks, and delivery.

### Missing personal capability

The requested independent capability is a Kang-maintained decision and quality layer:

- decide when visual-direction preview is warranted;
- give full-size visual and narrative directions before major design work;
- establish a project-specific visual system without fixed fonts, colors, or page structures;
- borrow mature design mechanisms without copying brands or proprietary assets;
- preserve Kang's evidence, claim, privacy, and delivery standards;
- reject low-value motion and thumbnail-collage substitutes;
- evaluate actual deck quality using a real deliverable.

### Decision

`Create New` as a companion standard, not a replacement renderer.

The new Skill owns presentation judgment and acceptance gates. The installed `Presentations` Skill remains the implementation authority for PPTX files. This separation provides an independent maintenance lifecycle without copying the engine or bundled templates.

## 3. Trigger Boundary

Trigger when the user requests Kang's presentation standard for:

- a new or substantially redesigned PPT, PPTX, or presentation;
- a visual/narrative quality upgrade;
- several presentation directions before production;
- evidence-aware project, customer, business, teaching, or portfolio decks;
- presentation-specific quality review before delivery.

Do not trigger for:

- ordinary PPT creation when the user did not request Kang's standard or elevated design quality;
- native PowerPoint implementation details already owned by `Presentations`;
- Google Slides or Feishu Slides operations that only need their platform Skill;
- extracting text from slides without design work;
- generic writing, frontend design, document formatting, or image generation;
- a one-off request to change one word, export a format, or answer a slide-content question.

## 4. Default Workflow

1. Identify the topic, intended audience, presentation purpose, audience outcome, source constraints, delivery format, and whether an existing deck or template is authoritative.
2. Classify the task:
   - major new deck or high-aesthetic redesign;
   - ordinary new deck;
   - template-based deck;
   - selective edit;
   - conversion or inspection.
3. Choose process depth:
   - major or visually sensitive work: propose three distinct, full-size narrative and visual directions before authoring;
   - small, well-specified, template-based, or selective work: proceed directly;
   - user instruction always overrides the default.
4. Build an evidence ledger separating verified facts, historical evidence, items to verify, and prohibited claims.
5. Define the communication job in one sentence and select a cumulative narrative arc.
6. Establish a project-specific visual system from the chosen direction or reference deck. Do not hard-code a universal font, palette, size system, or slide sequence.
7. Delegate PPTX implementation to the existing `Presentations` Skill and obey its runtime, template, source-note, and rendering contracts.
8. Render every slide and inspect it at full size. A montage supports sequence review but never replaces individual-slide inspection.
9. Fix unintended overlap, clipping, wrapping, low-quality images, weak hierarchy, excessive density, inconsistent spacing, unsupported claims, and unresolved placeholders.
10. Deliver the final file with verified checks and explicit missing evidence.

## 5. Visual Direction Rules

- A visual direction is a usable design thesis, not a palette card or a compressed thumbnail collage.
- Each direction must show representative slides at a readable size and explain its narrative logic, typography character, image behavior, layout rhythm, and motion logic.
- Directions must differ materially, not merely by color.
- Mature open-source templates, public design references, and supplied decks may be studied and adapted semantically.
- Do not copy another brand's logo, identity, exclusive imagery, proprietary assets, or unlicensed expression.
- If external references are inaccessible, record the limitation and use inspected local templates or an explicitly labeled original direction.
- The chosen test direction does not become a universal default.

## 6. Narrative And Content Rules

- Every slide has one narrative job and one primary claim.
- Titles communicate the takeaway rather than naming a topic.
- An agenda is not the narrative arc.
- Content visible to the audience must not expose prompts, timing scaffolds, model reasoning, production notes, or internal review instructions.
- Evidence must show meaning and consequence, not appear as an inventory of facts.
- Never invent customer names, quotes, metrics, outcomes, testimonials, screenshots, or business evidence.
- Use placeholders or `to_verify` labels when a fact is missing and still materially needed.
- For customer proposals, avoid unapproved guarantees about price, delivery, performance, security, or integration success.

## 7. Typography, Layout, Assets, And Motion

- Typography is chosen for audience, language, content density, display environment, and reference style. It is not globally fixed.
- Shorten content or change layout before shrinking text.
- Use a coherent system while varying slide silhouettes to match the narrative.
- Avoid dashboard-like card grids, pill collections, decorative UI controls, and other interface metaphors unless the presentation truly explains a UI.
- Use real, inspectable assets when the audience needs to understand the product, place, process, or result.
- Do not reuse low-resolution, distorted, dark, or poorly cropped imagery.
- Motion must reveal sequence, causality, hierarchy, comparison, or attention. Reject decorative spinning, floating, looping, and purposeless transitions.
- Missing video or animation is not automatically a quality failure; weak motion is worse than restrained static composition.

## 8. Package Design

Production package:

```text
kang-presentation-standard/
├── SKILL.md
├── README.md
├── manifest.json
├── agents/interface.yaml
├── references/
│   ├── task-and-process-routing.md
│   ├── visual-direction-method.md
│   ├── narrative-and-evidence.md
│   └── quality-gates.md
├── evals/
│   ├── trigger_cases.json
│   └── output_cases.json
├── reports/
│   ├── reuse-decision.md
│   ├── prior-art-research.md
│   ├── skill-ir.json
│   ├── trigger-eval.json
│   ├── output-eval.json
│   ├── runtime-case-renovation-customer-proposal.md
│   └── creation-handoff.md
└── docs/superpowers/specs/
```

Do not copy presentation builders, bundled templates, rendering tools, or dependency runtimes into this package.

## 9. Real Output Evaluation

Create a roughly seven-slide customer proposal for a renovation company.

### Communication job

By the end, a renovation-company decision maker should understand how the consultation Agent turns customer messages into reviewable follow-up leads and agree to a requirements discussion or limited trial.

### Required narrative

1. Customer consultation should not end in a chat window.
2. Current messages are incomplete and difficult to follow consistently.
3. The proposed flow connects consultation, extraction, human-reviewed reply, intention support, and Feishu handoff.
4. The customer-facing experience hides internal grades and integration details.
5. Rules remain reviewable; AI supports extraction, explanation, and drafting.
6. Optional integrations fail visibly and do not block the core result.
7. Close with a low-risk requirements discussion or trial path, not a purchase guarantee.

### Visual direction

Use the approved `B - architectural editorial` direction for this test only:

- warm neutral paper/material palette with restrained contrast;
- editorial typography and generous but controlled whitespace;
- one strong image or spatial composition where it materially helps;
- business logic remains legible and is not sacrificed for atmosphere;
- no copied architecture brand, logo, or proprietary template.

### Verification

- final PPTX opens and renders;
- every slide rendered and inspected individually;
- no unintended overlap, clipping, broken connectors, or unresolved placeholders;
- claims match the verified renovation project record;
- source notes accompany externally sourced claims and assets;
- output evaluation separates automated checks from human visual judgment;
- no real secrets, contact data, private resource identifiers, or production credentials.

## 10. Failure Handling

- Reference unavailable: record `missing evidence`, inspect local resources, and label original exploration honestly.
- Source claim unverified: remove, qualify, or mark `to_verify`; never beautify it into a fact.
- Asset quality insufficient: change the composition or replace the asset; do not stretch or blur it.
- Content overflow: shorten copy or change layout before shrinking below the established readable system.
- Rendering or font issue: select a compatible fallback and re-render all affected slides.
- Visual quality weak: revise the actual deck; do not present a direction board or montage as completion.
- Technical test passes but visual review fails: the deck remains incomplete.

## 11. Acceptance Criteria

- The root Skill clearly routes to, and does not duplicate, `Presentations`.
- Major-vs-small workflow selection is explicit and user-overridable.
- Visual directions are full-size, materially distinct, and reference-aware.
- No universal font, palette, page structure, or business-domain template is hard-coded.
- Evidence and public claims remain reviewable.
- Motion rules reject low-value decoration.
- Trigger and exclusion fixtures pass.
- Package validation passes with no failures.
- The renovation customer proposal passes automated and full-size visual inspection.
- Installation and publication remain `missing evidence` until separately authorized and verified.

## 12. Current Authorization

Authorized:

- create and validate the local Skill package;
- create the local renovation customer proposal as an output evaluation;
- use public read-only research and existing authorized local project evidence;
- start a local browser preview for design review.

Not authorized:

- install the new Skill globally;
- publish or push to GitHub;
- call production customer, model, Feishu, or account integrations;
- expose credentials or private customer information;
- initialize or commit a Git repository without separate approval.
