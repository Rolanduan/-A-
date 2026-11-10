# V18 — Y-CITY × SYORA: official-byte → routed GIS → decision evidence → manuscript

**Current delivery: executable source package.** We have **not** downloaded the official Census/TIGER/OSM raw bytes in this artifact, generated twelve real GraphML networks, produced a real city champion, or compiled an empirical PDF. Those outputs require a future, actually successful real-data run on a suitably connected computer. The project fails closed when data are missing.

## Unchanged research backbone

- **Study**: twelve preselected U.S. cities, ages 15–17 ACS proxy for 14–18, 2024 ACS five-year and 2024 TIGER geographies, genuine OSM pedestrian graph and network shortest paths.
- **Scientific engine**: frozen M0 family-context score and M1 road-constrained population-weighted opportunity; same-POI inventory/Euclidean/route/equity ablations; GIS external and raw-source replay; 27 structural scenarios, 18 route-stress cases, ACS MOE stress, six-utility LP/Pareto.
- **Original academic outcome**: complete official-optional-layout English paper, 1–2-page article, source-linked figures, independent AI-use appendix and manual scholarly review gate.
- **Additional V18 analysis, kept subordinate to M1**: an outer evidence horizon, a 24-item city-by-evidence verification queue, three explicit analyst-only household priority paths with exact leader-switch boundaries, a claim-evidence review registry and two evidence-bound analytical figures.

No data or code from another team's public repository are runtime inputs. Read `research/V18_TRANSFER_AND_DIFFERENTIATION.md` for clear provenance and limitations.

## Commands

From the **unzipped project root** (`Y_CITY_SYORA_V18/`), using Python 3.11 with a compatible GIS toolchain:

```bash
python -m pip install -r code_v18/requirements_v18.txt
PYTHONPATH=code_v18 python -m pytest -q tests_v18
python code_v18/run_v18.py --dry-run
python code_v18/run_v18.py --stage all --network auto
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\code_v18\run_v18_windows.ps1
```

Linux/macOS:

```bash
bash code_v18/run_v18_linux_macos.sh
```

The **30 stages** include actual original data acquisition, realistic network routes, independent replay, controlled ablation, figures, manuscript, and final proof checks. `--dry-run` prints stages only; it never downloads or computes a city rank. The full run may consume gigabytes and require native GIS packages, Graphviz and TeX Live. No guarantee of external hosts' availability is implied.

## Official primary sources and recovery options

The code is designed to obtain *four whole-table ACS 2024 five-year Table-Based Summary File* originals (`B01001`, `B25070`, `B28002`, `B17001`) and **24 official Census 2024 TIGER PLACE/TRACT ZIPs**, totaling 28 mandatory original files. It independently hashes every complete original and records publisher URL, download mode, date, byte length and schema. Census is the official source of these governmental files; locally computed SHA256 is a file identity check, not a publisher signature.

OSM pedestrian observations are collected from OSMnx/Overpass raw cached bytes **or** Geofabrik state-level `.osm.pbf` raw files parsed to genuine walkable GraphML and directed OD routes. OSM is a community dataset, not Census-certified pedestrian access. Entrances, public use and opening hours may be uncertain. Strict reference counts only candidate facilities tagged as public; unknown enters the outer scenario, not the base rank. Keep attribution and comply with ODbL.

If direct download fails, a human can fetch legitimate exact original files through another network and import **with a verifiable source attestation**. The command is:

```bash
python code_v18/run_v18.py --stage all --network auto --import-dir /path/to/raw_files --attestation-dir /path/to/verified_receipts --allow-attested-origin
```

Independent IMLS official library outlet records and COMAP official summary TeX require genuine original byte evidence and are not faked. If source structure changes, adapt parsers after inspecting the real schema; don't replace missing original files with URL lists or synthetic numbers.

## V18-only acceptance files (created only by actual successful computation)

| Evidence | Output |
|---|---|
| 12-city frozen primary reference | `results_v18_gis/FINAL_12_CITY_REAL_GIS_RANKING.csv` |
| Same-POI controlled model revision | `results_v18_gis/V18_CONTROLLED_ABLATION.csv` |
| Source-backed ACS sampling stress | `results_v18_gis/V18_ACS_MOE_STRESS_ENVELOPES.csv` |
| Evidence exclusion/non-exclusion outer bounds | `results_v18_gis/V18_EVIDENCE_HORIZON.csv` |
| Conditional verification ordering | `results_v18_gis/V18_TARGETED_EVIDENCE_QUEUE.csv` |
| Analyst-declared preference families | `results_v18_gis/V18_DECLARED_PREFERENCE_FAMILIES.csv` |
| Analytic leader-switch intervals | `results_v18_gis/V18_EXACT_LEADER_TRANSITIONS.csv` |
| Worst regret across these families | `results_v18_gis/V18_CROSS_FAMILY_MINIMAX_REGRET.csv` |
| Evidence-grounded discussion | `paper_v18_official_gis/V18_DECISION_EVIDENCE_ADDITIONS.tex` |
| Manuscript and release proof | `paper_v18_official_gis/*.pdf`; `qa_v18/final_release_audit.json` |
| Supplementary figure evidence | `figures/v18_decision_evidence/V18_DECISION_FIGURES_MANIFEST.json` |

All results are required to be internally consistent with original source SHA256. A rank that persists for some specified scenarios is **not** a probability that the city is best for actual teens. `NOT_EXCLUDED_BY_OUTER_BOUND` is only a conservative logical label, not a jointly feasible winning state.

## Human review and final release

`code_v18/decision_release.py` checks new V18 evidence after the original government/OSM QA. `code_v18/release_audit.py` verifies both the inherited GIS/paper contract and the new audit; anything missing remains blocked. The paper uses the official **optional** section order chosen for this study, with its real COMAP Summary template when obtained and a distinct AI use report. Users who have not registered for HiMCM cannot imply formal team control number or official COMAP approval.

Read the **master** `V18_MASTER.md`, source-differentiation `research/V18_TRANSFER_AND_DIFFERENTIATION.md`, requirement matrix `V18_QUALITY_GATES.csv`, and `AGENT_AUTORUN_PROMPT_V18.md` before executing. The source-only archive intentionally excludes old version files, old rankings and old PDF studies.
