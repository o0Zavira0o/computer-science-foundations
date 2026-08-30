---
id: NNE-0014
title: "Intracellular recording and patch clamp as a window into membrane voltage and currents"
track: neurotechnology-neural-engineering
level: L1
status: complete
curriculum_node: NNE-N-0014
concepts_introduced: ["NNE-C-0017"]
concepts_deepened: ["NNE-C-0007", "NNE-C-0008", "NNE-C-0012", "NNE-C-0016"]
concepts_used: ["NNE-C-0006", "NNE-C-0009", "NNE-C-0011", "NNE-C-0015"]
examples_added: ["NNE-EX-064", "NNE-EX-065", "NNE-EX-066", "NNE-EX-067", "NNE-EX-068"]
references_used: ["NNE-REF-060", "NNE-REF-061", "NNE-REF-062", "NNE-REF-063"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Intracellular recording and patch clamp as a window into membrane voltage and currents

## If you landed here directly

This lesson assumes `NNE-0013 — The electrode-tissue interface: charge transfer, impedance, and what an electrode actually senses`.

You should already know that an electrode is not an ideal transparent wire into biology. The interface, reference, amplifier, geometry, and tissue all participate in the measurement.

This lesson moves the measurement boundary across the cell membrane.

The central question is:

> what changes when the recording electrode gains electrical access to the inside of a cell rather than remaining outside it?

The central mental model is:

```text
extracellular recording
outside potential relative to a reference

intracellular recording
inside potential relative to outside

patch clamp
controlled electrical access through a glass pipette and membrane seal
```

By the end, you should be able to:

- distinguish extracellular potential from intracellular membrane potential;
- explain what a sharp intracellular electrode and a patch pipette physically access;
- explain why a high-resistance seal matters;
- distinguish cell-attached, whole-cell, inside-out, and outside-out patch configurations;
- distinguish current clamp from voltage clamp by the variable controlled and the response measured;
- use a minimal membrane-capacitance and ionic-current model;
- explain why command voltage is not automatically identical to membrane voltage;
- identify access or series resistance, capacitance, liquid-junction potential, dialysis, rundown, and space clamp as interpretation limits;
- distinguish single-channel current from whole-cell current;
- trace an intracellular measurement from membrane physiology to amplifier output;
- decide which configuration answers a stated biological question without treating one mode as universally best.

---

# Part I — The problem worth understanding

An extracellular electrode near a neuron can detect voltage changes produced by currents in the surrounding conductive medium.

But suppose the scientific question is different:

> what is the voltage difference directly across this cell's membrane?

The membrane potential is not the extracellular voltage at one point.

A simplified definition is:

$$ V_m = V_{inside}-V_{outside}. $$

To measure that quantity directly, the experiment needs electrical access to the cell interior and an external reference.

That change in access is profound.

You are no longer only asking what field reaches an electrode in tissue.

You are now perturbing and interrogating a microscopic electrical system whose membrane contains:

- capacitance;
- ion channels;
- pumps and transporters;
- synaptic conductances;
- spatially distributed dendrites and axons.

So intracellular electrophysiology is both a measurement technique and an intervention.

---

# Part II — Extracellular versus intracellular voltage

An extracellular recording usually measures a difference such as:

$$ V_{recorded}=V_{local}-V_{reference}. $$

An intracellular membrane-potential measurement aims at:

$$ V_m=V_{inside}-V_{outside}. $$

Those are different physical quantities.

This prevents a common mistake:

```text
large extracellular spike
≠
full action-potential membrane voltage
```

The extracellular waveform depends strongly on geometry, current-source distribution, tissue conduction, and referencing.

The intracellular waveform is much closer to the voltage across the membrane at the accessed region, but it is still measured through a real electrode and amplifier with nonidealities.

---

# Part III — Two broad intracellular strategies

Historically and experimentally, two useful families are:

```text
sharp intracellular electrode
and
patch-clamp pipette
```

A sharp electrode penetrates the membrane with a fine tip.

A patch pipette instead presses a polished glass opening against a small region of membrane and forms a very high-resistance seal.

Neither method is simply "better."

They differ in:

- electrical access resistance;
- mechanical perturbation;
- intracellular solution exchange;
- current resolution;
- stability;
- preparation requirements;
- suitability for particular cell sizes and questions.

The rest of this lesson focuses on patch clamp because its configurations make the measurement logic especially explicit.

---

# Part IV — The patch pipette is an electrical interface

A patch pipette is a glass micropipette filled with conductive solution.

A wire electrode in that solution connects the ionic current in the pipette to the electronic amplifier.

The simplified chain is:

```text
cell membrane
→ membrane patch / cell interior
→ pipette solution
→ electrode in pipette
→ headstage
→ amplifier
→ digitizer
```

The pipette tip is small enough to contact a microscopic membrane region.

Its resistance is not negligible.

Once the pipette has whole-cell access, this resistance becomes part of the series path between the cell and amplifier.

That fact will matter later when we discuss voltage error and bandwidth.

---

# Part V — Why the seal matters

If current can leak freely around the pipette rim, tiny membrane currents are mixed with a large uncontrolled shunt path.

Patch clamp therefore aims to form a very high-resistance seal between glass and membrane.

The classic improved patch-clamp method described gigaohm-scale seals, often called **gigaseals**.

A useful circuit intuition is:

```text
wanted path:
membrane patch → pipette

unwanted path:
solution around seal → pipette
```

Making seal resistance very large suppresses the unwanted path.

But a gigaseal is not a magical guarantee of perfect data.

Seal quality can change, mechanical drift can occur, and the cell can deteriorate.

---

# Part VI — Cell-attached configuration

Before rupturing the membrane beneath the pipette, the pipette can remain sealed to an intact patch.

This is the **cell-attached** configuration.

Conceptually:

```text
pipette
│
sealed membrane patch
│
intact cell interior
```

The membrane beneath the pipette remains intact.

This can allow recording of currents through channels in the patch while disturbing the intracellular environment less than whole-cell access.

However, the absolute transmembrane voltage across the patch may not be known exactly unless the cell's resting membrane potential is known.

So "less invasive electrically" can come with reduced control over another variable.

---

# Part VII — Whole-cell configuration

If the membrane patch beneath the pipette is ruptured while the outer seal remains high resistance, the pipette solution gains electrical continuity with the cell interior.

This is the **whole-cell** configuration.

The simplified path becomes:

```text
amplifier
↕
pipette
↕
cell interior
↕
cell membrane
↕
extracellular bath
```

Whole-cell recording can measure membrane voltage in current clamp or membrane current in voltage clamp.

But the word "whole-cell" does not mean every part of a spatially extended neuron is perfectly controlled.

That distinction becomes critical for dendrites and axons.

---

# Part VIII — Excised patches

Patch clamp can also physically isolate a membrane patch.

Two important configurations are:

- **inside-out**;
- **outside-out**.

The names describe which membrane face is exposed to the bath.

## Inside-out

After forming a cell-attached patch, the pipette can be withdrawn so the membrane patch is excised with its intracellular face exposed to the bath.

This is useful when the experimenter wants to manipulate the cytoplasmic side of channels.

## Outside-out

After whole-cell access, withdrawing the pipette can allow a small patch to reseal with its extracellular face exposed to the bath.

This is useful when extracellular ligands or transmitters are the manipulated variable.

The core reasoning rule is:

> configuration determines which side of the membrane the experimenter can control directly.

---

# Part IX — Single-channel versus whole-cell current

A tiny membrane patch may contain one or a few active channels.

A single open channel can produce a discrete current event.

At a simple level:

$$ i = g(V_m-E_{rev}), $$

where:

- $i$ is single-channel current;
- $g$ is channel conductance in an open state;
- $V_m$ is membrane voltage;
- $E_{rev}$ is the channel's reversal potential under the stated ionic conditions.

A whole-cell current is an aggregate across many channels and membrane regions.

So:

```text
single-channel event
≠
whole-cell macroscopic current
```

The macroscopic current depends on channel number, open probability, conductance, driving force, and spatial distribution.

---

# Part X — Current clamp: inject current, observe voltage

In current clamp, the experiment controls or commands current and measures voltage response.

The conceptual loop is:

```text
specified injected current
→ cell membrane and conductances
→ resulting membrane voltage
→ amplifier measurement
```

For example, a positive current pulse may depolarize a neuron enough to trigger action potentials.

Current clamp is well suited to questions such as:

- what is the resting membrane potential?
- how does voltage respond to current input?
- what is input resistance near rest?
- does the neuron fire, and with what pattern?
- how do synaptic inputs shape subthreshold voltage?

The experiment does not hold voltage fixed.

Voltage is the response variable.

---

# Part XI — Voltage clamp: command voltage, observe current

In voltage clamp, the feedback amplifier attempts to hold membrane voltage near a commanded value.

It supplies whatever current is needed, within the limits of the system, to oppose membrane-current-driven voltage changes.

The conceptual loop is:

```text
voltage command
→ compare command with measured voltage
→ feedback amplifier injects current
→ membrane voltage moves toward command
→ injected current is measured
```

The measured clamp current can be used to infer membrane currents under stated conditions.

This is not passive observation.

Voltage clamp is a **closed-loop control experiment**.

That connects directly back to `NNE-0011`.

---

# Part XII — A minimal membrane equation

A useful lumped electrical model treats the membrane as a capacitor plus ionic-current pathways.

At a simple level:

$$ I_{inj}=C_m\frac{dV_m}{dt}+I_{ion}. $$

Here:

- $I_{inj}$ is current delivered through the recording system;
- $C_m$ is membrane capacitance;
- $dV_m/dt$ is the membrane-voltage rate of change;
- $I_{ion}$ collects ionic currents through membrane pathways.

This is a model, not a complete cell.

It helps separate two reasons current can flow:

```text
charging the membrane capacitance
and
moving ions through membrane conductances
```

During a fast voltage step, capacitive current can be prominent even before the ionic current of interest settles.

---

# Part XIII — Worked example 1: current clamp and membrane resistance

Suppose a neuron near rest behaves approximately linearly over a small range.

A $50$ pA current step produces a $5$ mV steady voltage change.

Using the local Ohmic approximation:

$$ R_{in}=\frac{\Delta V}{\Delta I}. $$

Therefore:

$$ R_{in}=\frac{5\ \mathrm{mV}}{50\ \mathrm{pA}}=100\ \mathrm{M\Omega}. $$

This is `NNE-EX-064`.

The interpretation is intentionally limited.

It estimates input resistance around that operating condition.

It does not prove that the neuron is a single linear resistor over all voltages or times.

Voltage-dependent channels can make the response nonlinear.

---

# Part XIV — Capacitance creates transients

If the membrane were only a resistor, a voltage command would produce an instantaneous steady current.

Because membrane capacitance stores charge, a voltage step produces transient capacitive current.

For an ideal capacitor:

$$ I_C=C\frac{dV}{dt}. $$

A rapid change in voltage therefore produces a large brief current proportional to capacitance and rate of change.

The observed transient also contains effects from:

- access resistance;
- pipette capacitance;
- amplifier compensation;
- filtering;
- cell geometry.

So a transient is informative, but it must be interpreted through the measurement circuit.

---

# Part XV — Access resistance is part of the experiment

In whole-cell mode, current travels through the pipette and access opening before reaching the cell interior.

This path has finite resistance, often called **access resistance** or **series resistance** in the measurement model.

A simplified circuit is:

```text
voltage source / amplifier
→ R_s
→ cell membrane
```

If current $I$ flows through $R_s$, a voltage drop develops.

A first-order estimate is:

$$ \Delta V_s=I R_s. $$

Therefore the commanded voltage and actual membrane voltage need not be identical.

---

# Part XVI — Worked example 2: series-resistance voltage error

Suppose a voltage-clamp experiment produces $2$ nA of current while uncompensated series resistance is $10$ MΩ.

The simple Ohmic estimate is:

$$ \Delta V_s=(2\ \mathrm{nA})(10\ \mathrm{M\Omega})=20\ \mathrm{mV}. $$

This is `NNE-EX-065`.

The lesson is not that the true error must equal exactly $20$ mV in every real experiment.

Modern amplifiers use compensation, cells are not ideal lumped circuits, and direct measurements can differ from simple estimates.

The lesson is:

> finite access resistance means voltage control must be validated rather than assumed.

---

# Part XVII — Series resistance also limits speed

Access resistance and membrane capacitance form a time constant.

A simplified estimate is:

$$ \tau=R_s C_m. $$

If $R_s$ or $C_m$ is large, the clamp cannot change membrane voltage arbitrarily fast.

This matters when the biological current itself changes rapidly.

The measurement system can blur a fast process before it is analyzed computationally.

This reconnects to bandwidth from `NNE-0012`.

---

# Part XVIII — Pipette capacitance and compensation

The glass pipette and nearby conductive solution form parasitic capacitances.

A change in command voltage can therefore drive current that is not membrane ionic current.

Amplifiers often provide capacitance compensation controls.

The conceptual goal is to reduce predictable electrode or pipette transients without making the feedback system unstable.

Compensation is not free.

Too aggressive feedback can cause oscillation or ringing.

So compensation settings are part of the measurement method and should be documented.

---

# Part XIX — Voltage clamp is limited by space clamp

A neuron is not usually an isopotential sphere.

It may have long dendrites and an axon.

A somatic patch electrode measures and controls voltage most directly near the access point.

Distant membrane regions are connected through intracellular resistance.

Therefore:

```text
command voltage at soma
≠
perfectly identical voltage at every dendritic location
```

This is the **space-clamp problem**.

A recorded current can contain contributions from regions whose voltage is not perfectly controlled.

This is one reason morphology matters in electrophysiology.

---

# Part XX — Worked example 3: why distal current can break the simple clamp picture

Imagine a neuron with a soma connected to a long dendrite.

The amplifier holds the somatic measurement near $-70$ mV.

A large synaptic conductance opens far out on the dendrite.

Current must travel through the dendritic cable before reaching the soma and clamp electrode.

The distal membrane can deviate from $-70$ mV even while the somatic voltage looks well controlled.

This is `NNE-EX-066`.

The key failure mode is:

> good control at the electrode does not prove good voltage control everywhere in an extended neuron.

---

# Part XXI — Whole-cell access changes intracellular chemistry

When the pipette solution communicates with the cell interior, molecules can diffuse between pipette and cytoplasm.

This can be useful.

The experimenter can introduce:

- dyes;
- buffers;
- ATP or other constituents;
- blockers;
- molecular probes.

But it also perturbs the cell.

Small endogenous molecules may wash out or become diluted.

Thus whole-cell recording can produce **dialysis** of the intracellular environment.

The cell being measured can gradually become different from the unperturbed cell that existed before break-in.

---

# Part XXII — Rundown and time dependence

Measured currents can decrease or otherwise change during a recording.

Possible causes include:

- channel modulation;
- metabolic change;
- intracellular dialysis;
- seal deterioration;
- access-resistance drift;
- true biological adaptation.

A declining current is therefore not automatically "channel rundown" in a uniquely identified mechanistic sense.

Time is an experimental variable.

Repeated protocols should consider order, baseline stability, and recording duration.

---

# Part XXIII — Junction potentials and reference potentials

Two ionic solutions with different compositions can create a **liquid junction potential** at their boundary because ions have different mobilities.

In patch clamp, the pipette solution and bath solution are often chemically different.

A junction potential can therefore offset the voltage scale.

The important reasoning pattern is:

```text
reported command / measured voltage
=
biological voltage
+ reference and junction contributions
+ instrument offsets
```

The exact correction depends on solutions and conventions.

A voltage value without reference and solution context is incomplete.

---

# Part XXIV — Current direction and sign conventions

Electrophysiology papers may use sign conventions such as inward current being negative and outward current positive.

But sign conventions are definitions tied to the measurement orientation.

Before interpreting a trace, ask:

- what current direction is defined as positive?
- what is the voltage reference?
- what is the holding potential?
- which ions and reversal potentials are relevant?

Never infer "excitation" or "inhibition" from current sign alone without the electrochemical context.

---

# Part XXV — Worked example 4: reversal potential reasoning

Suppose a channel population is studied under voltage clamp.

At holding potentials below a certain voltage, the measured channel-associated current is inward under the stated sign convention.

Above that voltage, it is outward.

Near one voltage, the net current crosses zero.

That voltage is an experimentally relevant **reversal potential** for the measured conductance under those ionic conditions.

This is `NNE-EX-067`.

The zero crossing does not mean channels are closed.

It can mean opposing ionic driving forces balance so net current is zero.

---

# Part XXVI — Cell-attached, whole-cell, and excised patches answer different questions

A useful decision table is:

| Configuration | Membrane continuity | Strongest access | Typical question |
|---|---|---|---|
| Cell-attached | Cell largely intact | Channels in sealed patch | Channel activity with less intracellular disturbance |
| Whole-cell | Patch ruptured | Cell interior and aggregate membrane response | Membrane voltage, firing, macroscopic currents |
| Inside-out | Patch excised | Intracellular membrane face | Cytoplasmic regulation of channels |
| Outside-out | Patch excised/resealed | Extracellular membrane face | Ligand or transmitter effects on extracellular face |

These are conceptual distinctions.

Exact protocols vary by preparation and experimental purpose.

---

# Part XXVII — Worked example 5: choose the configuration from the question

Consider four questions:

1. Does extracellular ATP change a receptor channel quickly?
2. Does a cytoplasmic second messenger alter channel opening?
3. What is the neuron's subthreshold membrane response to injected current?
4. How often does one channel open while keeping the cell interior relatively intact?

A reasonable first mapping is:

```text
1 → outside-out
2 → inside-out
3 → whole-cell current clamp
4 → cell-attached
```

This is `NNE-EX-068`.

The point is not memorizing a lookup table.

The point is matching the **controlled side, measured variable, and biological perturbation** to the question.

---

# Part XXVIII — What patch clamp actually measures

Patch clamp does not directly reveal abstract entities such as "excitability" or "synaptic strength."

It produces electrical measurements under a defined configuration.

The inference chain is:

```text
membrane currents and voltages
→ electrode/pipette circuit
→ amplifier feedback and compensation
→ analog filtering
→ digitized voltage/current traces
→ extracted features
→ biological interpretation
```

Every arrow can add assumptions.

This is the same measurement-chain discipline introduced in `NNE-0009`, now at a deeper L1 level.

---

# Part XXIX — What voltage clamp can and cannot identify

Voltage clamp can isolate and characterize currents when experimental conditions make the interpretation sufficiently controlled.

But a current trace alone does not uniquely identify:

- one molecular channel type;
- one anatomical location;
- one signaling pathway;
- one causal mechanism.

Researchers often combine voltage clamp with:

- pharmacology;
- genetic manipulation;
- ion substitution;
- kinetic analysis;
- morphology;
- imaging.

Mechanistic identification comes from converging evidence, not from the clamp mode alone.

---

# Part XXX — What current clamp can and cannot identify

Current clamp is powerful for observing how membrane voltage evolves during injected current and synaptic activity.

It can reveal:

- resting voltage;
- action-potential thresholds and shapes;
- firing patterns;
- subthreshold responses;
- approximate input resistance;
- time-dependent membrane behavior.

But one voltage trace does not uniquely decompose all underlying conductances.

Different combinations of channel properties can produce similar voltage behavior.

Again:

```text
measurement
≠
unique mechanism
```

---

# Part XXXI — A quality-control checklist

Before interpreting a whole-cell recording, ask:

1. Was a high-quality seal obtained?
2. What was access or series resistance?
3. Was it stable over time?
4. What compensation was applied?
5. What was the cell capacitance estimate?
6. Was voltage clamp likely limited by morphology or large currents?
7. What were pipette and bath solutions?
8. Was junction potential corrected or at least reported?
9. What was the reference electrode?
10. What filtering and sampling were applied?
11. Did the measured current or voltage remain stable enough for the analysis?
12. Could whole-cell dialysis alter the phenomenon?

A trace without acquisition context is not a complete measurement report.

---

# Part XXXII — Common failure modes

## Failure mode 1: "Patch clamp measures membrane voltage"

Too broad.

Cell-attached and voltage-clamp configurations may measure different variables.

Always specify configuration and clamp mode.

## Failure mode 2: "Voltage clamp fixes the voltage everywhere"

False for spatially extended cells.

Space clamp can be poor.

## Failure mode 3: "The command voltage is the membrane voltage"

Not automatically.

Series resistance and feedback limits can create error.

## Failure mode 4: "Whole-cell recording leaves the cell unchanged"

False.

Break-in creates intracellular access and can dialyze the cell.

## Failure mode 5: "A zero current means the channel is closed"

False.

Net current can be zero near reversal even with channels open.

## Failure mode 6: "A gigaseal guarantees perfect recording"

False.

Seal quality is one component of a larger measurement system.

## Failure mode 7: "One current trace proves one channel mechanism"

False.

Mechanistic identification requires additional evidence.

---

# Part XXXIII — Active exercise set

## Exercise A — Clamp-mode classification

For each experiment, identify the controlled variable and measured response:

1. inject $100$ pA and record the voltage trajectory;
2. hold near $-70$ mV and record the current required during a synaptic event.

## Exercise B — Series resistance

If $R_s=8$ MΩ and current magnitude is $1.5$ nA, calculate the simple $IR_s$ voltage-drop estimate.

Then state why the estimate is a diagnostic approximation rather than a perfect reconstruction of membrane voltage.

## Exercise C — Space clamp

Explain why a neuron with a long dendritic tree may be harder to voltage clamp than a compact spherical cell with similar membrane area.

## Exercise D — Configuration selection

Choose between cell-attached, whole-cell, inside-out, and outside-out for a question about a cytoplasmic modulator of one channel.

Explain the side of the membrane that must be experimentally accessible.

## Exercise E — Inference discipline

A current decreases by $40\%$ over ten minutes.

List at least four plausible experimental or biological explanations before claiming a molecular mechanism.

---

# Part XXXIV — Retrieval practice

Without looking back, answer:

1. What voltage difference defines membrane potential?
2. Why is intracellular voltage not the same quantity as an extracellular spike waveform?
3. What is the role of a gigaseal?
4. What distinguishes cell-attached from whole-cell access?
5. Which membrane face is exposed in inside-out versus outside-out patches?
6. In current clamp, what is commanded and what is observed?
7. In voltage clamp, what feedback action does the amplifier perform?
8. Why does series resistance create voltage-control error?
9. What is space clamp?
10. Why can whole-cell recording alter intracellular chemistry?
11. Why can net current be zero even if channels are open?
12. What acquisition details should accompany a biological interpretation?

---

# Part XXXV — Backward connections

This lesson deepens several earlier ideas.

From `NNE-0004` and `NNE-0005`:

```text
membrane voltage and ionic gradients
→ electrical excitability
```

From `NNE-0009`:

```text
biological source
→ sensor
→ electronics
→ data
→ inference
```

From `NNE-0011`:

```text
feedback
→ controller attempts to regulate a measured variable
```

Voltage clamp is a concrete laboratory feedback controller.

From `NNE-0012`:

```text
spatial access
bandwidth
invasiveness
stability
safety
```

are coupled tradeoffs rather than independent scores.

From `NNE-0013`:

```text
electrode interface
impedance
reference
amplifier loading
```

remain part of the measurement even after we gain intracellular access.

---

# Part XXXVI — Forward connection

The next canonical lesson is:

`NNE-N-0015 — Extracellular spikes, multi-unit activity, and local field potentials`.

That lesson moves the electrode back outside cells, but with a much deeper question than before:

```text
intracellular membrane events
→ transmembrane currents
→ extracellular fields
→ spikes / multi-unit activity / local field potentials
```

Understanding intracellular measurements first gives us a reference for what extracellular electrodes do **not** measure directly.

---

# Compact summary

An intracellular recording gains electrical access to the cell interior so that membrane voltage and membrane-current behavior can be measured far more directly than with an extracellular electrode.

Patch clamp achieves high-resolution access by sealing a glass pipette to a small membrane region. Different configurations expose different membrane faces and perturb the cell differently.

Current clamp commands current and observes voltage. Voltage clamp uses feedback to command voltage and observes the current required to maintain that voltage, within the limits of access resistance, capacitance, feedback bandwidth, and cell geometry.

Whole-cell patch clamp is powerful but not transparent: series resistance, space clamp, junction potentials, pipette capacitance, intracellular dialysis, rundown, and referencing all affect interpretation.

The engineering habit to keep is:

> specify the configuration, controlled variable, measured variable, circuit limits, and biological inference separately.

---

# References used in this lesson

- `NNE-REF-060` — Neher and Sakmann (1976), single-channel currents recorded from denervated frog muscle fibres.
- `NNE-REF-061` — Hamill et al. (1981), improved patch-clamp techniques and high-resistance seals.
- `NNE-REF-062` — Noguchi, Ikegaya, and Matsumoto (2021), review of in vivo whole-cell patch-clamp methods.
- `NNE-REF-063` — Gray and Santin (2023), direct analysis of series-resistance voltage errors in whole-cell voltage clamp.
