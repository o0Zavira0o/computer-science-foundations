---
id: NNE-0015
title: "Extracellular spikes, multi-unit activity, and local field potentials"
track: neurotechnology-neural-engineering
level: L1
status: complete
curriculum_node: NNE-N-0015
concepts_introduced: ["NNE-C-0018"]
concepts_deepened: ["NNE-C-0008", "NNE-C-0010", "NNE-C-0011", "NNE-C-0012", "NNE-C-0016", "NNE-C-0017"]
concepts_used: ["NNE-C-0006", "NNE-C-0009", "NNE-C-0015"]
examples_added: ["NNE-EX-069", "NNE-EX-070", "NNE-EX-071", "NNE-EX-072", "NNE-EX-073"]
references_used: ["NNE-REF-041", "NNE-REF-044", "NNE-REF-064", "NNE-REF-065", "NNE-REF-066"]
last_reviewed: 2026-08-30
version_sensitive: false
review_after: null
---
# Extracellular spikes, multi-unit activity, and local field potentials

## If you landed here directly

This lesson assumes `NNE-0014 — Intracellular recording and patch clamp as a window into membrane voltage and currents`.

You should already understand two different measurement boundaries:

```text
intracellular recording
inside potential relative to outside

extracellular recording
outside potential relative to a reference
```

You should also remember from `NNE-0013` that an electrode is not an ideal transparent wire into biology. Tissue, geometry, the electrode interface, the reference, and the amplifier all participate in the recorded voltage.

This lesson asks the next question:

> when an electrode stays outside cells, what biological activity can appear in the extracellular voltage, and what do terms such as spike, single unit, multi-unit activity, and local field potential actually mean?

The central mental model is:

```text
transmembrane currents
→ extracellular current flow
→ conductive tissue + source geometry
→ electrode position + reference
→ measured extracellular voltage
→ acquisition and analysis choices
→ spikes, putative units, multi-unit representations, and field-potential representations
```

The most important discipline is:

> an extracellular electrode does not read a neuron's membrane voltage from the outside.

It measures a potential difference produced by currents flowing through the extracellular medium.

---

# Part I — The problem worth understanding

Suppose one microelectrode is placed in neural tissue.

The recorded trace may contain:

- brief, sharp transients associated with nearby action potentials;
- slower fluctuations related to coordinated transmembrane currents in neural populations;
- activity from multiple cells at once;
- contributions from distant sources through volume conduction;
- stimulus artifacts, movement artifacts, noise, and interference;
- a reference-electrode contribution.

The instrument therefore does **not** hand us labels such as:

```text
neuron 17 spike
neuron 42 spike
local synaptic input
inhibition
excitation
```

It gives us voltage as a function of time.

The labels come later, after biological reasoning and signal processing.

That distinction is the foundation of this lesson.

---

# Part II — What an extracellular electrode actually measures

## Voltage is a difference

A recording channel measures a potential difference.

A simplified notation is:

$$ V_{\mathrm{rec}}(t)=\phi_{\mathrm{site}}(t)-\phi_{\mathrm{ref}}(t). $$

Here:

- $\phi_{\mathrm{site}}$ is the potential at the recording site;
- $\phi_{\mathrm{ref}}$ is the potential at the reference;
- neither quantity is automatically zero;
- the measured waveform depends on both.

This is the same measurement discipline introduced in `NNE-0013`.

---

## Neural currents create extracellular potentials

Ionic current crosses neuronal membranes during:

- action potentials;
- synaptic transmission;
- voltage-gated subthreshold currents;
- calcium events;
- afterpotentials;
- other active and passive membrane processes.

Those transmembrane currents require return-current paths through the surrounding conductive medium.

At any extracellular location, contributions from many current sources and sinks can superimpose.

So the recording problem is fundamentally a **source-superposition problem**.

---

# Part III — A minimal volume-conductor intuition

A highly simplified point-current source in an infinite homogeneous ohmic conductor gives a useful intuition:

$$ \phi(r)=\frac{I}{4\pi\sigma r}. $$

where:

- $I$ is source current;
- $\sigma$ is conductivity;
- $r$ is distance from the idealized point source.

This equation is **not** a full neuron model.

Real neural sources are distributed across membranes, include simultaneous sinks and sources, and have complex morphology and orientation.

The useful lesson is only:

```text
current source properties
+ conductive medium
+ geometry
+ observation point
→ extracellular potential
```

A real neuron cannot generally be replaced by one scalar current at one point without losing important spatial information.

---

# Part IV — Why source geometry matters

Two neural populations can move similar amounts of transmembrane current and still generate very different extracellular potentials.

Why?

Because cancellation and reinforcement depend on how sinks and sources are arranged in space.

Consider two simplified cases:

```text
case A
nearby sources and sinks arranged so their fields cancel strongly

case B
sources and sinks arranged so their fields reinforce over part of space
```

Equal total cellular activity does not imply equal measured field amplitude.

This is why extracellular amplitude cannot be interpreted as a one-number measure of "how active the brain is."

---

# Part V — From an intracellular action potential to an extracellular spike

`NNE-0005` introduced the action potential as a regenerative membrane event.

`NNE-0014` showed how intracellular recording can observe membrane voltage directly relative to the extracellular space.

Extracellular recording sees something different.

During an action potential:

```text
voltage-gated conductances change
→ ionic currents cross membrane
→ current enters and leaves extracellular space at different membrane locations and times
→ extracellular potential changes around the cell
```

A nearby electrode may therefore observe a brief waveform called an **extracellular spike**.

The extracellular spike is a field signature of transmembrane current flow.

It is not a shrunken copy of the intracellular voltage waveform.

---

# Part VI — Why extracellular spike shape depends on position

The same neuron can produce different extracellular waveforms at different electrode sites.

Relevant factors include:

- distance to the active membrane;
- position relative to soma, dendrites, and axon;
- which membrane compartments dominate current at each moment;
- orientation of the neuron relative to the electrode;
- conductivity and boundaries in the surrounding medium;
- reference geometry;
- front-end transfer characteristics.

This means:

```text
same neuron
+ same action potential
+ different electrode position
→ different extracellular waveform
```

Gold and colleagues showed with modeling constrained by simultaneous intracellular and extracellular recordings that extracellular action-potential waveform and amplitude vary with electrode position relative to the cell.

The waveform therefore contains spatial and biophysical information, but interpreting that information requires a model.

---

# Part VII — Worked example NNE-EX-069: one neuron, two electrodes

Imagine a neuron produces the same intracellular action potential on two trials.

Two extracellular electrodes are positioned differently:

```text
site A
close to the soma

site B
farther away and displaced toward an axonal direction
```

Suppose the observations are:

```text
site A
large biphasic transient

site B
smaller transient with a different relative positive/negative shape
```

What can we conclude?

We should **not** conclude that the neuron generated two different intracellular action potentials.

A cleaner interpretation is:

```text
same biological spike
→ different spatial sampling of its transmembrane-current field
→ different extracellular waveforms
```

This deepens `NNE-EX-025`, which already established that an extracellular spike is not a scaled intracellular action potential.

---

# Part VIII — One electrode can see more than one neuron

An extracellular electrode usually sits in a field generated by many cells.

If several neurons are close enough and produce sufficiently large transients, one channel can contain spikes from multiple sources.

The raw trace may therefore look conceptually like:

```text
neuron A contribution
+
neuron B contribution
+
neuron C contribution
+
field fluctuations
+
noise and artifacts
→ one measured voltage trace
```

The electrode does not physically label which neuron produced which transient.

Source identity is an inference problem.

---

# Part IX — What "single-unit activity" actually means

A **unit** in extracellular electrophysiology is an operational signal-analysis object.

When detected events can be attributed with sufficient confidence to one putative neural source, researchers may call the result **single-unit activity**.

The word **putative** matters.

A useful mental model is:

```text
extracellular voltage
→ candidate spike events
→ waveform/features/context
→ attribution procedure
→ putative unit
```

At this stage we are not teaching the detailed algorithms used for event detection or spike sorting. Those belong later in `NNE-N-0027`.

For now, the critical idea is:

> "single unit" describes an attribution supported by the recording and analysis, not a magical wire connected to exactly one known neuron.

---

# Part X — A detected spike is not automatically a known neuron

Suppose an event crosses a threshold and has a stereotyped waveform.

That tells us useful things.

It does **not** automatically tell us:

- the neuron's anatomical identity;
- its molecular cell type;
- its projection target;
- whether another neuron sometimes produces a similar waveform;
- whether waveform drift occurs over time;
- whether the event assignment is perfect.

These questions require additional evidence.

Extracellular identity is therefore an inference with uncertainty.

---

# Part XI — What multi-unit activity means

**Multi-unit activity**, or MUA, refers broadly to extracellular spiking activity that represents contributions from more than one neuron rather than one confidently isolated putative unit.

But the term is used operationally in more than one way.

Depending on the study, MUA may refer to:

- all threshold-crossing spike-like events on a channel;
- events intentionally not separated into single units;
- pooled activity from multiple detected units;
- a high-frequency signal envelope used as a population-spiking proxy.

Therefore:

> when a paper says "MUA," ask how MUA was defined in that experiment.

The label alone is not enough.

---

# Part XII — What MUA is not

MUA is not:

```text
one biological cell type
```

It is not necessarily:

```text
the arithmetic average of several spike waveforms
```

It is not automatically:

```text
firing rate
```

And it is not a physical substance that exists separately in tissue.

It is a representation constructed from an extracellular recording under a specified analysis rule.

---

# Part XIII — Worked example NNE-EX-070: ambiguous attribution

Suppose two nearby neurons produce extracellular spikes with partially overlapping waveform shapes.

During one short interval, the recording contains six clear spike-like events.

However, the available evidence is insufficient to assign each event reliably to neuron A or neuron B.

A responsible report may say:

```text
six detected multi-unit events occurred
```

rather than pretending:

```text
neuron A fired four times
neuron B fired twice
```

The lesson is:

```text
event detection
≠
unique source identity
```

This is not a failure of electrophysiology.

It is an honest statement about what the measurement supports.

---

# Part XIV — What a local field potential is

A **local field potential** is an extracellularly recorded potential dominated, in common operational use, by slower components of population-level transmembrane-current activity than those used to identify extracellular spikes.

Several biological processes can contribute, including:

- synaptic transmembrane currents;
- active membrane currents;
- afterpotentials;
- synchronized population currents;
- other slower current components.

The important phrase is:

> extracellularly recorded potential.

LFP is not a direct recording of synaptic input, firing rate, excitation, inhibition, or one cell's membrane voltage.

---

# Part XV — LFP is a composite signal

Many current sources contribute simultaneously.

A conceptual model is:

```text
source 1
+
source 2
+
source 3
+
...
+
volume-conducted remote activity
→ potential at recording site
```

The measured LFP is therefore composite.

Its interpretation depends on:

- source geometry;
- synchrony;
- cellular morphology;
- population architecture;
- source distance;
- reference location;
- acquisition and filtering choices.

This is why the same LFP amplitude can arise from different underlying source configurations.

---

# Part XVI — "Local" does not guarantee local origin

The word *local* can be misleading.

An electrode measures fields that reach it.

It does not contain a built-in spatial gate that accepts only sources within a fixed radius.

Herreras emphasized that source geometry and volume conduction can make field potentials surprisingly nonlocal and can even place the largest measured potential away from the physical center of a complex source.

The figure below is a useful spatial anchor.

![Source configuration changes the spatial reach of extracellular field potentials](https://www.frontiersin.org/files/Articles/205896/xml-images/fncir-10-00101-g0005.webp)

*Visual anchor — source configuration changes the spatial reach of extracellular field potentials. Focus on the contrast among point-like, distributed, laminar, and curved source configurations; do not treat the sketch as a universal decay law for all neural tissue. Source: [Herreras, “Local Field Potentials: Myths and Misunderstandings,” Figure 5](https://www.frontiersin.org/journals/neural-circuits/articles/10.3389/fncir.2016.00101/full), Oscar Herreras, Frontiers in Neural Circuits (2016), CC BY 4.0. Registry: `NNE-REF-066`.*

This visual matters because "distance from the electrode" alone does not determine contribution.

---

# Part XVII — Electrode size does not define the biological listening radius

A small electrode contact may improve some aspects of spatial discrimination.

But it does not create a hard spherical boundary such as:

```text
inside 100 micrometers → recorded
outside 100 micrometers → invisible
```

Spatial contribution depends on source strength and geometry as well as electrode and tissue properties.

Therefore:

```text
small contact
≠ guaranteed purely local LFP
```

This connects directly to the coupled tradeoffs introduced in `NNE-0012`.

---

# Part XVIII — LFP polarity does not directly label excitation or inhibition

A common mistake is:

```text
negative LFP = excitation
positive LFP = inhibition
```

That rule is not generally valid.

Polarity depends on:

- where current enters and leaves cells;
- source orientation;
- recording position;
- the reference;
- geometry of active populations;
- which processes overlap in time.

An excitatory synaptic process can create different extracellular signs at different locations around a structured source.

Likewise, inhibitory currents do not map universally to one sign.

To infer cellular meaning from field polarity, one needs spatial and biophysical context.

---

# Part XIX — Reference choice still matters

`NNE-0013` showed that the reference is part of a differential measurement.

That remains true for both spikes and LFPs.

If the reference contains neural or artifactual activity, then:

$$ V_{\mathrm{rec}}(t)=\phi_{\mathrm{site}}(t)-\phi_{\mathrm{ref}}(t) $$

changes even when the local source near the signal electrode does not.

Re-referencing can therefore change:

- amplitude;
- polarity;
- apparent synchrony;
- common-mode structure;
- the apparent spatial pattern across channels.

A reference is not an invisible zero.

---

# Part XX — One broadband recording, multiple representations

A neural recording system can acquire one broadband extracellular voltage and then construct different analysis views.

Conceptually:

```text
broadband extracellular voltage
        |
        +→ fast transient analysis → extracellular spikes / units / MUA
        |
        +→ slower field analysis   → LFP representation
```

This is a useful engineering separation.

But the branches are not two completely independent biological signals that existed in separate wires before measurement.

They are representations of overlapping physical extracellular activity under different analysis choices.

---

# Part XXI — Frequency boundaries are operational, not biological walls

It is common to use different frequency ranges for spike and LFP analysis.

That is useful.

But no universal biological law says:

```text
below one exact cutoff = LFP biology
above one exact cutoff = spike biology
```

Why not?

Because:

- extracellular action-potential waveforms have spectral spread;
- population events can contain relatively fast components;
- filters have transition bands and phase/amplitude effects;
- different studies use different operational definitions;
- the physical sources can overlap.

Detailed filter design belongs later in `NNE-N-0026`.

The point here is conceptual:

> a frequency cutoff is part of the measurement-analysis definition.

---

# Part XXII — Worked example NNE-EX-071: one trace, two analysis views

Suppose a broadband intracortical recording contains:

- sharp transients lasting around a millisecond;
- a slower oscillatory fluctuation over tens to hundreds of milliseconds.

Two analysis pipelines are created:

```text
pipeline A
emphasizes fast transient events
→ spike/event representation

pipeline B
emphasizes slower extracellular fluctuations
→ LFP representation
```

Both pipelines begin from the same measured voltage.

The correct conclusion is:

```text
one measurement
→ different operational representations
```

not:

```text
the electrode physically recorded two independent substances called spikes and LFP
```

---

# Part XXIII — Spikes and LFP are related but not redundant

Spiking and field activity can correlate because they arise within the same neural network.

But correlation does not make them interchangeable.

Extracellular spikes emphasize brief transmembrane currents associated with action potentials from sufficiently nearby detectable neurons.

LFPs emphasize collective field structure generated by many transmembrane currents, often including synaptic and other subthreshold processes.

The two can therefore carry overlapping but different information about network state.

---

# Part XXIV — LFP is not simply low-pass firing rate

Imagine a population whose neurons become strongly synchronized in their transmembrane currents while average firing rate changes only slightly.

The field potential can change markedly because synchrony and geometry change how currents sum and cancel.

Conversely, firing rate can increase without producing a proportionally large LFP if the relevant currents cancel spatially or are poorly aligned for the recording geometry.

Therefore:

```text
LFP amplitude
≠ simple low-pass transform of firing rate
```

This distinction is essential before later studying rhythms and spectra.

---

# Part XXV — Worked example NNE-EX-072: the polarity trap

Suppose the same organized synaptic event is measured at two depths in a layered neural structure.

At site A, the event appears negative relative to the chosen reference.

At site B, it appears positive.

A naive interpretation would say:

```text
site A = excitation
site B = inhibition
```

That conclusion is not justified.

A better explanation is:

```text
one distributed source-sink pattern
+ different spatial observation points
+ one reference geometry
→ different measured polarity
```

Polarity becomes meaningful only after the source geometry and recording configuration are understood.

---

# Part XXVI — Worked example NNE-EX-073: spikes and LFP can dissociate

Consider two experimental conditions.

```text
Condition A
large increase in detected spike rate
small change in slow field amplitude

Condition B
small change in detected spike rate
large coherent field fluctuation
```

Neither condition is contradictory.

Condition A could occur when more neurons fire but their slower transmembrane currents do not become strongly aligned in a way that produces a large field at the electrode.

Condition B could occur when coordinated synaptic or other membrane currents become more spatially and temporally coherent without a large change in the detected spike count.

The lesson is:

```text
spiking output
and
field-potential structure
```

are related views of network activity, not duplicate measurements.

---

# Part XXVII — What a spike amplitude can and cannot tell you

A larger extracellular spike may suggest that the electrode is favorably positioned relative to a strong source.

But amplitude alone does not uniquely determine:

- neuron-to-electrode distance;
- neuron size;
- cell type;
- intracellular action-potential amplitude;
- orientation;
- recording quality.

Several factors change amplitude simultaneously.

This is an identifiability problem.

One observed number can be compatible with multiple underlying explanations.

---

# Part XXVIII — What LFP amplitude can and cannot tell you

A larger LFP means that the measured potential difference is larger under that recording configuration.

It does not by itself prove:

- more spikes occurred;
- more synapses were active;
- activity was more local;
- the source was closer;
- excitation increased;
- inhibition decreased;
- the tissue became more synchronous in one unique way.

A mechanistic interpretation requires additional spatial, temporal, and biological evidence.

---

# Part XXIX — Source superposition creates a cocktail-party problem

At one electrode, fields from many neural processes add together.

Conceptually:

$$ \phi_{\mathrm{site}}(t)=\sum_k \phi_k(t). $$

This equation is intentionally abstract.

Each $\phi_k$ represents the contribution of one source process under the chosen volume-conductor model.

The measurement contains the sum.

Recovering the individual sources from the sum is an inverse problem.

The answer may not be unique without extra spatial or model constraints.

This is why multichannel geometry becomes important in the next lesson.

---

# Part XXX — Current-source density is a different question

You may encounter **current-source density**, or CSD, in field-potential analysis.

CSD methods use spatially distributed voltage measurements and a model to estimate where net current sources and sinks may be located.

Do not confuse:

```text
LFP
measured extracellular potential
```

with:

```text
CSD
model-derived estimate of source/sink structure from spatial voltage data
```

A full treatment of CSD is beyond this lesson.

The important preview is that spatial sampling can help interpret a field that one channel alone cannot localize.

---

# Part XXXI — Single-unit, multi-unit, and LFP are not a quality ranking

It is tempting to imagine:

```text
single unit = best
multi-unit = worse
LFP = worst
```

That is not a valid universal ranking.

The appropriate representation depends on the question.

Examples:

- precise spike timing of one putative neuron may favor single-unit analysis;
- robust local population event rate may favor MUA;
- coordinated population dynamics may be visible in LFP;
- chronic applications may trade source specificity for stability.

The correct question is:

> which representation preserves the information needed for the scientific or engineering task?

---

# Part XXXII — The analysis object must match the claim

Suppose a study measures MUA but claims:

> neuron X increased its firing rate.

That claim is too specific unless the data support source identity.

Suppose another study measures LFP power and claims:

> local excitatory synaptic input doubled.

That claim is also too specific without additional evidence.

A disciplined hierarchy is:

```text
measured quantity
→ derived representation
→ supported inference
```

Never skip directly from a derived feature to a stronger biological claim than the measurement supports.

---

# Part XXXIII — A compact comparison

| Representation | What begins the chain | What the representation emphasizes | Major interpretation risk |
|---|---|---|---|
| Extracellular spike | brief extracellular voltage transient | action-potential-associated current field from a detectable nearby source | treating waveform as direct membrane voltage |
| Putative single unit | detected events plus attribution | events assigned to one putative source | treating inferred unit identity as known biological identity |
| Multi-unit activity | pooled or unresolved spike-related activity | local population spiking proxy under a stated operational definition | assuming one universal definition of MUA |
| Local field potential | slower extracellular potential representation | collective transmembrane-current field structure | assuming the signal is purely local or equals synaptic input/firing rate |

No row is a complete description of biology.

Each row is a measurement or analysis boundary.

---

# Part XXXIV — What we are deliberately not doing yet

## High-channel-count arrays

The next canonical lesson, `NNE-N-0016`, introduces microelectrode arrays and high-channel-count invasive recording.

That lesson will ask what changes when we sample extracellular space at many sites simultaneously.

---

## Detailed filtering

`NNE-N-0026` will treat filtering as an engineering operation with passbands, transition regions, phase, causality, and phenomenon-preservation constraints.

This lesson uses only the idea that analysis can emphasize different components.

---

## Spike sorting algorithms

`NNE-N-0027` will introduce event detection, thresholds, waveform features, clustering/template ideas, and the validation problem of spike sorting.

Here we only need the concept of putative source attribution.

---

## Spectra and time-frequency analysis

`NNE-N-0028` will treat spectra, rhythms, time-frequency representations, and oscillatory features.

Here we do not assign mechanisms to frequency bands.

---

# Part XXXV — Common failure modes

## Failure mode 1 — "An extracellular spike is a smaller intracellular action potential"

Wrong because extracellular voltage is generated by transmembrane current fields and depends strongly on geometry.

---

## Failure mode 2 — "One electrode records one neuron"

Wrong because one site can receive superimposed contributions from many neurons and other field sources.

---

## Failure mode 3 — "A detected spike identifies a known neuron"

Wrong because event detection and biological identity are different inferential steps.

---

## Failure mode 4 — "Single-unit means physically isolated from every other source"

Wrong because single-unit activity is an attribution supported by available evidence, not a proof that no other extracellular sources contributed to the channel.

---

## Failure mode 5 — "MUA has one universal definition"

Wrong because studies operationalize multi-unit activity differently.

Always inspect the method.

---

## Failure mode 6 — "MUA is the average waveform of several neurons"

Wrong because MUA commonly represents pooled or unresolved spike-related activity, not a required waveform average.

---

## Failure mode 7 — "LFP is low-pass firing rate"

Wrong because LFP reflects composite transmembrane-current fields whose amplitude and spatial reach depend on geometry and synchrony, not just spike count.

---

## Failure mode 8 — "LFP is purely local"

Wrong because volume-conducted remote sources can contribute substantially.

---

## Failure mode 9 — "Negative LFP means excitation"

Wrong without a spatial source model and reference context.

---

## Failure mode 10 — "Positive LFP means inhibition"

Wrong for the same reason.

---

## Failure mode 11 — "Larger LFP means more firing"

Wrong because the relationship between field amplitude and spiking depends on current-source geometry, synchrony, and the sampled network state.

---

## Failure mode 12 — "A smaller electrode automatically gives a more local LFP"

Wrong because biological source geometry and volume conduction remain part of the measurement.

---

## Failure mode 13 — "Spike band and LFP band are biologically separate signals before recording"

Wrong because they are analysis representations of overlapping extracellular electrical activity.

---

## Failure mode 14 — "A frequency cutoff reveals a unique biological mechanism"

Wrong because cutoffs are operational analysis choices and multiple biological processes can overlap spectrally.

---

# Part XXXVI — Active work

## Exercise A — identify the measured quantity

For each statement, decide whether it refers to:

```text
raw extracellular voltage
extracellular spike event
putative single unit
multi-unit representation
LFP representation
biological inference
```

Statements:

1. "The electrode voltage crossed -60 microvolts."
2. "A putative unit fired 12 detected events in one second."
3. "High-frequency threshold crossings increased after cue onset."
4. "The low-frequency extracellular potential became more negative."
5. "Excitatory synaptic input increased."

Then identify which statements require the strongest biological assumptions.

---

## Exercise B — same neuron, different waveform

A neuron produces a stable intracellular action potential.

An electrode is moved 50 micrometers.

The extracellular waveform changes strongly.

List at least four explanations that do **not** require the intracellular action potential itself to have changed.

---

## Exercise C — single unit or MUA?

A recording has clear spike-like events but two partially overlapping waveform families drift over time.

What evidence would you want before making a strong single-unit claim?

Do not design a complete sorting algorithm yet.

Focus on the evidence boundary.

---

## Exercise D — polarity

A field event is negative on one contact and positive on a nearby contact.

Explain why this observation alone cannot be translated into:

```text
excitation here
inhibition there
```

---

## Exercise E — local does not mean nearby only

Use the visual anchor from Herreras.

Describe how a distributed or curved source can produce a large field away from the physical center of active tissue.

Then explain why a fixed "listening radius" is not a universal property of an electrode.

---

## Exercise F — choose the representation

For each question, choose the most defensible starting representation and justify it:

1. Does one putative neuron's spike timing lock to a sensory event?
2. Does local population spiking increase after movement onset when unit isolation is unreliable?
3. Does a coordinated slow population field change before a behavioral transition?
4. Does one signal source have a known cellular identity?

The fourth question is intentionally different: an extracellular representation alone may not answer it.

---

# Part XXXVII — Retrieval practice

Without looking back, answer:

1. What physical quantity does an extracellular electrode measure?
2. Why is extracellular voltage not membrane voltage?
3. What creates extracellular current flow around neurons?
4. Why do contributions from different neural sources superimpose?
5. What does the simplified point-source equation teach, and what does it omit?
6. Why can the same neuron produce different extracellular spike waveforms at different electrode positions?
7. Why is an extracellular spike not a scaled intracellular action potential?
8. Why can one channel contain spikes from multiple neurons?
9. What does "putative single unit" mean?
10. Why is a detected spike not automatically a known biological neuron?
11. What is multi-unit activity?
12. Why must a paper define how MUA was operationalized?
13. What is a local field potential?
14. Why is an LFP composite?
15. Why can the word "local" be misleading?
16. Why does electrode size not define one universal listening radius?
17. Why does LFP polarity not directly label excitation or inhibition?
18. Why does the reference matter for LFP interpretation?
19. How can one broadband recording produce spike and LFP representations?
20. Why is a frequency cutoff an operational boundary rather than a biological wall?
21. Why is LFP not simply low-pass firing rate?
22. How can spike rate change strongly while LFP changes little?
23. How can LFP change strongly while detected spike rate changes little?
24. What does source superposition imply about inverse interpretation?
25. What is the conceptual difference between LFP and CSD?
26. Why are single-unit, MUA, and LFP not a simple quality ranking?
27. Why must the analysis object match the strength of the biological claim?
28. What topic is deliberately deferred to `NNE-N-0016`?
29. What topic is deliberately deferred to `NNE-N-0027`?
30. What topic is deliberately deferred to `NNE-N-0028`?

---

# Part XXXVIII — Backward connections

## Connection backward: NNE-0005

`NNE-0005` introduced action potentials as regenerative membrane events.

This lesson explains one way those events leave extracellular electrical signatures.

The chain becomes:

```text
action potential
→ transmembrane current
→ extracellular field
→ electrode waveform
```

---

## Connection backward: NNE-0007

`NNE-0007` moved from single neurons to populations and circuits.

That scale hierarchy matters here because:

```text
single-cell current fields
+
population geometry
+
coactivation
→ extracellular population field
```

---

## Connection backward: NNE-0008

`NNE-0008` distinguished biological events, measured signals, and derived features.

This lesson deepens that distinction:

```text
biological action potential
≠ extracellular spike waveform
≠ detected event
≠ putative unit identity
```

and:

```text
population current activity
≠ LFP feature
≠ biological mechanism inferred from that feature
```

---

## Connection backward: NNE-0009

`NNE-0009` established the neural measurement chain:

```text
source
→ tissue
→ sensor
→ electronics
→ data
→ inference
```

This lesson fills in one especially important source-to-sensor segment for extracellular electrophysiology.

---

## Connection backward: NNE-0013

`NNE-0013` established that the electrode-tissue interface and reference affect the measured waveform.

This lesson adds the biological field generators on the tissue side of that interface.

---

## Connection backward: NNE-0014

`NNE-0014` crossed the membrane with intracellular recording.

This lesson moves back outside the cell and uses intracellular understanding to explain what extracellular methods can and cannot infer.

Together:

```text
intracellular
membrane voltage / membrane current under controlled access

extracellular
spatially mixed potential generated by transmembrane currents in tissue
```

---

# Part XXXIX — Connection to linear algebra

A multichannel extracellular recording can be viewed abstractly as a mixture:

$$ \mathbf{v}(t)=A\mathbf{s}(t)+\mathbf{n}(t). $$

where:

- $\mathbf{s}(t)$ represents latent source processes;
- $A$ represents a geometry- and physics-dependent mixing relationship;
- $\mathbf{v}(t)$ is the measured channel vector;
- $\mathbf{n}(t)$ represents noise or unmodeled contributions.

This is only a conceptual linearized model.

Real neural tissue and measurement systems can violate its assumptions.

But it explains why source interpretation is related to mixing, identifiability, and inverse problems.

---

# Part XL — Forward connection

The next canonical lesson is:

`NNE-N-0016 — Microelectrode arrays and high-channel-count invasive recording`.

One extracellular site gives a spatially mixed view.

Many sites create new opportunities:

- compare waveforms across space;
- estimate propagation and source location more effectively;
- observe larger neural populations;
- exploit spatial structure;
- improve some forms of source attribution;
- study field gradients and spatial patterns.

But many channels also create new engineering problems:

- data rate;
- wiring and multiplexing;
- power;
- heat;
- crosstalk;
- channel failures;
- calibration;
- chronic stability;
- analysis scale.

That is the next step.

---

# Compact summary

Keep these statements:

```text
1. Extracellular electrodes measure potential differences, not membrane voltage.

2. Transmembrane currents generate extracellular fields.

3. Geometry, distance, orientation, tissue, reference, and superposition shape the waveform.

4. An extracellular spike is a current-field signature associated with an action potential.

5. A putative single unit is an inferred source attribution.

6. MUA is a study-specific representation of unresolved or pooled spike-related activity.

7. LFP is a composite extracellular field-potential representation, not a direct readout of one biological variable.

8. "Local" does not mean a fixed biological radius around the electrode.

9. LFP polarity alone does not identify excitation or inhibition.

10. Spike and LFP representations can come from one broadband recording and are related but not redundant.

11. Frequency boundaries are analysis choices, not universal biological walls.

12. Strong biological claims require stronger evidence than a waveform or derived feature alone.
```

---

# References used in this lesson

- **NNE-REF-041** — György Buzsáki, Costas A. Anastassiou, and Christof Koch, *The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes*, Nature Reviews Neuroscience 13, 407–420 (2012), DOI 10.1038/nrn3241. Used for the biophysical origin and superposition of extracellular fields and the relationship among spikes and field-potential measurements.
- **NNE-REF-044** — Hernan Gonzalo Rey, Carlos Pedreira, and Rodrigo Quian Quiroga, *Past, present and future of spike sorting techniques*, Brain Research Bulletin 119(Pt B), 106–117 (2015), DOI 10.1016/j.brainresbull.2015.04.007. Used for the distinction between extracellular mixtures, detected spikes, and putative unit attribution while deferring sorting algorithms to a later lesson.
- **NNE-REF-064** — Carl Gold, Darrell A. Henze, Christof Koch, and György Buzsáki, *On the Origin of the Extracellular Action Potential Waveform: A Modeling Study*, Journal of Neurophysiology 95(5), 3113–3128 (2006), DOI 10.1152/jn.00979.2005. Used for the dependence of extracellular action-potential waveform and amplitude on electrode position relative to the cell.
- **NNE-REF-065** — Gaute T. Einevoll, Christoph Kayser, Nikos K. Logothetis, and Stefano Panzeri, *Modelling and analysis of local field potentials for studying the function of cortical circuits*, Nature Reviews Neuroscience 14, 770–785 (2013), DOI 10.1038/nrn3599. Used for LFP as an extracellular population signal with multiple contributing neural processes and for disciplined biophysical interpretation.
- **NNE-REF-066** — Oscar Herreras, *Local Field Potentials: Myths and Misunderstandings*, Frontiers in Neural Circuits 10, 101 (2016), DOI 10.3389/fncir.2016.00101. Used for source-geometry, spatial-reach, polarity, volume-conduction, and locality cautions; Figure 5 is embedded as the lesson's verified visual anchor under CC BY 4.0.
