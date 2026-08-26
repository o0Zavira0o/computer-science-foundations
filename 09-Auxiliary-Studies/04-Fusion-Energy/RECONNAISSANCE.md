# Fusion Energy Curriculum Reconnaissance

**Track:** `fusion-energy` (`FUS`)
**Baseline audit date:** 2026-08-26
**Entry model:** zero subject-specific knowledge

## Why this track needs its own curriculum

Fusion energy is not one topic. A learner can understand the reaction equation and still misunderstand plasma confinement; can understand a confinement experiment and still misunderstand a power plant; or can read a gain headline and compare incompatible energy boundaries. The curriculum therefore treats fusion as a coupled chain from nuclear reaction physics to grid-level performance.

The first-order curriculum question is not “tokamak or laser?” It is:

> What physical and engineering claims must all be true at the same time for controlled fusion to become a useful energy system, and what evidence supports each claim?

## Baseline source classes

The audit uses multiple independent source classes rather than one project website:

- **ITER Organization** (`FUS-REF-001`, `FUS-REF-006`) for controlled-fusion fundamentals, D-T operation, plasma gain definitions, and the distinction between ITER’s experimental mission and electricity production.
- **U.S. Department of Energy, Office of Science** (`FUS-REF-002`) for an independent public-science description of fusion energy science and plasma control.
- **IAEA, _Fusion Physics_** (`FUS-REF-003`) as a comprehensive textbook/reference spanning the physics and major confinement approaches.
- **MIT OpenCourseWare** (`FUS-REF-004`) as an independent university-course coverage map for plasma and fusion topics.
- **Lawrence Livermore National Laboratory / NIF** (`FUS-REF-005`) for current, explicitly bounded inertial-confinement ignition and target-gain evidence.

The baseline therefore satisfies the repository rule that an audited track use at least three sources and at least two source classes.

## Coverage decisions

### 1. Start before plasma physics

The track assumes no prior nuclear physics. L0 introduces nuclei, isotopes, binding-energy bookkeeping, electrostatic repulsion, tunneling intuition, plasma, fusion fuels, the confinement requirement, and gain metrics before device detail.

### 2. Teach the system boundary before celebrating a number

“More energy out than in” is incomplete until the boundary is named. The curriculum distinguishes at least:

- fusion energy versus externally delivered plasma/target energy;
- plasma gain such as ITER’s `Q`;
- target gain used in inertial-confinement experiments;
- facility or engineering breakeven;
- gross versus net electric output of a hypothetical power plant.

This distinction is introduced in `FUS-0001`, deepened in `FUS-N-0008`, and revisited in plant-level and research-literacy nodes.

### 3. Keep magnetic and inertial confinement in the common core

Tokamaks are important but do not define the field. The graph gives magnetic-confinement geometry, tokamaks, stellarators, and inertial confinement their own nodes before advanced specialization.

### 4. Do not stop at plasma performance

A credible fusion-energy curriculum must include tritium, 14 MeV neutrons, activation and shielding, materials damage, plasma-facing components, blankets, heat extraction, superconducting magnets, cryogenics, vacuum, remote maintenance, safety, availability, recirculating power, and deployment constraints.

### 5. Separate stable foundations from a moving frontier

Basic nuclear and plasma concepts are relatively stable. Device records, project schedules, performance claims, regulatory status, and commercial projections are version-sensitive. Current-status material therefore uses dated references and `research/FRONTIER.json` has an explicit refresh date.

## Deliberate exclusions from the baseline

The curriculum does not treat company press releases, financing claims, projected commercialization dates, or a single device’s preferred metric as baseline authority. Those may become objects of analysis later, but they do not define the foundational graph.

Weapons design and operational weaponization are outside the educational scope of this track. Inertial-confinement material is limited to the physics and energy-system questions needed for fusion-energy literacy.

## Audit conclusion

The evidence baseline covers nuclear foundations, plasma physics, magnetic and inertial confinement, experimental measurement, reactor technology, whole-plant energy accounting, computational/research methods, and the major engineering constraints that separate fusion experiments from practical electricity production. No blocking coverage gap is recorded in `COVERAGE.json`.
