# kang-ppt-skill

English | [简体中文](README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-ppt-skill?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-ppt-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-ppt-skill?style=flat-square)](https://github.com/KanG-ciyuan/kang-ppt-skill/commits/main)

**Kang Presentation Standard** is an evidence-aware presentation **design** skill. It fixes the
communication job, the narrative arc, the visual direction and the evidence boundary *before* a deck is
authored, and it refuses to call the work complete until a real deck has been rendered and inspected
slide by slide at full size.

**It does not render PPTX.** There is no authoring engine, renderer, template library or dependency
runtime in this package — that exclusion is explicit and repeated (`SKILL.md:13,73`). All file
production is delegated to an installed `Presentations` Skill (`SKILL.md:11`; `manifest.json:10`;
`agents/interface.yaml:22-23`).

| | |
| --- | --- |
| **Is** | a pre-render planning, visual-direction and acceptance layer for presentations |
| **Is not** | a PowerPoint generator, a PPTX renderer, a theme, or a slide runtime |
| **Delegates** | PPTX authoring, template/master/layout inheritance, runtime setup, rendering and overflow inspection to `Presentations` (`SKILL.md:61-73`) |
| **Ships** | 4 reference documents, 14 recorded trigger fixtures, 4 output-contract fixtures, one 185-line Python report checker, 6 package contract tests |

Because of that delegation, **a real `.pptx` requires an external `Presentations` Skill that this package
does not ship, version or link.** "The actual PPTX was produced through `Presentations` when a file was
requested" is one of this skill's own completion preconditions (`SKILL.md:94`), so on its own the skill
cannot self-complete — if the runtime is absent it can only stop authoring and report the blocker
(`agents/interface.yaml:35`). Everything below is written with that boundary in place.

It is built for Kang's presentation work and for authorized collaborators using his standard
(`manifest.json:13`). It is not a general-purpose deck generator.

## Why This Exists

Decks usually fail before anyone opens a layout tool. The slides get designed while the communication
job is still unstated. Directions that differ only in colour are presented as alternatives. Unsupported
claims get polished until they look researched. A montage of thumbnails is mistaken for a deck. A
technically clean render is mistaken for a good one.

This package exists to put those judgments — and the evidence gate that backs them (`SKILL.md:92`) — in
front of the renderer, and to give the finished file a second, visual acceptance gate. The repository's
own design record describes the split as: personal design judgment should be able to evolve without
forking the PPTX engine (`reports/reuse-decision.md`).

## Before And After

| Without this standard | With this standard |
| --- | --- |
| Slides are planned before the communication job is stated | The job is written down first: `By the end, [audience] should [outcome] because [central takeaway].` (`SKILL.md:31-33`) |
| "Three options" means three palettes | Three directions that must differ in narrative emphasis, typography, imagery and rhythm — palette changes alone do not count (`references/visual-direction-method.md:18`) |
| Options arrive as an unreadable thumbnail collage | Representative slides are shown one at a time at readable, full-size scale (`references/visual-direction-method.md:32`) |
| Confident copy is treated as evidence | Every visible claim carries one of four evidence states, and invented metrics, customers, quotes and screenshots are prohibited (`SKILL.md:43-48`) |
| A technical pass is treated as a quality pass | Two separate gates; "A technical pass cannot override a failed visual review" (`references/quality-gates.md:42`, `SKILL.md:100`) |
| A direction board or montage is shown as the deliverable | A direction board, screenshot or montage is explicitly not the final deck (`references/quality-gates.md:44`) |
| The presentation engine is forked to change the house style | No universal font, palette, page structure, domain or motion preset is hard-coded (`SKILL.md:59`) |

## How It Works

Six behaviours are mandated by the skill, in this order.

1. **Route the task by size.** Major or explicitly high-aesthetic work: clarify consequential gaps,
   present three materially different full-size directions, and wait for selection before authoring.
   Ordinary, template-bound, selective or read-only work goes straight to execution
   (`SKILL.md:15-25`; `references/task-and-process-routing.md:5-11`).
2. **State the communication job** before planning slides (`SKILL.md:27-37`).
3. **Establish evidence boundaries** across four states (`SKILL.md:39-48`).
4. **Create visual directions** that are usable design theses, not colour cards
   (`SKILL.md:50-59`; `references/visual-direction-method.md`).
5. **Delegate PPTX implementation** to `Presentations` (`SKILL.md:61-73`).
6. **Review quality** against a technical gate and a per-slide full-size visual gate
   (`SKILL.md:75-85`; `references/quality-gates.md`).

Process depth is proportional, and an explicit user instruction overrides every default
(`references/task-and-process-routing.md:3,23`):

| Task | Default process |
| --- | --- |
| Major new or high-aesthetic deck | clarify the job, show three full-size directions, wait for selection, then author |
| Ordinary new deck | clarify only consequential gaps, choose a direction, then author |
| User template or reference deck | the template is authoritative; no style mixing |
| Selective edit | lock the stated scope, leave unrelated slides alone, edit directly |
| Conversion or read-only question | route to `Presentations` without this standard |

## Core Capabilities

### Communication goal

A single fill-in-the-blank sentence that must exist before slide count or layout is chosen
(`references/narrative-and-evidence.md:5-9`; `SKILL.md:31-33`):

```text
By the end, [audience] should [outcome] because [central takeaway].
```

The outcome may be understanding, approval, a decision, a trial, a discussion or a concrete action —
persuasion is not forced onto a teaching or reference deck (`references/narrative-and-evidence.md:11`).

### Narrative

A cumulative arc chosen for the audience and the decision — problem → cause → response → evidence →
action, question → analysis → answer, current → change → future, or another defensible sequence. Each
slide gets one narrative job and one primary claim, titles state the takeaway rather than the topic, and
each slide either answers a question raised by the previous one or creates the need for the next
(`references/narrative-and-evidence.md:15-20`; `SKILL.md:35`). An agenda or feature inventory is
explicitly not a narrative (`references/narrative-and-evidence.md:19`).

### Visual direction

"A direction is a usable design thesis for a real deck, not a color card or decorative mood board"
(`references/visual-direction-method.md:3`). Each direction must contain eight elements
(`references/visual-direction-method.md:7-18`):

1. communication thesis and narrative emphasis;
2. representative slides shown at readable, full-size scale;
3. typography character and hierarchy behaviour;
4. image, chart and diagram behaviour;
5. layout rhythm and expected silhouette variation;
6. motion logic, including when motion should be absent;
7. mature references actually inspected, or an explicit local/original fallback label;
8. trade-offs for the intended audience and decision.

Directions must differ materially in narrative emphasis, composition, typography, imagery and rhythm;
palette changes alone do not count (`references/visual-direction-method.md:18`). The chosen direction is
converted into task-specific decisions and is never reused as a permanent house template
(`references/task-and-process-routing.md:33`).

### Evidence boundaries

Four states, defined in `references/narrative-and-evidence.md:22-29` and enforced at `SKILL.md:39-48`:

| State | Allowed use |
| --- | --- |
| `verified` | current inspected source or runtime evidence; may be stated within its actual scope |
| `historical` | dated evidence; state the date or historical boundary when material |
| `to_verify` | unresolved; remove, qualify, or show only as an explicit gap |
| `do_not_publish` | secret, private, irrelevant, unsafe or prohibited; never placed in the deck |

The hard prohibition is direct: never invent a metric, customer, quote, testimonial, screenshot,
outcome, ratings, research or performance claim (`SKILL.md:48`;
`references/narrative-and-evidence.md:35`). Unsupported claims are removed, narrowed, or visibly marked
`to_verify` when the audience genuinely needs to see the gap
(`references/narrative-and-evidence.md:36`). Source semantics are preserved — installs are not ratings,
historical test results are not current runtime proof, a prototype is not production deployment
(`references/narrative-and-evidence.md:39`).

### Quality gates

Technical validity and visual quality are separate gates, and both must pass
(`references/quality-gates.md:3`). The review sequence renders every final slide, inspects every slide
individually at full size, uses a montage only for rhythm and continuity, then runs the `Presentations`
overflow and technical checks and re-inspects after every revision
(`references/quality-gates.md:31-38`). Failure rules (`references/quality-gates.md:40-46`):

- a technical pass cannot override a failed visual review;
- a beautiful slide cannot excuse an unsupported claim or a privacy violation;
- a direction board, screenshot or montage is not the final deck;
- a low-quality asset is replaced or removed, not hidden by blur, darkness or cropping;
- a cramped slide is rewritten or recomposed, not rescued with unreadably small type.

<details>
<summary>Completion gate — the 8 conditions checked before delivery (<code>SKILL.md:87-100</code>)</summary>

The skill may not be reported as complete unless:

- the communication job, audience outcome and narrative arc are coherent;
- all visible claims have an evidence state and required sources;
- the selected process depth matches the task and the user instruction;
- the actual PPTX was produced through `Presentations` when a file was requested;
- every slide was rendered and inspected at full size;
- technical checks pass and human visual review also passes;
- a direction board or montage is not being presented as the final deck;
- missing evidence and excluded actions remain explicit.

</details>

## Outputs And Artifacts

`manifest.json:15` declares four outputs. Three are prose or decision artifacts with no template, no
schema and no write path; the fourth is produced by a different skill.

| Output | Where it is defined | What it actually is |
| --- | --- | --- |
| Communication job and narrative | `SKILL.md:31-33`; `references/narrative-and-evidence.md:8,15-20` | a stated sentence plus a chosen arc — precision, not a file |
| Evidence ledger | `references/narrative-and-evidence.md:22-29` | a two-column markdown table of state and allowed use |
| Visual direction decision | `references/visual-direction-method.md:5-18` | an eight-item content list plus the recorded user selection |
| Quality-gated presentation deliverable | produced by `Presentations`, not by this repository | the real `.pptx` and its renders |

The only **machine artifact** this repository produces is the JSON report written by
`scripts/output_eval.py` (`--output <path>`). Its shape is fixed at `scripts/output_eval.py:143-163`:
`ok`, `summary{total_cases,passed,failed,missing_evidence}`, `results[]`, `failures[]`,
`evidence{rule_contract,runtime_visual_review,runtime_report}` and three `method_limitations` entries.
The process exits with code 2 when `ok` is false (`scripts/output_eval.py:180-181`).

<details>
<summary>Repository layout</summary>

| Path | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | The skill itself: trigger, exclusions, six mandated behaviours, completion gate |
| [`manifest.json`](manifest.json) | Package identity, intent, permissions, release gates |
| [`agents/interface.yaml`](agents/interface.yaml) | Discoverable interface: display name, default prompt, examples, permission boundary, gates |
| [`references/task-and-process-routing.md`](references/task-and-process-routing.md) | Task-size → process-depth routing, scope lock, delegation boundary |
| [`references/narrative-and-evidence.md`](references/narrative-and-evidence.md) | Communication job, narrative arc, four-state evidence ledger, claim rules |
| [`references/visual-direction-method.md`](references/visual-direction-method.md) | The eight required elements of a direction, reference-use rules, selection handoff |
| [`references/quality-gates.md`](references/quality-gates.md) | Typography and fit, composition, assets, motion, review sequence, failure rules |
| [`evals/`](evals) | Trigger fixtures and output-contract fixtures |
| [`scripts/output_eval.py`](scripts/output_eval.py) | The only executable code in the package |
| [`tests/`](tests) | Six package contract tests |
| [`examples/renovation-customer-proposal/`](examples/renovation-customer-proposal) | The one runtime artifact: a 7-slide deck plus full-size renders |
| [`reports/`](reports) | Development-process records, evaluation reports and the recorded runtime case |

There is no `package.json`, `pyproject.toml`, `setup.py` or `requirements.txt`, and no installer or
`bin/` entrypoint other than `SKILL.md` (`manifest.json:9`).

</details>

## Evidence And Validation

Every number below was produced by running the listed commands against this repository on 2026-09-15.
Nothing else in this README is claimed as measured.

**What was run**

| Command | Result |
| --- | --- |
| `python3 -m pytest tests/ -q` | `6 passed` — exit code 0 |
| `python3 -m unittest discover -s tests -v` | `Ran 6 tests … OK` |
| `python3 scripts/output_eval.py --cases evals/output_cases.json --runtime-report reports/runtime-case-renovation-customer-proposal.md --output reports/output-eval.json` | `ok: true`, `4/4` cases passed, `missing_evidence: 0`, `runtime_visual_review: "verified"` |
| companion `kang-meta-skill`: `python3 scripts/validate_skill.py ../kang-ppt-skill` | `ok: true`, zero failures, zero warnings |
| companion `kang-meta-skill`: `python3 scripts/trigger_eval.py ../kang-ppt-skill --cases ../kang-ppt-skill/evals/trigger_cases.json --output ../kang-ppt-skill/reports/trigger-eval.json` | `14/14` passed, `0` false positives, `0` false negatives — byte-identical to the committed [`reports/trigger-eval.json`](reports/trigger-eval.json) |

**What those results do and do not prove**

- The six tests are **package contract tests**. Five of them assert only that files exist or that
  strings appear (`tests/test_package.py:19-62`); one executes `scripts/output_eval.py` and asserts
  properties of its report (`tests/test_output_eval.py:13-42`). They do not open the example PPTX, read
  a rendered image, or invoke a model. No Pytest badge is published here because a static test count
  goes stale.
- `scripts/output_eval.py` is a **keyword and file-presence checker** over this repository's own
  markdown. It says so itself: "Keyword and file-presence checks verify recorded rule coverage, not
  presentation beauty or model compliance" (`scripts/output_eval.py:159`).
- `runtime_visual_review: "verified"` is **not independent visual verification**. It is produced by
  `runtime_status()` (`scripts/output_eval.py:99-113`), which matches five literal phrases inside the
  author's own report — `rendered every slide`, `full-size visual review`, `overflow check`,
  `technical gate: pass`, `visual gate: pass`. It inspects no deck, no render and no overflow result.
  Read it as "the runtime record contains the required statements", nothing more.
- The 14 trigger results are **recorded fixtures**, not model-scored evaluation. They are deterministic
  keyword scoring against `evals/trigger_cases.json` (5 `should_trigger`, 6 `should_not_trigger`,
  3 `near_neighbor`) with a hand-written negative-pattern list; no model is invoked.
- There is **no CI** in this repository. `.github/` does not exist, and the only YAML file is
  `agents/interface.yaml` (a skill-interface manifest, not a pipeline). Releases were cut by hand.

**A genuine run exists.** [`reports/runtime-case-renovation-customer-proposal.md`](reports/runtime-case-renovation-customer-proposal.md)
records one local case end to end: every slide rendered through an installed `render_slides.py` helper
(L39), a montage generated from the seven rendered PNGs (L40), an overflow check that returned
`Test passed. No overflow detected.` (L41), `Technical gate: pass.` (L42) and `Visual gate: pass.` (L58).
It also documents the revision loop: after the first technically successful render, an over-broad AI
claim and a punctuation wrap on a wrapped line were fixed, and a later human visual review rejected a
full-bleed dark slide, which was moved to the paper background used by its neighbours (L60-69). The
same report carries an honest Missing Evidence list (L81-88). This is the repository's strongest
evidence, and it remains a self-reported record of one local run.

**Still unverified**

- installation and public-package behaviour — see Quick Start;
- cross-model trigger and output consistency;
- real customer preference, and sales, conversion or business impact;
- projector, meeting-room and broader PowerPoint-version behaviour;
- independent designer review or blind comparison;
- whether the committed PNG renders were produced from the committed PPTX — there is no hash linkage;
- the provenance of the AI-generated concept image (`examples/renovation-customer-proposal/assets/`) —
  its declared generation path is recorded in the runtime case, but there is no generation log, prompt
  record or content-credentials manifest in this repository;
- the `Presentations` Skill itself: it is this package's only dependency and the gate on its own
  completion condition, and it is referenced by name only, with no vendor path, URL or version.

## Status And Limitations

- **Version.** The live chain agrees: `SKILL.md:6` = `manifest.json:3` = git tag `v0.1.3` = the GitHub
  release. Four tags exist (`v0.1.0` … `v0.1.3`), all cut on 2026-08-16.
- **Repository state.** Public and not archived. Five commits total, all on 2026-08-16 within about
  32 minutes, ending with `release: kang-ppt-skill v0.1.3`. The repository has no `CHANGELOG` and no CI.
  Development history is concentrated in that single session; this is an earlier, stable skill in the
  ecosystem rather than an actively evolving one.
- **Status metadata disagrees with itself.** `manifest.json:6` says `"status": "published"`, while
  `agents/interface.yaml:31-32` still says `installation: "not authorized"` and
  `publication: "not authorized"`, and [`reports/creation-handoff.md`](reports/creation-handoff.md)
  (L10-12, L104) still states that no Git initialization, commit, push, repository creation or
  publication was performed. That text is historical and now false as shipped — the repository is
  public with four releases. `agents/interface.yaml` also carries no `version` field at all, so version
  agreement cannot be established from that file alone.
- **The release gates are self-stamped.** `manifest.json:24-27` marks four gates
  `"verified locally 2026-08-16"` with no commit or artifact hash, so they cannot be tied to the tagged
  tree. `manifest.json:28` still lists `installation` as `missing evidence`.
- **Stale naming and stale text remain in the repository.** The two documents under
  [`docs/superpowers/`](docs/superpowers) were written under the package's former name
  `kang-presentation-standard`, and one self-review assertion there freezes the package name and the
  version at values that are both false as shipped. "Kang Presentation Standard" survives
  deliberately as the human-readable display name of this skill (`SKILL.md:9`,
  `agents/interface.yaml:2`), and `kang presentation standard` is a live trigger keyword in
  `evals/trigger_cases.json:14`; the repository/package identifier is `kang-ppt-skill`.
- **Some repository files record absolute paths from the author's machine** (`docs/superpowers/`,
  [`reports/creation-handoff.md`](reports/creation-handoff.md), [`reports/output-eval.json`](reports/output-eval.json)).
  These publish a local directory convention and a private knowledge-base path. They are recorded here
  as a remediation item and are intentionally not reproduced.
- **Two shipped records are known to be incomplete or failed.** The exported skill IR
  (`reports/skill-ir.json`) carries four empty `workflow` arrays despite the repository defining a
  router, a workflow and gates, and `reports/prior-art-candidates.json` is a shipped failed-run
  artifact (`"ok": false`, `candidate_family_count: 0`). Neither should be read as a capability source.

## Example

[`examples/renovation-customer-proposal/`](examples/renovation-customer-proposal) holds the only
runtime artifact in the repository.

| Artifact | Verified fact |
| --- | --- |
| [`renovation-consultation-agent-proposal.pptx`](examples/renovation-customer-proposal/renovation-consultation-agent-proposal.pptx) | valid OOXML deck ("Microsoft PowerPoint 2007+"), 2,348,593 bytes, 47 zip entries — 7 `ppt/slides/slideN.xml`, 7 `ppt/notesSlides/notesSlideN.xml`, 2 embedded images, a real slide master and theme |
| [`rendered/slide-1.png`](examples/renovation-customer-proposal/rendered/slide-1.png) … `slide-7.png` | 7 full-size renders, each 1280×720 |
| [`montage.png`](examples/renovation-customer-proposal/montage.png) | sequence montage, 2096×526 |
| [`assets/`](examples/renovation-customer-proposal/assets) | one AI-generated architectural concept image (labelled as atmosphere, not a project case photo), one product-UI screenshot |

**This is a realistic synthetic worked example, not a client engagement.** It is a seven-slide proposal
*addressed to* a hypothetical renovation company, pitching an AI consultation and lead-follow-up agent.
There is no customer identity, no customer data, no contract, no price and no delivery date; the
runtime case lists "real renovation-company or customer preference" itself under Missing Evidence
(L83). The artifact is genuine — a valid deck that really was rendered — but no customer stands behind
it.

The deck is de-identified. A scan of the repository found zero phone numbers, zero prices, zero real
company names, zero personal names and zero credentials, and every commercial claim inside the deck is
bounded — the reliability slide states that no unverified availability, performance or production
stability is promised, and the closing slide asks only for a bounded trial. The deck's own notes carry
`[Sources]` blocks on each slide.

Known caveats about this example, recorded rather than hidden:

- the speaker-note provenance citations cannot be verified from this repository;
- one slide reuses a product screenshot from the author's own separate `renovation-agent` project; this
  package forbids copying brand assets (`agents/interface.yaml:27`, `SKILL.md:56`) and states no
  same-author exception, so the example is recorded as a reconciliation item rather than as compliant;
- the PPTX `docProps` metadata names an authoring tool unrelated to this package and reports
  `Slides: 0` / `Notes: 0`; it is not usable as provenance.

## Use And Do Not Use

It activates on four things (`SKILL.md:3`):

1. a request for Kang's presentation quality standard;
2. several full-size visual or narrative directions before a major deck;
3. evidence-aware presentation design;
4. a high-quality review of a PPT/PPTX.

It is invoked in natural language — for example "按 Kang 的 PPT 标准" or `Use $kang-ppt-skill`
(`agents/interface.yaml:4,6`).

### Natural examples

The interface ships three example invocations verbatim (`agents/interface.yaml:6-8`). They are written in
Chinese, the author's working language — 你可以直接这样说:

| As shipped | Meaning | What the standard does |
| --- | --- | --- |
| `按 Kang 的 PPT 标准，为这份客户方案先给 3 套完整视觉方向` | "By Kang's PPT standard, give me three complete visual directions for this client proposal first" | treats it as major work: three materially different full-size directions before authoring (`SKILL.md:19`) |
| `直接优化这份月度汇报，保留模板，只改叙事和信息层级` | "Optimise this monthly report directly; keep the template, change only the narrative and information hierarchy" | treats the template as the visual authority and locks the scope (`references/task-and-process-routing.md:9,27`) |
| `检查这份 PPT 的证据、字体、图片、动效和逐页交付质量` | "Review this PPT's evidence, type, images, motion and per-slide delivery quality" | runs the dual gate and the per-slide full-size review (`references/quality-gates.md:31-38`) |

Routing is not fixed by phrasing: an explicit instruction to skip directions, or a task with a supplied
authoritative template, is treated as direct (`references/task-and-process-routing.md:23`).

**It excludes seven things** (`SKILL.md:3`; `manifest.json:16`):

| Out of scope | Where it goes instead |
| --- | --- |
| Ordinary PPT creation that does not ask for this standard | `Presentations` directly |
| Single-word or single-line edits | direct edit |
| Read-only slide questions | `Presentations`, no quality layer |
| Format conversion (for example PPTX → PDF) | `Presentations` |
| Native Feishu / Google Slides operations | the platform's own tooling |
| Frontend design | not a presentation task |
| Image-only generation | an image workflow |

Also out of scope by construction: **producing the `.pptx` file itself.** This skill produces judgment,
direction and acceptance decisions; `Presentations` produces the file.

## Safety And Human Boundary

Governance content is the strongest part of this package, and none of it is enforced by code — the only
automated check over the package text is a narrow secret-pattern regex
(`tests/test_package.py:55-62`) that does not scan images or the PPTX.

- **No invented evidence.** Metrics, customers, quotes, testimonials, screenshots, outcomes, ratings,
  research and performance claims may never be invented (`SKILL.md:48`). Customer proposals may not
  promise price, delivery date, security, availability, integration success, performance, savings or
  conversion without authorized evidence; a bounded trial or requirements discussion is preferred
  instead (`references/narrative-and-evidence.md:41-43`).
- **Privacy boundary.** `do_not_publish` covers secret, private, irrelevant, unsafe or prohibited
  material and is never placed in the deck (`references/narrative-and-evidence.md:29`).
- **Brand boundary.** Mature references may be studied and their mechanisms adapted, but brand identity,
  logos, exclusive imagery, proprietary assets and unlicensed expression are not copied
  (`SKILL.md:56`; `references/visual-direction-method.md:22-26`; `agents/interface.yaml:27`).
- **Honest degradation.** If reference access fails, the limitation is recorded as `missing evidence`
  and the direction is labelled local/original (`references/visual-direction-method.md:28`). If the
  `Presentations` runtime is unavailable, PPTX authoring stops and the blocker is reported
  (`agents/interface.yaml:35`).
- **Human decision points.** Direction selection for major work is a human choice (`SKILL.md:19`); the
  full-size visual review is a human judgment that a technical pass cannot override
  (`references/quality-gates.md:42`); publication and installation authorization are listed as
  permissions of the package rather than assumed (`manifest.json:18-22`).
- **Content-free examples.** The example deck is de-identified; no personal data, pricing or customer
  identity is published in this repository.

## Quick Start

### Install (not independently verified)

```bash
npx skills add KanG-ciyuan/kang-ppt-skill
```

This is the standard discovery form for a public agent-skill repository, and the repository is public.
It has **not** been executed during this documentation pass, and the package ships no `package.json`,
so treat the command as unverified rather than proven. The repository's own record lists installation
and public-package behaviour under Missing Evidence (`reports/creation-handoff.md:93`,
`manifest.json:28`), and this README publishes no install evidence it does not have.

### Verify the package locally

Run from the repository root. The commands below were executed against this tree on 2026-09-15.

```bash
python3 -m pytest tests/ -v
# equivalent, without pytest:
python3 -m unittest discover -s tests -v
```

```bash
python3 scripts/output_eval.py \
  --cases evals/output_cases.json \
  --runtime-report reports/runtime-case-renovation-customer-proposal.md \
  --output reports/output-eval.json
```

`--runtime-report` is **required**. Without it the evaluator sets
`runtime_visual_review: "missing evidence"` and `missing_evidence: 1`, which overwrites the committed
"verified" report with a downgraded one. Pass the flag and the report stays consistent with what is
committed.

### Package validation and trigger fixtures

`validate_skill.py` and `trigger_eval.py` are **not** part of this package. They ship in the companion
[kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) toolchain. From a checkout of that
repository, with this repository checked out beside it:

```bash
python3 scripts/validate_skill.py ../kang-ppt-skill

python3 scripts/trigger_eval.py ../kang-ppt-skill \
  --cases ../kang-ppt-skill/evals/trigger_cases.json \
  --output ../kang-ppt-skill/reports/trigger-eval.json
```

Both were run this way and both passed; the trigger run reproduces the committed
`reports/trigger-eval.json` byte for byte. The repository's `reports/trigger-eval.json` result therefore
does have a runnable origin — in that companion toolchain, not in this package.

### Prerequisites

- [ ] An installed, callable `Presentations` Skill. This package does not copy, bundle or substitute a
  PPTX engine, template library or runtime, and it cannot produce a `.pptx` without one.
- [ ] For real authoring, the workspace-provided Node.js and rendering toolchain — no substitute
  dependency is installed.
- [ ] Facts, screenshots and assets verified at source and classified as
  `verified / historical / to_verify / do_not_publish`.
- [ ] Explicit authorization for any publication or installation action.

## Troubleshooting

| Symptom | Cause | What to do |
| --- | --- | --- |
| Every task is asked for three directions | task-size routing is not being applied | ordinary, template-bound and selective work executes directly (`references/task-and-process-routing.md:5-11`) |
| The "directions" arrive as an unreadable thumbnail collage | the preview carries no typography or hierarchy | show one representative slide at a time at readable, full-size scale (`references/visual-direction-method.md:32-34`) |
| A file was requested but nothing was produced | `Presentations` is not installed | expected behaviour: this package contains no PPTX engine and refuses to substitute one (`SKILL.md:13,73`); it stops authoring and reports the blocker (`agents/interface.yaml:35`) |
| Technical checks pass and it still looks bad | a technical pass is not a quality pass | run the per-slide full-size visual review; a technical pass cannot override it (`references/quality-gates.md:42`) |
| The user's template was overridden by a new style | the template was not treated as the visual authority | return to the original master and layouts; do not mix style systems without authorization (`references/task-and-process-routing.md:9,27`) |
| The copy is persuasive but unsupported | creation is being treated as fact | remove it, narrow the language, or mark it `to_verify` (`references/narrative-and-evidence.md:36`) |
| `output_eval.py` reports `missing evidence` | `--runtime-report` was omitted | re-run with `--runtime-report reports/runtime-case-renovation-customer-proposal.md` |
| The committed `reports/output-eval.json` no longer says `"verified"` | it was regenerated without the runtime report | restore it from git, then re-run the documented command above |

---

## Part of the Kang Open-Source AI System

```text
DISCOVER
Enterprise AI Diagnostic Skills
        ↓
DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
DELIVER
Kang GitHub README
Kang PPT Skill
```

> This is an ecosystem map, not a strict runtime pipeline. The stages describe where
> each project sits in the work, not a mandatory execution order.

This project is one part of an evidence-driven system for enterprise AI transformation,
agent collaboration, and AI-native product delivery.

| Stage | Project | Role |
| --- | --- | --- |
| DISCOVER | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | Understand how the business actually works before automating it |
| DEFINE | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | Turn ambiguous requirements into an implementation-ready product contract |
| DEFINE | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | Review whether workflows are executable, accountable and recoverable |
| BUILD & COORDINATE | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | Role-based AI product workforce with explicit handoffs |
| BUILD & COORDINATE | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent collaboration and handoff protocol |
| BUILD & COORDINATE | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | Frontend quality standard for AI-built interfaces |
| VERIFY | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | Can users actually finish the work? |
| VERIFY | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | Independent acceptance of AI-built products |
| DELIVER | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | Evidence-aware README engineering |
| DELIVER | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | Evidence-aware presentation design |

**Cross-cutting infrastructure:** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill engineering, evaluation and release governance.

**Earlier work:** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules),
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps),
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent).

This repository sits at **DELIVER**: it decides what a deck must communicate and whether the finished
file is acceptable, and hands the file itself to a separate implementation authority.

## License

Released under the [MIT License](LICENSE).
