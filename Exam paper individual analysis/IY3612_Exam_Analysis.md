# IY3612 Critical Infrastructure Security — Comprehensive Past Paper Analysis

**Papers Analysed:** 2021, 2022, 2023, 2024, 2025 (5 years)
**Exam Format:** 2 hours, attempt 3 out of 5 questions (each worth 25 marks)
**All questions offer choice — no compulsory questions.**

---

## 1. Question Pattern Analysis

### Structure & Format

Every paper follows the same format: 5 questions, each worth exactly 25 marks, with students choosing any 3. Questions are consistently titled with a topic label (e.g., "Control Systems Security", "Adversary Modelling"). Each question is split into parts — typically (a) and (b), often with sub-parts (i) and (ii).

### Recurring Question Structures

| Question Type | Description | Frequency |
|---|---|---|
| **"Give a brief, reasoned answer"** | The dominant format. Presents a scenario and asks students to reason through consequences, feasibility, or limitations. | Every question in every paper |
| **Scenario-based attack analysis** | Describes a specific adversary action against a system and asks what damage is possible, or how the system responds. | ~80% of all questions |
| **Compare two approaches** | E.g., feed-forward vs feedback controllers under attack; degree centrality vs betweenness centrality. | ~3–4 per year |
| **Construct/Convert a model** | Build an Attack Tree, convert to ACT, apply game theory. | 1–2 per year (increasing) |
| **Identify algorithm(s)** | Name and justify the algorithmic approach to solve a graph/network problem (e.g., min-cut, max-flow). | 1 per year |
| **Policy/strategy reasoning** | Discuss deterrence, deniability, national strategy implications, or hack-back risks. | 1–2 per year (increasing) |

### Mark Distribution Patterns

| Part Structure | Typical Marks | Notes |
|---|---|---|
| Single large scenario part | 10–17 marks | Demands depth and reasoning |
| Medium part with sub-questions | 6–9 marks each | Most common format |
| Short definitional sub-part | 5–6 marks | Rarer; usually paired with an application |
| Two-part (a)+(b) equal split | 12+13 or 13+12 | Common for dependency/network questions |
| Three-part (a)+(b)+(c) | 6+6+13 or 7+6+12 | Seen in control systems and 2025 modelling |

---

## 2. Topic Frequency Mapping

### Complete Topic Appearance Table

| Topic | 2021 | 2022 | 2023 | 2024 | 2025 | Total Appearances | Typical Marks |
|---|---|---|---|---|---|---|---|
| **Control Systems / ICS / SCADA** | Q4 | Q1, Q2 | Q3, Q4 | Q1 | Q3 | **All 5 years (8 Qs)** | 25 each |
| **Attack Modelling (AT/ACT/ADT)** | Q5 | Q5 | Q1 | Q2 | Q2 | **All 5 years (5 Qs)** | 25 each |
| **MITRE ATT&CK Framework** | — | Q5 | — | Q2 | Q2 | 3 years | Part of 25 |
| **Game Theory (pure/mixed strategies)** | Q5 | — | — | — | Q2(c) | 2 years | 5–10 marks |
| **BGP / Internet Routing Security** | Q3 | Q3 | — | Q4 | Q1, Q4 | 4 years (5 Qs) | 25 each |
| **Scale-Free Graphs / Power-Law** | Q3 | — | — | Q5(a) | Q1(a) | 3 years | 7–15 marks |
| **Network Robustness / Betweenness** | Q2 | Q3 | — | Q5 | Q1 | 4 years | 12–25 marks |
| **Dependency / Interdependency Models** | — | — | Q5 | Q5 | — | 2 years | 25 each |
| **Cyber Conflict / Policy / Strategy** | — | — | Q2 | Q3 | Q5 | **3 consecutive years** | 25 each |
| **National Cyber Security Strategy** | — | — | Q2(b) | — | — | 1 year | 13 marks |
| **Supply Chain Attacks** | Q1 | Q2(b), Q3 | Q3(b) | Q1 | — | 4 years | Part of 25 |
| **IEC 61850 / GOOSE / IEC 64283** | — | Q1(b) | — | Q1(b) | — | 2 years | 6–12 marks |
| **Field Bus / OT Protocol Security** | Q4 | Q2(b) | — | Q1(b) | Q3(b) | 4 years | Part of 25 |
| **Power Grid / Energy Systems** | — | Q2(a) | Q5 | — | Q1(b) | 3 years | 10–25 marks |
| **Subsea Cable Infrastructure** | Q3(b) | — | — | Q3(a)(ii) | — | 2 years | 7–10 marks |
| **Cyber Insurance** | — | — | Q2(a) | — | — | 1 year | 12 marks |
| **DNS Security** | — | — | — | — | Q4(a) | 1 year | 12 marks |
| **Feedback vs Feed-Forward Control** | — | Q1(a) | Q4(a) | — | — | 2 years | 13 marks |
| **Safety Instrumentation Systems (SIS)** | — | Q1(c) | — | — | — | 1 year | 6 marks |
| **Social Interaction Graphs** | — | — | — | Q5(b) | — | 1 year | 12 marks |
| **Max-Flow / Min-Cut Algorithms** | — | — | Q5(b) | — | Q1(b) | 2 years | 10–13 marks |
| **Data Historian Attacks** | — | — | — | — | Q3(a) | 1 year (new) | 12 marks |
| **Modbus / Wireless Sensor Security** | — | — | — | — | Q3(b) | 1 year (new) | 13 marks |
| **Hack Back / Offensive Cyber** | — | — | — | Q3(b) | Q5(b) | 2 years | 12 marks |
| **Hybrid Warfare / Deniable Ops** | — | — | — | Q3(a) | Q5(b) | 2 years | 6–12 marks |

### "Banker" Topics (Appear Every Year Without Fail)

1. **Control Systems / ICS / SCADA Security** — At least 1 full question every year (often 2)
2. **Attack/Adversary Modelling (AT/ACT/ADT/MITRE)** — At least 1 full question every year

---

## 3. Trend Analysis

### Topics Increasing in Frequency

| Topic | Trend | Evidence |
|---|---|---|
| **Cyber Conflict & Policy** | ↑ Strongly increasing | Absent 2021–2022 → full question 2023, 2024, 2025 |
| **MITRE ATT&CK** | ↑ Increasing | Absent 2021, 2023 → explicit focus 2022, 2024, 2025 |
| **Attack Countermeasure Trees (ACTs)** | ↑ Increasing | 2023 introduced ACTs; also in 2025. Becoming the preferred modelling tool |
| **Hack back / offensive operations** | ↑ New and growing | First appeared 2024 Q3, returned 2025 Q5 |
| **DNS as infrastructure target** | ↑ New for 2025 | Not previously tested at IY3612 level |
| **Specific CPS scenarios (water, gas)** | ↑ Increasing specificity | Scenarios getting more detailed and industry-specific |

### Topics Decreasing or Stable

| Topic | Trend | Evidence |
|---|---|---|
| **Pure game theory definitions** | ↓ Declining as standalone | Full question 2021 → reduced to 5 marks in 2025 |
| **Betweenness centrality calculations** | ↓ Declining | Major question 2021 → absorbed into broader topics |
| **Subsea cables** | Stable/niche | Appears when cyber conflict is tested |
| **BGP security** | Stable | Consistently tested but with evolving angles (hijacking → deflection → DoH) |

### Rotation Patterns

| Pattern | Evidence |
|---|---|
| **ICS/Control Systems vs CPS** alternate between "pure control theory" and "applied scenario" | 2022/2023 = control theory focus; 2024/2025 = supply chain + applied scenario |
| **BGP question angle rotates** | 2021: scale-free routing; 2022: APT supply chain on routers; 2024: prefix hijacking + BGPsec; 2025: deflection attacks |
| **Dependency models appear every other year** | Present 2023, 2024; absent 2021, 2022, 2025 |

---

## 4. Gap Analysis

### Syllabus Topics Not Yet Examined (or Underexamined)

| Syllabus Topic | Last Appeared | Risk Assessment |
|---|---|---|
| **Common Criteria / Assurance / Certification** | **NEVER** (in any paper) | Covered in Unit 7 syllabus; potential future appearance |
| **Petri Nets for adversary modelling** | **NEVER** | In syllabus Unit 8; theoretical but examinable |
| **Agent-Based Modelling** | **NEVER** directly | In syllabus Unit 5; may appear with interdependency |
| **Cascading Failures** | **NEVER** directly | In syllabus Unit 5; highly relevant to infrastructure |
| **Erdős–Rényi / Watts-Strogatz models** | **NEVER** directly | In syllabus Unit 3; only scale-free has been tested |
| **DDoS attacks** | **NEVER** as standalone | In syllabus Unit 4; could combine with DNS/BGP |
| **Input-Output economic models** | **NEVER** directly | In syllabus Unit 4; theoretical but possible |
| **Colonial Pipeline / Sunburst** specifics | **NEVER** explicitly | In syllabus Unit 1 introduction; could be scenario context |
| **DNS Security** | 2025 (first time) | May recur — now established as testable |
| **Intrusion Detection in ICS** | **NEVER** directly | In syllabus Unit 7; could pair with SCADA question |

### Topics Absent Recently but Previously Tested

| Topic | Last Tested | Gap |
|---|---|---|
| **Subsea cables as infrastructure** | 2024 | Could recur with cyber conflict |
| **Cyber insurance** | 2023 | 2-year gap; relevant to policy |
| **National cyber security strategy** (standalone) | 2023 | 2-year gap; UK strategy is core content |
| **SIS (Safety Instrumentation Systems)** | 2022 | 3-year gap; high relevance for CPS |
| **Feedback vs feed-forward** (explicit comparison) | 2023 | 2-year gap; fundamental control theory |

---

## 5. Predictions for Your 2026 Exam

### Very Likely (appears almost every year — would be a shock if absent)

| Prediction | Reasoning | Confidence |
|---|---|---|
| **ICS/SCADA/CPS scenario question** | Appeared every single year (8 total questions across 5 papers). The examiner clearly considers this the core of the module. Expect a specific industrial scenario (water, gas, power, manufacturing). | ★★★★★ |
| **Attack modelling question (AT/ACT/ADT + MITRE ATT&CK)** | Appeared every single year. The trend is towards combined questions: MITRE framework for describing attacks → ACT for modelling countermeasures → game theory for optimisation. The 2025 paper combined all three in one 25-mark question — expect this format again. | ★★★★★ |
| **BGP / Internet infrastructure security** | Appeared 4 of 5 years. 2025 expanded to include DNS. Expect either BGP deflection/hijacking or a combined BGP + DNS question. BGPsec and RPKI mechanisms are likely. | ★★★★☆ |

### Likely (strong pattern suggests it)

| Prediction | Reasoning | Confidence |
|---|---|---|
| **Cyber conflict / policy question** | Three consecutive years (2023–2025) with increasing marks and complexity. Hybrid warfare, deniable operations, and hack-back are clearly part of the examiner's evolving interests. Expect a scenario involving state vs non-state actors and proportionate response. | ★★★★☆ |
| **Supply chain attack scenario** | Appeared 4 of 5 years. The examiner loves supply chain contexts for ICS questions (intercepted IEDs, modified firmware, smart pigs). Could combine with ICS or adversary modelling. | ★★★★☆ |
| **Network graph models / robustness** | Scale-free graphs, power-law distributions, and centrality measures appear in some form in most years. May be combined with dependency models. | ★★★☆☆ |

### Possible (gap analysis or rotation suggests it)

| Prediction | Reasoning | Confidence |
|---|---|---|
| **Dependency/interdependency models** | Present 2023 and 2024, absent 2025. Rotation pattern suggests it could return. The gas NTS diagram style or financial network centrality could feature. | ★★★☆☆ |
| **Common Criteria / assurance models** | NEVER tested despite being in the syllabus. This is the biggest gap. The examiner may consider it too theoretical for the applied focus, OR it may be overdue. | ★★☆☆☆ |
| **SIS (Safety Instrumentation Systems)** | 3-year gap since 2022. Could return as part of a CPS question. | ★★☆☆☆ |
| **Cascading failures** | Never directly tested but in syllabus. Could appear as part of dependency/power grid question. | ★★☆☆☆ |
| **IEC 61850 / IEC 64283 protocols** | 2-year gap. These standards are core to ICS security questions and could return. | ★★★☆☆ |

### Unlikely but Worth Knowing

| Prediction | Reasoning |
|---|---|
| **Petri nets** | In syllabus but never tested — likely considered too theoretical for undergrad |
| **Agent-based modelling** | In syllabus but never tested — may be briefly mentioned in context |
| **ER random graphs / Watts-Strogatz** | In syllabus but never directly tested; scale-free dominates |
| **Input-output economic models** | In syllabus but never tested — very mathematical, unlikely for IY3612 |
| **DDoS as a standalone question** | In syllabus but never tested alone — more likely as part of DNS/infrastructure |

---

## 6. Recommended Revision Priorities

### Priority 1: MUST KNOW — Absolute Bankers

These topics appear every year. If you know these well, you can answer 2 of your 3 required questions.

**A. Control Systems / ICS / SCADA / CPS Security**
- How feedback and feed-forward controllers respond to attacks (delayed messages, suppressed commands, injected values)
- SCADA architecture: PLC, RTU, IED, data historian, field bus
- IEC 61850 (GOOSE/SV) and IEC 64283 security measures
- Supply chain attacks on ICS components
- Safety instrumentation systems vs regular control systems
- Modbus protocol and its lack of authentication
- Specific scenarios: power grid, gas pipeline, water treatment

**B. Attack/Adversary Modelling**
- Attack Trees: construction, AND/OR nodes, algebraic representation
- Attack Countermeasure Trees: adding detection and mitigation nodes, probability calculations
- Attack-Defence Trees: representing attacker-defender interactions
- MITRE ATT&CK framework: tactics, techniques, Enterprise vs ICS matrix
- Game theory basics: pure vs mixed strategies, strategy sets, which model to choose for a given scenario
- How to connect MITRE ATT&CK → ACT → game theory in one coherent answer

### Priority 2: SHOULD KNOW — Highly Likely Topics

**C. BGP & Internet Infrastructure Security**
- How BGP routing works at the AS level
- Prefix hijacking, MITM via BGP, deflection attacks
- BGPsec and RPKI mechanisms
- DNS hierarchy, TLD delegation, DoH (DNS-over-HTTPS)
- Why the Internet exhibits scale-free / power-law properties
- Subsea cable vulnerabilities and their infrastructure implications

**D. Cyber Conflict & Policy**
- Nation-state cyber operations below the threshold of war
- Deniability through criminal proxies
- Hack-back risks and proportionality
- Attribution challenges
- How national cyber security strategies serve as deterrence
- UK offensive cyber capability and its strategic implications
- Cyber insurance and war exclusion clauses

### Priority 3: GOOD TO KNOW — Possible Topics

**E. Dependency & Interdependency Models**
- Centrality and betweenness centrality in infrastructure networks
- Max-flow / min-cut algorithms for identifying critical edges
- Power-law degree distribution and what it means for attackers vs defenders
- Social interaction graphs for targeting and defence

**F. Power Grid & Energy Infrastructure**
- State estimation and PMU (phasor measurement unit) attacks
- Grid balancing, frequency/voltage requirements
- Smart grid communication and control vulnerabilities

### Priority 4: LOW PRIORITY — Brief Awareness Sufficient

- Common Criteria / assurance (know the concept, not the detail)
- Cascading failures (understand the principle)
- Agent-based modelling and Petri nets (be aware they exist)
- Erdős–Rényi and Watts-Strogatz models (know how they differ from scale-free)

---

## Key Exam Strategy Notes

1. **The examiner values reasoning over recall.** Almost every question says "give a reasoned answer." Your marks come from explaining *why* something works or doesn't, not from reproducing definitions.

2. **Scenarios are getting more specific and applied.** Earlier papers (2021–2022) were more abstract; recent papers (2024–2025) name specific systems (gas compressors, wastewater plants, payment processors). Prepare by understanding how attacks play out in real infrastructure.

3. **The combined modelling question is the new standard.** The 2025 Q2 pattern (MITRE → ACT → game theory in one question) is likely to recur. Practise building a multi-stage attack and then modelling it with all three frameworks.

4. **Cyber conflict is the examiner's growing interest.** This topic has expanded from absent (2021) to a full 25-mark question with creative fictional scenarios. Expect to reason about international law, proportionality, and infrastructure consequences.

5. **Every question is 25 marks.** There are no "easy" short questions — budget ~40 minutes per question and plan your answer structure before writing.
