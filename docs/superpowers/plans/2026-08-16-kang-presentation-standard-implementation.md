# Kang Presentation Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and locally validate `kang-presentation-standard` as a reusable presentation-quality companion Skill, then prove it with a rendered renovation-company customer proposal.

**Architecture:** The new Skill owns task classification, visual-direction decisions, narrative/evidence standards, motion judgment, and acceptance gates. It delegates PowerPoint authoring, template handling, runtime setup, rendering, and overflow inspection to the installed `Presentations` Skill instead of copying that engine. Production evidence is stored in trigger/output reports and one real PPTX runtime case.

**Tech Stack:** Agent Skill Markdown/YAML/JSON, Kang Meta Skill 2.0.0 validators, Python standard-library contract tests, installed `Presentations` Skill, `@oai/artifact-tool`, bundled presentation render/overflow tools, local browser visual review.

**Authorization boundary:** Local files, read-only public research, local PPTX creation, and local preview are authorized. Git initialization/commit, global installation, GitHub publication, and production integrations are excluded.

---

## File Map

### Skill authority

- `SKILL.md`: trigger boundary, routing, mandatory workflow, delegation to `Presentations`.
- `agents/interface.yaml`: discoverable name, prompt, examples, adapter and permission boundary.
- `manifest.json`: package identity, maturity, lifecycle, release gates, dependency declaration.
- `README.md`: public-facing value, distinction from `Presentations`, usage, examples, evidence, troubleshooting.

### Judgment references

- `references/task-and-process-routing.md`: classify task and decide visual-preview depth.
- `references/visual-direction-method.md`: create full-size, materially different directions without fixed styling.
- `references/narrative-and-evidence.md`: communication job, narrative arc, claim ledger, source handling.
- `references/quality-gates.md`: typography, assets, motion, rendering, full-size review, delivery failure behavior.

### Evaluation

- `evals/trigger_cases.json`: positive, negative, and near-neighbor routing cases.
- `evals/output_cases.json`: quality expectations for major, small, template, and review tasks.
- `tests/test_package.py`: deterministic contract, identity, reference, boundary, and secret-pattern checks.
- `scripts/output_eval.py`: deterministic evaluation of the recorded runtime case and output fixtures.

### Evidence

- `reports/reuse-decision.md`: Presentations reuse boundary and Create New justification.
- `reports/prior-art-research.md`: inspected candidates and keep/adapt/reject/invent ledger.
- `reports/skill-ir.json`: portable intent, inputs, outputs, permissions, dependencies, and evidence state.
- `reports/trigger-eval.json`: generated routing smoke result.
- `reports/output-eval.json`: generated output-contract result.
- `reports/runtime-case-renovation-customer-proposal.md`: actual deck build and visual QA record.
- `reports/creation-handoff.md`: final capabilities, evidence labels, limits, and publication state.

### Runtime evaluation artifact

- `examples/renovation-customer-proposal/renovation-consultation-agent-proposal.pptx`: final seven-slide test deck.
- `examples/renovation-customer-proposal/rendered/`: individual slide renders used for inspection.
- `examples/renovation-customer-proposal/montage.png`: sequence-only overview, never sole visual evidence.
- Temporary builder code, source notes, and planning text stay under a task-specific `/tmp` directory and are not shipped as Skill resources.

---

### Task 1: Freeze The Package Contract With Failing Tests

**Files:**
- Create: `tests/test_package.py`
- Create: `evals/trigger_cases.json`
- Create: `evals/output_cases.json`

- [ ] **Step 1: Create trigger fixtures before the Skill exists**

Write `evals/trigger_cases.json` with this exact top-level shape:

```json
{
  "should_trigger": [
    {"text": "按 Kang 的 PPT 标准给这个客户方案先出三套完整视觉方向", "family": "major_new"},
    {"text": "用 kang-presentation-standard 重做这份项目汇报的叙事和视觉", "family": "major_redesign"},
    {"text": "检查这份客户提案的证据、字号、图片和逐页交付质量", "family": "quality_review"},
    {"text": "按我的演示标准制作一份有来源的 AI 教学 PPT", "family": "teaching"},
    {"text": "这个 PPT 审美要求高，先给我不同叙事和版式方向", "family": "visual_direction"}
  ],
  "should_not_trigger": [
    {"text": "帮我正常制作一份三页 PPT", "family": "ordinary_presentations"},
    {"text": "把第 4 页的错别字改掉", "family": "single_edit"},
    {"text": "读取这个 PPT 第三页的表格数据", "family": "read_only_qa"},
    {"text": "在飞书幻灯片新建一页", "family": "lark_slides"},
    {"text": "把网页的按钮做得更好看", "family": "frontend"},
    {"text": "生成一张建筑室内效果图", "family": "image"}
  ],
  "near_neighbor": [
    {"text": "按照现有公司模板替换本月数字，布局不要变", "family": "template_execution"},
    {"text": "把 PPTX 转成 PDF", "family": "conversion"},
    {"text": "帮我写一份客户提案文案，不需要 PPT", "family": "writing"}
  ]
}
```

- [ ] **Step 2: Create output fixtures before implementation**

Write `evals/output_cases.json` with four cases:

```json
{
  "cases": [
    {
      "id": "major-new",
      "input": "从零制作一份高审美客户提案",
      "required": ["communication_job", "three_full_size_directions", "evidence_ledger", "presentations_delegate", "full_slide_review"]
    },
    {
      "id": "small-edit",
      "input": "只修正一页标题换行",
      "required": ["direct_execution", "scope_lock", "presentations_delegate"],
      "forbidden": ["three_full_size_directions"]
    },
    {
      "id": "template-authority",
      "input": "基于用户给定 PPTX 更新内容",
      "required": ["template_is_authoritative", "no_style_mix", "full_slide_review"]
    },
    {
      "id": "claim-safety",
      "input": "缺少真实数据但希望写得更有说服力",
      "required": ["remove_qualify_or_to_verify", "no_invented_metrics", "missing_evidence"]
    }
  ]
}
```

- [ ] **Step 3: Write deterministic failing package tests**

Create `tests/test_package.py` with tests that assert:

```python
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageContractTests(unittest.TestCase):
    def test_required_files(self):
        required = [
            "SKILL.md", "README.md", "manifest.json", "agents/interface.yaml",
            "references/task-and-process-routing.md",
            "references/visual-direction-method.md",
            "references/narrative-and-evidence.md",
            "references/quality-gates.md",
            "evals/trigger_cases.json", "evals/output_cases.json",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_single_identity_and_delegate(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: kang-presentation-standard", skill)
        self.assertIn("author: Kang", skill)
        self.assertIn("Presentations", skill)
        self.assertRegex(skill, r"Do not (copy|duplicate).*(engine|renderer|template)")

    def test_no_fixed_universal_style(self):
        text = "\n".join(
            p.read_text(encoding="utf-8", errors="ignore")
            for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.yaml"))
        )
        self.assertIn("Do not hard-code", text)
        self.assertNotIn("always use Inter", text)
        self.assertNotIn("always use #", text)

    def test_trigger_fixture_balance(self):
        cases = json.loads((ROOT / "evals/trigger_cases.json").read_text())
        self.assertGreaterEqual(len(cases["should_trigger"]), 5)
        self.assertGreaterEqual(len(cases["should_not_trigger"]), 5)
        self.assertGreaterEqual(len(cases["near_neighbor"]), 3)

    def test_no_secret_values(self):
        text = "\n".join(
            p.read_text(errors="ignore") for p in ROOT.rglob("*")
            if p.is_file() and p.suffix in {".md", ".yaml", ".json"}
        )
        self.assertNotRegex(text, re.compile(r"(sk-|Bearer\s+)[A-Za-z0-9._-]{16,}"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 4: Run tests and confirm the intended red baseline**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: `test_required_files`, `test_single_identity_and_delegate`, and style tests fail because implementation files do not exist; fixture-balance and secret tests pass.

No Git step: the current authorization explicitly excludes repository initialization and commits.

---

### Task 2: Implement The Lean Skill Authority And References

**Files:**
- Create: `SKILL.md`
- Create: `agents/interface.yaml`
- Create: `manifest.json`
- Create: `references/task-and-process-routing.md`
- Create: `references/visual-direction-method.md`
- Create: `references/narrative-and-evidence.md`
- Create: `references/quality-gates.md`

- [ ] **Step 1: Write the root routing contract**

`SKILL.md` must include:

```yaml
---
name: kang-presentation-standard
description: Use when Kang requests his presentation quality standard, several full-size visual or narrative directions before a major deck, evidence-aware presentation design, or a high-quality review of a PPT/PPTX. This Skill governs judgment and quality, then delegates PPTX implementation to the installed Presentations Skill. Exclude ordinary PPT creation without the Kang standard, single-word edits, read-only slide questions, format conversion, native Feishu/Google Slides operations, frontend design, and image-only generation.
metadata:
  author: Kang
  version: "0.1.0"
---
```

The body must define:

- `Role`: presentation design director and quality reviewer, not a replacement renderer;
- `Process depth`: major/high-aesthetic -> three full-size directions; small/template/selective -> direct;
- `Delegation`: invoke `Presentations` for PPTX authoring and its technical workflow;
- `Evidence`: verified/historical/to_verify/do_not_publish;
- `Completion gate`: full-size slide review plus technical checks;
- `Boundary`: no fixed universal style and no copied renderer/template library.

- [ ] **Step 2: Write task routing reference**

`references/task-and-process-routing.md` must define this decision table:

| Task | Default process |
|---|---|
| major new/high-aesthetic deck | clarify communication job, show 3 directions, wait for selection, then author |
| ordinary new deck | clarify only consequential gaps, choose direction, author |
| user template/reference deck | template is authoritative; inspect and edit inherited elements |
| selective edit | lock scope and edit directly |
| conversion/read-only question | route to `Presentations` without this standard unless requested |

It must state that user instructions override defaults and that the chosen direction is task-local.

- [ ] **Step 3: Write visual direction method**

`references/visual-direction-method.md` must require each direction to include:

- communication and narrative thesis;
- representative full-size slides, not a collage;
- typography character, image behavior, layout rhythm, and motion logic;
- concrete mature references or an explicit original/fallback label;
- material differences beyond palette;
- license/brand boundaries.

It must reject palette-only cards, unreadable miniatures, repeated cards, decorative motion, copied logos, and claims that an inaccessible reference was studied.

- [ ] **Step 4: Write narrative and evidence method**

`references/narrative-and-evidence.md` must define:

```text
communication_job = By the end, [audience] should [outcome] because [central takeaway].
```

It must cover one job/claim per slide, takeaway titles, cumulative arc, source notes, audience-facing copy, and the four evidence states. It must forbid invented metrics, testimonials, screenshots, customers, quotes, and results.

- [ ] **Step 5: Write quality gates**

`references/quality-gates.md` must include:

- typography selected per task, never globally fixed;
- copy shortening/layout change before font reduction;
- coherent but varied silhouettes;
- asset resolution/crop/consistency checks;
- motion only for sequence, hierarchy, causality, comparison, or attention;
- render every slide, inspect every slide full size, then inspect montage for sequence;
- technical pass cannot override failed visual review;
- no direction board or montage can be delivered as the final deck.

- [ ] **Step 6: Create aligned interface and manifest**

`agents/interface.yaml` must expose three natural examples and state that file creation delegates to `Presentations`.

`manifest.json` must contain:

```json
{
  "name": "kang-presentation-standard",
  "version": "0.1.0",
  "owner": "Kang",
  "updated_at": "2026-08-16",
  "status": "local-candidate",
  "maturity_tier": "production",
  "entrypoint": "SKILL.md",
  "dependencies": ["Presentations"],
  "permissions": {"network": "read-only research when needed", "file_write": "approved deck and package files", "publish": false},
  "release_gates": {"package_validation": "required", "trigger_eval": "required", "output_eval": "required", "runtime_deck": "required", "installation": "missing evidence", "publication": "not authorized"}
}
```

- [ ] **Step 7: Run the package contract tests**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all tests pass. If the validator's wording does not satisfy the delegation regex, improve `SKILL.md`; do not weaken the assertion.

No Git step under current authorization.

---

### Task 3: Research And Record Reference Capabilities

**Files:**
- Create: `reports/reuse-decision.md`
- Create: `reports/prior-art-research.md`
- Create: `reports/prior-art-candidates.json` when the Meta Skill runner returns data

- [ ] **Step 1: Record the installed-capability decision**

Write `reports/reuse-decision.md` with:

- requested outcome;
- installed `Presentations` capability inventory;
- exact overlap;
- missing personal decision/quality layer;
- `Create New` decision and user approval;
- routing and maintenance consequence;
- evidence gaps and excluded actions.

- [ ] **Step 2: Run time-boxed public research**

From the Kang Meta Skill directory, run its unified researcher with two focused queries:

```bash
python3 scripts/research_prior_art.py \
  "presentation design narrative visual direction skill" \
  "PowerPoint quality review evidence slide design" \
  --summary \
  --output reports/prior-art-candidates.json
```

Expected: either a candidate JSON file or recorded catalog failures. Do not install candidates or execute their scripts. If the network/catalog is unavailable, mark it `missing evidence` and continue with the installed first-party `Presentations` Skill and inspected local/open references.

- [ ] **Step 3: Inspect only relevant candidate instructions**

For 2-4 genuinely relevant candidates, read the source `SKILL.md`, license, permissions, and only the references needed to understand a useful mechanism. Do not copy wording, proprietary templates, author profiles, avatars, QR codes, or brand material.

- [ ] **Step 4: Write the contribution ledger**

`reports/prior-art-research.md` must name inspected sources and record:

- `keep`: audience outcome, narrative arc, full-size QA, source notes;
- `adapt`: visual-direction preview and task-size routing for Kang;
- `reject`: fixed universal template, palette-only direction, copied brand identity, thumbnail-only QA, ornamental animation;
- `invent`: companion routing boundary and technical-pass/visual-fail completion rule.

Mutable metrics must include observation dates and their exact meaning. No popularity number may be called a rating.

No Git step under current authorization.

---

### Task 4: Build Trigger And Output Evaluation

**Files:**
- Create: `scripts/output_eval.py`
- Generate: `reports/trigger-eval.json`
- Generate: `reports/output-eval.json`
- Create: `reports/skill-ir.json`

- [ ] **Step 1: Run the bundled package validator**

Run:

```bash
python3 <kang-meta-skill-worktree>/scripts/validate_skill.py .
```

Expected: `ok: true`, zero failures. Warnings must be reviewed rather than ignored.

- [ ] **Step 2: Generate trigger evaluation**

Run:

```bash
python3 <kang-meta-skill-worktree>/scripts/trigger_eval.py \
  . \
  --cases evals/trigger_cases.json \
  --output reports/trigger-eval.json
```

If the generic evaluator cannot represent the package-specific concepts, add explicit `positive_concepts`, `description_required_concepts`, and `negative_patterns` to `evals/trigger_cases.json`; do not hand-edit a passing report.

- [ ] **Step 3: Implement deterministic output evaluation**

Create `scripts/output_eval.py` that:

- loads `evals/output_cases.json`;
- checks that every required mechanism appears in the relevant reference or runtime report;
- checks forbidden mechanisms are absent for small-edit behavior;
- emits `ok`, `summary`, per-case results, failures, and method limitations;
- never claims visual quality from keyword checks.

Its CLI must be:

```bash
python3 scripts/output_eval.py --cases evals/output_cases.json --output reports/output-eval.json
```

- [ ] **Step 4: Run output evaluation before the runtime deck**

Expected: structure/routing cases pass; the real-runtime case remains `missing evidence` until Task 6. The script exits non-zero only for failed asserted behavior, not for explicitly declared provider/human evidence gaps.

- [ ] **Step 5: Export and inspect Skill IR**

Run:

```bash
python3 <kang-meta-skill-worktree>/scripts/export_skill_ir.py \
  . \
  --output reports/skill-ir.json
```

Confirm the IR names `Presentations` as a dependency, records no publication/install proof, and describes the visual-review evidence boundary.

No Git step under current authorization.

---

### Task 5: Write The Reader-Facing README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the first-screen value and distinction**

The first screen must answer:

- this improves PPT judgment and delivery quality;
- it does not replace the existing `Presentations` engine;
- major work can preview directions, while small work stays direct;
- current state is local and not installed/published.

- [ ] **Step 2: Add natural usage examples**

Include at least:

```text
“按 Kang 的 PPT 标准，为这份客户方案先给 3 套完整视觉方向。”
“直接优化这份月度汇报，保留模板，只改叙事和信息层级。”
“检查这份 PPT 的证据、字体、图片、动效和逐页交付质量。”
```

- [ ] **Step 3: Document workflow, boundaries, and evidence**

Explain process-depth routing, reference/template priority, evidence states, motion rules, full-size QA, output files, and current missing evidence. Do not advertise an install command until a public repository and isolated installation are verified.

- [ ] **Step 4: Add troubleshooting**

Include rows for:

- every task unexpectedly asks for three directions;
- a direction looks like a compressed collage;
- the deck technically passes but looks weak;
- a template was overridden;
- a claim lacks evidence;
- a public install command is unavailable.

- [ ] **Step 5: Re-run package tests and validator**

Expected: tests pass, validator has zero failures, and any README heuristic warnings are manually reconciled with actual sections.

No Git step under current authorization.

---

### Task 6: Produce The Real Renovation Customer Proposal

**Files:**
- Create: `examples/renovation-customer-proposal/renovation-consultation-agent-proposal.pptx`
- Create: `examples/renovation-customer-proposal/rendered/slide-1.png` through the final slide
- Create: `examples/renovation-customer-proposal/montage.png`
- Create: `reports/runtime-case-renovation-customer-proposal.md`
- Temporary: task-specific build directory under `/tmp`

- [ ] **Step 1: Load the approved evidence**

Read:

- the local project-archive note `项目档案·renovation-agent.md` (kept outside this repository);
- the current local renovation-agent source if its path is available;
- only the local files needed to verify current architecture, scoring, integration, and UI claims.

Create a temporary `source-notes.txt` separating verified current source, historical knowledge-base evidence, `to_verify`, and prohibited claims. Do not copy keys, private identifiers, or customer data.

- [ ] **Step 2: Freeze the seven-slide narrative**

Use this sequence unless source verification requires removing a claim:

1. `客户说出的需求，不该停在聊天框里` — minimal opening and decision problem.
2. `咨询信息越零散，后续跟进越依赖个人经验` — show the operational gap without invented loss metrics.
3. `一条链路，把回复与跟进连接起来` — consultation -> extraction -> human-reviewed reply -> intention support -> Feishu preview.
4. `客户只看到有用回应，内部判断留在服务端` — customer/internal visibility split.
5. `规则负责可复核判断，AI负责提取、解释与草拟` — responsibility boundary.
6. `外部服务失败，也不能让核心咨询结果消失` — optional integration and business-code-aware degradation.
7. `先用一个真实咨询场景验证，再决定扩展范围` — low-risk discovery/trial CTA.

- [ ] **Step 3: Load the workspace presentation runtime**

Call the workspace dependency loader and use exactly its returned Node executable, node modules, and binary directory. Create a task-specific `/tmp` build directory and a local `node_modules` symlink to the returned package directory. Do not install dependencies or search for alternates.

- [ ] **Step 4: Inspect the required presentation references**

Read the installed `Presentations` Skill's:

- `style_guidelines.md`;
- `artifact_tool_docs/API_QUICK_START.md`;
- `artifact_tool_docs/api/API_DOCS.md`;
- any exact image, text, notes, or shape API reference needed by the builder.

Because the visual direction is explicit and there is no source template, use a from-scratch architectural-editorial route and do not use Codex Grid.

- [ ] **Step 5: Start the artifact operation exactly once**

Run the installed Skill's marker with:

```bash
node "$SKILL_DIR/container_tools/mark_artifact_operation_started.mjs" \
  --operation-kind create \
  --expected-output-count 1 \
  --output-format pptx
```

Expected: successful marker output. Do not rerun it for revisions in the same creation operation.

- [ ] **Step 6: Build the PPTX through `@oai/artifact-tool`**

Create one `.mjs` builder in the temporary directory. It must:

- create a 16:9 deck;
- use the approved architectural-editorial system without copied branding;
- use compatible Chinese typography discovered from the runtime/system;
- add source notes for external claims/assets;
- use lower-density, audience-facing copy;
- create native shapes only for simple process explanation;
- avoid UI-card layouts and decorative loops;
- export exactly one PPTX to the approved final path.

Run the builder with the loader-provided Node runtime.

- [ ] **Step 7: Render and run technical checks**

Run the installed helpers:

```bash
python3 "$SKILL_DIR/container_tools/render_slides.py" "$FINAL_PPTX"
python3 "$SKILL_DIR/container_tools/create_montage.py" \
  --input_dir "$RENDERED_DIR" \
  --output_file "$MONTAGE_PATH"
python3 "$SKILL_DIR/container_tools/slides_test.py" "$FINAL_PPTX"
```

Expected: every slide renders, montage is created, and no unreviewed overflow remains.

- [ ] **Step 8: Inspect every slide at full size**

Use local image inspection for all rendered slides. Record pass/fail for:

- title wrapping;
- text clipping and density;
- hierarchy and spacing;
- image crop/resolution;
- color contrast and palette balance;
- narrative continuity;
- evidence/source notes;
- customer/internal information separation;
- visual consistency without repetitive silhouettes.

The montage may only judge deck rhythm and sequence.

- [ ] **Step 9: Revise until technical and visual gates pass**

For every failed item, modify the builder, regenerate the PPTX, re-render all slides, rerun overflow checks, and re-inspect the affected slide plus adjacent slides. Do not shrink text below the task's readable system to force a pass.

- [ ] **Step 10: Record the runtime case**

`reports/runtime-case-renovation-customer-proposal.md` must record:

- audience, purpose, chosen direction, and source evidence;
- exact slide count and narrative;
- automated commands/results;
- individual visual-review findings and revisions;
- what the Skill changed compared with ordinary direct PPT creation;
- `missing evidence`: real customer preference, sales impact, projection environment, independent designer review.

No Git step under current authorization.

---

### Task 7: Final Output Evaluation And Creation Handoff

**Files:**
- Update: `reports/output-eval.json`
- Create: `reports/creation-handoff.md`
- Update: `reports/skill-ir.json` evidence status if the exporter supports the fields; otherwise document evidence in the handoff

- [ ] **Step 1: Re-run output evaluation with runtime evidence**

Run:

```bash
python3 scripts/output_eval.py \
  --cases evals/output_cases.json \
  --runtime-report reports/runtime-case-renovation-customer-proposal.md \
  --output reports/output-eval.json
```

Expected: all asserted output cases pass; human/customer effectiveness stays `missing evidence`.

- [ ] **Step 2: Run the complete local verification suite**

Run independently and read every result:

```bash
python3 -m unittest discover -s tests -v
python3 <kang-meta-skill-worktree>/scripts/validate_skill.py .
python3 <kang-meta-skill-worktree>/scripts/trigger_eval.py . --cases evals/trigger_cases.json --output reports/trigger-eval.json
python3 scripts/output_eval.py --cases evals/output_cases.json --runtime-report reports/runtime-case-renovation-customer-proposal.md --output reports/output-eval.json
```

Also run a filename-only secret-pattern scan; report only match count and locations, never secret values.

Expected: zero validation failures, all unit/trigger/output assertions pass, and no secret-value matches.

- [ ] **Step 3: Write creation handoff**

`reports/creation-handoff.md` must include:

- result, version, local path, and no-install/no-publication state;
- installed and public reference capabilities studied;
- keep/adapt/reject/invent decisions;
- `design advantage`: companion boundary, process-depth routing, full-size direction rule;
- `validated advantage`: only results backed by named tests and the rendered deck;
- `hypothesis`: customer comprehension or visual preference claims without user/customer evidence;
- missing evidence and excluded permissions;
- recommended next trial before installation/publication.

- [ ] **Step 4: Verify final file inventory and context cost**

Count package files excluding rendered images, root `SKILL.md` words/bytes, and report files. Flag ceremonial or duplicated resources and remove them before completion.

- [ ] **Step 5: Deliver locally without expanding authorization**

Provide links to:

- final PPTX;
- rendered montage for convenient review;
- `SKILL.md`;
- README;
- runtime report;
- creation handoff.

State that the Skill is not installed, not published, and has no verified public install command. Do not initialize Git, create a commit, push, publish, or install.

---

## Plan Self-Review

- Spec coverage: every approved design section maps to Tasks 1-7.
- Independence: the plan creates only a decision/quality companion and reuses the installed rendering engine.
- Runtime proof: Task 6 creates and individually inspects a real customer proposal, not a mock direction board.
- Safety: public research is read-only; credentials, customer data, Git, installation, publication, and live integrations remain excluded.
- No placeholders: all files, commands, test shapes, narrative titles, and expected states are specified.
- Type consistency: package name is always `kang-presentation-standard`; version is always `0.1.0`; the runtime report and output evaluator use the same filename.
