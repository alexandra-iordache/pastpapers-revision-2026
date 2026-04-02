# Past Paper Analysis Report — Royal Holloway BSc/MSc Modules

## Overview

- **Modules Analysed**: 6
- **Total Papers Read**: 26
- **Modules**: CS3003, IY3501, IY3609, IY3612, IY3660, IY5606

---

## 1. The "Hardest" Module: IY3612 — Critical Infrastructure Security

**IY3612 is the most objectively difficult exam across your entire set.** Here is the justification:

### Complexity and Cognitive Load

IY3612 questions demand you synthesize knowledge from an unusually wide range of disciplines *simultaneously*. A single question can require you to reason across graph theory, control systems engineering, ICS protocols (IEC 61850, Modbus, GOOSE/SV), BGP networking, game theory, and international law/policy. No other module in your set has this breadth.

For example, the 2025 paper asks you to:

- (a) Reason about power-law degree distributions in BGP
- (b) Identify min-cut algorithms for attacking power grids
- (c) Construct Attack Countermeasure Trees with probability analysis
- (d) Identify game-theoretic models for attacker strategy
- (e) Debate UK policy responses to cyber attacks from allied nations

…all in a single sitting.

### Depth of Knowledge and Critical Thinking

Nearly every mark in IY3612 requires *novel analytical reasoning* rather than recall. Questions present unique, never-before-seen scenarios (e.g., "An adversary delays 10% of sensor messages in a feedback control loop — what happens?", or "Should a wastewater plant operator continue operating if they know flow sensors are compromised?"). You cannot memorise answers to these; you must reason from first principles every time.

Compare this to IY3501 (Security Management), where many questions are definition-based (e.g., "Define PII" for 3 marks), or IY3660 where the crypto calculations follow a repeatable, practised method.

### Multi-part Demands Relative to Marks

IY3612 questions are deceptively dense. A 25-mark question might have three cascading sub-parts where each answer depends on the previous one (e.g., Q2 in 2025: describe a multi-stage ATT&CK attack → build an ACT from it → then identify a game-theoretic model for it). The Inoperability Input-Output model question (2022, Q4) requires you to formulate matrix equations *and* design algorithms for min-flow problems *and* prove properties about k-connected graphs — all within a single question.

### Almost No "Easy" Marks

Unlike every other module, IY3612 has virtually no low-hanging fruit. There are almost no 2–3 mark definition questions. Almost every sub-question requires a "brief, reasoned answer" — the examiner's favourite phrase, appearing dozens of times across the papers.

### Runner-Up: IY3660 (Applications of Cryptography)

IY3660 is a close second due to its mathematical rigour, but its difficulty is more *predictable*. The block cipher calculations, security game definitions, and the recurring 34-mark essay (Ruritania/BizCorpInc/TLS scenario) appear year after year with only minor variations, making it highly preparable through practice.

---

## 2. Formula & "Working-Out" Heavy Exams

Using **IY3660 (Applications of Cryptography)** as the baseline, here are all modules that fit this profile:

### IY3660 — Applications of Cryptography (The Baseline)

This is your gold standard for "working out" exams. Every year includes:

- **Block cipher encryption/decryption**: Step-by-step XOR operations using a 4-bit lookup table in ECB, CBC, and CTR modes. You must show each intermediate step (e.g., XOR plaintext with IV, look up in table, chain to next block).
- **Modular arithmetic**: RSA signature computation (σ = M^d mod N), Diffie-Hellman shared key (K = g^xy mod p), factoring N to recover signing keys.
- **Formal security proofs**: Constructing and reasoning about IND-CPA, IND-CCA, UF-CMA, EUF-CMA, and SUF-CMA security games.
- **Birthday paradox**: Calculating collision probabilities for hash functions (after ~2^(n/2) blocks).
- **Padding scheme logic**: Implementing and applying padding in pseudo-code.

### CS3003 — IT Project Management (Moderate Working Out)

This module requires two types of step-by-step calculation every single year:

- **Earned Value Management (EVM)**: You must compute EV (Earned Value), PV (Planned Value), AC (Actual Cost), then calculate SV = EV − PV, CV = EV − AC, and sometimes SPI and CPI. These appear in *every* paper (2023 Q1b, 2024 Q2a, 2025 Q1c).
- **Critical Path Method (CPM)**: Draw a full network diagram from a dependency table, compute forward pass (ES, EF), backward pass (LS, LF), calculate all floats, and identify the critical path. This also appears in *every* paper.
- **TCO Formula Construction**: The 2024 paper (Q3a) requires building a formula TCO = aN + bM + c from a complex licensing scenario with per-user, per-CPU, and annual maintenance costs over 5 years.

While less mathematically intense than IY3660, calculators are explicitly *not permitted*, so you must do all arithmetic by hand.

### IY3609 — Digital Forensics (Light Working Out)

IY3609 has intermittent calculation requirements, not as central as IY3660 but still present:

- **Hex-to-decimal cluster addressing**: Combining MSB and LSB values (e.g., 0x0000 || 0x002A = cluster 42), then tracing through FAT chains.
- **File size vs cluster size**: Calculating how many clusters a file occupies and quantifying unrecoverable data (e.g., 5500 bytes with 4KiB clusters means 2 clusters needed, but 5500 − 4096 = 1404 bytes on second cluster).
- **RAID fault tolerance**: Reasoning about which disk failures are survivable in RAID 5, 10, and 50 configurations using parity/mirroring logic.

### IY3612 — Critical Infrastructure Security (Conceptual/Formal Working Out)

IY3612 contains some formal/mathematical elements, but they are more conceptual than computational:

- **Graph theory formulas**: Betweenness centrality BC(x) = Σ σ_st(x)/σ_st, time complexity arguments (O(|V||E|) vs O(|E|)).
- **Inoperability I-O model**: The matrix equation q = A*q + c* and reasoning about how to combine interdependency matrices.
- **Attack tree algebraic conversion**: Converting graphical attack trees into Boolean/algebraic expressions.
- **Max-flow/min-cut**: Conceptual application to infrastructure networks (no actual computation, but you need to identify and justify the right algorithm).

### Modules with NO Working Out

- **IY3501 (Security Management)**: Purely essay-based. Definitions, case study analysis, risk assessments, GDPR discussion. Zero calculations.
- **IY5606 (Embedded Technologies / Smart Cards)**: Entirely qualitative. Explain/describe/discuss format with short-answer definitions and system design essays. Zero calculations.

---

## 3. Module Summary Table

| Module Code | Module Name | Primary Question Style | Requires Working Out? | Difficulty (1–10) |
|---|---|---|---|---|
| **CS3003** | IT Project Management | Scenario-based MCQ with justification, EVM calculations, network diagram / critical path analysis, true/false with reasoning | **Yes** (EVM + CPM every year) | **4** |
| **IY3501** | Security Management | Essay / discussion, definitions, GDPR case study analysis, risk assessment tables, policy writing | **No** | **3** |
| **IY3609** | Digital Forensics | Scenario-based technical reasoning, hex/binary calculations, forensic procedure analysis, legal reasoning | **Moderate** (some hex/cluster/RAID calculations) | **7** |
| **IY3612** | Critical Infrastructure Security | Extended analytical essays, attack scenario reasoning, graph theory, game theory, ICS/SCADA analysis, cyber conflict policy | **Moderate** (conceptual graph theory + formal models) | **9** |
| **IY3660** | Applications of Cryptography | Formal crypto definitions, step-by-step block cipher calculations, security game proofs, protocol analysis essay | **Yes (Heavily)** — the benchmark | **8** |
| **IY5606** | Embedded Technologies / Smart Cards | Short-answer definitions (2–5 marks each), describe/discuss, system design scenario essay | **No** | **4** |

---

## 4. Key Revision Strategy Takeaways

### Priority 1: IY3612 and IY3660

These are your two hardest exams by a significant margin. IY3612 is the harder of the two but IY3660 is the one where practice pays off the most (the calculations are repeatable patterns).

### For IY3660 (Applications of Cryptography)

- Drill the 4-bit block cipher table calculations until they are second nature. The **same lookup table** appears in *every single year*.
- Practice ECB, CBC, and CTR mode encryption/decryption repeatedly.
- Memorise the security game templates (IND-CPA, UF-CMA).
- Prepare a strong essay plan for the TLS/Ruritania-style question (34 marks, appears every year).

### For IY3612 (Critical Infrastructure Security)

- You cannot rely on memorisation. Instead, build a mental framework for *how to reason* about attacks on infrastructure.
- Understand graph theory fundamentals (min-cut, betweenness centrality, connectivity).
- Learn control system feedback loop basics.
- Know the MITRE ATT&CK matrix structure.
- Practice writing "brief, reasoned answers."

### For CS3003 (IT Project Management)

- Master EVM formulas (SV, CV, SPI, CPI) and the critical path method mechanically.
- These appear every year and are free marks if you know the procedure.

### For IY3609 (Digital Forensics)

- Learn FAT32 file system structure, cluster addressing, and RAID configurations.
- Study legal frameworks: Daubert criteria, RIPA Section 49, Overseas Production Orders.
- Practice scenario-based reasoning across storage, memory, network, mobile, and malware forensics.

### For IY3501 and IY5606 (Lowest-Effort Modules)

- These can be revised through reading and memorising key definitions and frameworks.
- IY3501: CIA triad, ISO 27001/27002, GDPR rights, incident management phases, risk management process.
- IY5606: Smart card technology, EMV standards, SIM/USIM, TEEs (Intel SGX, ARM TrustZone), NFC, IoT security.
- Practice structured essay writing.

---

## 5. Recurring Question Patterns by Module

### CS3003 — IT Project Management (Every Year)
- EVM calculation (choose correct statement + justify)
- Critical path / network diagram (draw + identify critical path)
- Scenario-based PM decision (choose best option + justify)
- True/false statements with justification

### IY3501 — Security Management (Every Year)
- Define CIA triad / threat / vulnerability / attacker
- Risk management process description
- Case study analysis (BA, Yahoo, Ticketmaster breaches)
- Incident management 5 phases
- GDPR and data protection questions
- ISO 27001/27002 and Statement of Applicability

### IY3609 — Digital Forensics (Every Year)
- Storage forensics: FAT32 file recovery, cluster calculations
- Memory forensics: live imaging techniques, rootkit detection
- Legal matters: Daubert criteria, RIPA, Overseas Production Orders
- RAID configuration analysis (fault tolerance)
- Mobile forensics: unlocking devices, data extraction
- Network forensics: C2 detection, traffic analysis

### IY3612 — Critical Infrastructure Security (Every Year)
- ICS/SCADA attack scenarios (control loops, actuators, sensors)
- Network/graph modelling (BGP, Internet structure)
- Adversary modelling (MITRE ATT&CK, Attack Trees, ACTs)
- Dependency models (Inoperability I-O, graph algorithms)
- Cyber conflict and policy (nation-state scenarios)

### IY3660 — Applications of Cryptography (Every Year)
- 4-bit block cipher lookup table calculations (ECB/CBC/CTR)
- Formal security definitions (IND-CPA, UF-CMA, etc.)
- RSA / Diffie-Hellman descriptions and security analysis
- Hash functions and MACs (Merkle-Damgard, HMAC)
- 34-mark essay: TLS protocol OR Ruritania/BizCorpInc scenario
- Quantum computing threats to cryptography

### IY5606 — Embedded Technologies / Smart Cards (Every Year)
- Smart card technology fundamentals
- SIM/USIM and GSM/3G authentication
- TEEs (Intel SGX, ARM TrustZone)
- EMV payment system standards
- 25-mark system design scenario (NFC payments, biometric POS, etc.)
- IoT security considerations

---

*Report generated from analysis of 26 past exam papers across 6 modules (2019–2025).*
