# Runtime Case: Renovation Customer Proposal

- Date: 2026-08-16
- Skill version: `0.1.0`
- Audience: renovation-company decision maker or service lead
- Purpose: obtain agreement for a requirements discussion or limited trial
- Chosen direction: architectural editorial
- Final output: `examples/renovation-customer-proposal/renovation-consultation-agent-proposal.pptx`
- Slide count: 7

## Evidence Used

- `verified`: local `renovation-agent` source at commit `3407313`, checked 2026-08-16.
- `verified`: project knowledge record last verified 2026-08-13.
- `verified`: customer-facing homepage captured locally from `127.0.0.1:3005` after the initial animation settled; no consultation or contact submission was made.
- `generated asset`: one architectural-interior concept image created through `llmtoken.io / gpt-image-2`; explicitly labeled as atmosphere, not a project case photo.
- `to_verify`: production Feishu delivery, real-customer accuracy, business impact, and commercial performance.
- `do_not_publish`: credentials, webhook values, private customer information, and secret values.

## Communication Job

By the end, a renovation-company decision maker should agree to a requirements discussion or limited trial because the current demo connects customer consultation, structured lead extraction, controlled reply, and internal follow-up without exposing internal scoring to the customer.

## Narrative

1. 客户说出的需求，不该停在聊天框里
2. 咨询信息越零散，后续跟进越依赖个人经验
3. 一条链路，把及时回复与后续跟进连接起来
4. 客户只看到有用回应，内部判断留在服务端
5. 规则负责可复核判断，AI负责理解、解释与草拟
6. 外部服务失败，也不能让核心咨询结果消失
7. 先用一个真实咨询场景验证，再决定扩展范围

## Implementation And Technical Evidence

- Authoring engine: installed `Presentations` Skill with `@oai/artifact-tool` from a JavaScript ES module.
- Artifact operation marker: completed once before the first authoring run and not repeated for revisions.
- Runtime: loader-provided Node.js, package path, and override binaries only.
- Final PPTX render: rendered every slide through the installed `render_slides.py` helper.
- Sequence overview: generated `examples/renovation-customer-proposal/montage.png` from the seven rendered PNG files.
- Overflow check: `slides_test.py` returned `Test passed. No overflow detected.`
- Technical gate: pass.

## Full-Size Visual Review

Every final PPTX slide was inspected individually at full size. The montage was used only for sequence and silhouette rhythm.

| Slide | Review result |
|---|---|
| 1 | Title remains two deliberate lines; photo crop is clear; concept-image label is visible; contrast passes. |
| 2 | One-line title fits; three information rows are aligned; green contrast panel is readable without crowding. |
| 3 | Five process nodes read left to right; connectors stay behind the nodes; customer/internal boundary and evidence caveat are visible. |
| 4 | Runtime screenshot crop is sharp enough for the intended evidence role; customer-visible and internal-only content are separated. |
| 5 | Two-column responsibility split is readable; the title was revised to avoid implying that the current AI already performs all extraction. |
| 6 | Paper-background contrast passes; the green action bar keeps emphasis while current fallback behavior and unverified hardening need remain distinct. |
| 7 | Three-step trial decision is balanced; the first-step sentence was shortened twice to remove punctuation at a line start. |

Visual gate: pass.

## Revision Loop

The first render exposed two factual/layout defects:

1. Slide 5 could imply that the current AI already owns all extraction. The title and boundary line were narrowed to state that the present demo uses rule-based extraction and optional model enhancement.
2. Slide 7 placed punctuation at the start of a wrapped line. The sentence was rewritten to a shorter, natural form and regenerated.

After review feedback, a third visual revision changed slide 6 from a full-bleed dark green background to the paper background used by the surrounding chapters. Deep green is now reserved for the action bar and key response text, so the reliability section keeps emphasis without dominating the deck.

After each revision, the complete PPTX was regenerated, rendered from the exported file, checked for overflow again, and re-inspected at full size.

## What The Skill Changed

- It defined the audience decision and a cumulative seven-slide narrative before authoring.
- It enforced the selected direction as task-local rather than a permanent house style.
- It separated runtime evidence, generated atmosphere, historical records, and unverified claims.
- It blocked completion after the first technically successful render because two visible defects remained.
- It kept the final ask to a bounded trial instead of inventing price, delivery time, conversion, or production success.

These observations validate process behavior in this recorded local case. They do not prove that every future model run will comply or that customers prefer the design.

## Missing Evidence

- real renovation-company or customer preference;
- sales or conversion impact;
- projector, meeting-room, and PowerPoint-version behavior;
- independent designer review or blind comparison;
- cross-model trigger and output consistency;
- global installation and public-package behavior.
