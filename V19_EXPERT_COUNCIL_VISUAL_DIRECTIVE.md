# V19 学术视觉与排版专家模拟廷议 — 正式决议（设计版）

> **事实边界**：本文件是基于 HiMCM 2026 官方网页、官方题目、公开评审评论摘要、Nature/PLOS 图形规范与 V18 实际源码的多学科**模拟评审**，没有真实 HiMCM 评委受邀或发表意见。V19 的论文与图谱仍须真实数据运行；本文件只制定实施合同和验收标准。

## 0. 已记录的用户决定／不改主线

算法主线：I 自适应有向截断 Dijkstra；II 基于真实 OD 的固定权重次模设施机会优化（Greedy/CELF）；III 人口加权尾部 CVaR 与关键边扰动。保持十二城 Census/TIGER/OSM 数据源、系统论框架、参考 M0/M1 排名以及原有结果的严谨门禁。具体数学假设、近似界的适用条件见 `V19_DECISION_LOCK.md`。

## 1. 资料级别与直接发现

**官方硬约束（不是编辑建议）：** 单份英文 PDF；第1页 Summary；解答、目录、参考文献、新闻稿等合计不超过25页；正文可读字至少12 pt；每页顶部 Team Control Number + 页码且不得出现个人、学校身份；AI使用报告附在25页后不计入25页。A题要求至少十城、显著模型修订、1–2页非技术新闻稿。对于本未报名独立项目，绝不能填造 Team Control Number 或声称可以官方提交。官方建议的正文分节是 Optional Layout，不可混同于硬格式。

**官方评审关注点：** 建模过程、分析、数学方法、清楚且有证据的结论；公开的 Consortium HiMCM Judges’ Commentary 强调图、表与文本平衡，并把说明放在相关图表附近。

**V18 实际源码发现（审计而非猜测）：** `render_atlas.py` 设置默认字号10 pt，局部包含6–8 pt 标签及250dpi栅格导出；`decision_atlas.py`和地图函数也有9–11 pt；`build_empirical_gis_paper.py` 的 `\documentclass[12pt,letterpaper]{article}` 与 `.78in` 边距基本合理，但仍依赖若干 `F17_GIS_*` 旧文件名； `render_city_atlas_v18.py` 的15×7双图若直接嵌进Letter纸将严重缩小注释。因此 V19 要解决的是最终打印尺寸的可读性，不是单纯把 PNG 改成 PDF。

## 2. 十席模拟审稿与综合裁决

| 专业角色（模拟） | 关键质询 | V19 采用的决议 |
|---|---|---|
| HiMCM 主审 | 读完Summary能否立即知道前提、模型修订、12城结论、未验证之处？ | Summary一页，最后生成；最多1个主结果视觉；来源与条件必须在页内。 |
| HiMCM 数学审 | 三个算法各自解决什么，在哪些假设下成立？ | 每个算法必须有现实问题、变量/单位、伪代码、关键定理/性质与同数据benchmark。 |
| 运筹专家 | 设施选择是不是偷偷替代了12城排名？ | 优化是干预反事实子研究；仅比较固定预算/候选集，禁止重置M1。 |
| GIS专家 | 几何地图能否反映合法步行路线与入口不确定？ | 导出实际图边/设施/tract；GIS地图必须图例、CRS、比例、时间和准入注释。 |
| 统计专家 | MOE外包络是否被错误写成联合95%置信区间？ | 统计抽样/设施资格/偏好情景分层绘制，禁止混并概率术语。 |
| 科学图形设计师 | 图是否存在字小、图例重复、无实义多面板？ | 每图单一主张；常规主文仅约7张高价值图，其余输出atlas。 |
| 学术排版专家 | A4/Letter转码、字体、公式、参考文献会不会违例？ | 12pt实际PDF跨度审查、25页实际分页审查、页眉/摘要模板审查。 |
| 无障碍评审 | 黑白或色盲是否仍可区分？ | 同时使用线型、标记、图例与直接标签；不得仅靠红绿对比。 |
| 复现专家 | 图和文字是否确实来自同一批源文件？ | figure ID ↔ claim ID ↔ equation ID ↔ result CSV ↔ raw SHA ↔ run ID，全部自动关联。 |
| 非技术编辑 | 非技术新闻稿会不会成为换词版Summary？ | 独立写作2页以内，面向家长/城市公共议题，同一数据事实但另一种叙事。 |

## 3. 学术视觉系统（Design Tokens）

| 元素 | 推荐规范 | 原因 |
|---|---|---|
| 论文纸张 | US Letter 8.5×11英寸；边距0.78–0.85英寸，全文统一 | 与V18已有LaTeX兼容；保证图幅预测可靠 |
| 主文本 | 12pt，合理行距1.15–1.22倍；数学字体与正文配套 | 遵守COMAP可读性要求；无需故意填满25页 |
| 一级标题 | 15–16pt、醒目但不夸张；二级13–14pt | 建立层级而非海报化 |
| 图轴/标注/图例 | 优选最终PDF打印尺寸下12pt；确实困难时拆分图，而非缩至6pt | 保守满足主办方至少12pt约束 |
| 图注 | 12pt正文宽度；顺序：结论型标题—数据/单位—不确定性—来源 | 图应与正文独立可解释 |
| 表格 | booktabs；数值按小数点或单位对齐；不用竖线与浓色背景 | 减少视觉噪声与误读 |
| 数学 | amsmath＋cleveref；每个核心公式附变量与单位；只编号被引用的式子 | 数学不是装饰 |
| 主色 | 深海军蓝 `#183B56` | 主参考模型／可信证据 |
| 机会色 | 冷青 `#087E8B` | 真实可达机会 |
| 干预色 | 沙金 `#C18C39` | Algorithm II反事实资源配置 |
| 负效应色 | 暖赭 `#AD5D58` | 风险、限制、未知资格（须配线型） |
| 中性色 | `#5D6B75` / `#E9EEF0` / 白 | 文字、网格、浅底；不使用大片彩底 |
| 数据源编码 | 实心=观测；空心=代理；虚线=情景；斜线/问号=未知 | 灰度或色盲场景也能识别 |

**对Nature/PLOS规范的正确借鉴：** 学它们的视觉精确、有限色彩、清楚轴单位、矢量源文件和来源说明，而不复制期刊常见的5–7pt缩印字号到COMAP报告。Nature指出应避免多余彩色与装饰，PLOS建议在栅格交付时使用300–600dpi；但具体图中文字字号需服从本报告更严格的竞赛约束。

## 4. 统一视觉语法（不是三篇独立论文）

**层级逻辑图：**

`Urban boundary [TIGER PLACE] → Tract youth proxy [ACS B01001] → Facility eligibility [OSM/IMLS] → Road access [Algorithm I] → Current M0/M1 city score → Intervention [Algorithm II] → Tail/edge robustness [Algorithm III] → Verified decision + uncertainty [LP/Evidence]`。

凡箭头都标变量或文件名，如`n_g`, `OD_{gj}`, `A_{gk}`, `a_g`, `M1(c)`, `∆F(K)`, `L_0.1`, `R_e`。用一个小角标区分：**Observed / Inferred / Normative / Counterfactual**。以虚线和旁注画研究流程中的“诊断→改模型→验算”；不得将其说成测得的真实城市社会反馈。

**Algorithm I 的视觉结构：** 先展示真实有向路网、源点与设施节点；再显示正向与反向截断Dijkstra，同一OD值一致；最后给出速度与内存基准。须标注数据规模、速度阈值和重现条件。

**Algorithm II 的视觉结构：** 图一显示候选点与受益区域；图二显示K=0...Kmax的实际边际改善和近似比较；图三显示固定候选集下 Greedy、Random、Count、Euclidean 在相同预算下的结果，不直接声称现实可建。

**Algorithm III 的视觉结构：** 人口加权机会分布分位曲线说明 Q10 与 CVaR区别；关键边扰动前后的图像要求重路由而不是扣分；同一图中不要把统计抽样误差与断边情景合并成“置信带”。

## 5. V19 图谱计划

见机器可读 `V19_FIGURE_PROGRAM.csv`，列出16张图的唯一ID、来源、所需实算、主论文/atlas去向和科学误用禁令。**主PDF仅保留约7幅：F19-01/03/04/05/06/07/08**，辅助图以证据图谱提供，非强制塞入25页。图号是规划标识；没有真实数据的数值图不能预先生成或假填。

最终的专题图谱建议四组：

- A 证据与空间数据：来源谱系、人口/城市地理、12城同尺度地图；
- B 模型与算法：Dijkstra精确解/基准、控制消融、次模收益/定理对照；
- C 决策与系统论：12城主榜、LP/Pareto、不确定性、跨界性与韧性；
- D 科研复现：模型输入—输出注册表、地图坐标元数据、图表来源 SHA256。

对“10/20/30分钟服务区”，严格用道路图可达子图与合法构造的服务区域几何表达，不允许把欧氏圆或凸包直接称为精确真实网络服务圈。绘制多个城市时颜色尺度、分位法、边界口径、图例、字体一律统一。

## 6. 图表选型细则

| 要表达的判断 | 首选可视化 | 不推荐的做法 |
|---|---|---|
| 城市第一与完整排序 | 12城水平点/条图，标数值和单位 | 饼图、雷达图当主结果、只有热图没榜单 |
| 重大修订引起的名次变化 | M0→同设施库存→直线→路网→公平 slopegraph，另分维解释 | 只有M0 vs M1却归因于道路 |
| 地理机会和服务覆盖 | 正确 CRS 的路网、tract、设施与真实OD路径 | 装饰性城市地图、未经验证入口、虚假等时圈 |
| 贪心设施优化 | K-收益曲线、与确切小实例对照、同预算基线 | 只给出看似理想的选址点、没有真实收益 |
| 最差群体机会 | 人口加权尾部曲线、Q10/CVaR比较 | 把Q10画成统计置信下界 |
| 不确定性 | ACS MOE与资格上界分开；端点类型文字清晰 | 一个大误差棒同时当“95%置信” |
| 系统稳定与脆弱 | 删边后的机会损失/路由变化分布 | 用一张动态箭头图谎称长期稳定性 |
| 数据论据可追溯 | 有输入文件/字段/公式/运行ID的因果审查图 | 仅有箭头方框、无变量单位和事实接口 |

## 7. 25页内容预算——“纸张先行，图像后做”

详见 `V19_25PAGE_EDITORIAL_PLAN.csv`，提供每一物理页的工作预算：P1摘要、P2目录、P3–21正文、P22–23新闻稿、P24–25参考文献（最后一页为伸缩预留）。如新闻稿实际仅1页或参考文献一页，空余页可转给关键推导，但不能超25页。目录和参考文献都计入25页，AI报告附后不计。不要在第25页突然附大量不可读伪代码/链接；完整代码和数据保存在独立可复现包中，不作为正式提交附录。

## 8. 实施工具栈与已有源码修复

- 数据和线路：Census/TIGER、GeoPandas、OSMnx/NetworkX、SciPy；原始源与缓存都存 SHA。
- 静态科研图：Matplotlib 输出 `PDF + SVG + PNG`；避免透明叠图过多、PDF裁剪框过紧和对文档整体缩放。
- 概念系统图：Graphviz `dot` 生成初稿后矢量精修；只允许用于无地理尺度的流程图；节点展示变量/单位。
- 数学和排版：`article[12pt,letterpaper]` + `amsmath`, `mathtools`, `booktabs`, `tabularx`, `siunitx`, `cleveref`, `microtype`, `hyperref`, `fancyhdr`, `graphicx`；使用原版 COMAP Summary TeX 的真实下载副本，修改团队字段时若未注册用独立研究标识且显式标记不合官方提交要求。
- 自动排版：`latexmk` 编译；`pymupdf`/`pypdf` 检查页码与文字，200dpi逐页渲染；逐页检查文字尺寸、图表溢出、公式截断、超页、孤行和英文字符问题。
- 发现的具体遗留应修复：`render_atlas.py` 中6–8pt文字，250dpi；`render_city_atlas_v18.py` 15×7图在 Letter 上缩印；`build_empirical_gis_paper.py` 中仍引用旧版 F17 图名；图表与正文使用不同字体与图注习惯。V19规范要求统一命名 `F19-*`、统一图表尺寸并在最终嵌入尺寸下重新绘图，而非简单放大旧位图。

## 9. 论文硬门禁和人工评审

参见 `V19_VISUAL_QUALITY_GATES.csv`。最低要求：

1. **源**：每张图的原始输入链接、文件SHA256、软件版本、准确单位和算法条件可追溯。
2. **格式**：一份英文PDF，Summary第一物理页，页码，控制号规则（正式参赛才填写真正控制号），正文/TOC/新闻稿/参考文献在25页内；AI报告在后。
3. **可读性**：PDF最终打印尺寸≥12pt文本；独立渲染所有页；若嵌入图导致小字先拆图，不能以“期刊允许小字”为由绕过比赛规则。
4. **数学**：Algorithm I/II/III 均要有原数据验证、公式单位、条件证明、失败例和对应图；CELF 近似界只在满足约束条件时成立。
5. **审稿**：检查每个结果段落是否出现 `Claim → Evidence → Computation → Possible counterexample → Scope` 五要素；新闻稿的数字与 Summary/正文完全一致。
6. **负结果**：若没有原始官方数据与12城路网，所有真实排名图、GPS地图、性能提升和正式PDF均保持 BLOCKED，不准用假结果实现视觉预览。

## 10. 高优先级建议及反对意见决议

| 争议 | 反对意见 | 最终建议 |
|---|---|---|
| 是否做Nature式图形 | 期刊小字号/精细多面板易违反HiMCM12pt与25页 | **保留学术美学，拒绝期刊的小字密图** |
| 是否把12城全部地图放主文 | 空间比较全面但大概率缩小到不可读 | **主文一城机制地图＋多城对照小表，完整地图独立atlas** |
| 是否做3D城市效果图 | 视觉抓人但可能无法证实高程/步行阻抗 | **仅在真实DEM与坡度算法存在时做可证据化3D，绝不占核心主文版面** |
| 是否展示三算法全部伪代码 | 有助数学辨识但版面有限 | **I、II主文短伪码，III主文公式＋验证，完整流程在独立复现包** |
| 是否用复杂桑基图表示所有数据源 | 适合汇报但遮挡具体字段 | **用带变量/单位的分层DAG，原始字段表辅助** |
| 是否追求全25页满页 | 内容拥挤并降低可信度 | **不必填满25页；只保留支持结论的证据与论证** |

## 11. 建议交付结构

```text
Y_CITY_SYORA_V19/
  V19_MASTER.md                     # 将本决议并入唯一主控，不丢V18模型合同
  V19_DECISION_LOCK.md             # 用户锁定的三算法与主模型边界
  design_v19/
    editorial_design_tokens.json
    figure_program.csv
    page_budget.csv
    visual_quality_gates.csv
    algorithm_figure_contracts.csv
  code_v19/
    render_scientific_atlas.py
    render_algorithm_figures.py
    render_city_maps.py
    paper_layout_and_font_audit.py
    build_empirical_paper.py
  figures_v19/                     # 真实运行后产生，不预填数值图
  paper_v19/                       # 真实运行后产出TeX/PDF与附录
  qa_v19/                          # 字体/页数/图源/单位/截图/发布证明
```

该结构是下一轮可执行升级的目标目录，并不表示这些源代码在本“廷议”交付中已经全部实现。

## 12. 可靠参考来源（链接已核对）

- COMAP 2026 Instructions: https://contest.comap.org/highschool/contests/himcm/instructions.html
- 2026 HiMCM A original PDF: https://contest.comap.org/highschool/contests/himcm/2026_Problems/2026_HiMCMProblem_A.pdf
- COMAP generic Summary LaTeX: https://www.contest.comap.com/highschool/contests/himcm/flyers/HiMCM-MidMCM_Summary.tex
- COMAP Consortium HiMCM Judges Commentary: https://www.contest.comap.com/highschool/contests/himcm/flyers/Cons_HiMCM.pdf
- Nature scientific graphics: https://www.nature.com/nature/for-authors/formatting-guide
- Nature research figure guide: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
- PLOS figure requirements: https://journals.plos.org/plosbiology/s/figures
- NetworkX+OSMnx geospatial example: https://networkx.org/documentation/latest/auto_examples/geospatial/plot_osmnx.html

**最终审查状态：** `V19_VISUAL_CONSENSUS_DOCUMENTED / ALGORITHM_DESIGN_LOCKED / CODE_MIGRATION_PENDING / EMPIRICAL_DATA_PENDING`。未声称实际评委出席、真实数据实算、正式论文编译或获得评审认可。
