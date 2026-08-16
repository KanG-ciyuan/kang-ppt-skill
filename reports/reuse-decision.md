# Reuse Decision

- Date: 2026-08-16
- Requested outcome: create a reusable Kang presentation-quality Skill and verify it with a real customer proposal.
- Decision: `Create New`, approved by Kang after the decision card.
- Publication/install state: not authorized.

## Capabilities Found

The installed `Presentations` Skill already covers:

- PowerPoint and Google Slides creation and editing;
- user-provided template, master, layout, and inherited-element handling;
- narrative, typography, composition, asset, and source-note guidance;
- PPTX authoring through `@oai/artifact-tool`;
- rendering, montage, and overflow inspection;
- local deliverable handoff.

## Overlap

Both capabilities touch presentation narrative, visual quality, and final review. Recreating the PPTX engine, bundled layouts, helper scripts, dependency runtime, or complete first-party instructions would be duplication.

## Independent Capability

The new package owns a separate Kang-maintained decision and acceptance layer:

- decide whether a task needs three full-size visual/narrative directions or direct execution;
- keep directions readable, materially different, and reference-aware;
- establish a task-specific visual system without fixed fonts, colors, or slide structures;
- apply Kang's evidence and public-claim boundaries;
- reject low-value motion and thumbnail-collage substitutes;
- block completion when technical checks pass but full-size visual review fails;
- maintain its own personal preference and quality lifecycle while the engine can update independently.

## Routing Consequence

- `kang-ppt-skill`: process depth, communication job, evidence, visual direction, motion judgment, and acceptance gates.
- `Presentations`: PPTX implementation, templates, runtime, rendering, testing, and file delivery.
- Native Feishu or Google Slides operations continue to use their platform routing.

## Evidence Gaps

- Cross-model routing and output consistency are not tested.
- Real customer preference and business impact are not tested.
- The generated Skill is not installed or published.
- Upstream `Presentations` behavior may change and must be re-inspected when the runtime version changes materially.

## Excluded Actions

No Git initialization, commit, publication, installation, production integration, customer-data access, or credential handling is authorized in this test.
