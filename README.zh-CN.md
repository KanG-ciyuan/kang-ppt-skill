# kang-ppt-skill

[English](README.md) | 简体中文

[![Release](https://img.shields.io/github/v/release/KanG-ciyuan/kang-ppt-skill?display_name=tag&sort=semver&style=flat-square)](https://github.com/KanG-ciyuan/kang-ppt-skill/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/KanG-ciyuan/kang-ppt-skill?style=flat-square)](https://github.com/KanG-ciyuan/kang-ppt-skill/commits/main)

**Kang Presentation Standard** 是一套证据感知的演示文稿**设计** Skill。它在动手排版之前，先把沟通目标、叙事弧线、视觉方向和证据边界定下来；在真实成品逐页完成全尺寸检查之前，它不会把工作判为完成。

**它不渲染 PPTX。** 本包内没有制作引擎、渲染器、模板库和依赖运行时——这是被反复明确声明的排除项（`SKILL.md:13,73`）。所有文件产出都交给已安装的 `Presentations` Skill（`SKILL.md:11`；`manifest.json:10`；`agents/interface.yaml:22-23`）。

| | |
| --- | --- |
| **是** | 演示文稿的渲染前规划、视觉方向与验收层 |
| **不是** | PowerPoint 生成器、PPTX 渲染器、主题或幻灯片运行时 |
| **委托** | PPTX 制作、母版/布局继承、运行时装配、渲染与溢出检查交给 `Presentations`（`SKILL.md:61-73`） |
| **自带** | 4 份 `references/` 文档、14 条录制的触发 fixture、4 条输出契约 fixture、1 个 185 行的 Python 报告检查脚本、6 项包契约测试 |

正因为存在这层委托，**要产出一个真正的 `.pptx`，必须依赖一个本包不附带、不锁版本、也不提供链接的外部 `Presentations` Skill。**「请求文件时，真实 PPTX 确实由 `Presentations` 产出」本身就是本 Skill 的完成前提之一（`SKILL.md:94`），所以单独使用时它无法自我完成——运行时缺失时，它只能停止制作并报告阻塞（`agents/interface.yaml:35`）。以下所有内容都建立在这条边界之上。

它服务于 Kang 本人的演示工作，以及使用该标准的授权协作者（`manifest.json:13`），不是通用幻灯片生成器。

## 为什么需要它

演示文稿通常在做页面之前就已经失败了。沟通目标还没写下来，页面就开始排版；只换了颜色的方案被当成不同方向；没有证据的说法被反复打磨到看起来像调研过；缩略图拼盘被当成了成品；渲染技术上过关被当成了质量过关。

本包的作用，就是在渲染器之前放上这些判断以及支撑它们的证据门禁（`SKILL.md:92`），并为成品再加一道视觉验收门禁。仓库自己的设计记录把这条分界写成：个人设计判断应当可以独立演进，而不用去 fork PPTX 引擎（`reports/reuse-decision.md`）。

## 用与不用的区别

| 没有这套标准 | 有这套标准 |
| --- | --- |
| 先排页面，再补沟通目标 | 先写下目标：`By the end, [audience] should [outcome] because [central takeaway].`（`SKILL.md:31-33`） |
| 「三套方案」就是三套配色 | 三套方向必须在叙事重点、字体、图像和节奏上实质不同——只换配色不算（`references/visual-direction-method.md:18`） |
| 方案以看不清的缩略拼盘交付 | 一次展示一页代表性页面，保持可读的完整尺寸（`references/visual-direction-method.md:32`） |
| 写得自信的文案被当成证据 | 每个可见说法都带四种证据状态之一，禁止编造指标、客户、引语和截图（`SKILL.md:43-48`） |
| 技术通过就当成质量通过 | 两道独立门禁：「技术通过不能覆盖视觉检查失败」（`references/quality-gates.md:42`、`SKILL.md:100`） |
| 方向板或拼图被当作最终交付物 | 方向板、截图或拼图明确不是最终成品（`references/quality-gates.md:44`） |
| 为了改风格去 fork 演示引擎 | 不写死任何通用字体、配色、固定页面结构、业务领域或动效预设（`SKILL.md:59`） |

## 工作方式

Skill 强制要求六个动作，顺序固定。

1. **按任务规模分流。** 大型或明确高审美任务：先澄清关键缺口，展示三套实质不同的全尺寸方向，等用户选定后再动手。普通任务、模板任务、局部修改或只读问答直接执行（`SKILL.md:15-25`；`references/task-and-process-routing.md:5-11`）。
2. **先声明沟通目标**，再规划页面（`SKILL.md:27-37`）。
3. **建立四态证据边界**（`SKILL.md:39-48`）。
4. **产出视觉方向**，方向必须是可用的设计主张，而不是配色卡（`SKILL.md:50-59`；`references/visual-direction-method.md`）。
5. **把 PPTX 实现委托给 `Presentations`**（`SKILL.md:61-73`）。
6. **做质量复核**：技术门禁 + 逐页全尺寸视觉门禁（`SKILL.md:75-85`；`references/quality-gates.md`）。

流程深度是成比例的，用户的明确指令覆盖所有默认值（`references/task-and-process-routing.md:3,23`）：

| 任务 | 默认流程 |
| --- | --- |
| 大型新稿或高审美任务 | 澄清目标 → 展示三套全尺寸方向 → 等待选定 → 制作 |
| 普通新稿 | 只澄清关键缺口 → 选定一个方向 → 制作 |
| 用户模板或参考稿 | 模板是权威，不混入另一套风格体系 |
| 局部修改 | 锁定约定范围，不动无关页面，直接改 |
| 格式转换或只读问答 | 直接交给 `Presentations`，不带本标准 |

## 核心能力

### 沟通目标

一句必须在选择页数和版式之前就写出来的填空句（`references/narrative-and-evidence.md:5-9`；`SKILL.md:31-33`）：

```text
By the end, [audience] should [outcome] because [central takeaway].
```

结果可以是理解、批准、决策、试用、讨论或具体行动——不会把「说服」强加到教学稿或参考稿上（`references/narrative-and-evidence.md:11`）。

### 叙事

叙事弧线按受众和决策来选：问题 → 起因 → 应对 → 证据 → 行动，提问 → 分析 → 回答，现状 → 变化 → 未来，或其他站得住的顺序。每页只承担一个叙事任务和一个主要主张，标题说的是结论而不是话题；每页要么回答上一页提出的问题，要么制造对下一页的需要（`references/narrative-and-evidence.md:15-20`；`SKILL.md:35`）。议程、功能清单和按时间罗列本身都不算叙事（`references/narrative-and-evidence.md:19`）。

### 视觉方向

「方向是一份真实演示可用的设计主张，不是配色卡，也不是装饰性情绪板」（`references/visual-direction-method.md:3`）。每个方向必须包含八个要素（`references/visual-direction-method.md:7-18`）：

1. 沟通主张与叙事重点；
2. 以可读的完整尺寸展示的代表性页面；
3. 字体性格与层级行为；
4. 图片、图表和图解的处理方式；
5. 版式节奏与预期的轮廓变化；
6. 动效逻辑，包括何时不该有动效；
7. 实际看过的成熟参考，或明确标注为本地/原创探索；
8. 面向目标受众与决策的取舍说明。

方向之间必须在叙事重点、构图、字体、图像和节奏上实质不同，只换配色不算（`references/visual-direction-method.md:18`）。被选中的方向会转成本次任务的设计决策，不会变成永久模板（`references/task-and-process-routing.md:33`）。

### 证据边界

四种状态，定义在 `references/narrative-and-evidence.md:22-29`，由 `SKILL.md:39-48` 强制：

| 状态 | 允许用法 |
| --- | --- |
| `verified` | 当前已检查的来源或运行时证据；只能在其真实范围内陈述 |
| `historical` | 有日期的证据；重要时须写明日期或历史边界 |
| `to_verify` | 未解决；删除、收窄表述，或只作为明确的缺口展示 |
| `do_not_publish` | 机密、私人、无关、不安全或被禁止；绝不放进页面 |

硬性禁止很直接：绝不编造指标、客户、引语、证言、截图、结果、评分、调研或性能声明（`SKILL.md:48`；`references/narrative-and-evidence.md:35`）。没有支撑的说法要删除、收窄，或在受众确实需要看见缺口时显式标记为 `to_verify`（`references/narrative-and-evidence.md:36`）。来源语义必须保留——安装量不是评分，历史测试结果不是当前运行时证明，原型不是生产部署（`references/narrative-and-evidence.md:39`）。

### 质量门禁

技术有效性与视觉质量是两道独立的门禁，必须同时通过（`references/quality-gates.md:3`）。复核顺序是：渲染每一页最终稿 → 逐页按全尺寸单独检查 → 拼图只用于节奏和连续性 → 运行 `Presentations` 的溢出与技术检查 → 每次修改后重新渲染并复检（`references/quality-gates.md:31-38`）。失败规则（`references/quality-gates.md:40-46`）：

- 技术通过不能覆盖视觉检查失败；
- 页面再好看，也不能为没有证据的说法或隐私违规开脱；
- 方向板、截图或拼图不是最终成品；
- 低质量素材只能替换或删除，不能靠模糊、压暗或裁掉主体蒙混；
- 拥挤的页面只能重写或重新构图，不能靠缩小到读不出来的字号救回来。

<details>
<summary>完成门禁——交付前必须核对的 8 个条件（<code>SKILL.md:87-100</code>）</summary>

除非满足以下全部条件，否则不得报告为完成：

- 沟通目标、受众结果与叙事弧线相互一致；
- 所有可见说法都有证据状态和必要的来源；
- 选定的流程深度与任务和用户指令匹配；
- 请求文件时，真实 PPTX 确实由 `Presentations` 产出；
- 每一页都已渲染并按全尺寸检查；
- 技术检查通过，且人工视觉复核也通过；
- 没有把方向板或拼图当作最终成品交付；
- 缺失证据与未执行的动作保持显式记录。

</details>

## 输出物

`manifest.json:15` 声明了四项输出。其中三项是文字或决策产物，没有模板、没有 schema、也没有写入路径；第四项由另一个 Skill 产出。

| 输出 | 定义位置 | 实际形态 |
| --- | --- | --- |
| 沟通目标与叙事 | `SKILL.md:31-33`；`references/narrative-and-evidence.md:8,15-20` | 一句被写下来的话，加一条选定的弧线——是精确度，不是文件 |
| 证据账本 | `references/narrative-and-evidence.md:22-29` | 一张两列的 markdown 表格：状态与允许用法 |
| 视觉方向决策 | `references/visual-direction-method.md:5-18` | 一份八要素清单，加上记录下来的用户选择 |
| 通过质量门禁的演示交付物 | 由 `Presentations` 产出，不由本仓库产出 | 真实的 `.pptx` 及其渲染图 |

本仓库产出的唯一**机器产物**是 `scripts/output_eval.py` 写出的 JSON 报告（`--output <path>`）。其结构固定在 `scripts/output_eval.py:143-163`：`ok`、`summary{total_cases,passed,failed,missing_evidence}`、`results[]`、`failures[]`、`evidence{rule_contract,runtime_visual_review,runtime_report}`，以及三条 `method_limitations`。当 `ok` 为 false 时进程以退出码 2 结束（`scripts/output_eval.py:180-181`）。

<details>
<summary>仓库结构</summary>

| 路径 | 用途 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Skill 本体：触发条件、排除项、六项强制动作、完成门禁 |
| [`manifest.json`](manifest.json) | 包身份、意图、权限、发布门禁 |
| [`agents/interface.yaml`](agents/interface.yaml) | 可发现接口：显示名、默认 prompt、示例、权限边界、门禁 |
| [`references/task-and-process-routing.md`](references/task-and-process-routing.md) | 任务规模 → 流程深度分流、范围锁定、委托边界 |
| [`references/narrative-and-evidence.md`](references/narrative-and-evidence.md) | 沟通目标、叙事弧线、四态证据账本、说法规则 |
| [`references/visual-direction-method.md`](references/visual-direction-method.md) | 方向的八个必备要素、参考使用规则、选定交接 |
| [`references/quality-gates.md`](references/quality-gates.md) | 字体与适配、构图、素材、动效、复核顺序、失败规则 |
| [`evals/`](evals) | 触发 fixture 与输出契约 fixture |
| [`scripts/output_eval.py`](scripts/output_eval.py) | 本包唯一的可执行代码 |
| [`tests/`](tests) | 6 项包契约测试 |
| [`examples/renovation-customer-proposal/`](examples/renovation-customer-proposal) | 唯一的运行时产物：7 页成品与全尺寸渲染图 |
| [`reports/`](reports) | 开发过程记录、评估报告与记录下来的运行时案例 |

仓库中没有 `package.json`、`pyproject.toml`、`setup.py` 或 `requirements.txt`，除 `SKILL.md` 外没有安装器和 `bin/` 入口（`manifest.json:9`）。

</details>

## 证据与验证

下列每个数字都来自 2026-09-15 在本仓库实际运行命令的结果。本 README 不把其他任何内容称为「已测量」。

**实际运行过的命令**

| 命令 | 结果 |
| --- | --- |
| `python3 -m pytest tests/ -q` | `6 passed`，退出码 0 |
| `python3 -m unittest discover -s tests -v` | `Ran 6 tests … OK` |
| `python3 scripts/output_eval.py --cases evals/output_cases.json --runtime-report reports/runtime-case-renovation-customer-proposal.md --output reports/output-eval.json` | `ok: true`，4/4 用例通过，`missing_evidence: 0`，`runtime_visual_review: "verified"` |
| 配套仓库 `kang-meta-skill`：`python3 scripts/validate_skill.py ../kang-ppt-skill` | `ok: true`，0 失败，0 警告 |
| 配套仓库 `kang-meta-skill`：`python3 scripts/trigger_eval.py ../kang-ppt-skill --cases ../kang-ppt-skill/evals/trigger_cases.json --output ../kang-ppt-skill/reports/trigger-eval.json` | 14/14 通过，0 误触发，0 漏触发，结果与已提交的 [`reports/trigger-eval.json`](reports/trigger-eval.json) 逐字节一致 |

**这些结果能证明什么、不能证明什么**

- 这 6 项测试是**包契约测试**。其中 5 项只断言文件存在或字符串出现（`tests/test_package.py:19-62`）；1 项执行 `scripts/output_eval.py` 并断言其报告属性（`tests/test_output_eval.py:13-42`）。它们不会打开示例 PPTX、不会读取渲染图、也不会调用模型。本 README 不挂测试数量徽章，因为静态数字会过期。
- `scripts/output_eval.py` 是**关键词与文件存在性检查器**，检查对象是本仓库自己的 markdown。它自己就写明了这一点：「Keyword and file-presence checks verify recorded rule coverage, not presentation beauty or model compliance」（`scripts/output_eval.py:159`）。
- `runtime_visual_review: "verified"` **不是独立视觉验证**。它由 `runtime_status()` 产出（`scripts/output_eval.py:99-113`），做法是在作者自己写的报告里匹配五个字面短语——`rendered every slide`、`full-size visual review`、`overflow check`、`technical gate: pass`、`visual gate: pass`。它不检查任何成品、任何渲染图、任何溢出结果。请把它读作「运行时记录里包含了这些陈述」，仅此而已。
- 14 条触发结果是**录制的 fixture**，不是模型评分评估。它们是对 `evals/trigger_cases.json`（5 条 `should_trigger`、6 条 `should_not_trigger`、3 条 `near_neighbor`）的确定性关键词打分，附一份手写的负例模式表，不调用任何模型。
- 本仓库**没有 CI**。`.github/` 不存在，唯一的 YAML 文件是 `agents/interface.yaml`（Skill 接口清单，不是流水线）。Release 是手工切的。

**确实存在一次真实运行。** [`reports/runtime-case-renovation-customer-proposal.md`](reports/runtime-case-renovation-customer-proposal.md) 完整记录了一次本地案例：每一页都通过已安装的 `render_slides.py` 渲染（L39），用 7 张渲染 PNG 生成拼图（L40），溢出检查返回 `Test passed. No overflow detected.`（L41），`Technical gate: pass.`（L42）与 `Visual gate: pass.`（L58）。报告还记录了返工循环：第一次技术成功后仍发现一处过宽泛的 AI 能力和一处换行后标点跑到行首的问题；后续人工视觉复核又否掉了一张满版深色页，改回与相邻章节一致的纸张底色（L60-69）。同一份报告附有一份诚实的 Missing Evidence 清单（L81-88）。这是本仓库最有力的证据，但它仍只是一次本地运行的自述记录。

**仍未验证**

- 安装与公开发布后的包行为——见「快速开始」；
- 跨模型的触发与输出一致性；
- 真实客户偏好，以及销售、转化或业务影响；
- 投影仪、会议室与更多 PowerPoint 版本下的表现；
- 独立设计师评审或盲测对比；
- 已提交的 PNG 渲染图是否确实出自已提交的 PPTX——两者之间没有哈希关联；
- AI 生成概念图的来源（`examples/renovation-customer-proposal/assets/`）——运行时案例记录了它声明的生成路径，但本仓库没有生成日志、prompt 记录或内容凭证清单；
- `Presentations` Skill 本身：它是本包唯一的依赖，也是本 Skill 完成条件的门禁，却只有名字，没有来源路径、URL 或版本。

## 状态与已知限制

- **版本。** 活跃链路一致：`SKILL.md:6` = `manifest.json:3` = git tag `v0.1.3` = GitHub Release。共 4 个 tag（`v0.1.0` … `v0.1.3`），全部切于 2026-08-16。
- **仓库状态。** 公开、未归档。总计 5 个 commit，全部在 2026-08-16 的约 32 分钟内完成，最后一个是 `release: kang-ppt-skill v0.1.3`。仓库没有 `CHANGELOG`，也没有 CI。开发历史集中在这一个工作时段，因此它是这套体系里较早、已趋稳定的一个 Skill，而不是正在快速迭代的项目。
- **状态元数据自相矛盾。** `manifest.json:6` 写 `"status": "published"`，而 `agents/interface.yaml:31-32` 仍写 `installation: "not authorized"` 与 `publication: "not authorized"`，[`reports/creation-handoff.md`](reports/creation-handoff.md)（L10-12、L104）也仍声称没有做过 Git 初始化、commit、push、建仓或发布。这段文字是历史遗留，按当前实际情况已经为假——仓库是公开的，且有 4 个 Release。此外 `agents/interface.yaml` 完全没有 `version` 字段，仅凭该文件无法确认版本一致。
- **发布门禁是自我盖章。** `manifest.json:24-27` 把四个门禁标为 `"verified locally 2026-08-16"`，但没有 commit 或产物哈希，因此无法与打 tag 的代码树对应。`manifest.json:28` 至今仍把 `installation` 列为 `missing evidence`。
- **仓库里仍有旧名与过期文字。** [`docs/superpowers/`](docs/superpowers) 下的两份文档写在包名还是 `kang-presentation-standard` 的时期，其中一条自审断言把包名和版本写死为两个按当前实际情况都已为假的值。「Kang Presentation Standard」是**有意保留**的人类可读显示名（`SKILL.md:9`、`agents/interface.yaml:2`），`kang presentation standard` 也是 `evals/trigger_cases.json:14` 里活跃的触发关键词；仓库与包标识符则是 `kang-ppt-skill`。
- **部分仓库文件记录了作者本机的绝对路径**（`docs/superpowers/`、[`reports/creation-handoff.md`](reports/creation-handoff.md)、[`reports/output-eval.json`](reports/output-eval.json)）。这些内容公开了本地目录命名习惯和一条私有知识库路径。此处仅作为待修复项记录，本 README 有意不复现这些路径。
- **有两份随包记录已知不完整或失败。** 导出的 skill IR（`reports/skill-ir.json`）中四个 `workflow` 数组为空，尽管仓库明确定义了路由、工作流和多道门禁；`reports/prior-art-candidates.json` 则是一份失败运行的产物（`"ok": false`、`candidate_family_count: 0`）。两者都不应被当作能力来源引用。

## 示例

[`examples/renovation-customer-proposal/`](examples/renovation-customer-proposal) 是仓库里唯一的运行时产物。

| 产物 | 已核实的事实 |
| --- | --- |
| [`renovation-consultation-agent-proposal.pptx`](examples/renovation-customer-proposal/renovation-consultation-agent-proposal.pptx) | 合法 OOXML 文件（`Microsoft PowerPoint 2007+`），2,348,593 字节，47 个 zip 条目——7 个 `ppt/slides/slideN.xml`、7 个 `ppt/notesSlides/notesSlideN.xml`、2 张内嵌图片，含真实 slide master 与 theme |
| [`rendered/slide-1.png`](examples/renovation-customer-proposal/rendered/slide-1.png) … `slide-7.png` | 7 张全尺寸渲染图，均为 1280×720 |
| [`montage.png`](examples/renovation-customer-proposal/montage.png) | 顺序拼图，2096×526 |
| [`assets/`](examples/renovation-customer-proposal/assets) | 一张 AI 生成的建筑室内概念图（标注为氛围图，非项目案例照片）、一张产品界面截图 |

**这是一份真实感强的合成示例，不是真实客户项目。** 它是一份**发给**假设中装修公司的 7 页提案，推销一个 AI 咨询与线索跟进 Agent。其中没有客户身份、没有客户数据、没有合同、没有报价、没有交付日期；运行时案例本身也把「真实装修公司或客户偏好」列在 Missing Evidence 里（L83）。这份文件本身是真实的——它是一份确实被渲染过的合法成品——但它背后并没有真实客户。

成品已做去标识化处理。对仓库的扫描结果是：0 个电话号码、0 个价格、0 个真实公司名、0 个人名、0 个凭据。成品内每一条商业性说法都有边界——可靠性那一页明确声明不承诺尚未验证的可用性、性能或生产稳定性，结尾页只请求一次有边界的试用。每一页的备注里都带 `[Sources]` 来源块。

关于这份示例、需要记录而不是隐藏的已知问题：

- 备注里的来源引用无法从本仓库得到验证；
- 其中一页复用了作者另一个独立项目 `renovation-agent` 的产品截图；本包禁止复制品牌素材（`agents/interface.yaml:27`、`SKILL.md:56`），且没有声明同作者例外，因此这里把该示例记为待协调事项，而不是合规样板；
- PPTX 的 `docProps` 元数据里写着一个与本包无关的制作工具名，并把 `Slides` / `Notes` 记为 0；它不能作为来源证据使用。

## 适用与不适用

它在四种情况下被触发（`SKILL.md:3`）：

1. 需要 Kang 的演示质量标准；
2. 重要演示之前需要多套全尺寸的视觉或叙事方向；
3. 需要证据感知的演示设计；
4. 需要对 PPT/PPTX 做高质量复核。

调用方式是自然语言——例如「按 Kang 的 PPT 标准」或 `Use $kang-ppt-skill`（`agents/interface.yaml:4,6`）。

### 你可以直接这样说

接口里原样附带三条示例调用（`agents/interface.yaml:6-8`）：

| 示例（原文） | 含义 | 标准会做什么 |
| --- | --- | --- |
| `按 Kang 的 PPT 标准，为这份客户方案先给 3 套完整视觉方向` | 先要三套完整视觉方向 | 判定为大型任务：动手前先给三套实质不同的全尺寸方向（`SKILL.md:19`） |
| `直接优化这份月度汇报，保留模板，只改叙事和信息层级` | 保留模板，只改叙事与层级 | 把模板当作视觉权威，并锁定改动范围（`references/task-and-process-routing.md:9,27`） |
| `检查这份 PPT 的证据、字体、图片、动效和逐页交付质量` | 做一次交付前质量复核 | 跑双门禁与逐页全尺寸复核（`references/quality-gates.md:31-38`） |

分流不取决于措辞：明确要求跳过方向，或任务已带有权威模板时，一律按直接执行处理（`references/task-and-process-routing.md:23`）。

**它排除七类任务**（`SKILL.md:3`；`manifest.json:16`）：

| 不在范围内 | 应该走哪里 |
| --- | --- |
| 不要求本标准的普通 PPT 制作 | 直接交给 `Presentations` |
| 单字或单行修改 | 直接编辑 |
| 只读的幻灯片问答 | `Presentations`，不带质量层 |
| 格式转换（例如 PPTX → PDF） | `Presentations` |
| 原生飞书 / Google Slides 操作 | 平台自身工具 |
| 前端设计 | 不是演示任务 |
| 纯图片生成 | 图片工作流 |

此外，**产出 `.pptx` 文件本身**也按设计不在范围内：本 Skill 产出判断、方向与验收决策，文件由 `Presentations` 产出。

## 安全边界与人工决策

治理内容是本包最强的部分，而且它不由代码强制执行——对包内文本唯一的自动化检查是一条窄范围密钥正则（`tests/test_package.py:55-62`），且它不扫描图片和 PPTX。

- **不编造证据。** 指标、客户、引语、证言、截图、结果、评分、调研和性能声明一律不得编造（`SKILL.md:48`）。客户提案在缺少授权证据时不得承诺价格、交付日期、安全性、可用性、集成成功率、性能、节省或转化；此时宁可提出有边界的试用或需求沟通（`references/narrative-and-evidence.md:41-43`）。
- **隐私边界。** `do_not_publish` 覆盖机密、私人、无关、不安全或被禁止的内容，绝不放进页面（`references/narrative-and-evidence.md:29`）。
- **品牌边界。** 可以研究成熟参考并借鉴其机制，但不复制品牌标识、Logo、专属图像、专有素材和无授权表达（`SKILL.md:56`；`references/visual-direction-method.md:22-26`；`agents/interface.yaml:27`）。
- **诚实降级。** 参考不可获取时，记为 `missing evidence`，并把方向标为本地/原创（`references/visual-direction-method.md:28`）。`Presentations` 运行时不可用时，停止 PPTX 制作并报告阻塞（`agents/interface.yaml:35`）。
- **人工决策门。** 重要任务的方向选择由人来做（`SKILL.md:19`）；全尺寸视觉复核是人工判断，技术通过不能覆盖它（`references/quality-gates.md:42`）；发布与安装授权在包里被列为需要授权的权限，而不是默认拥有（`manifest.json:18-22`）。
- **示例不含真实内容。** 示例成品已去标识化，本仓库不发布任何个人数据、报价或客户身份。

## 快速开始

### 安装（未经独立验证）

```bash
npx skills add KanG-ciyuan/kang-ppt-skill
```

这是公开 agent skill 仓库的通用发现命令，仓库本身也是公开的。但本次文档工作**没有执行过**它，包里也没有 `package.json`，因此请把这条命令当作未验证，而不是已验证。仓库自己的记录把安装和公开发布后的包行为列在 Missing Evidence 里（`reports/creation-handoff.md:93`、`manifest.json:28`），本 README 也不发布任何自己并不掌握的安装证据。

### 本地校验

在仓库根目录执行。下列命令都已于 2026-09-15 在本代码树上实际运行。

```bash
python3 -m pytest tests/ -v
# 没有 pytest 时的等价写法：
python3 -m unittest discover -s tests -v
```

```bash
python3 scripts/output_eval.py \
  --cases evals/output_cases.json \
  --runtime-report reports/runtime-case-renovation-customer-proposal.md \
  --output reports/output-eval.json
```

`--runtime-report` 是**必需的**。省略它时，评估器会给出 `runtime_visual_review: "missing evidence"` 与 `missing_evidence: 1`，从而用一份降级报告覆盖已提交的那份「verified」报告。带上该参数，报告才与仓库中已提交的内容一致。

### 包校验与触发 fixture

`validate_skill.py` 和 `trigger_eval.py` **不属于本包**，它们由配套的 [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) 工具链提供。在该仓库的检出目录中、并把本仓库检出在它旁边时：

```bash
python3 scripts/validate_skill.py ../kang-ppt-skill

python3 scripts/trigger_eval.py ../kang-ppt-skill \
  --cases ../kang-ppt-skill/evals/trigger_cases.json \
  --output ../kang-ppt-skill/reports/trigger-eval.json
```

两条都以这种形式运行过并全部通过；触发评估的结果与已提交的 `reports/trigger-eval.json` 逐字节一致。因此仓库中的 `reports/trigger-eval.json` 确实存在可运行来源——但那来源是配套工具链，而不是本包。

### 前置条件

- [ ] 已安装且可调用的 `Presentations` Skill。本包不复制、不内置、也不替代 PPTX 引擎、模板库或运行时；没有它就无法产出 `.pptx`。
- [ ] 真实制作时使用工作区提供的 Node.js 与渲染工具链，不自行安装替代依赖。
- [ ] 对外展示的事实、截图与素材已完成来源核验，并区分 `verified / historical / to_verify / do_not_publish`。
- [ ] 任何发布或安装动作都已获得明确授权。

## 常见问题排查

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 每个任务都被要求给三套方向 | 没有按任务规模分流 | 普通任务、模板任务和局部修改一律直接执行（`references/task-and-process-routing.md:5-11`） |
| 所谓「方向」只是一张看不清的缩略拼盘 | 预览无法承载字体和层级信息 | 一次展示一页代表性页面，保持可读的完整尺寸（`references/visual-direction-method.md:32-34`） |
| 要求产出文件却什么都没生成 | 没有安装 `Presentations` | 这是预期行为：本包不含 PPTX 引擎，也拒绝用别的引擎替代（`SKILL.md:13,73`）；它会停止制作并报告阻塞（`agents/interface.yaml:35`） |
| 技术检查通过了，但页面依然不好看 | 技术通过不等于质量通过 | 跑逐页全尺寸视觉复核；技术通过不能覆盖它（`references/quality-gates.md:42`） |
| 用户的模板被新风格覆盖了 | 没有把模板当作视觉权威 | 回到原母版与布局；未经授权不混用风格体系（`references/task-and-process-routing.md:9,27`） |
| 文案有说服力但没有证据 | 把创作当成了事实 | 删除、收窄表述，或标记为 `to_verify`（`references/narrative-and-evidence.md:36`） |
| `output_eval.py` 报告 `missing evidence` | 漏掉了 `--runtime-report` | 加上 `--runtime-report reports/runtime-case-renovation-customer-proposal.md` 重新运行 |
| 已提交的 `reports/output-eval.json` 不再显示 `"verified"` | 它在没有运行时报告的情况下被重新生成过 | 先用 git 恢复该文件，再按上面的命令重新运行 |

---

## 属于 Kang 开源 AI 体系

```text
发现 DISCOVER
企业 AI 诊断 Skills
        ↓
定义 DEFINE
Kang Product Architect
Kang Enterprise Process Reviewer
        ↓
构建与协同 BUILD & COORDINATE
Kang Agent Workforce
Kang Agent Collab
Kang Frontend Standard
        ↓
验证 VERIFY
Kang B2B UX Auditor
Kang Product Acceptance Auditor
        ↓
交付 DELIVER
Kang GitHub README
Kang PPT Skill
```

> 这是一张生态地图，不是严格的运行时流水线。各阶段描述的是项目所处的工作位置，
> 而不是强制的执行顺序。

本项目是「面向企业 AI 转型、Agent 协作与 AI 原生产品交付的证据驱动体系」的一部分。

| 阶段 | 项目 | 作用 |
| --- | --- | --- |
| DISCOVER 发现 | [enterprise-ai-diagnostic-skills](https://github.com/KanG-ciyuan/enterprise-ai-diagnostic-skills) | 在自动化之前，先弄清企业真实业务如何运行 |
| DEFINE 定义 | [kang-product-architect](https://github.com/KanG-ciyuan/kang-product-architect) | 把模糊需求转化为可实施、可审查的产品契约 |
| DEFINE 定义 | [kang-enterprise-process-reviewer](https://github.com/KanG-ciyuan/kang-enterprise-process-reviewer) | 审查流程是否可执行、可追责、可恢复 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-workforce](https://github.com/KanG-ciyuan/kang-agent-workforce) | 角色化的 Agent 数字员工团队与显式交接 |
| BUILD & COORDINATE 构建与协同 | [kang-agent-collab](https://github.com/KanG-ciyuan/kang-agent-collab) | Agent 协作与交接协议 |
| BUILD & COORDINATE 构建与协同 | [kang-frontend-standard](https://github.com/KanG-ciyuan/kang-frontend-standard) | AI 构建界面的前端质量标准 |
| VERIFY 验证 | [kang-b2b-ux-auditor](https://github.com/KanG-ciyuan/kang-b2b-ux-auditor) | 用户能否真正把工作做完 |
| VERIFY 验证 | [kang-product-acceptance-auditor](https://github.com/KanG-ciyuan/kang-product-acceptance-auditor) | AI 构建产品的独立验收 |
| DELIVER 交付 | [kang-github-readme](https://github.com/KanG-ciyuan/kang-github-readme) | 证据感知的 README 工程 |
| DELIVER 交付 | [kang-ppt-skill](https://github.com/KanG-ciyuan/kang-ppt-skill) | 证据感知的演示文稿设计 |

**横向基础设施：** [kang-meta-skill](https://github.com/KanG-ciyuan/kang-meta-skill) —
Skill 工程化、评估与发布治理。

**早期工作：** [ai-agent-rules](https://github.com/KanG-ciyuan/ai-agent-rules)、
[workflow-five-steps](https://github.com/KanG-ciyuan/workflow-five-steps)、
[renovation-agent](https://github.com/KanG-ciyuan/renovation-agent)。

本仓库处在 **DELIVER** 阶段：它决定一份演示必须传达什么、成品是否可以接受，而把文件本身交给另一个实现权威。

## 开源许可证

本项目采用 [MIT License](LICENSE) 开源。
