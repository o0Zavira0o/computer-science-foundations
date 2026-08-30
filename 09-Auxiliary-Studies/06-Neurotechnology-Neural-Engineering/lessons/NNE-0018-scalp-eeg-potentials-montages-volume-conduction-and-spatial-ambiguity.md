---
id: NNE-0018
title: "Scalp EEG: potentials, montages, volume conduction, and spatial ambiguity"
track: neurotechnology-neural-engineering
level: L1
status: complete
curriculum_node: NNE-N-0018
concepts_introduced: ["NNE-C-0021"]
concepts_deepened: ["NNE-C-0010", "NNE-C-0011", "NNE-C-0012", "NNE-C-0015", "NNE-C-0016", "NNE-C-0018", "NNE-C-0020"]
concepts_used: ["NNE-C-0009"]
examples_added: ["NNE-EX-084", "NNE-EX-085", "NNE-EX-086", "NNE-EX-087", "NNE-EX-088"]
references_used: ["NNE-REF-041", "NNE-REF-084", "NNE-REF-085", "NNE-REF-086", "NNE-REF-087", "NNE-REF-088", "NNE-REF-089", "NNE-REF-090"]
last_reviewed: 2026-08-30
version_sensitive: false
review_after: null
---
# Scalp EEG: potentials, montages, volume conduction, and spatial ambiguity

## If you landed here directly

The direct prerequisite is:

`NNE-0017 — ECoG and intracranial EEG: recording from the cortical surface and depth`.

That lesson established a principle that becomes even more important when the sensor moves outside the skull:

> a neural recording channel is a selective voltage-difference measurement, not a direct label of one anatomical source.

You should already be comfortable with:

```text
source currents
→ extracellular electric fields
→ electrode potentials
→ reference or montage
→ channels
→ inference
```

and with the distinction:

```text
sensor location
≠
source location
```

Scalp EEG now inserts several additional conductive tissues between the dominant cortical generators and the electrodes:

```text
cortex
→ meninges / CSF
→ skull
→ scalp
→ electrode interface
→ amplifier
```

The central question of this lesson is:

> what can a pattern of voltages measured on the scalp tell us about neural electrical activity inside the head, and what can it not tell us without additional assumptions?

The sentence to keep throughout the lesson is:

> scalp EEG gives excellent temporal access to distributed brain electrical activity, but each channel is a reference-dependent spatial mixture shaped by volume conduction and sensor geometry.

---

# Part I — What scalp EEG measures

Electroencephalography measures differences in electric potential between electrodes.

For scalp electrode $i$ and a reference electrode or derived reference:

$$ V_i(t)=\phi_i(t)-\phi_{\mathrm{ref}}(t). $$

This equation looks simple.

Its interpretation is not.

The potential $\phi_i(t)$ is not generated only by tissue directly beneath electrode $i$.

It can contain contributions from many neural current sources whose fields propagate through the conductive head.

Therefore:

```text
electrode label
≠
one local cortical generator
```

and:

```text
channel waveform
≠
absolute voltage of one brain region
```

---

# Part II — Where scalp EEG signals mainly come from

At the scale of conventional scalp EEG, the strongest measurable brain-generated fields usually require coordinated transmembrane currents across populations of neurons.

Cortical pyramidal neurons are especially important because:

- their dendritic geometry is relatively aligned within cortical tissue;
- synaptic and return currents can form spatially organized current source-sink patterns;
- sufficiently synchronous activity can sum rather than cancel completely.

A useful causal chain is:

```text
synaptic and membrane currents
→ organized population current flow
→ extracellular potential field
→ conduction through the head
→ scalp potential distribution
```

Do not reduce that to:

```text
EEG = action potentials
```

Scalp EEG is primarily a population field-potential measurement.

---

# Part III — Why many active neurons can still produce little scalp signal

Large numbers of active neurons do not guarantee a large scalp voltage.

If current sources are:

- weakly synchronized;
- oppositely oriented;
- spatially arranged so their fields cancel;
- too deep or geometrically unfavorable;

their net scalp expression may be small.

So:

```text
many active neurons
≠
large EEG amplitude
```

Conversely, a strongly synchronized population can create a measurable scalp field.

---

# Part IV — A useful source abstraction: an equivalent current dipole

For introductory reasoning, a patch of synchronized cortical current can often be approximated by an equivalent current dipole.

This does **not** mean the cortex literally contains a tiny battery-like point dipole.

It means a complex local current distribution can sometimes be summarized by:

- a location;
- an orientation;
- a dipole moment.

Conceptually:

```text
distributed cortical current pattern
→ equivalent source description
→ predicted scalp field
```

The approximation is useful because orientation strongly changes the scalp topography.

---

# Part V — Radial and tangential orientation

Cortical folding means source orientation varies.

A generator near the crown of a gyrus may have a different dominant orientation from a generator along a sulcal wall.

Two generators of similar strength but different orientation can create very different scalp patterns.

Therefore:

```text
same cortical region
+
different source orientation
→
different scalp topography
```

and:

```text
same scalp electrode maximum
≠
same underlying source orientation
```

---

# Part VI — The head is a volume conductor

The electric field produced by neural currents spreads through conductive tissues.

At EEG frequencies and scales, a useful first approximation treats this propagation as quasi-static volume conduction.

The field passes through tissues with different electrical properties, including:

- brain tissue;
- cerebrospinal fluid;
- skull;
- scalp.

The skull is particularly important because its conductivity differs strongly from that of surrounding soft tissues.

The result is not a simple straight-line projection from cortex to electrode.

---

# Part VII — Volume conduction causes spatial spread

Imagine a compact cortical generator.

Its contribution may be measurable at several scalp electrodes.

Conceptually:

```text
one source
        ↓
    broad field
   ↙   ↓   ↘
 F3   Fz   F4
```

This means:

```text
one source
→
many sensors
```

The reverse mistake is common:

```text
many active sensors
→
many independent sources
```

That conclusion does not follow.

---

# Part VIII — Volume conduction is not "signal leakage" between wires

Do not confuse physical field spread with electronic crosstalk.

**Volume conduction** occurs because electric potentials generated in tissue extend through the conductive head.

**Electronic crosstalk** occurs because acquisition channels contaminate one another through hardware or wiring.

The two can produce superficially similar multichannel patterns.

Their mechanisms are completely different.

---

# Part IX — The scalp map is a sensor-space field, not a cortical picture

Suppose an EEG topographic map shows a broad negative region over left central scalp.

The correct first interpretation is:

> the measured scalp potential distribution has a relative negative field over that sensor region under the chosen reference.

It is **not yet** correct to say:

> the left central cortical patch shown under the color is the uniquely identified generator.

That requires a source model and additional assumptions.

---

# Part X — Sensor coordinates and source coordinates are different spaces

Scalp sensors live on a surface outside the skull.

Neural generators live inside a folded three-dimensional brain.

So:

```text
sensor space
≠
source space
```

A topographic EEG map is therefore not a cortical activation map.

It is a map of measured or interpolated scalp voltages.

---

# Part XI — The International 10–20 idea

Standardized electrode placement makes recordings more comparable across people and centers.

The classic 10–20 family uses anatomical landmarks and proportional head measurements.

The terms **10** and **20** refer to electrode positions based on percentages of measured head distances rather than fixed distances in centimeters.

This matters because head sizes differ.

---

# Part XII — Verified visual anchor: scalp electrode geometry

![International 10-20 and extended EEG electrode placement geometry](https://upload.wikimedia.org/wikipedia/commons/3/38/International_10-20_system_for_EEG-MCN.png)

*Visual anchor — the International 10–20 family of scalp locations shown with modified combinatorial nomenclature. Use this figure to understand relative placement, symmetry, midline `z` labels, odd/even hemispheric numbering, and the relationship between standard and additional positions. Do not treat each label as a precise cortical parcel or as proof that a source lies directly underneath the electrode. Source: [Wikimedia Commons — International 10-20 system for EEG-MCN.png](https://commons.wikimedia.org/wiki/File:International_10-20_system_for_EEG-MCN.png), Brylie Christopher Oxley; CC0 1.0 Universal Public Domain Dedication. Registry: `NNE-REF-090`.*

The image solves a physical-spatial problem:

```text
where are standardized scalp positions relative to one another?
```

It does **not** solve the inverse problem:

```text
where inside the brain did a waveform originate?
```

---

# Part XIII — Reading electrode labels

Common letters include:

```text
Fp  frontopolar
F   frontal
C   central
P   parietal
O   occipital
T   temporal
```

Additional high-density nomenclature can include combinations such as:

```text
AF
FC
CP
PO
FT
TP
```

A key warning:

> `C` in EEG nomenclature means **central scalp location**. It is not the name of a cerebral lobe.

---

# Part XIV — Odd, even, and z

In common scalp nomenclature:

```text
odd numbers
→ left hemisphere side

even numbers
→ right hemisphere side

z
→ midline
```

For example:

```text
F3  left frontal-side scalp position
F4  right frontal-side scalp position
Fz  frontal midline scalp position
```

Again, these names describe **sensor placement**, not guaranteed source anatomy.

---

# Part XV — Standardized position does not mean identical cortex underneath

The 10–20 system scales positions using head landmarks.

That improves reproducibility.

But individual brains differ in:

- skull shape;
- cortical folding;
- brain size;
- relationship between scalp and cortex.

Therefore:

```text
same scalp label across people
≠
identical cortical tissue directly underneath
```

This becomes important for source localization and group studies.

---

# Part XVI — Modern standard arrays go beyond the simplest 10–20 drawing

The IFCN has recommended a standardized basic clinical array that improves inferior temporal sampling beyond older minimal layouts.

High-density EEG systems can use many more scalp electrodes.

The important conceptual hierarchy is:

```text
classic sparse layout
→ denser 10–10-type positions
→ high-density arrays
```

But:

```text
more electrodes
≠
removal of volume conduction
```

and:

```text
more electrodes
≠
unique source solution
```

---

# Part XVII — Worked example NNE-EX-084: standardized geometry is proportional, not metric

Suppose two adults have different head circumferences.

A fixed 6-cm spacing copied from one participant to the other would not preserve the intended standardized geometry.

The 10–20 approach instead uses proportional landmark-based measurements.

The lesson is:

```text
standardization
≠
same centimeter coordinates on every head
```

It means:

```text
repeatable relative positions
based on anatomical landmarks
```

This improves correspondence without claiming identical cortical anatomy.

---

# Part XVIII — Electrode density and spatial sampling

If two scalp fields vary rapidly over space, a sparse electrode array may undersample their topography.

A denser array can better sample spatial gradients.

This is a spatial version of a general sampling idea.

However, detailed sampling theory belongs to `NNE-N-0023`.

For now:

```text
higher spatial density
→
more detailed sampling of scalp potential topography
```

not:

```text
higher spatial density
→
one electrode per neural source
```

---

# Part XIX — Why scalp EEG is usually measured in microvolts

The skull and distance from cortical generators attenuate the potentials that reach the scalp.

Conventional EEG signals are therefore small.

This makes:

- electrode contact;
- front-end input range;
- amplifier noise;
- common-mode rejection;
- environmental interference;

important engineering issues.

Detailed front-end design belongs to `NNE-N-0024`.

---

# Part XX — Every EEG channel is a difference

Return to:

$$ V_i=\phi_i-\phi_{\mathrm{ref}}. $$

The reference can be:

- one physical electrode;
- linked electrodes;
- an offline average;
- another scalp electrode in a bipolar derivation;
- another mathematically constructed reference.

The chosen representation changes the waveform.

---

# Part XXI — There is no perfectly silent scalp reference

An ideal reference would have zero or constant potential for all relevant brain activity.

In practice, no ordinary point on the body is guaranteed to satisfy that condition.

That means:

```text
reference electrode
≠
electrically invisible point
```

This is one of the central conceptual difficulties of scalp EEG.

---

# Part XXII — The recorded reference and the displayed reference can differ

An EEG system must acquire voltages using a physical hardware reference or equivalent front-end arrangement.

After acquisition, data can often be re-referenced mathematically.

Thus:

```text
acquisition reference
≠
final analysis reference
```

But offline re-referencing cannot recreate information that was never measured because of saturation, bad channels, or inadequate acquisition.

---

# Part XXIII — Referential montage

A referential montage displays multiple electrodes against a common reference:

```text
F3 - R
F4 - R
C3 - R
C4 - R
P3 - R
P4 - R
```

This makes it easy to compare relative amplitude across sites.

But if the reference itself contains brain activity or artifact, that contribution appears in every channel.

---

# Part XXIV — Bipolar montage

A bipolar montage subtracts neighboring electrode potentials:

```text
Fp1 - F7
F7  - T7
T7  - P7
P7  - O1
```

The channel is:

$$ V_{A-B}=\phi_A-\phi_B. $$

A bipolar derivation emphasizes spatial differences.

It is not a direct cortical source measurement.

---

# Part XXV — Average reference

An average reference estimates a reference from the mean across a set of electrodes.

For $N$ electrodes:

$$ \bar{\phi}(t)=\frac{1}{N}\sum_{k=1}^{N}\phi_k(t). $$

Then:

$$ V_i^{\mathrm{AR}}(t)=\phi_i(t)-\bar{\phi}(t). $$

This can be useful when coverage is broad and sufficiently dense.

Its quality depends on the spatial sampling and on the signals included in the average.

---

# Part XXVI — Linked ears or mastoids are not zero either

Earlobe or mastoid electrodes are often used in reference schemes.

They are physically convenient and can be relatively distant from some cerebral maxima.

But they are still not guaranteed zero-potential points.

Their own signal and asymmetry can shape the derived EEG.

---

# Part XXVII — Laplacian-type derivations

A surface Laplacian or current-source-density-style representation emphasizes local spatial curvature in the scalp potential field.

Conceptually:

```text
broad shared field
→ attenuated

local spatial maximum/minimum
→ emphasized
```

This can improve spatial sharpness in some analyses.

It does not magically recover the true cortical source distribution.

Detailed derivation and signal-processing implications are deferred.

---

# Part XXVIII — Montage is a mathematical transformation

Suppose the vector of electrode potentials relative to some acquisition reference is:

```text
v(t)
```

A montage can be viewed as a linear transformation:

$$ y(t)=M v(t). $$

Here:

- $v(t)$ is the original channel vector;
- $M$ encodes subtraction or re-referencing;
- $y(t)$ is the displayed or analyzed montage.

This perspective is powerful:

> changing montage changes the coordinate representation of the measured field.

It does not move the electrodes or change the original neural event.

---

# Part XXIX — Worked example NNE-EX-085: one physical field, three references

Suppose at one instant:

```text
φF3 = +80 μV
φC3 = +50 μV
φP3 = +20 μV
```

### Reference at P3

```text
F3-P3 = +60 μV
C3-P3 = +30 μV
P3-P3 = 0 μV
```

### Average reference

The mean is:

$$ \bar{\phi}=\frac{80+50+20}{3}=50\ \mu\mathrm{V}. $$

Therefore:

```text
F3-avg = +30 μV
C3-avg =   0 μV
P3-avg = -30 μV
```

### Bipolar chain

```text
F3-C3 = +30 μV
C3-P3 = +30 μV
```

Same physical instantaneous scalp potentials.

Different displayed channel values.

Therefore:

```text
waveform amplitude and polarity
depend partly on montage
```

---

# Part XXX — A zero channel does not mean zero brain activity

In the previous example, `C3-avg = 0 μV`.

That does **not** mean:

```text
no neural activity beneath C3
```

It means only:

```text
φC3 equals the chosen average reference
at that instant
```

This is a crucial interpretation boundary.

---

# Part XXXI — Phase reversal in a bipolar chain

Consider three electrodes:

```text
A = +10 μV
B = +50 μV
C = +10 μV
```

Bipolar derivations:

```text
A-B = -40 μV
B-C = +40 μV
```

The two channels have opposite polarity.

This **phase reversal** indicates that electrode B is a local voltage extremum in that bipolar chain.

It does not, by itself, prove that the neural generator is exactly under B.

---

# Part XXXII — Worked example NNE-EX-086: phase reversal is a field clue, not a source coordinate

Suppose a broad cortical source produces:

```text
F7 = -40 μV
T7 = -90 μV
P7 = -50 μV
```

Then:

```text
F7-T7 = +50 μV
T7-P7 = -40 μV
```

A phase reversal occurs around T7.

Safe conclusion:

> T7 is near the largest negative scalp potential among these sampled electrodes in this montage.

Unsafe conclusion:

> the cortical generator is uniquely located directly under T7.

Volume conduction and source orientation prevent that leap.

---

# Part XXXIII — Why reference choice can alter correlation

Suppose two channels share the same reference:

$$ V_A=\phi_A-\phi_R $$

and:

$$ V_B=\phi_B-\phi_R. $$

Both contain the term $-\phi_R$.

If the reference varies, it can create or alter statistical relationships between the channels.

Therefore:

```text
channel correlation
≠
pure neural interaction
```

Reference choice can affect:

- covariance;
- correlation;
- coherence;
- phase;
- network metrics.

This is why connectivity analysis requires special caution.

---

# Part XXXIV — Volume conduction can also create zero-lag similarity

Even with an ideal reference, one neural generator can project to multiple electrodes at essentially the same time.

Then two scalp channels may look correlated because they share a common physical source.

Therefore:

```text
high zero-lag scalp correlation
≠
direct communication between two cortical areas
```

This failure mode will matter later in network analysis.

---

# Part XXXV — A scalp topography can be broad even for one source

Suppose one localized cortical generator produces a smooth field maximum over several frontal electrodes.

The map may look like a large activated frontal region.

But the broadness can arise from:

- volume conduction;
- skull smoothing;
- source depth;
- orientation;
- interpolation between electrodes.

The colored area is not automatically the anatomical extent of the generator.

---

# Part XXXVI — Spatial interpolation adds no new measurements

Topographic plotting software often fills the space between electrodes smoothly.

That is useful for visualization.

But:

```text
interpolated pixel
≠
new electrode
```

A 64-channel EEG remains a 64-electrode measurement even if the plot contains thousands of colored pixels.

---

# Part XXXVII — Electrode maximum and source maximum are different concepts

Suppose F3 has the largest measured negative amplitude.

That identifies a sensor-space maximum or minimum.

It does not necessarily identify:

- the source centroid;
- the most active cortical voxel;
- the nearest cortical patch;
- the causal origin.

Source inference requires a forward model.

---

# Part XXXVIII — The EEG forward problem

The forward problem asks:

> if the neural current sources were known, what scalp voltages would they produce?

A simplified linear model is:

$$ v(t)=L s(t)+\epsilon(t). $$

where:

- $s(t)$ represents source amplitudes;
- $L$ is the lead-field or forward matrix;
- $v(t)$ is the scalp sensor vector;
- $\epsilon(t)$ represents noise and model error.

The matrix $L$ depends on:

- source location;
- source orientation;
- head geometry;
- tissue conductivities;
- electrode positions.

---

# Part XXXIX — The lead field is a source-to-sensor map

Each column of $L$ describes how one modeled source contributes to the sensor array.

Conceptually:

```text
source 1 → pattern across all electrodes
source 2 → another pattern across all electrodes
source 3 → another pattern across all electrodes
```

Measured EEG is a mixture of these patterns.

This formalizes the statement:

```text
one source → many sensors
```

and:

```text
one sensor ← many possible sources
```

---

# Part XL — The inverse problem

The inverse problem asks:

> given the scalp voltages, what sources produced them?

Symbolically, it might look tempting to write:

$$ s=L^{-1}v. $$

But in realistic EEG source imaging, the problem is generally underdetermined or ill-posed.

There are far more possible source configurations than independent scalp measurements.

A simple inverse does not uniquely exist.

---

# Part XLI — Non-uniqueness is the core spatial ambiguity

Imagine 64 scalp channels and thousands of candidate cortical source locations.

Many distinct source combinations can reproduce nearly the same sensor pattern.

Therefore:

```text
one scalp map
→
many possible internal source configurations
```

without additional constraints.

That is the fundamental EEG inverse problem.

---

# Part XLII — Worked example NNE-EX-087: two source models, one plausible scalp field

Suppose a measured scalp topography has a broad left-frontal negativity.

Model A explains it with:

```text
one strong superficial cortical dipole
```

Model B explains it with:

```text
two weaker nearby dipoles
with compatible orientations
```

If both predict nearly the same measured voltages within noise:

```text
sensor data alone
cannot uniquely choose A over B
```

Additional assumptions or evidence are needed.

---

# Part XLIII — Source localization requires priors or constraints

Common constraints can encode assumptions about:

- allowed source locations;
- source orientations;
- smoothness;
- sparsity;
- source number;
- anatomy;
- temporal structure.

These assumptions select one solution from many possible solutions.

Therefore:

> a source-localization map is a model-based inference, not a direct photograph of electrical activity.

Detailed inverse methods belong later in the curriculum.

---

# Part XLIV — Head models matter

A source-to-sensor model needs a representation of conductive head anatomy.

Approaches can range from:

- simplified spherical models;
- template MRI head models;
- individual anatomical MRI;
- finite-element or boundary-element models.

A better geometric model can reduce some forward-model error.

It does not remove inverse non-uniqueness.

---

# Part XLV — Conductivity assumptions matter

The predicted scalp field depends on assumed tissue conductivities.

Important compartments can include:

- scalp;
- skull;
- CSF;
- gray matter;
- white matter.

Errors in conductivity or geometry can alter estimated source location and orientation.

Therefore:

```text
perfect inverse algorithm
+
wrong forward model
→
wrong source inference
```

---

# Part XLVI — Individual electrode coordinates matter for source imaging

For visual inspection, nominal 10–20 labels can be adequate.

For high-precision source imaging, actual sensor coordinates can matter.

Cap placement varies.

Heads vary.

Therefore:

```text
nominal label
≠
exact individual 3D coordinate
```

Photogrammetry, digitizers, or other localization methods can improve electrode-coordinate estimates.

---

# Part XLVII — High-density EEG helps the forward/inverse pipeline

More scalp electrodes can improve:

- topographic sampling;
- localization of field maxima;
- spatial gradients;
- source-imaging performance under appropriate models.

Modern recommendations recognize the value of 64–256 channel high-density arrays for specific source-imaging applications.

But:

```text
256 electrodes
≠
256 independent cortical sources
```

and:

```text
high-density EEG
≠
intracranial recording
```

---

# Part XLVIII — More electrodes can still be redundant

Because volume conduction makes neighboring sensors correlated, the number of physically recorded channels can exceed the effective number of independent spatial degrees of freedom.

This does not make extra electrodes useless.

It means:

```text
channel count
≠
independent source count
```

This connects directly to `NNE-0016`.

---

# Part XLIX — The skull changes spatial information

The skull attenuates and spatially smooths electrical potentials.

This is one reason ECoG can show sharper local spatial patterns than scalp EEG.

The comparison is:

```text
ECoG
sensor close to cortex
less intervening tissue

scalp EEG
sensor outside skull
more spatial smoothing
```

But scalp EEG gains a major advantage:

```text
noninvasive whole-head access
```

---

# Part L — Scalp EEG is not "low-quality ECoG"

This framing is wrong.

Scalp EEG and ECoG solve different engineering and clinical problems.

Scalp EEG offers:

- noninvasive access;
- repeated measurements;
- whole-head coverage;
- low procedural risk;
- relatively low cost;
- millisecond temporal sampling.

ECoG offers:

- closer source proximity;
- stronger local fields;
- better local spatial specificity;
- higher-frequency access in many contexts;

but requires invasive placement.

The tradeoff is multidimensional.

---

# Part LI — Deep sources are not simply invisible

A common oversimplification is:

> scalp EEG only records superficial cortex.

Deeper generators are generally harder to detect and localize because of distance and field geometry.

But a sufficiently strong, synchronized, and favorably oriented deep source can contribute to scalp EEG.

So:

```text
deep
≠
automatically invisible
```

and:

```text
visible on scalp
≠
necessarily superficial
```

---

# Part LII — Source orientation can matter as much as depth

A relatively superficial source with an unfavorable field geometry may appear weak.

A deeper but strongly synchronized and favorable source may still be detectable.

Therefore:

```text
amplitude
≠
simple distance meter
```

The head acts as a field-mixing volume, not a ruler.

---

# Part LIII — Bilateral symmetry can cancel or reinforce

Suppose homologous cortical areas are active simultaneously.

Depending on:

- orientation;
- phase;
- synchrony;
- geometry;

their scalp fields can partially cancel or reinforce.

Thus the scalp pattern reflects the **vector-like field geometry of currents**, not only the amount of active tissue.

---

# Part LIV — Clinical interpretation often stays in sensor space

Many clinical EEG questions do not require solving a full inverse source problem.

Experienced readers can characterize:

- focal versus generalized patterns;
- symmetry;
- temporal evolution;
- waveform morphology;
- distribution;
- reactivity;
- state changes;

in sensor space.

Source localization is an additional analysis, not a prerequisite for every useful EEG interpretation.

---

# Part LV — Standard clinical EEG needs reproducible acquisition

Modern IFCN/ILAE recommendations specify minimum recording standards for routine and sleep EEG.

These include issues such as:

- standardized electrode arrays;
- electrode impedance;
- sampling rate;
- recording duration;
- additional physiological channels;
- display and storage.

This lesson uses those standards only to establish why acquisition geometry and metadata are part of the measurement.

Detailed sampling and filtering come later.

---

# Part LVI — Scalp preparation is part of the sensor interface

Scalp electrodes do not directly touch neural tissue.

They interact with:

```text
electrode
→ conductive medium
→ skin
```

Hair, skin condition, gel or paste, contact area, and electrode material affect the interface.

This reconnects to `NNE-0013`.

The exact impedance and front-end consequences are deferred to `NNE-N-0024`.

---

# Part LVII — Low impedance is useful, but balance matters

A practical scalp EEG system seeks stable electrode contact and appropriate impedance.

But simply minimizing one electrode's impedance without considering channel balance and amplifier characteristics is not the whole problem.

Modern amplifiers have high input impedance.

The measurement depends on the entire interface-amplifier system.

---

# Part LVIII — Ground and reference are not the same concept

In EEG terminology, learners often confuse:

```text
reference
```

with:

```text
ground
```

The reference participates in the definition of measured channel voltage.

The ground or driven/common-mode electrode serves a different instrumentation role.

Detailed grounding and common-mode rejection belong to `NNE-N-0024`.

For now:

```text
reference
≠
ground
```

---

# Part LIX — Artifacts can dominate scalp EEG

Scalp EEG is vulnerable to non-neural signals, including:

- eye movements;
- blinks;
- facial and neck muscle activity;
- cardiac activity;
- electrode movement;
- cable movement;
- mains interference.

A large scalp waveform is not automatically neural.

Detailed artifact mechanisms and rejection belong to `NNE-N-0025`.

---

# Part LX — Eye artifacts are spatial fields too

The eye behaves as an electrical dipole.

Eye movements can therefore project broadly across frontal scalp electrodes.

This is another example of:

```text
one source
→
many sensors
```

but the source is non-neural.

It reinforces why waveform topography alone does not prove cortical origin.

---

# Part LXI — Muscle artifact can mimic high-frequency brain activity

Cranial and neck muscles generate electrical activity that can contaminate EEG, especially at higher frequencies.

Therefore:

```text
high-frequency scalp power
≠
automatically cortical gamma activity
```

This is one reason artifact reasoning must precede physiological interpretation.

---

# Part LXII — Filtering can change apparent morphology

High-pass, low-pass, and notch filters can alter:

- waveform amplitude;
- timing;
- sharpness;
- ringing;
- baseline.

Detailed filter behavior belongs to `NNE-N-0026`.

This lesson only establishes:

```text
displayed EEG
=
measured signal transformed by acquisition and processing
```

---

# Part LXIII — Frequency bands are not physical channels

Delta, theta, alpha, beta, and gamma are analysis conventions applied to EEG spectra.

An electrode does not contain a separate alpha wire and beta wire.

Formal spectral reasoning belongs to `NNE-N-0028`.

---

# Part LXIV — Alpha topography illustrates sensor-space reasoning

Posterior dominant alpha activity often appears most strongly over posterior scalp sensors during relaxed wakefulness with eyes closed.

A safe description is:

> posterior scalp channels show stronger activity in the alpha range under this state.

A stronger anatomical interpretation requires additional source evidence.

---

# Part LXV — Event-related potentials are also reference-dependent fields

Averaging time-locked EEG across repeated trials can reveal event-related potentials.

But an ERP component's:

- amplitude;
- polarity;
- scalp distribution;

still depends on reference and volume conduction.

A named ERP component is not a single anatomical source.

---

# Part LXVI — One scalp component can arise from several generators

Suppose an ERP peak appears at 300 ms.

Different cortical sources can overlap in time.

Their scalp fields sum linearly to a first approximation.

Therefore:

```text
one visible peak
≠
one neural process
```

Temporal overlap is another mixing problem.

---

# Part LXVII — The superposition principle

Under the quasi-static linear approximation, fields from multiple sources add.

If source A produces scalp vector $v_A$ and source B produces $v_B$:

$$ v_{\mathrm{total}}=v_A+v_B. $$

This is why source separation is difficult.

The sensor receives mixtures.

---

# Part LXVIII — Cancellation is the other side of superposition

If two sources produce opposite scalp fields:

$$ v_A\approx -v_B, $$

then:

$$ v_{\mathrm{total}}\approx 0. $$

So:

```text
small scalp voltage
≠
little neural activity
```

The underlying fields may cancel.

---

# Part LXIX — Worked example NNE-EX-088: source cancellation hides activity

Imagine two synchronized cortical patches.

At electrode Cz:

```text
source A contribution = +35 μV
source B contribution = -32 μV
```

The measured contribution is approximately:

```text
+3 μV
```

A naive interpretation would say:

> almost nothing happened.

The correct interpretation is:

> the net scalp field at Cz is small; substantial opposing source contributions can still exist.

This is why scalp amplitude cannot be read as a direct activity meter.

---

# Part LXX — Sensor-space connectivity is especially dangerous

If one source volume-conducts to electrodes A and B, then:

```text
A ↔ B correlation
```

can appear even without direct interaction between two separate cortical regions.

Reference choice can further alter the relationship.

Therefore sensor-level functional connectivity requires methods designed to address:

- shared sources;
- zero-lag field spread;
- reference effects.

Detailed network analysis is deferred.

---

# Part LXXI — Topographic similarity across people can still hide source differences

Two participants may show similar scalp voltage maps.

But individual differences in:

- skull;
- CSF;
- cortical folding;
- source orientation;

can make the underlying sources different.

Conversely, similar sources can produce somewhat different scalp maps.

Group averaging can obscure these distinctions.

---

# Part LXXII — Bad channels change more than one trace

If a bad electrode is included in an average reference, it can contaminate every re-referenced channel.

Therefore:

```text
one bad sensor
→
many bad derived channels
```

depending on montage.

This is another reason preprocessing order matters.

Detailed artifact handling belongs to `NNE-N-0025`.

---

# Part LXXIII — Re-referencing after deleting channels changes the average

Suppose an average reference uses 64 electrodes.

If 10 noisy electrodes are removed, the average reference is now computed from 54 electrodes.

The numerical reference changes.

Therefore analysis pipelines should document:

- which electrodes were included;
- when bad channels were removed;
- how re-referencing was performed.

---

# Part LXXIV — A montage can create a local-looking waveform

Bipolar subtraction can suppress a broad common field and emphasize a local gradient.

That can make a waveform appear spatially sharper.

This does not mean the underlying source physically became smaller.

It means the montage transformed the sensor field.

---

# Part LXXV — A montage can also hide a broad waveform

If two neighboring electrodes receive nearly equal contributions:

```text
φA ≈ φB
```

then:

$$ \phi_A-\phi_B\approx 0. $$

A bipolar montage can therefore attenuate broad synchronous activity.

No montage reveals every feature equally well.

---

# Part LXXVI — There is no universally best montage

Different montages emphasize different spatial questions.

A useful principle is:

```text
choose montage
to match the phenomenon and inference goal
```

not:

```text
one montage is always correct
```

This is supported by clinical montage literature.

---

# Part LXXVII — Reference changes do not create new biological events

If a spike appears much larger after re-referencing, the brain did not generate a second spike.

The representation changed.

Always separate:

```text
biological event
from
measurement representation
```

This distinction generalizes to every neural signal modality.

---

# Part LXXVIII — Scalp EEG and spatial resolution

It is common to say EEG has "poor spatial resolution."

That sentence needs qualification.

Spatial performance depends on:

- electrode density;
- source depth;
- source geometry;
- signal-to-noise ratio;
- head model;
- electrode localization;
- inverse method;
- priors.

Conventional sensor-space EEG has substantial spatial ambiguity.

High-density source imaging can improve localization under suitable conditions.

---

# Part LXXIX — Temporal resolution and spatial ambiguity coexist

Scalp EEG can capture changes on millisecond time scales.

At the same time, its source localization is difficult.

So:

```text
excellent temporal resolution
+
ambiguous spatial inverse
```

can both be true.

Do not collapse temporal and spatial resolution into one "quality" score.

---

# Part LXXX — Scalp EEG is a strong engineering tradeoff

Scalp EEG remains powerful because it combines:

```text
noninvasive
+
portable
+
relatively inexpensive
+
millisecond-scale electrical measurement
+
repeatable
+
whole-head sampling
```

with costs:

```text
small signal amplitudes
+
artifacts
+
reference dependence
+
volume conduction
+
inverse ambiguity
```

This is exactly the coupled-tradeoff reasoning from `NNE-0012`.

---

# Part LXXXI — The complete scalp EEG measurement chain

```mermaid
flowchart LR
    A["Neural transmembrane currents"] --> B["Intracranial electric field"]
    B --> C["Brain, CSF, skull, scalp volume conductor"]
    C --> D["Scalp electrode potentials"]
    D --> E["Reference and front end"]
    E --> F["Digitized channels"]
    F --> G["Montage and preprocessing"]
    G --> H["Sensor-space patterns"]
    H --> I["Optional source model"]
    I --> J["Clinical or scientific inference"]
```

Every stage changes what can be inferred.

---

# Part LXXXII — A compact forward/inverse mental model

Forward:

```text
source model
+
head model
+
electrode geometry
→
predicted scalp voltages
```

Inverse:

```text
measured scalp voltages
+
head model
+
priors
→
estimated source model
```

The inverse arrow contains assumptions.

Never hide them.

---

# Part LXXXIII — What scalp EEG can support strongly

Depending on acquisition and analysis quality, scalp EEG can support strong evidence about:

- timing;
- rhythmic state;
- transient waveforms;
- gross scalp distribution;
- sleep and vigilance patterns;
- epileptiform activity;
- event-related responses;
- some source estimates when appropriate models are used.

---

# Part LXXXIV — What scalp EEG does not give automatically

Raw scalp channels do not automatically provide:

- one source per electrode;
- exact cortical location;
- absolute voltage of a brain region;
- direct firing rate;
- direct synaptic excitation-versus-inhibition labels;
- direct connectivity;
- artifact-free neural activity.

Each stronger inference needs extra evidence or modeling.

---

# Part LXXXV — Common failure modes

## Failure mode 1 — "EEG electrode F3 records the F3 part of cortex"

Why it fails:

F3 is a scalp coordinate label.

Its voltage can contain contributions from multiple neural sources.

---

## Failure mode 2 — "The electrode with largest amplitude sits directly over the source"

Why it fails:

Source orientation, depth, head conductivity, and reference shape the maximum.

---

## Failure mode 3 — "10–20 means electrodes are exactly 10 or 20 cm apart"

Why it fails:

The numbers refer to proportional head measurements.

---

## Failure mode 4 — "Standardized scalp position means identical cortical anatomy across people"

Why it fails:

Individual head and brain geometry vary.

---

## Failure mode 5 — "A reference electrode has zero brain signal"

Why it fails:

No ordinary body location is guaranteed electrically silent.

---

## Failure mode 6 — "Changing reference changes the biology"

Why it fails:

It changes the mathematical channel representation.

---

## Failure mode 7 — "A zero-valued referenced channel means no brain activity"

Why it fails:

It means the electrode potential equals the chosen reference at that moment.

---

## Failure mode 8 — "A bipolar phase reversal uniquely localizes the cortical source"

Why it fails:

It identifies a scalp voltage extremum within that derivation, not a unique source coordinate.

---

## Failure mode 9 — "Average reference is always neutral"

Why it fails:

Its quality depends on electrode density, coverage, and included signals.

---

## Failure mode 10 — "Linked ears are electrically silent"

Why it fails:

They can carry brain or artifact-related potential.

---

## Failure mode 11 — "Volume conduction is electronic crosstalk"

Why it fails:

Volume conduction is physical field spread through tissue.

---

## Failure mode 12 — "Many correlated electrodes prove many connected cortical areas"

Why it fails:

A common source and reference can create shared signals.

---

## Failure mode 13 — "A broad topographic color patch is a broad activated cortical region"

Why it fails:

Interpolation and volume conduction broaden sensor-space maps.

---

## Failure mode 14 — "High-density EEG removes the inverse problem"

Why it fails:

More sensors constrain the problem but do not make source inference unique.

---

## Failure mode 15 — "Deep sources are invisible to scalp EEG"

Why it fails:

Detectability depends on synchrony, strength, orientation, geometry, and depth.

---

## Failure mode 16 — "Scalp EEG amplitude is a direct meter of neural activity"

Why it fails:

Superposition and cancellation can increase or reduce the net field.

---

## Failure mode 17 — "More electrodes means the same number of independent sources"

Why it fails:

Neighboring electrodes can share volume-conducted components.

---

## Failure mode 18 — "A scalp topography is already source localization"

Why it fails:

It is a sensor-space voltage map.

---

## Failure mode 19 — "A perfect inverse algorithm can compensate for a wrong head model"

Why it fails:

Forward-model error propagates into source estimates.

---

## Failure mode 20 — "Reference and ground are the same electrode concept"

Why it fails:

They have different roles in channel definition and instrumentation.

---

## Failure mode 21 — "All high-frequency scalp EEG is cortical gamma"

Why it fails:

Muscle and other artifacts can dominate high-frequency power.

---

## Failure mode 22 — "Filtering only removes noise"

Why it fails:

Filters can reshape neural waveforms as well.

---

## Failure mode 23 — "One ERP peak equals one neural generator"

Why it fails:

Several sources can overlap and superpose at the same latency.

---

## Failure mode 24 — "Small scalp voltage means weak brain activity"

Why it fails:

Opposing source fields can cancel.

---

## Failure mode 25 — "One montage is universally best"

Why it fails:

Different montages emphasize different spatial features and assumptions.

---

# Part LXXXVI — Active work

## Exercise A — sensor or source?

Classify each statement:

```text
sensor-space statement
source-space statement
```

1. F3 is 40 μV more negative than the reference.
2. A left frontal cortical dipole is estimated at a specific coordinate.
3. A broad posterior scalp maximum is present.
4. Source imaging suggests bilateral occipital generators.

### Check

1. sensor;
2. source;
3. sensor;
4. source.

---

## Exercise B — montage arithmetic

Suppose:

```text
F3 = +70 μV
C3 = +40 μV
P3 = +10 μV
```

Find:

1. `F3-P3`;
2. `C3-P3`;
3. `F3-C3`;
4. the average reference value;
5. `F3-average`.

### Check

```text
F3-P3 = 60 μV
C3-P3 = 30 μV
F3-C3 = 30 μV
average = 40 μV
F3-average = 30 μV
```

---

## Exercise C — phase reversal

Suppose:

```text
F7 = -30 μV
T7 = -80 μV
P7 = -40 μV
```

Compute:

```text
F7-T7
T7-P7
```

### Check

```text
F7-T7 = +50 μV
T7-P7 = -40 μV
```

There is a phase reversal around T7.

Safe interpretation:

T7 is near a sampled scalp voltage extremum in this bipolar chain.

---

## Exercise D — source versus channel count

A 128-channel scalp EEG shows nearly identical waveforms on 15 neighboring electrodes.

Does that imply 15 synchronized cortical sources?

### Check

No.

One or a few generators can volume-conduct to many neighboring sensors.

---

## Exercise E — topographic interpolation

A 64-channel EEG plot contains 20,000 colored pixels.

How many independent scalp measurements were created by interpolation?

### Check

Zero.

The measurement count remains determined by the actual electrodes.

---

## Exercise F — cancellation

Two sources contribute:

```text
+25 μV
-24 μV
```

to Cz at the same time.

What is the net contribution?

### Check

```text
+1 μV
```

Small sensor amplitude does not imply weak underlying source activity.

---

## Exercise G — inverse ambiguity

You have 64 channels and a cortical source grid containing 5,000 candidate locations.

Can the sensor vector alone uniquely determine all 5,000 source amplitudes?

### Check

No.

Constraints or priors are necessary.

---

## Exercise H — choose the next conceptual tool

For each problem, identify the later lesson that owns the detailed treatment:

1. anti-aliasing;
2. reference amplifier and common-mode rejection;
3. blink and muscle artifact;
4. filter phase distortion;
5. alpha-band power;
6. dataset channel metadata.

### Check

1. `NNE-N-0023`;
2. `NNE-N-0024`;
3. `NNE-N-0025`;
4. `NNE-N-0026`;
5. `NNE-N-0028`;
6. `NNE-N-0029`.

---

# Part LXXXVII — Retrieval practice

Answer without looking back.

1. What physical quantity does a scalp EEG channel measure?
2. Why is an EEG channel not an absolute potential?
3. What kinds of neural currents contribute strongly to scalp EEG?
4. Why does synchrony matter?
5. What is an equivalent current dipole?
6. Why does source orientation matter?
7. What does volume conduction mean?
8. Why is volume conduction not hardware crosstalk?
9. What is sensor space?
10. What is source space?
11. What do 10 and 20 mean in the 10–20 system?
12. Why are proportional positions used?
13. What does `z` mean in an electrode label?
14. What do odd and even numbers usually indicate?
15. Why does C3 not mean "cortical area C3"?
16. Why can the same scalp label overlie different cortex across participants?
17. What does higher electrode density improve?
18. Why does high density not remove volume conduction?
19. Write the basic reference equation.
20. Why is there no perfectly silent reference?
21. What is a referential montage?
22. What is a bipolar montage?
23. What is average reference?
24. What can contaminate an average reference?
25. Why are linked ears or mastoids not guaranteed neutral?
26. What does a phase reversal indicate in a bipolar chain?
27. Why does phase reversal not uniquely identify a cortical source?
28. Why can reference choice alter correlation?
29. Why can volume conduction create zero-lag correlation?
30. Why is a topographic map not a cortical activation image?
31. What is the forward problem?
32. What does the lead-field matrix describe?
33. Write the simplified forward equation.
34. What is the inverse problem?
35. Why is the inverse problem non-unique?
36. Why are priors required?
37. Why does the head model matter?
38. Why do individual electrode coordinates matter?
39. Why can high-density EEG improve source imaging?
40. Why is channel count not source count?
41. Why is scalp EEG not merely low-quality ECoG?
42. Can deep sources contribute to scalp EEG?
43. Why is amplitude not a simple distance meter?
44. What is field cancellation?
45. Why can a small scalp voltage hide strong source activity?
46. Why can one ERP peak have multiple generators?
47. Why is ground not the same as reference?
48. Why can muscle contaminate high-frequency EEG?
49. Which later lesson owns sampling theory?
50. Which later lesson owns detailed referencing and front ends?
51. Which later lesson owns artifacts?
52. Which later lesson owns filtering?
53. Which later lesson owns spectral analysis?
54. Which later lesson owns dataset structure?
55. What is the next canonical lesson after scalp EEG?
56. Finish: scalp EEG gives excellent temporal access, but each channel is a ______-dependent spatial ______ shaped by volume conduction.

---

# Part LXXXVIII — Backward connections

## NNE-0006 — synaptic currents

The field measured at the scalp begins with transmembrane and synaptic currents.

Scalp EEG is not detached from cellular neurophysiology.

---

## NNE-0007 — populations

Single neurons are too small and unsynchronized to explain conventional scalp EEG alone.

Population organization and synchrony are central.

---

## NNE-0008 — signal modalities

EEG is one member of a broader measurement family.

Its physical variable is electrical potential difference at the scalp.

---

## NNE-0009 — measurement chain

This lesson is a detailed example of:

```text
source
→ tissue
→ sensor
→ electronics
→ data
→ inference
```

The tissue stage is unusually important because the entire head becomes part of the volume conductor.

---

## NNE-0012 — coupled tradeoffs

Scalp EEG trades invasive spatial specificity for:

- safety;
- repeatability;
- portability;
- whole-head access.

---

## NNE-0013 — electrode interface

The scalp electrode still requires a stable electrical interface.

The interface is different from an implanted metal-tissue interface, but it remains part of the measurement.

---

## NNE-0015 — extracellular field physics

The same superposition and geometry principles that shaped extracellular spikes and LFPs also shape EEG.

The spatial scale is different.

---

## NNE-0017 — intracranial EEG

The key transition is:

```text
intracranial contact
→
outside-skull scalp electrode
```

which adds:

- greater source distance;
- skull and scalp conduction;
- stronger spatial smoothing;
- noninvasive access.

---

# Part LXXXIX — Forward connections

## NNE-N-0019 — Peripheral neural and neuromuscular signals: ENG and EMG

The next lesson moves from central scalp fields to peripheral nerves and muscle.

It asks:

```text
what changes when the electrical source is an axon bundle
or a contracting muscle rather than distributed cortical currents?
```

---

## NNE-N-0023 — Sampling, digitization, aliasing, dynamic range, and quantization

Scalp EEG only becomes digital data after analog acquisition and sampling.

---

## NNE-N-0024 — Biopotential front ends

This lesson introduced reference and ground conceptually.

The later lesson owns:

- differential amplification;
- input impedance;
- common mode;
- CMRR;
- grounding;
- detailed referencing.

---

## NNE-N-0025 — Noise and artifacts

Blinks, EMG, motion, cable effects, and mains contamination are deferred there.

---

## NNE-N-0026 — Filtering

Filter cutoff, order, phase, ringing, and distortion are deferred there.

---

## NNE-N-0028 — Spectra, rhythms, and time-frequency analysis

Alpha and other frequency-band interpretations are deferred there.

---

## NNE-N-0029 — Neural datasets

Electrode coordinates, channel labels, references, bad-channel annotations, and events become formal dataset metadata there.

---

# Compact summary

```text
1. Scalp EEG measures voltage differences between electrodes; it does not measure an absolute voltage of one cortical location.

2. Conventional scalp EEG mainly reflects coordinated population transmembrane and synaptic currents rather than individual action potentials.

3. The head is a volume conductor: brain, CSF, skull, and scalp shape how neural fields reach scalp electrodes.

4. One neural source can contribute to many scalp sensors.

5. Many active sensors therefore do not imply many independent neural sources.

6. A scalp topographic map is a sensor-space voltage field, not a cortical activation image.

7. The 10–20 family standardizes relative scalp positions using anatomical landmarks and proportional distances.

8. Electrode labels are sensor coordinates, not guaranteed cortical parcels.

9. Every EEG montage is a mathematical voltage-difference representation.

10. No ordinary scalp or body reference is guaranteed electrically silent.

11. Referential, bipolar, average-reference, linked-ear/mastoid, and Laplacian-style representations emphasize different spatial features.

12. A bipolar phase reversal identifies a sensor-space voltage extremum in that derivation, not a unique cortical source.

13. Reference choice can alter amplitude, polarity, correlation, coherence, and network metrics.

14. Volume conduction can create strong zero-lag similarity across sensors without direct cortical connectivity.

15. The forward problem predicts scalp voltages from modeled sources and a head model.

16. The inverse problem estimates sources from scalp voltages and is fundamentally non-unique without constraints.

17. Head anatomy, tissue conductivity, electrode coordinates, and source orientation affect source inference.

18. High-density EEG improves scalp spatial sampling and can improve source imaging, but it does not eliminate volume conduction or inverse ambiguity.

19. Small scalp amplitude can coexist with strong neural activity because source fields can cancel.

20. Scalp EEG combines excellent temporal resolution and noninvasive whole-head access with reference dependence, artifacts, volume conduction, and spatial ambiguity.
```

---

# References used in this lesson

- **NNE-REF-041** — György Buzsáki, Costas A. Anastassiou, and Christof Koch, *The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes*, Nature Reviews Neuroscience 13, 407–420 (2012), DOI 10.1038/nrn3241. Reused for extracellular-field generation, superposition, source geometry, distance, synchrony, and the relation between intracranial fields and scalp EEG.
- **NNE-REF-084** — Margitta Seeck et al., *The standardized EEG electrode array of the IFCN*, Clinical Neurophysiology 128(10), 2070–2077 (2017), DOI 10.1016/j.clinph.2017.06.254, PMID 28778476. IFCN guideline used for modern standardized electrode arrays, 10–10-compatible nomenclature, inferior temporal sampling, and high-density EEG context.
- **NNE-REF-085** — Ekrem Kutluay and Giridhar P. Kalamangalam, *Montages for Noninvasive EEG Recording*, Journal of Clinical Neurophysiology 36(5), 330–336 (2019), DOI 10.1097/WNP.0000000000000546, PMID 31490450, PMCID PMC6733527. Review used for referential and bipolar montage interpretation, polarity, spatial maxima, and phase reversal.
- **NNE-REF-086** — Dezhong Yao et al., *Which Reference Should We Use for EEG and ERP practice?*, Brain Topography 32(4), 530–549 (2019), DOI 10.1007/s10548-019-00707-x, PMID 31037477, PMCID PMC6592976. Review used for the nonzero-reference problem, average reference, linked ears/mastoids, bipolar and Laplacian reference families, and reference-dependent downstream measures.
- **NNE-REF-087** — Tae-Hoon Eom, *Electroencephalography source localization*, Clinical and Experimental Pediatrics 66(5), 201–209 (2023), DOI 10.3345/cep.2022.00962, PMID 36596745, PMCID PMC10167408, CC BY-NC 4.0. Review used for the scalp EEG forward problem, head models, inverse non-uniqueness, source constraints, and high-density source imaging.
- **NNE-REF-088** — R. W. Homan, J. Herman, and P. Purdy, *Cerebral location of international 10-20 system electrode placement*, Electroencephalography and Clinical Neurophysiology 66(4), 376–382 (1987), DOI 10.1016/0013-4694(87)90206-9, PMID 2435517. Primary anatomical study used to separate standardized scalp positions from exact underlying cerebral anatomy.
- **NNE-REF-089** — Maria E. Peltola et al., *Routine and sleep EEG: Minimum recording standards of the International Federation of Clinical Neurophysiology and the International League Against Epilepsy*, Clinical Neurophysiology 147, 108–120 (2023), DOI 10.1016/j.clinph.2023.01.002, PMID 36775678; parallel open-access Epilepsia publication DOI 10.1111/epi.17448, PMCID PMC10006292. IFCN/ILAE guideline used for current routine EEG acquisition standards and the role of standardized electrode arrays and technical metadata.
- **NNE-REF-090** — Brylie Christopher Oxley, *International 10-20 system for EEG-MCN.png*, Wikimedia Commons (2017), CC0 1.0 Universal Public Domain Dedication. Verified static visual anchor for standardized scalp electrode geometry and nomenclature.
