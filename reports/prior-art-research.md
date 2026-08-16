# Prior-Art Research

- Research date: 2026-08-16
- Purpose: identify reusable presentation-design mechanisms before completing `kang-ppt-skill`.
- Scope: public source inspection only. No candidate code, installer, renderer, template, or script was executed.
- Adoption rule: study methods semantically; do not copy branding, logos, proprietary assets, large preset libraries, or complete implementations.

## Evidence Boundary

The preferred skills.sh and SkillsMP catalog searches did not complete. skills.sh timed out after 30 seconds for both queries, and SkillsMP failed DNS/network access. Those failures are preserved in [`prior-art-candidates.json`](prior-art-candidates.json) as `missing evidence`.

Therefore:

- no catalog install count, repository-star comparison, rating, or popularity ranking is claimed;
- the three candidates below came from a public web-search fallback and were then inspected at their canonical GitHub source;
- GitHub repository metadata and license paths were re-checked on 2026-08-16;
- all three repositories currently identify their license as MIT, but license permission does not make wholesale copying desirable or necessary.

## Candidate Ledger

### `siril9/presentation-skill`

- Source: <https://github.com/siril9/presentation-skill/blob/main/SKILL.md>
- License evidence: <https://github.com/siril9/presentation-skill/blob/main/LICENSE> (`MIT`, checked 2026-08-16)
- Source revision inspected: `2d3100b8a13d88b5677d7cc345553b69ca263463`

**Keep**

- Treat an editable source representation as the authority and regenerate the deck from source instead of repeatedly patching an opaque PPTX.
- Combine deterministic geometry checks with rendered visual inspection and a repair loop.

**Adapt**

- Express the source-first principle as a quality expectation while delegating actual PPTX authoring and rendering to the installed `Presentations` Skill.
- Use full-size slide inspection as the primary visual proof; use a montage only for sequence and consistency.

**Reject**

- Do not copy its renderer, preset families, composition grammar corpus, template inventory, or runtime.
- Do not convert its style families into universal Kang defaults.

### `Pingozhu/knowledge-cat-ppt-skill`

- Source: <https://github.com/Pingozhu/knowledge-cat-ppt-skill/blob/main/SKILL.md>
- License evidence: <https://github.com/Pingozhu/knowledge-cat-ppt-skill/blob/main/LICENSE> (`MIT`, checked 2026-08-16)
- Source revision inspected: `bf440a63fecd21b6939a9ea5e0052778a25dd2a4`

**Keep**

- Start with audience, decision, story, action-oriented titles, and evidence before choosing layouts.
- Require story, evidence, implementation lane, and rendered QA to agree.
- Include at least one fix-and-recheck loop when the first render exposes defects.

**Adapt**

- Use the evidence discipline without importing a domain-specific content pipeline.
- Keep output-lane routing as a boundary: this Skill owns design judgment; `Presentations` owns PPTX implementation.

**Reject**

- Do not copy its large style library, HTML/image-first generation engines, bundled builders, or project-specific content system.
- Do not use a catalog of named looks as a substitute for task-specific design judgment.

### `aaronvanston/agent-skills/skills/creating-presentations`

- Source: <https://github.com/aaronvanston/agent-skills/blob/main/skills/creating-presentations/SKILL.md>
- License evidence: <https://github.com/aaronvanston/agent-skills/blob/main/LICENSE> (`MIT`, checked 2026-08-16)
- Source revision inspected: `d9ab2c56797494e26b37b285d8223880087f295d`

**Keep**

- Give each slide one main message.
- Make headlines carry the conclusion and keep visible copy concise.
- Keep speaker-facing cues out of audience-facing slide content unless requested.

**Adapt**

- Apply these principles as narrative checks, not as a fixed seven-part deck formula.
- Let the audience, decision, evidence, and chosen visual direction determine the final sequence.

**Reject**

- Do not hard-code a standard flow, section colors, font system, or layout family as the universal presentation style.
- Do not copy generic defaults when a user template or explicit direction is authoritative.

## Synthesis

### Keep

- source-aware, reproducible authoring;
- one message and one narrative job per slide;
- audience and decision before layout;
- evidence-aware claims and action-oriented titles;
- deterministic checks plus full-size rendered review;
- repair and recheck after visible defects.

### Adapt

- Make three full-size directions the default only for major or explicitly high-aesthetic work.
- Keep visual direction task-local rather than turning any inspected style into a permanent house style.
- Delegate implementation to `Presentations` so upstream engine, template, and QA improvements remain reusable.

### Reject

- wholesale Skill prose or code copying;
- renderer and dependency duplication;
- fixed preset libraries as a substitute for judgment;
- thumbnail collages as final visual proof;
- palette-only directions, decorative motion, unsupported claims, and inaccessible-reference claims.

### Invent

- A process-depth router that distinguishes major direction work from ordinary, template-based, selective, conversion, and read-only tasks.
- A four-state claim ledger: `verified / historical / to_verify / do_not_publish`.
- A dual completion gate in which technical success cannot override failed full-size visual review.
- A motion test based on sequence, hierarchy, causality, comparison, or attention.
- A personal quality layer that can evolve independently while continuing to use the installed first-party presentation engine.

## Research Conclusion

The inspected work supports creating a small judgment-and-acceptance layer, not another presentation engine. The useful prior art is complementary and can be adopted semantically. `kang-ppt-skill` remains original in its routing combination, evidence states, full-size direction gate, motion test, and explicit separation between personal quality standards and the installed `Presentations` implementation authority.

## Missing Evidence

- skills.sh install telemetry for the selected queries;
- SkillsMP star-ranked candidate results for the selected queries;
- independent user ratings or comparative quality scores;
- cross-model behavior using these candidates;
- evidence that any candidate improves real customer conversion or preference.
