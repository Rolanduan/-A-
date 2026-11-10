# Y-CITY × SYORA | V18 — COMPLETE STANDALONE EMPIRICAL RESEARCH ENGINE

**Identity:** V18-only executable research directive; no earlier-version archives, master documents, datasets, reports or source code are bundled. Any indispensable earlier algorithms have been integrated under `code_v18/` and migrated to V18 storage paths.

**Research target:** Download and verify 28 original 2024 U.S. Census ACS/TIGER files, acquire 12 authentic OSM pedestrian street networks from OSMnx/Overpass or Geofabrik/PBF, calculate route-based opportunity with tract-scale youth proxies, rank all 12 cities, independently recompute results, run systems-science and uncertainty tests, render real scientific charts and GIS maps, then compile an English scientific PDF to the official optional layout. Data acquisition and final empirical paper have NOT been executed in this packaged edition. A ZIP containing scripts is not a proof of downloads.

**Binding rules:**
1. The only valid code namespace is `code_v18/`, only runnable tests are under `tests_v18/`, and the only frozen reference weights are `config_v18/reference_model_v18.json`. No external version folder is a runtime dependency.
2. A ranking or compiled empirical manuscript may be released only after 28 original Census bytes with SHA256 and actual source provenance, 12 OSM graphs and their raw OSM sources, real route/POI inputs, complete scores, independent replay, sensitivity, system hypotheses, source-grounded figures, PDF preflight and human scientific review.
3. Census is the government publisher of ACS and TIGER; OSM street observations are from OpenStreetMap contributors (and may be obtained through Geofabrik or Overpass), not a government-certified walking network.
4. The official paper layout supplied by the user is explicitly optional, but the project chooses to follow it and audit that choice. Scientific validity and model uncertainty cannot be established by chapter labels alone.
5. Hard failure or unavailable data produces `BLOCKED_FOR_FINAL_GIS_PAPER` and a precise evidence ledger, never invented Census, maps, ranking or results.

**Canonical entrypoint:** `python code_v18/run_v18.py --stage all --network auto`. Use `--dry-run` only to inspect phases; never describe a dry run as completed empirical execution. Windows users may run `code_v18/run_v18_windows.ps1`; Linux/macOS users may run `code_v18/run_v18_linux_macos.sh`.

---

## 1. V18 original research purpose and the single model spine

The question remains **Which city among twelve fixed U.S. candidates is most favorable for a high-school-aged resident under explicitly defended, measurable and potentially reachable opportunities?** Preserve the 12-city study set as frozen before seeing results: Austin TX (`4805000`), Boston MA (`2507000`), Chicago IL (`1714000`), Denver CO (`0820000`), Madison WI (`5548000`), Minneapolis MN (`2743000`), Pittsburgh PA (`4261000`), Portland OR (`4159000`), Raleigh NC (`3755000`), San Diego CA (`0666000`), Seattle WA (`5363000`), Atlanta GA (`1304000`). Each seven-digit place GEOID is a **string** and must retain leading zeros. No city is dropped for scoring convenience, and there is no peeking at the champion to re-select indicators.

The unified mathematical narrative is **systems boundary → observations → M0 simple baseline → explicit model diagnosis → M1 network-constrained opportunity revision → M2 fairness, trade-offs and robustness → qualitative meaning → separate limitations/conditional interpretations.** Never present M0/M1/M2 as three unrelated city indices. A historical city-level proxy ranking must not be imported as the network-GIS champion or used to tune the model.

V18 explicitly combines two non-interchangeable original source families:

- **Official federal originals:** 2024 ACS five-year Table-Based Summary File at the full `.dat`-file byte level and 2024 Census TIGER/Line place/tract shapefile ZIPs. These support statistical, population and municipal boundary assertions. The Census all-roads county shapefiles are additional independent road geometry, not a legal pedestrian-access routing network.
- **Actual OSM network originals:** Overpass's actual HTTP response bytes cached by OSMnx **or** Geofabrik's actual downloaded `.osm.pbf` bytes. OpenStreetMap contributors provide OSM observations under ODbL; these are not official U.S. Census walking network records. The saved `GraphML` is derived by actual parsing of original OSM bytes, not raw OSM source.

**Evidence hierarchy:** `SOURCE_URL_DISCOVERED` ≠ `ORIGINAL_BYTE_DOWNLOADED` ≠ `HASH_RECORDED` ≠ `SCHEMA_PASSED` ≠ `GEO_TIME_ALIGNED` ≠ `GRAPH_ROUTES_CALCULATED` ≠ `INDEPENDENTLY_RECOMPUTED` ≠ `COMPLETE_PAPER_COMPILED` ≠ `HUMAN_SCIENTIFIC_REVIEW_PASSED`. Do not publish a winning city until the final conditions are met.

## 2. Mandatory 28 Census originals: complete, executable download contract

**Data version decision (freeze):** 2024 five-year ACS means observations from 2020–2024; geographic boundaries from TIGER 2024. They do not constitute a 2026 survey or exact 2024 individual housing observation. Record the 2026 retrieval date separately. The official dataset and file grammar are documented at:

- `https://www.census.gov/programs-surveys/acs/data/summary-file.2024.html`
- `https://www.census.gov/programs-surveys/acs/data/summary-file/getting-started.html`
- `https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/`
- `https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html`

**All 28 original files are REQUIRED for the reference main model:**

1. `acsdt5y2024-b01001.dat` → project file `acs_2024_5y_B01001.dat`: population by sex and age, tract and city.
2. `acsdt5y2024-b25070.dat` → project file `acs_2024_5y_B25070.dat`: household rent as share of income; exclude 'not computed'.
3. `acsdt5y2024-b28002.dat` → project file `acs_2024_5y_B28002.dat`: use **`B28002_E004` broadband of any type**, NOT `B28002_E002` (any internet subscription). Verify all actual labels using official table definitions.
4. `acsdt5y2024-b17001.dat` → project file `acs_2024_5y_B17001.dat`: poverty status by sex/age universe; use correctly scoped B17001 002/001 ratio for citywide household-context proxy, not a direct child poverty probability.
5–28. For all **twelve** state FIPS prefixes `06,08,13,17,25,27,37,41,42,48,53,55` download both `https://www2.census.gov/geo/tiger/TIGER2024/PLACE/tl_2024_{STATE}_place.zip` and `https://www2.census.gov/geo/tiger/TIGER2024/TRACT/tl_2024_{STATE}_tract.zip`. The 24 state-specific ZIPs must each be a real ZIP containing shapefile geometry, not a scraped city outline or synthesized GeoJSON.

The acquisition executable is `code_v18/acquire_census.py` using a robust transfer kernel in `code_v18/fetch_verified.py`. It attempts HTTPS streaming with bounded exponential retry and true byte-offset resume. A resumed `206` must confirm `Content-Range` begins at the already received offset; a server that ignores Range and returns `200` restarts the file, never concatenates duplicate bytes. On network failures the downloader can legally attempt installed **aria2, curl and wget** with bounded retries, without evading authentication or server rate limits. Downloaded files are kept byte-for-byte, not decompressed into replacement pretend originals.

`SHA256(original_byte_stream)` is generated only after the original file exists. For each source store: `source_id,publisher,official_url,final_response_url,datetime_utc,file_path,exact_byte_count,http_status,sha256,content_type,zip_or_dat_schema_pass,origin_verification,release_eligible`. Save manifests atomically to `qa_v18/census_original_manifest.json` and optionally append sidecar `sha256sum` checks; manually typed or pre-existing hashes do not prove retrieval. **The official source does not necessarily publish a trusted reference SHA256; a locally computed SHA256 demonstrates identity and later consistency, while actual official-domain TLS/download records support provenance.** Do not claim publisher-certified checksum without an official published expected digest.

The parser must stream the real **pipe-delimited** table-based ACS original (`|`), not assume a comma-delimited CSV, and distinguish its `B01001_E006` / `B01001_M006` form from Census API's `B01001_006E` / `B01001_006M`. Match `GEO_ID` exactly: `1600000US` + seven-digit city GEOID or `1400000US` + eleven-digit tract GEOID. Reject missing/malformed estimate and MOE columns, duplicates, negative Census sentinel codes, values marked unavailable and incompatible denominator universes. Retain a 12-city derived CSV **and its hash**, linked to the hash of the actual full-table source.

A Census API response may be used **as an independently hashed cross-validation source**, but it does **not** replace a missing whole-table `.dat` when the strict V18 full-original release gate requires the latter. `data.census.gov` CSV exports and legal archives are also acceptable for independent validation and recovery, clearly tagged with their own exact data format/vintage and local SHA. They do not silently downgrade the 28-original condition.

## 3. More-than-one-way acquisition without compromising provenance

The source hierarchy is a **decision tree**, not a guarantee of HTTP availability:

- **A: Direct federal originals:** `www2.census.gov` official Table-Based `.dat`, official TIGER ZIP, exact names and vintage. Download via Python, curl, aria2 or wget. Support HTTPS system proxy settings where legally and securely configured. Do not bypass access control or falsify a user agent to defeat explicit denial.
- **B: A different legitimate client on the same official origin:** browser, approved network or remote machine; download exact official bytes to a local folder. Do not edit their raw bytes; compute SHA256 and record the real official HTTPS URL and browser/download evidence. Import through `--import-dir` and actual per-file JSON attestation; use `--allow-attested-origin` only after human verification. This is separately labeled as **human-attested**, not machine-proven direct-source transfer. Official original files may also be brought in from an institutionally obtained lawful copy with independently verifiable trusted receipt.
- **C: Geofabrik fallback for OSM:** `https://download.geofabrik.de/north-america/us/{state}-latest.osm.pbf`. Download state original PBF to a stored file; independently SHA256 it; use Pyrosm's `OSM(...,bounding_box=...)`, `get_network(network_type='walking',nodes=True)` and `to_graph(...,graph_type='networkx')` to build the actual walking network. Recover POIs from actual PBF features. This is source independent of the Overpass HTTP API.
- **D: Overpass fallback for OSM:** OSMnx `graph_from_polygon(...,network_type='walk')` + saved raw HTTP cache and `features_from_polygon()` for candidate libraries/parks. Respect Overpass rate limits and timeout. A legal second public Overpass endpoint can be configured only if its behavior/terms are reviewed. Do not assert that an untried endpoint was successfully used.
- **E: Other openly documented OSM extract indexes for further recovery:** Pyrosm's `find_extracts/get_data_by_area` discovers Geofabrik, BBBike and Movisda options. If a new source is used, preserve its actual original PBF bytes, URL, exact SHA256, license/attribution and geometry extent. Verify walk/POI coverage using the same graph tests. Record the different source ID; never silently relabel a BBBike extract as Geofabrik. Do not claim an automatically cropped derivative PBF is the unmodified upstream original file.
- **F: The Census 2024 TIGER county `ROADS` series** is available through the optional `code_v18/acquire_tiger_roads.py` stage. It provides independent original cartographic street geometry and SHA256 for city-covering counties, useful for cross-source topology checks, **but cannot silently replace a legal pedestrian walking graph**. TIGER includes vehicular/private facilities and lacks all pedestrian entitlement constraints.

The permitted sources and links are only candidate inputs until actual download logs certify bytes. Avoid treating the existence of URLs, GitHub repositories, or a ZIP folder named `raw` as evidence of acquisition. Stop after reasonable bounded retries; print exact missing records for human continuation instead of promising unlimited background downloads. The run can be resumed after the external availability or source evidence improves.

## 4. Actual OSM pedestrian network: 12-city geometry, topology, origin–destination proof

Start from actual TIGER place polygons (project with EPSG:5070 to buffer 3.5–4 km in real metres), not city names or coarse city centroid rectangles. Download/parse beyond municipal administrative borders so that service catchments can genuinely cross them. Source snapshot vintage of OSM PBF or Overpass query date is **recorded separately** from Census 2024. A `2026-latest` OSM graph cannot be called an actual 2024 historical street graph.

**Native geometry sequence:** TIGER PLACE ZIP → unique 7-digit GEOID city polygon → 2024 tract TIFF? **No:** use TIGER `TRACT` shapefile, intersect with city polygon → 2024 ACS 15–17 estimated population weighted by area fraction → one actual inside-city representative tract origin → walkable `OSM` road graph + true graph nodes/edges → snapped origin and candidate facilities → Dijkstra network distance → 10/20/30-minute opportunity values. Any claim about precise residence address, park access gateway, admission or travel reliability remains unobserved.

For every one of the 12 cities save: original raw Overpass cache `.json` responses with SHA256 **or** one referenced original state Geofabrik `.pbf` (SHA256, source URL and source timestamp), derived `.graphml` (SHA256), full graph node/edge counts, CRS, speed and cutoff settings, nearest-node snap distance distribution, actual observed POI list with OSM IDs/access tags, tract origins, gzipped OD route pairs, per-tract computed facilities, and one per-city receipt. No synthetic network, no bird-flight time formula, no fabricated bus feed.

**Walk model:** edge cost is measured network distance in metres and pedestrian time is `distance / 1.25 m/s` in the frozen reference case. Re-evaluate alternative reasonable speeds as separate scenarios. Respect graph direction and any actual legal foot access restrictions; directed disconnected reaches are `unreachable`, not zero-minute access. Project geometries before KD-tree node snapping. Fail graph QA if network tiny, implausible lengths, missing actual libraries/parks, excessive snap distances, no tract populations or missing original response/PBF. A public facility point is a *potential opportunity* until opening hours, entry constraints and gate points are verified.

**Important park entrance caveat:** an OSM park polygon's `boundary.representative_point()` is only a geometric **boundary-access proxy**, not evidence of a public entrance. Never call an OSM point a validated gate unless an observed `entrance=*` point or official local park-access record supports it. All such entries are labeled in `poi_osm_*.csv`; quantify how exclusions or assumptions could change accessibility. Document duplicate park geometries and point POIs separately; do not double-count the same mapped park and its centroid as two opportunities.

**Conditional fallback route:** first OSMnx/Overpass, next full state-level Geofabrik/PBF + Pyrosm. On one city failing, continue only in controlled recovery attempts; do not publish ten cities under an unannounced changed sample. To maintain the fixed 12-city reference main model, require **all 12 valid graphs**. Network retry does not imply scheduler or cloud task automation; human reruns commands after addressing failures.

## 5. Spatial demography, time alignment and scientific error accounting

Age 15–17 proxy: for tract $g$, $n_g=\mathrm{B01001}_{E006,g}+\mathrm{B01001}_{E030,g}$; record both marginal $M006/M030$ and whether the sum's MOE treatment conservatively bounds unknown covariance. If actual official target 14–18 values cannot be observed at comparable tract granularity, label the age-proxy limitation and test reasonable scenarios rather than inventing enrollment counts. **Never treat the 15–17 estimate as an exact 14–18 population.**

For a tract intersecting a city boundary, $n_{gc}=n_g\cdot A(g\cap c)/A(g)$ using EPSG:5070 projected area; $\sum_c n_{gc}$ need not equal actual city census counts because area interpolation assumes locally uniform density within the source tract. The difference must be assessed and reported. City inputs and raw source universes must use 2024 ACS five-year common vintage; do not merge a Census 2025 one-year estimate into the main 2024 five-year score without a separately disclosed scenario and modified uncertainty treatment.

`B25070` housing burden: $r_c=(E007+E008+E009+E010)/(E001-E011)$; numerator represents household gross-rent burden at or above 30% **among computed cases**, not the fraction of all students paying rent. `B17001`: $p_c=E002/E001$ citywide population below poverty in table universe. `B28002`: $b_c=E004/E001$ broadband-of-any-type household subscription, **not** E002 and not individual teenage broadband access. All three are environmental proxies, not actual youth welfare outcome measures.

**Uncertainty ledgers must remain separate:**

| Channel | Source of uncertainty | Auditable treatment | Prohibited inference |
|---|---|---|---|
| ACS sample | Census published marginal 90% MOE | `uncertainty_envelopes.py` propagates numerator/denominator worst-case endpoint ranges into M0 and M1 | The resulting simultaneous bounds are not a 90% joint confidence interval |
| Spatial allocation | Tract area share, representative origin, MAUP | stratified sensitivity of geographies, origins and missing tracts; compare place youth totals | Exact house-to-road travel observed |
| OSM geometry | missing roads, direction, fragmented graph, feature duplication | network coverage, snap errors, compare TIGER all-roads as a cartographic *crosscheck* | TIGER all-roads proves foot access |
| Eligibility | park gates, fees, hours, public access | evidence-based access tags and lower/upper opportunity scenarios; never silently set unknown=true | modelled proximity proves actual participation |
| Normative model | score anchors, dimension weights, fairness preference and cutoff | 27 actual recomputed scenarios plus explicit alternative bottleneck operator | rank frequencies are population preferences or frequentist confidence |
| Temporal | mixed ACS 2020–2024 and OSM acquisition snapshot | label two vintages in every figure and caveat | cross-sectional correlation proves dynamic feedback |

## 6. Mathematical spine, actual testable properties and the main model revision

**M0: household-context baseline** is a transparent fixed normative scoring rule (model definitions are decisions, not discoveries):

\[
\begin{aligned}
 u_r &= \operatorname{clip}((0.80-r_c)/0.60,0,1),\\
 u_p &= \operatorname{clip}((0.35-p_c)/0.35,0,1),\\
 u_b &= \operatorname{clip}((b_c-0.60)/0.40,0,1),\\
 M_0(c) &= 100(0.35u_r+0.35u_p+0.30u_b).
\end{aligned}
\]

For true pedestrian routes and facilities, with reference $v=1.25$ m/s, cutoff $T=20$ min, and exponential decay constant $\tau=12$ min:

\[
 t_{gj}=\ell_{gj}^{\mathrm{network}}/v,
 \quad K_{gjk}=\mathbf1\{j\in k,t_{gj}\le 60T\}\exp[-t_{gj}/(60\tau)],
 \quad A_{gk}=\sum_jK_{gjk}.
\]

An opportunity candidate is *not* a youth attendance probability. With $k=L$ (libraries) and $P$ (parks), let $U_{gk}=1-e^{-A_{gk}/2}$ and $a_g=0.55U_{gL}+0.45U_{gP}$. Let $\bar a_c=\sum_gn_ga_g/\sum_gn_g$, $Q_{0.1,c}$ the weighted lower 10% quantile of $a_g$ across tracts (not a 10% bootstrap confidence interval), and $V_c=0.75\bar a_c+0.25Q_{0.1,c}$. The final frozen reference score is

\[
 \boxed{M_1(c)=0.60M_0(c)+40V_c}
\]

Because $M_0\in[0,100]$ and $V\in[0,1]$, $M_1\in[0,100]$. The revision changes the mathematical object by introducing genuine route-limited spatial opportunity, population weighting and a lower-decile equity component; it is **not** merely retuning weights. Still, its predictive/external *merit* must be demonstrated separately; a changed winner is not evidence of increased empirical validity.

M2 is a **robustness/decision layer** over M1, not a third selectively marketed trophy ranking. For 3 cutoff values `10/20/30 min` × 3 ACS share weights `0.50/0.60/0.70` × 3 fairness weights `0/0.25/0.50`, actually recompute all 12 cities = **324 score rows** and exactly 27 full rank permutations. Scenario champion frequency $\hat p_c=(1/27)\sum_{s=1}^{27}\mathbf1\{c\mbox{ ranks first in }s\}$ has the interpretation **share of specified finite preference scenarios**, not a posterior probability or a human preference sample. Use stable tie-breaking. Compare rank confidence only when a valid sampling/measurement design warrants it.

Proof obligations for validation: (i) M0 bound and monotonicity; (ii) increasing travel distance cannot increase feasible $K$, conditional on fixed eligibility; (iii) adding a verified reachable facility cannot reduce raw $A$; (iv) adding an unreachable facility leaves $A$ unchanged; (v) weighted accessibility remains in domain; (vi) no prohibited division-by-zero; (vii) rank permutation exactly 1…12 for each of 27 scenarios; (viii) both marginal ACS MOE and missing network snap perturbations recorded; (ix) source version changes cause re-computation; (x) final English Summary, table, figures and news article all use the same released score CSV.

## 7. The eight systems principles become falsifiable empirical science

Use the `8-4-2` conception as a **study-specific organizing heuristic**, not a claim that an uncontested set of eight universal laws exists. Key implementation is in `code_v18/systems_hypothesis_tests.py`, generating `results_v18/SYSTEMS_THEORY_EMPIRICAL_TESTS.csv`, `H3_CROSS_BOUNDARY_SERVICE_FLOW.csv`, `H4_COMPLEMENTARITY_BOTTLENECK.csv` and independent receipts. Use only observed inputs; for unidentifiable principles report `NOT_IDENTIFIABLE` instead of decorating the paper with unsupported jargon.

| Systems principle | Observable / falsifiable operating hypothesis | Actual source-linked computation | Interpretation boundary |
|---|---|---|---|
| **目的性 Purpose** | a youth-relevant metric set differs from adult commuting/diploma prestige | age 15–17 proxy; remove adult-only indicators; compare M0 and feature choice | normative age fit ≠ observed teen preference |
| **整体性 Holism** | resource access can be bottlenecked when only one channel is available | additive $0.55U_L+0.45U_P$ versus $\sqrt{U_LU_P}$ with same measured inputs | geometric mean is a policy operator, not empirical proof of synergy |
| **层次性 Hierarchy** | city mean conceals tract disparity | population-weighted $\bar a$, weighted $Q10$, gap and choropleth | tract representative points are proxies for residents |
| **开放性 Openness** | reachable opportunities and services cross city borders | GIS classify OSM facilities vs TIGER city polygon; report share of actual decay-weighted route-pair contributions outside city | this particular share is route-pair weighted, **not** population-weighted |
| **突变性 Threshold behavior** | 10/20/30 min constraints can sharply remove opportunities | 27 real parameter scenarios and cutoff rank changes | change at a policy threshold is not a physical phase transition |
| **稳定性 Stability** | cities' access structure persists under time-varying shocks | cross-year panel only if multiple actual historical graphs and comparable data are supplied | one mixed-vintage cross-section: **NOT IDENTIFIABLE** |
| **自组织性 Self-organization** | local youth groups create endogenous opportunities | only testable with repeated observed real social/club network data | currently **NOT IDENTIFIABLE**; do not fabricate mechanism |
| **相似性 Similarity/transfer** | score structure applies to comparable held-out cities | optional independent cities with frozen definitions and new original data | current selected 12 do not prove general national representativeness |

The systems loop represented in the Introduction graphic is a **research feedback cycle** (diagnose empirical error, revise model, re-run, test counterexamples), not a measured causal feedback mechanism in students or cities. To claim self-regulation/dynamic stability, specify a temporally indexed state transition model and obtain repeated measurements first.

## 8. High-level rigorous empirical tests beyond a pretty leaderboard

All tests must be computed from frozen, genuinely obtained inputs. At a minimum run:

1. **Base quality:** source byte lengths/SHA, ACS variable and GEOID integrity, polygon validity, CRS, duplicate POIs, graph edge costs, snap-error extremes, dataset timestamp and source citation.
2. **All-city complete M0/M1 rerun:** same 12 population/period/geometry, frozen anchors, clear champion and 12-row rank output; no selective replacement city.
3. **Model revision audit:** M0→M1 all-city delta ranks, Kendall τ and Spearman ρ, a citypair explanatory case and ablation of network access and fairness. A change in ordering is necessary to understand the revision, not proof of objective correctness.
4. **GIS external audit:** source-snapshot crosschecks, optionally Census county all-roads and official IMLS FY2024 library outlets / NCES 2024–25 school directory as independent facility-coverage comparators. These sources require real downloaded bytes and version/coverage checks; they are not silently added to the main score without common nationwide data and eligibility evidence.
5. **Target-population error:** tract area interpolation and school-age proxy denominators compared to ACS municipal controls. Document observations that cannot be mapped (including OSM disconnected segments) and the consequences for cities at risk of score reversal.
6. **Spatial fairness:** tract Q10, population-weighted city mean, mean-minus-Q10 and within-city geographic dot/choropleth showing real tract boundaries and graph access scores; labels distinguish tracts from individuals.
7. **Cross-border openness:** share of real 20-minute route-pair facility contributions lying outside city polygon; boundary spillovers demonstrate system permeability and make them nontrivial to count.
8. **Conservative ACS sampling stress:** use each needed 2024 ACS `E` and matching `M` fields to generate numerator/denominator ratio bounds; propagate to M0/M1; label endpoint ranges as **stress envelopes, not a simultaneous confidence interval**.
9. **27 actual preference and structural scenarios:** 324 row matrix, champion changes, spatial non-compensatory alternatives, no invented posterior probabilities.
10. **Counterfactual limits:** no real teen happiness/educational-attainment outcome data implies no causal effect and no objectively universally best city. Document failed hypotheses and weak external validity.

The source-backed city ranking is only the **reference** under frozen preferences. A family whose priority is disability access, school-district eligibility, rental availability, safety, special needs or mass transit must not be told that the top city in this limited model is universally best for them.

## 9. Production scientific visualization: 10+ figure evidence atlas

`code_v18/render_atlas.py` is an **evidence-gated** graphics producer. The figure outputs are not generated or fabricated before the requisite actual data exist. On full successful execution it generates vector PDF and SVG plus high-resolution PNG as appropriate, with a `figure_manifest.json` linking every published figure to the SHA256 of the final ranking file and its own exported PDF hash. A graph of concepts may be drafted before the run, but numerical and map figures cannot be presented as completed until their evidence is available.

| Figure | Research question | Form and exact source |
|---|---|---|
| F18-01 | Who leads the frozen reference? | ordered horizontal bar, exact 12-city M1 values from audited CSV |
| F18-02 | Was model revision substantive? | 12-city M0→M1 slopegraph showing every actual change |
| F18-03 | Do Census sampling errors challenge the conclusion? | bound whiskers using genuine official ACS `M` field calculations; **not confidence intervals** |
| F18-04 | When does each city lead under different preferences? | complete 12×27 rank-acceptability heatmap, exact scenario labels |
| F18-05 | Which type of public opportunity drives observed differences? | library vs park population-weighted score comparison |
| F18-06 | Where do the worse-served tracts hide behind averages? | city mean vs weighted tenth-percentile dumbbell chart |
| F18-07 | Is GIS based on actual streets, or hand-drawn proximity? | Austin real Census boundaries, actual OSM street graph, real POIs and tract origins, actual scoring; projected geometry |
| F18-08 | Can every claimed result be traced backwards? | source→spatial transforms→M0/M1→QA/uncertainty→paper architecture, deterministic Graphviz DOT+SVG+PDF |
| F18-09 | How open are municipal service areas? | ranked cross-city-boundary decay-weighted route-pair contributions |
| F18-10 | Is a single excellent opportunity type masking weakness elsewhere? | additive vs geometric-complementarity small scatter using real city components |

**Scientific graphic house rules:** PLOS/Nature-style restrained visual language rather than decorative infographics; each figure has a clear analytical question, readable direct labels, meaningful baseline/units, uncertainty definition, consistent city order/colour, colorblind-safe and grayscale-distinguishable visual channels, true coordinate reference, credible geographic scale and source vintage. Render all streets from actual GraphML. The only valid map coordinate values are from traceable TIGER/OSM data; a schematic flowchart is not a geospatial map. Never use unlicensed satellite tiles, fictional gates, decorative heat maps or fabricated contours. Graphviz/TikZ is for conceptual system diagrams, not street geometry. Labels need legibility at printed page size and no obstruction or clipping.

For the final 25-page manuscript include the **highest-impact 3–5 figures** selected for argumentative economy; retain the rest as reproducibility/technical appendix and high-quality standalone research atlas, rather than clogging the main paper with 10 decorative figures. Page count and format must be verified on the actually compiled PDF.

## 10. Submission-grade English scientific paper: write from results, not from wishes

The generated target is a **publication-grade independent research paper**, written after real ranks and graphs are available. It is not official COMAP submission without valid team registration and independent competition compliance; none is claimed. Use `code_v18/build_empirical_gis_paper.py` and `code_v18/release_audit.py` after all upstream audits; no synthetic data or manually composed champion is permitted. Sources and corresponding code/receipt IDs must be cited for every quantitative result. Ensure the scholarly narrative does not overstate the link between potential facility access and actual teen welfare.

**Suggested reading order (≤25-page solution where practical, not forced padding):**

1. **One-page research Summary** with actual champion/score, 12 cities, time/vintage, measurable definition, explicit revision, most important robust conclusion and one failure/conditionality statement.
2. **Contents and Introduction** with one professional systems-and-evidence architecture, no hollow history of systems-theory authors and no fake feedback loop measurement.
3. **Problem analysis and indicator choices**, 14–18 target vs ACS 15–17 proxy, facility eligibility, exclusions, prior city sample, known alternative plausible values.
4. **Data & GIS methods**, exact source provenance, 4 ACS DAT + 24 TIGER ZIP + 12 OSM originals, MOEs, geographies, buffer, network, snap error, city/tract geometry.
5. **M0 analytical definition and diagnosis**, all physical units and frozen normative score anchors.
6. **M1 mathematical derivation and substantive revision**, true route length, exponential kernel, bounded facility type utility, population weighting, lower decile, proof of key monotonic properties and empirical mechanism.
7. **Actual 12-city results** and full comparison table with exact references, real Austin map and spatial equity case, unambiguous conditional reference winner.
8. **Independent verification, model comparison and falsification**, source-asset hashes, Kendall τ and rank changes, precision limitations, 27 scenarios, ACS sampling stress, systems principles tested/not identifiable.
9. **Limitations and defensible improvements**, historical vintage mismatch, OSM data completeness, park gates/eligibility, schools, socioeconomic construct, spatial resolution and noncausal interpretation.
10. **Conclusion and 1–2 page nontechnical news article**, exact same champion, score, assumptions, major revision effect and weak points as Summary.
11. **Full references and honest AI-use statement** describing actual model/code/figure/drafting assistance, not a generic fictitious disclosure.

All tables and captions should be produced by programs from the same frozen result object. The summary is written last. A valid TeX bundle is not sufficient: actually compile the PDF, audit page count, readable font size, source/caption consistency, render quality, no unintentional clipping, abstract/table/news cross-consistency, and source DOI/URL validity. V18's automated PDF gate returns `TECHNICAL_PRECHECK_PASS_HUMAN_SCIENCE_REVIEW_PENDING` at most, never claims a human or official reviewer accepted the paper. If an unexpected class/package or LaTeX template issue occurs, repair and recompile; do not delete substantive sections to hide the issue.

## 11. Single-command deterministic workflow and exact release files

Human operator opens `README_START_V18.md` and runs one of these commands after installing Python 3.11/compatible native GIS wheels, Graphviz and LaTeX. Use appropriate bandwidth and disk budget. OSM data may require gigabytes, especially on Geofabrik fallback for California and Texas; do not try to fetch all USA if only 12 cities are needed.

```bash
# Linux or macOS
bash code_v18/run_v18_linux_macos.sh

# All operating systems, after dependencies installed
python code_v18/run_v18.py --stage all --network auto

# Lightweight no-network command inspection
python code_v18/run_v18.py --dry-run

# Full offline unit tests before data acquisition
PYTHONPATH=code_v18 python -m pytest -q tests_v18

# Optional independent official Census county-roads acquisition (not pedestrian routing)
python code_v18/run_v18.py --stage census_streets
```

In Windows PowerShell, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\code_v18\run_v18_windows.ps1
```

When direct TLS download fails but human has downloaded the exact official originals:

```bash
python code_v18/run_v18.py --stage all --import-dir /path/to/original_files --attestation-dir /path/to/reviewed_source_receipts --allow-attested-origin
```

This human-attested branch explicitly needs actual source records and actual reviewer signoff. It cannot be triggered by putting a ZIP in a folder or inventing checksums. Standalone code cannot prove the authenticity of an externally supplied file unless a trusted publisher hash or trustworthy provenance chain is provided. In the official acquisition run, the direct TLS source + generated SHA256 is its evidence mechanism.

**Phase states in `qa_v18/v18_execution_state.json`:** `tests` → `census` → `geography` → `networks` → `score` → `audit` → `sensitivity` → `uncertainty` → `systems` → `figures` → `atlas` → `paper` → `release`. Every phase must actually exit zero. Any phase failure sets `BLOCKED_FOR_FINAL_GIS_PAPER` with logs; no text instruction may overwrite this state.

**Mandatory post-run file proofs (not pre-created empty placeholders):**

```text
qa_v18/census_original_manifest.json            # 28 actual Census source records, true SHA256 and verified schema
qa_v18/full_gis_qa.json                       # independent 12-city graph/CSV/source-hash audit
qa_v18/v18_execution_state.json               # actual run gates, not planning checklist
data/raw_official/v18/acs_2024_5y_*.dat        # actual full Census original table bytes
data/raw_official/v18/tl_2024_*.zip            # actual 24 place and tract TIGER originals
data/raw_osm/v18/cache/...                     # actual Overpass JSON response originals OR
data/raw_osm/v18_geofabrik/*.osm.pbf           # actual Geofabrik originals
data/raw_osm/v18/graphml/*.graphml             # 12 actual derived walking graphs, plus hashes
data/processed/v18_network/walk_pairs_*.csv.gz # actual directed network OD route lengths
results_v18_gis/FINAL_12_CITY_REAL_GIS_RANKING.csv
results_v18_gis/REAL_GIS_27_SCENARIOS.csv       # exactly 324 actual score rows
results_v18_gis/V18_ACS_MOE_STRESS_ENVELOPES.csv
results_v18/SYSTEMS_THEORY_EMPIRICAL_TESTS.csv
figures/v18_real_gis_atlas/figure_manifest.json  # ≥10 rendered empirical figures and hashes
paper_v18_official_gis/V18_EMPIRICAL_YOUTH_CITY_NETWORK_RESEARCH.tex
paper_v18_official_gis/V18_EMPIRICAL_YOUTH_CITY_NETWORK_RESEARCH.pdf
qa_v18/final_release_audit.json
```

The final response of a subsequently executing AI must report **not only downloadable filenames but actually observed n=12, exact champion and score, most influential revision, robustness conditions, published MOE stress envelopes, systems tests and actual SHA256 evidence**. If official originals or OSM graph evidence are absent, output the exact acquisition/coverage blockers and all legitimate existing research outputs. Never change the fixed scoring definitions or sample secretly to force a desired champion.

## 12. Professional engineering: frozen environment, defensive execution, and reproducibility

The delivered code includes `requirements_v18.txt`, conda-forge `environment.yml`, cross-platform launchers, `Dockerfile`, unit tests, a source attestation template and a separate release auditor. Record the actual execution environment with `python -V`, installed package versions, Pyrosm/OSMnx version, GDAL/PROJ version, `dot -V`, `latexmk -v`, operating system, and actual source URLs and retrieval times; for reproducibility freeze dependency versions and model config at run time. Never silently change an old source hash: any new download or corrected code requires a fresh run ID and score refresh.

The official acquisition module requires the `all_pass` gate for *all 28 official originals* including source origin and real schema. The B28002 variable is corrected from any-internet `E002` to broadband `E004`. V18 score and PDF must be computed from actual 2024 raw bytes; no earlier rankings may be carried forward by renaming CSVs.

No external credentials, Census API keys, private institutional assets or copyrighted images are bundled. Optional public-data endpoints are not proof of retrieval. Protect large-file downloads with bounded retries and disk checks, respect human/supplier usage terms and preserve original source notice and OSM ODbL attribution. If a legally obtained proprietary access dataset cannot be redistributed, archive its metadata, original SHA and a permitted recreation route rather than unlawfully redistributing the byte stream.

## 13. Independent release gates, manual peer critique and explicit no-success shortcuts

- **RG-01 Originality**: precisely 28 actual 2024 official Census original files or explicit human-attested copies, all byte SHA256 + schema and 12-city GEOID checks passed. A 12-row scraped CSV is insufficient.
- **RG-02 Geometry**: official 2024 city/tract shapefiles intersect with expected GEOIDs; age 15–17 tract proxy coverage and area interpolation included, not hidden.
- **RG-03 Walking route**: all 12 actual graph files and raw source caches/PBF with SHA; roads are connected enough to reach sampled facilities and graph monotonicity/snap validated. Straight line is never titled a travel-time isochrone.
- **RG-04 Score**: actual `FINAL_12_CITY_REAL_GIS_RANKING.csv` has 12 unique geoid rows, no invalid scores, one stable complete M1 rank permutation and explicit conditional reference champion.
- **RG-05 Systems evidence**: actual 8-principle hypothesis registry, including honestly unidentifiable dynamics/self-organization, measured cross-border spillovers and tract equity.
- **RG-06 Statistical evidence**: actual 27 scenarios, 324 rows, marginal ACS MOE stress endpoints, direction and denominator consistency, independent negative results when applicable.
- **RG-07 Visual evidence**: ten source-backed atlas figures and hash manifest, with accurate geographic CRS and legend; paper uses authentic maps, not aesthetics in lieu of data.
- **RG-08 English argument**: numbered formulas in narrative, justified data choices, M0→M1 revision, complete 12-city conclusions, model sensitivity, genuine limitations, citations, one-page summary, 1–2 page lay article, compiled final PDF.
- **RG-09 Independent code replay**: at least two computational paths or clean-environment rerun of scores, plus file checksum comparison. Unit tests cannot substitute actual source audit.
- **RG-10 Human review**: source provenance and scientific construct validity, licensing, map accuracy, potential eligibility issues and writing claims checked by a real reviewer; no “simulated peer review” signed as an actual outside expert.

Only RG-01–RG-09 machine verifiability plus final human review can justify calling the completed PDF a release-quality **independent paper**. `qa_v18/final_release_audit.json` may say `TECHNICAL_PRECHECK_PASS_HUMAN_SCIENCE_REVIEW_PENDING` after actual machine checks. It may not say peer-reviewed, official COMAP-approved, uploaded or accepted when those things did not happen.

### Verified scholarly/technical entrypoints (consult actual version and license before executing)

- Census 2024 ACS Table-Based Summary File and user guide: https://www.census.gov/programs-surveys/acs/data/summary-file.2024.html ; https://www.census.gov/programs-surveys/acs/data/summary-file/getting-started.html
- Census 2024 original table directory: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/
- Census 2024 TIGER/Line place, tract and county-road file interface: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
- ACS B28002 variable and annotation definition: https://api.census.gov/data/2024/acs/acs5/groups/B28002.html
- OpenStreetMap contributor license and attribution: https://www.openstreetmap.org/copyright
- Geofabrik United States source directory and state extracts: https://download.geofabrik.de/north-america/us.html
- OSMnx 2 API: https://osmnx.readthedocs.io/
- Pyrosm PBF network parser and download methods: https://pyrosm.readthedocs.io/en/latest/reference.html ; https://pyrosm.readthedocs.io/en/latest/downloading_data.html
- Optional independent site validation: IMLS PLS https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls ; NCES CCD https://nces.ed.gov/ccd/files.asp ; ParkServe https://www.tpl.org/park-data-downloads

**Final document metadata:** `V18_OPERATIONAL_DIRECTIVE_PREPARED` — independent 12-city research, official-byte/GIS mandatory data gates, cross-platform reproducible source. Requires future real execution to become `V18_EMPIRICAL_GIS_RESEARCH_COMPLETE`.

---

# 15 — V18.2 OFFICIAL OPTIONAL PAPER LAYOUT INTEGRATION / 论文结构、短文件与参考文献终版门禁

> **增量版本：V18.2（2026-11-07）。** 本章专门落实用户提供的官方 `Optional Paper Layout` 原文。它不改变 V18 的真实数据、数学、GIS、系统论、科研绘图和发布硬闸；它只把正式论文的组织顺序、短文件归档、参考文献和PDF版式变成可执行合同。
>
> **官方原文的关键限定词是 Optional。** 官方说明完整解答“may be organized as follows”，并明确允许团队根据解法和表达方式调整。因此本项目选择严格采用推荐顺序作为默认排版，不把“Optional Paper Layout”错误升级为另一条不可调整的独立竞赛规则。若题目本身或当届规则要求不同，先服从题目/当届规则并记录理由。

## 15.0 官方原文（用户提供，按原文保留）

> Optional Paper Layout. In general, a complete solution submission may be organized as follows. Teams are welcome to adjust their submission format to meet the needs of their solution method and communication style.
>
> - Summary Sheet – Write this summary after you have done all your work. This one-page summary is Page #1 of your solution document. It provides an overview of your work, including the problem, your approach, and actual results.
> - Table of Contents – List the major items in your solution document to show the organization of your paper.
> - Introduction and Restatement of the Problem – Introduce the problem. Restate the problem and requirements in your own words.
> - Assumptions with Justifications – State any assumptions you made to simplify and solve the problem and state why you made those assumptions.
> - Presentation of Model and Solution – Ensure you address all requirements and describe what you are doing in solving the problem. Show and explain all your work, especially the model you created or selected and why. How it was applied. Use representations that help you tell the reader how you solved the problem (for example: equations, tables, graphs, pictures, etc.).
> - Analysis of Your Work – Describe the implication of your work. Perform a sensitivity, which means to adjust or remove an assumption to see its impact on the result. Address any strengths (good points) and limitations (weaknesses) of your model and solution.
> - Concluding Paragraph – End your solution paper with a final concluding paragraph that summarizes your results and/or makes recommendations for future work.
> - Include all 1-2 page documents and memos, if not already included earlier.
> - Reference List – List any sources that you used to solve the problem (for example: websites, AI tools, scientific, newspaper or magazine articles, etc.).

## 15.1 唯一默认论文顺序

V18.2 生成的英文论文必须按以下顺序组织：

1. **Summary Sheet** — 一页，PDF第1页。必须在全部工作完成后最后撰写，内容概括问题、方法和真实结果。
2. **Table of Contents** — 紧接Summary Sheet，PDF第2页开始；目录可占一页以上，页码必须来自最终编译结果。
3. **Introduction and Restatement of the Problem** — 介绍问题，并用作者自己的语言重述题目及要求。
4. **Assumptions with Justifications** — 逐项列出假设及采用理由；每项假设还须说明其影响、边界和对应敏感性/反证测试。
5. **Presentation of Model and Solution** — 完整呈现数据、模型、数学公式、求解步骤、应用过程、实际结果、表格、地图和图形；不得只介绍工具而不回答题目。
6. **Analysis of Your Work** — 解释结果含义，开展敏感性分析，说明调整或移除假设后的影响，并讨论模型优势与局限。
7. **Concluding Paragraph** — 以一个清晰的最终结论段落收束主解答，概括结果并提出有证据边界的未来工作建议。
8. **Supplementary 1–2 Page Documents and Memos** — 所有未在前文纳入的1–2页文件/备忘录集中放置。A题要求的非技术新闻稿作为第一份补充文件；其他必要短文件不得遗漏。
9. **Reference List** — 参考文献是主论文的最后一个主要章节，列出实际使用过的全部来源。

不得增加独立封面页而把Summary Sheet推到第2页；Summary Sheet必须是整份解答PDF的第一页。若Summary Sheet内容溢出，必须压缩或重写摘要，而不能把溢出部分当作正文继续占页。

## 15.2 Summary Sheet事实合同

Summary Sheet必须在所有模型、排名、稳健性和限制分析完成之后生成。它必须从冻结的最终结果对象读取事实，至少包括：

- **Problem**：研究的问题、年龄范围及城市比较对象；
- **Approach**：真实数据来源、M0→M1实质性修订及核心计算机制；
- **Actual results**：实际城市数量、真实冠军、得分、关键名次变化和实际敏感性结果；
- **Conclusion and limits**：冠军适用的条件、重要限制及不可声称的因果结论。

所有数值必须由同一个冻结的`FINAL_12_CITY_REAL_GIS_RANKING.csv`、场景结果和证据清单生成；Summary、正文、新闻稿不得人工重抄并各自维护不同数字。没有真实最终排名时，不生成含虚构冠军的Summary；论文生成器应继续保持`BLOCKED_FOR_FINAL_GIS_PAPER`。

## 15.3 Assumptions with Justifications 必须独立成章

V18.2 将假设从零散的模型说明中抽出，独立形成A1–A10表。每行至少包含：`Assumption ID / Assumption / Why it is reasonable / Consequence and test`。默认覆盖：

- 预先冻结的12城目的性样本及其外推限制；
- ACS 15–17岁作为14–18岁目标的代理；
- tract与市界相交时的人口面积加权近似；
- 步行速度和10/20/30分钟时间阈值；
- 路网快照时间与ACS年份不一致；
- 图书馆、公园点位仅是候选机会，不等于准入/开放/安全；
- M0固定归一化锚点及维度权重；
- M1城市条件、机会、图书馆/公园、均值/低分位的偏好权重；
- 不虚构学校录取资格、设施容量或实际参与概率；
- 横截面数据不能识别长期稳定性、内生自组织或因果福利。

假设值应从`config_v18/reference_model_v18.json`读取，而不是在论文生成器中另写一套数值。对可扰动假设，必须链接到实际执行的敏感性结果；不能扰动的假设应解释为什么当前数据不能检验。

## 15.4 Presentation of Model and Solution 的内容边界

该章将数据与模型组织成一条连续的解题论证：

1. 原始数据、版本、时间、空间口径、SHA256及质量筛查；
2. Census/TIGER与OSM真实空间对象的连接方式；
3. M0基线定义、归一化、权重和单位；
4. M1网络可达性、人口加权、设施类型和公平项的数学定义与推导；
5. Austin真实GIS案例和必要的其他实证案例；
6. 12城完整实际排名、分数和M0/M1对照；
7. 关键公式的适用条件、计算步骤、性质测试和结果解释。

不能将研究工程说明、依赖安装清单、GitHub仓库列表或概念系统图替代实际求解。每个定量主张仍必须回溯到原始文件、计算run、代码版本、表格和图形。

## 15.5 Analysis of Your Work 必须同时报告正反证据

本章至少包括：

- 为什么M0不足、M1究竟改变了什么，以及是否有实证证据支持此次修订；
- 算法验证、独立数值复算、空间与数据质量验证之间的区别；
- 真实运行的27组情景、ACS MOE压力区间及模型结构/路网误差；
- 系统论原则中哪些被实际计算检验，哪些因缺少纵向或个体数据而不可识别；
- 模型优势、数据优势、适用边界和主要弱点；
- 负结果、冠军翻转条件和不能从横截面排名推断的事项；
- 实际使用的AI工具和软件的透明披露。

不得把情景频率写成置信概率或公众偏好；不得把“可达机会”写成实际参加、学校录取或因果改善。

## 15.6 Concluding Paragraph 必须是主解答的最后一个结论段

主解答以一个结论段落结束。它应当：

- 明确指出在冻结条件下的实际排名结论；
- 解释这个结论适用于哪些样本、指标、年份和偏好；
- 指出最重要的限制；
- 提出下一步最有价值的实证工作。

不要在结论之后继续添加新的主模型、主要结果或一串没有层级的未来工作清单。补充新闻稿/备忘录属于官方布局中的独立短文件，放在结论之后、参考文献之前。

## 15.7 所有1–2页文件和备忘录的注册机制

新增目录：`paper_supplemental/`，主清单：`paper_supplemental/manifest.json`。

- 自动生成的`Nontechnical News Article`是第一份补充文件；
- 任何其他尚未在主文中纳入的1–2页文件或memo，必须保存为`.tex`并在manifest中登记`id,title,path,pages_min=1,pages_max=2`；
- 未登记的`.tex`文件会阻止论文编译，避免遗漏；
- 生成PDF后，逐份核验其实际页数必须为1或2页；
- 所有补充文件都必须位于最终Reference List之前。

如果某份memo已经在正文完整纳入，则不得再重复插入；清单需说明其已在正文中，不重复计页。当前默认manifest为空，因为除自动新闻稿外尚无其他已确认必须插入的独立memo；后续执行时如产生，必须登记。

## 15.8 Reference List 必须是最后一个主要章节

Reference List列出实际使用的来源，不按类别机械凑数。根据实际使用情况包括：

- 官方数据集和政府网站（Census ACS、TIGER等）；
- OSM/Geofabrik等实际使用的地图与数据服务；
- 学术论文、理论著作、方法手册；
- 实际运行的软件/程序文档；
- 实际使用的AI工具及其模型/版本、访问日期和用途；
- 若真正引用过新闻或杂志文章，则列入；未使用则不虚构。

新增`sources/ai_tool_use_ledger.csv`记录本项目已发生的AI工具使用；新增`sources/additional_references.csv`记录实际使用的其他网站、数据集、学术论文、新闻或杂志来源。未来执行者必须将新增AI工具、模型、版本、用途、日期及其他实际来源继续登记；未实际使用的候选来源不得进入Reference List。AI工具在Reference List中的引用不取代单独的AI使用披露；若适用的当届竞赛政策要求单独AI报告，应作为独立合规附件处理，不得把它伪装成主论文的References章节。

Reference List之后不得再出现新的主论文章节。若赛事另要求AI合规报告，该报告属于独立合规材料，不改变主论文以Reference List结束的结构。

## 15.9 V18.2代码与自动版式验收

新增/修改以下文件：

- `code_v18/paper_layout_contract.py`：同时检查TeX源结构与编译PDF；
- `code_v18/build_empirical_gis_paper.py`：按官方可选布局重新组织论文，生成Summary Sheet、TOC、Assumptions表、模型与结果、Analysis、单段Conclusion、新闻稿/补充文件和最终Reference List；
- `code_v18/release_audit.py`：将版式验收加入正式发布门禁，且检查审计收据与PDF SHA256一致；
- `code_v18/package_evidence.py`：把补充文件清单、AI工具账本和版式审计收据纳入复现包；
- `tests_v18/test_official_paper_layout.py`：对第一页、目录起始页、章节顺序、补充文件页数、参考文献位置进行合成PDF测试。

PDF自动门禁至少要求：

1. PDF第1页是唯一一页Summary Sheet，包含Problem/Approach/Actual results；
2. Table of Contents从PDF第2页开始；
3. 主要章节按上述顺序出现，允许两个章节标题在同一物理页，但不允许逻辑顺序颠倒；
4. 主结论是一个最终段落，之后才进入补充文件；
5. 每份补充文件实际占1–2页；
6. Reference List为TeX源中的最后一个主要章节；
7. PDF页数满足本项目另行核验的页数门禁；
8. TeX结构审计与PDF审计均通过，且收据SHA256绑定最终PDF。

**当前V18.2实际验证边界：** 使用合成PDF fixture完成了版式审计器测试，并对论文生成器进行了隔离的合成数据TeX smoke build；该临时目录已删除，绝不作为城市研究结果或正式论文交付。V18专属离线测试通过，说明相关代码与门禁通过合成测试；不表示Census原始数据、OSM路网或12城实证已经完成。

## 15.10 V18.2执行命令与发布状态

离线测试命令：

```bash
PYTHONPATH=code_v18 python -m pytest -q tests_v18
```

实际论文仍只能通过原V18完整流水线生成。任何Census、TIGER、OSM、GIS、独立复算或敏感性阶段失败，论文仍为`BLOCKED_FOR_FINAL_GIS_PAPER`；版式门禁不得绕过上游实证门禁。

V18.2状态：`OFFICIAL_OPTIONAL_LAYOUT_IMPLEMENTED_AND_SYNTHETICALLY_TESTED / EMPIRICAL_PAPER_NOT_EXECUTED`。

## 16 — V18 P0/P1 EVIDENCE-AND-VALIDITY REPAIR (AUTHORITATIVE ADDENDUM)

## 16 — V18 P0/P1 EVIDENCE-AND-VALIDITY REPAIR (AUTHORITATIVE ADDENDUM)

> **Authoritative correction to inherited directives (2026-11-09).** This V18-only source tree is the entire current research engine. Every existing rule above remains useful unless contradicted by the stricter empirical science and file contracts in this section. Version labels in the inherited narrative are historical context only; at runtime only `code_v18`, `tests_v18`, `config_v18`, `qa_v18` and `V18_*` output names are authoritative. No V11–V16 source folders or archives are required or included. This is a complete *runnable engineering source package*, not a claim that twelve-city public downloads or final GIS scores have already occurred.

### 16.1 Non-negotiable research identities and scientific truth

- Study: 2026 HiMCM Problem A; twelve fixed US incorporated places: Austin, Boston, Chicago, Denver, Madison, Minneapolis, Pittsburgh, Portland OR, Raleigh, San Diego, Seattle, Atlanta. Every place GEOID is a seven-character STRING, not an integer.
- Evidence: Four official 2024 ACS 5y table-based SF `.dat` originals (`B01001`, `B25070`, `B28002`, `B17001`), twelve 2024 TIGER PLACE ZIPs and twelve 2024 TIGER TRACT ZIPs (total **28 actual originals**), and twelve REAL OSM walkable graph assets each traceable to hashed original Overpass JSON or state-level Geofabrik OSM PBF. Add IMLS FY2024 official outlet ZIP as independent verification and original COMAP summary template `.tex`.
- Census original SHA256 computed from actual bytes is a *local integrity and reproducibility fingerprint*, not publisher certification unless a published Census digest independently matches. Preserve official URL and TLS evidence; manually imported copies need separate human source attestation and should never be relabeled as direct publisher transfer.
- Geographic analysis is network-derived and sourced; TIGER ROADS is a secondary roads geometry crosscheck only, not validated pedestrian legality. Do not call park polygon representative points actual gates or inferred opportunities actual participation.
- `code_v18/run_v18.py --stage all --network auto` is the only all-stage orchestrator. It fails closed. Dry Run is not a successful research execution. Human can re-run after failed downloads and source validation.

### 16.2 P0-01/02: Mandatory dataset and full research-output gates

The rank gate MUST find 28 verified federal originals + appropriate age & geometry rows in the source files, plus 12 verified walked network graphs, verified raw OSM source bytes, and all source-recorded city/geography/POI/OD files. Disallow missing, zero-filled, copied historic final rankings, synthetic roads or maps. A source success requires file existence, valid structure, exact local SHA256, provenance, vintage, all 12 expected FIPS/GEOIDs, and quality checks.

The published machine result is `results_v18_gis/FINAL_12_CITY_REAL_GIS_RANKING.csv`, with exactly twelve distinct place GEOIDs and proper rank permutation. Other outputs (scenarios, figures, paper) MUST derive from the same frozen run. If any real original, route, downstream test or human-required attestation fails: `BLOCKED_FOR_FINAL_GIS_PAPER`. Do not export a fake champion. All 30 stages must exit zero and final release audit must explicitly authorize machine precheck before a PDF can be described as technically checked. Human peer review and COMAP registration are distinct.

### 16.3 P0-03: Controlled model revision that isolates *mechanisms*

The inherited household-context M0 does **not** include a facility inventory; its addition to M1 is both new data and a new spatial mechanism. Never call `M0 → M1` itself a causal proof that pedestrian routes outperform inventory. V18 introduces an explicit **same-facility-set counterfactual ladder** with source-aligned OSM entities and fixed denominators:

1. `M0_household` — Census rent-burden, poverty, broadband, no facilities (diagnostic only).
2. `P0_facility_inventory` — actual candidate counts for library/park facilities over the fixed study geography and administrative buffer; does not imply eligibility.
3. `P1_geodesic_proxy` — **the same eligible/candidate facility set** using geometric straight-line proxy; NOT a walking-route estimate.
4. `P2_directed_network` — same facilities, actual directed OSM network paths and travel kernel, same city/tract and population weights.
5. `P3_network_spatial_equity` — adds frozen population-weighted lower-decile fairness to the same network access.
6. `P4_unknown_access_upper` — explicit counterfactual *unknown facilities may be usable* upper bound, not the reference and not a verified observed improvement.

The controlling file is `code_v18/model_ablation.py`, output `V18_CONTROLLED_ABLATION.csv`. The paper must state *what changed at each step* and show real differences; do not falsely infer better predictive validity from a ranking change. Population/eligibility/network/fairness are compared only where original observations support the comparison. Methodology improvement needs an independent comparator; otherwise report `MECHANISM_ISOLATED / EXTERNAL_MERIT_NOT_ESTABLISHED`.

### 16.4 P0-04: Unknown facility access is a two-sided, NOT one-sided measurement

`code_v18/access_policy.py` is a shared policy for Overpass and PBF routes. `access=private/no/...` is `RESTRICTED`, `access=yes/public/permissive` or comparable explicitly tagged facility is `OSM_TAGGED_PUBLIC`, and everything with no trustworthy access tag or ambiguous tags is `UNKNOWN`. Reference opportunity **never silently accepts UNKNOWN**. Present lower (= observed OSM public-tagged candidates) and optimistic upper (= lower + unknown) as a reproducible **assumption interval**; `OSM_TAGGED_PUBLIC` itself is not legally authoritative admission, school eligibility or opening hours. If intervals are large enough to change policy ranking, describe the conditionality. Original POI tags, OSM IDs, coordinate provenance, duplicate checks and candidate admission classification go into traceable per-city files.

### 16.5 P0-05 / P1-10: Independent GIS reconstruction, not rerunning a derived score CSV

`code_v18/replay_raw_network.py` re-parses original Overpass ways/nodes or the original Geofabrik PBF into a separate actual directed graph, then independently recomputes source-based shortest paths for geographically stratified origin–destination pairs and compares against production OD records. Record number checked, discrepancy thresholds, disconnected paths, node IDs, graph version, and result hash. If parser differences or distances are scientifically irreconcilable, FAIL. The runtime gate also requires IMLS FY2024 outlet-to-OSM one-to-one spatial matching (`external_imls_validation.py`) as an **independent facility-coverage diagnostic**. Match rate does not demonstrate legal access or actual youth outcomes. `edge_failure_stress.py` checks an explicit sampled network link-removal scenario; it is **not** a complete twelve-city rank recalculation.

### 16.6 P0-06: Official summary, paper-length limits and separate AI use disclosure

A valid paper run must download the **original** `HiMCM-MidMCM_Summary.tex` from COMAP's own host (or receive a separately human-attested publisher original), save its exact byte SHA256, compile a derived one-page Summary using that source's preamble and the **actual scored claims**, and splice it as solution PDF page 1. Without original official TeX do not claim template compliance. Real team number only when provided; for the independent research, label **Not Registered** rather than inventing a number.

The remaining solution follows the user's official *Optional Paper Layout*: Table of Contents, Introduction and Restatement, Assumptions and Justifications, Presentation of Model and Solution, Analysis of Your Work (sensitivity and strengths/limits), final Concluding Paragraph, 1–2-page news article and any registered memos, Reference List. Preserve one-page Summary and ≤25 pages for the solution in the competition-shaped technical preflight. Typesetting at 12pt class is not enough: verify real output page spans and figure/text legibility, rejecting microscopic table/axis text. Use the *actual* AI tool and prompt log in `sources/`, human-confirmed prompt provenance including genuinely lost prompts marked as such; compile a separate **Report on Use of AI Tools** after the ≤25-page solution and record different solution vs combined hashes. Never invent previous prompts, external reviewers or contest approval.

### 16.7 P0-07: Evidence-generated prose, independent research gate

`code_v18/paper_claims.py` is executed only after the final real ranking, ablation table, original-OSM independent replay receipt, IMLS comparison, and constrained-weight robust preferences exist. It writes `research/v18_claim_evidence_registry.csv`, `research/v18_equation_contracts.csv`, an evidence-linked narrative LaTeX section and its SHA256 receipt. Each claimed result must take the form **Claim → observed source and units → exact computation → actual result → counterexample/negative evidence → inference boundary**, explicitly cite its model version and original source SHA. Human scholarly editing is still required; source-generated sentences are not a guarantee of O-Award quality. Never let a paper template with blanks substitute for actual result evidence.

### 16.8 P1-01/02/03/04/05: Public service evidence and honest target-age GIS

- IMLS FY2024 original library outlet ZIP is mandatory as an external audit, including ZIP SHA, file member and true outlet coordinates; its system records must not be counted as independent libraries. The `IMLS` comparator operates at outlet and OSM candidate entity grain, not individual verified admission.
- NCES/EDGE schools, ParkServe and official city park directories remain **discovery/conditional validation inputs**. Do not silently score school presence as a guaranteed school seat, or a school district as admission. If stable, comparable original data/eligibility are available, extend frozen experimental branches with a new run ID; otherwise preserve `NOT_MODELED_DUE_TO_ELIGIBILITY_OR_COVERAGE` and describe the consequence. Do NOT claim these optional full modules are already installed.
- Census age 15–17 estimate remains a proxy for the 14–18 question. Without comparable single-age location observations, no algorithm may claim exact 14–18 residents; record age proxy uncertainty separately.
- TIGER tract partial-overlap weights and one representative origin per tract are *spatial approximations*, not real home addresses; evaluate consistency vs city-level population controls, MAUP and residential-weight spatial alternatives only when legitimate underlying data exist.
- Candidate POI snaps to walked graph node, 1.25 m/s frozen base and varied speeds/edge removal; pedestrian bridge, access law and park entrance are not fully observed. Show 10/20/30-minute reached **network corridors** rather than claiming validated walkable isochrone polygons unless actual reachable polygon algorithm and entrance validation exists.

### 16.9 P1-07/08/09: Five sensitivity axes + exact preference theory

1. **Normative preferences**: official 27 scenario matrix = 3 travel-time cutoffs × 3 ACS share weights × 3 equity weights, 324 actual city-score records. It is a finite declared grid, not a preference distribution.
2. **Sampling and measurement**: real 2024 ACS E/M published MOE endpoint stress; distinguish marginal MOEs, unknown covariance and conservative envelopes from true joint 90% confidence intervals.
3. **GIS and access stress**: 18 actual OD-based city rerankings (3 walk speeds × 3 *hypothetical* feature missing rates × 2 eligibility assumptions). Include scored cases of OSM unknown lower/upper and actual edge dropout on stratified OD sample; none of these hypothetical missing percentages may be represented as independently observed error rates.
4. **Structural and model revision**: same facility inventory vs geodesic proxy vs directed network vs equity, non-compensatory holism comparison, with outputs from the exact same frozen source corpus.
5. **Temporal and geographic**: check 12 cities' OSM acquisition times and mixed-vintage ACS, compare years/city or spatial origin only if verified compatible observations are acquired; if not, explicitly mark cross-year stability and national representativeness **NOT_IDENTIFIABLE**, not PASS.

`robustness_lp.py` computes Pareto non-dominated city set, worst-case preference region via constrained LP over weights, and maximum regret. Its pre-specified 6-dimensional utility vector and admissible polytope must be documented; robust-first is only within that mathematical set. Simple stochastic rank frequencies are not frequentist probabilities of the true preferred city. Dynamic feedback, youth-club self-organization, or welfare causation are **not identifiable** without genuinely observed panel/participation evidence.

### 16.10 P1-11/12/13/14/15/16: Scientific figures, formula contracts and reproducibility

The figure system creates twelve actual city-level network/tract panels (`render_city_atlas_v18.py`), a research atlas with ≥10 evidence-backed maps/plots, and source-bonded SHA256 figure manifest. Only authentic TIGER polygons and OSM nodes/ways/POIs may be used in geo maps. Publicity-grade but unverifiable renderings are prohibited. Add original sources and graphics in reference/bibliography and use the *smallest* set of informative figures in the ≤25-page main text.

Maintain traceable `V18` claim–source–calculation–figure–paper and equation–proof–test–actual-result registries. Every displayed rank and number must be traceable to machine result files. Dependent software must log actual environment: Python, GIS packages, PROJ/GDAL, Graphviz and LaTeX, and packages at the moment of actual execution. Dependencies in requirements are **ranged but not locked** in this package; a real execution environment must generate a pinned per-run lock/provenance receipt and compare on an independent machine, if claiming clean reproducibility. Do not claim cross-platform live GIS tested merely because pure Python pytest passes. Clean V18 maintains no V11–V16 code/runtime dependency, no inherited old rankings or old maps.

### 16.11 Full phase order, machine release and human review

The 30-stage single-command orchestrator's stages are:
`tests → environment → official_summary → census → geography → networks → osm_temporal → score → audit → independent_replay → raw_network_replay → controlled_ablation → sensitivity → uncertainty → evidence_frontier → systems → external_imls → robustness_lp → preference_paths → route_stress → edge_failure → figures → atlas → multicity_maps → decision_figures → evidence_review → decision_gate → paper → release → package`.

If original real data are missing, output a real failure receipt and exact missing files. A failed stage must NOT create a fake success CSV or PDF. Runtime receipt `qa_v18/v18_execution_state.json` records the truth. Any future technical release means only **machine tests/real data check passed; human scientific review pending** unless an actual human reviewer certifies its full scientific adequacy. Authoring/reading the MD does not execute its stages.

**Exactly four independently assessable releases:** (A) this source-only V18 reproducible engine, (B) future frozen Census/OSM original source-and-hash manifest, (C) future true network/12-city numerical results atlas, (D) future real study PDF and TeX plus AI appendix. The current delivery has only (A). B–D may be generated only when all their actual prerequisites exist.

### 16.12 Acceptance crosswalk

The tracked obligation register is `V18_QUALITY_GATES.csv` and the full original source/provenance evidence contracts in this master. All P0/P1 defects are coded as `CODE_IMPLEMENTED_OFFLINE_TESTED`, `IMPLEMENTED_CONDITIONAL_REQUIRES_REAL_SOURCE`, `NOT_IMPLEMENTED_OPTIONAL_OR_NOT_IDENTIFIABLE`, or `BLOCKED_NO_REAL_INPUT`, *never* a blanket `DONE`. Source-independent mathematical test status does not certify any city result. After live human execution, rerun acceptance matrix based on actual machine receipts and real science review.

**Scientific quality criterion:** every mathematical result must have grounded data; every graphical result must be regenerable from original bytes; every section must answer the problem; every unavailable observation must be stated as such. Formal submission is a future outcome, not a label assigned by this source-only package.

---

# V18 PRIORITY OVERRIDE — EVIDENCE HORIZON AND DECISION-BOUNDARY UPGRADE

> **Binding release:** This section supersedes prior details in this file only where it adds a stricter V18 evidence gate. The core twelve-city sample, original Census/OSM acquisition, fixed M0/M1 score, same-facility ablation, systems-theory structure, official paper layout and release conditions remain unchanged. This section never imports another team's data, code or contest answer. Source-only state: **V18_CODE_PREPARED_EMPIRICAL_NOT_RUN**.

## V18.1 Research originality and protected model core

We are studying original municipal measurements and the geographic transformation of amenities into potentially accessible opportunities. V18 is an independent empirical GIS inquiry, not an adaptation of a competitor's globally mixed city-ranking paper. Its only valid research core remains:

`28 authenticated official Census originals → 12 real OSM walk networks → 12-city fixed-score real-GIS comparison → independent routing and uncertainty QA → systems-science falsification → full English research manuscript`.

The comparative provenance and our independent transformation are documented in `research/V18_TRANSFER_AND_DIFFERENTIATION.md`. We reviewed general methodological ideas about evidence uncertainty, prioritizing verification, preference dependence, and claim-specific writing; we did **not** copy any external paper's prose, code, values, figures, global city sample, weight matrix, TOPSIS/VIKOR scoring architecture or incomplete-data results. Mathematical concepts that are established in the literature should be cited as established rather than misrepresented as new inventions.

## V18.2 Two-layer scientific interpretation

The first layer is the **unchanged observed-data reference** $M_1(c)$ and the actual same-facility mechanism decomposition. The second layer is a *decision evidence audit*, not a competing final scoring model. It must never overwrite `FINAL_12_CITY_REAL_GIS_RANKING.csv`, reselect the twelve cities by their performance or invent missing values.

### V18.2.1 Evidence outer horizon, not joint probability

For city $c$, let $H_c$ be the household-context score in $[0,100]$, $L^H_c,U^H_c$ the source-grounded 2024 ACS marginal-MOE endpoint **stress** values, $Y_c$ the network opportunity component under OSM-tagged-public reference, and $Y_c^+$ the additional upper-bound result when unverified access is hypothetically granted. The frozen normative weights still satisfy $0.60+0.40=1$:

\[
S^{\rm ref}_c = 0.60 H_c + Y_c,
\quad\underline S_c=0.60 L^H_c+Y_c,
\quad\overline S_c=0.60 U^H_c+Y_c^+.
\]

Here $Y_c\in[0,40]$ already contains the $40\times$ share of weighted access; its upper extension is **not** an additional bonus. The permitted outer envelope is $[\underline S_c,\overline S_c]$. It intentionally lets ACS and unknown-access components vary independently, and may be wider than any realizable simultaneous observation. **It is neither a joint 90% confidence region nor an empirical posterior.**

Define only logically supportable labels:

- Sufficient elimination: $\overline S_c < \max_{j\ne c}\underline S_j$ (under declared outer bounds).
- Sufficient single-winner certification: $\underline S_c > \max_{j\ne c}\overline S_j$ (under declared outer bounds).
- Otherwise, `NOT_EXCLUDED_BY_OUTER_BOUND`, which is **not** a proof of realistic simultaneous feasibility or of being objectively best.

The actual executable is `code_v18/evidence_frontier.py`. It reads *actual* `FINAL_12_CITY_REAL_GIS_RANKING.csv`, `V18_ACS_MOE_STRESS_ENVELOPES.csv`, and `V18_CONTROLLED_ABLATION.csv`. It validates the same GEOID set, exact reference identity, bounds, 0–100 domains, and scores; it refuses to produce any result before the original Census/GIS audit.

### V18.2.2 Verification priority as conditional decision influence

`V18_TARGETED_EVIDENCE_QUEUE.csv` is a ranked set of 24 city-by-evidence-family suggestions (12 cities × 2 concrete families: ACS denominator/MOE and official access/entrance verification). It calculates the **maximum upper-score reduction conditional on returning a resolution equal to the reference**; it does not assume the result of a field visit, provide a survey sampling probability or claim a monetary expected return. Priority must not be used to skip the mandatory official 28 source files or 12 networks.

This is evidence-gathering triage. The absence of an affordable/available way to verify one site must be recorded as an unresolved constraint, never changed to a numerical zero or a fabricated positive answer.

## V18.3 Declarative household archetypes without surveys or change to M1

Write each reference city score as a six-component additive utility vector:

\[
 u_c=(u_{\text{rent}},u_{\text{poverty}},u_{\text{broadband}},
 u_{\text{library}},u_{\text{park}},u_{\text{lower decile}})_c.
\]

Our *actual frozen reference* $S_c^{\rm ref}=100\,w^{\!0}\cdot u_c$ has

\[
 w^{\!0}=(0.210,0.210,0.180,0.165,0.135,0.100),
\]

**derived programmatically** from `config_v18/reference_model_v18.json` and verified against the authoritative M1 column to numerical tolerance. We declare only three alternative **analyst-proposed hypothetical** household priorities (household continuity, nearby free public opportunity, safeguard of poorly served tracts). Each is a positive multiplier of $w^0$ followed by normalization. No teen survey or AHP elicitation is claimed. The original M1 rank remains the final reference; policy family winners are a separate sensitivity surface.

For each family weight vector $w^a$, analyze the entire affine preference path

\[
 w(t)=(1-t)w^0+t w^a,\qquad t\in[0,1].
\]

For each city-pair $i,j$, their score difference is an affine function of $t$. Solve all distinct pairwise line intersections analytically, partition $[0,1]$, and determine the first-place city on each open segment. Only genuine first-place transitions are reported; this avoids arbitrary grid discretization and does **not** convert a constructed preference domain to a population probability.

Executable: `code_v18/preference_paths.py`; outputs: `V18_DECLARED_PREFERENCE_FAMILIES.csv` (4×12), `V18_EXACT_LEADER_TRANSITIONS.csv` (dynamic number of leader segments), `V18_CROSS_FAMILY_MINIMAX_REGRET.csv` (12 rows). The family-level regret is a decision stress number over **four declared cases**, not a theorem over all possible preferences; the existing `robustness_lp.py` retains the exact six-dimensional polytope certificate.

## V18.4 Systems theory and evidence semantics

These additional decision tools make the existing systems-science interpretation more *falsifiable*: 

- **Openness/Hierarchy:** Cross-municipal service catchments and tract-level bottom-decile exposure stay tied to genuinely routed OSM streets and ACS tract proxies, not a country-level average.
- **Purpose:** Which families' priorities alter the city choice is a normative counterfactual; real adolescents' preferences remain unmeasured.
- **Holism/Constraints:** Unknown facility entry cannot be assumed open. The score upper bound shows how missing access evidence can alter the interpretation.
- **Stability versus robust choices:** Weight-space robustness, city sample robustness, parameter stability and longitudinal actual system stability are *different objects*. Only the first three can be evaluated by the current static data. Multi-year endogenous urban adjustment is **NOT IDENTIFIABLE** without real repeated states.
- **Feedback:** The research loop `measure → diagnose → identify decision-critical uncertainty → verify with new independent data → re-run` is real in the methodology; a causal feedback loop among cities/students is not established by a static map.

Explicitly distinguish sampling/measurement, normativity, city context, qualification and structural model uncertainty in all paper figure captions. A small rank-change number is not evidence of causal welfare validity.

## V18.5 New paper and figures are real-results gated

`code_v18/decision_atlas.py` generates two complete three-format source-bound scientific figures only after real data: 

- F18 Decision 01: twelve-city **outer evidence envelope** with the frozen reference marker and logical elimination labels. No 90% probability language.
- F18 Decision 02: four declared hypothetical household priority ranking columns. No implied student poll.

`code_v18/decision_evidence_review.py` generates the **V18 epistemic claim registry** and `V18_DECISION_EVIDENCE_ADDITIONS.tex` as a supplementary evidentiary subsection of the official `Analysis of Your Work`, not as a new main paper or appended independent ranking. It connects observed city results to source-hash references and reports one counterexample plus the failure boundary of each quantitative claim. `research/V18_EPISTEMIC_REVIEW_CONTRACT.csv` documents what evidence each argument needs and what it must not claim.

`code_v18/decision_release.py` is a **new mandatory release gate**. It checks the 12-row horizon, 24-row verification queue, 48 preference-family rows, genuine transition segments, 12-row family regret, exact hashes of source ranking/MOE/ablation/config, both figures in PDF/SVG/PNG with manifests, and the text/source evidence registry. Paper building and final release call this validator again. A fake or stale file name cannot replace actual original-source evidence.

**Official optional paper sequence remains:** one-page Summary Sheet (page 1), Table of Contents, Introduction/Restatement, justified assumptions, Presentation of Model/Solution, Analysis of Your Work (including V18 evidence uncertainty), concluding paragraph, actual 1–2-page requested news article/memos, and References; separate AI-use disclosure as genuinely applicable. We obey the official recommended structure by choice, not by misdescribing `Optional` as mandatory.

## V18.6 Expanded authoritative end-to-end pipeline

The **30 actual code stages** are:

`tests → environment → official_summary → census → geography → networks → osm_temporal → score → audit → independent_replay → raw_network_replay → controlled_ablation → sensitivity → uncertainty → evidence_frontier → systems → external_imls → robustness_lp → preference_paths → route_stress → edge_failure → figures → atlas → multicity_maps → decision_figures → evidence_review → decision_gate → paper → release → package`.

Start in the unzipped root with `python code_v18/run_v18.py --stage all --network auto`. The V18 extras **cannot** run before official raw-data and GIS passes; they therefore do not add fake analysis when the original data are unavailable.

**Success requires every original-source, model, reference/ablation, path, rank, Figure, manuscript, supplementary, AI-disclosure and human scholarship condition previously declared, plus all V18 addendum outputs.** There is no claim that this source-only package has downloaded the 28 original Census files, computed 12 real graphs or produced a real winner yet. Failure must provide the real exception and state `BLOCKED_FOR_FINAL_GIS_PAPER`, not a synthetic number or a promised future automatic result.

## V18.7 Finite handoff rather than uncontrolled feature growth

Do not expand the primary score beyond its two facility categories purely because another project uses ten indicators. Education/safety/environment may be developed as **independent, comparably acquired scope/construct-validity checks**, but their inclusion in the reference metric requires pre-registered scientific justification, synchronized twelve-city sources, entire pipeline rerun, and a new recorded model policy. Do not use V18 to change the winner after seeing it.

**The new standards are implemented as executable input-output contracts, not paper-writing slogans.** Future running agents must report observed data status, exact source hashes, 12-city frozen reference, exclusion/non-exclusion sets, verification priorities, leader-switch intervals, counterevidence and final paper audit separately. Without actual source data, the proper result remains `CODE_AUTHORED / REAL_EMPIRICAL_RUN_PENDING`.
