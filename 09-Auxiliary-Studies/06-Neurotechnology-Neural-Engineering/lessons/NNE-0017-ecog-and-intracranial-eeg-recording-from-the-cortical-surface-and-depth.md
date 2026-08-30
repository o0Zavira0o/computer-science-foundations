---
id: NNE-0017
title: "ECoG and intracranial EEG: recording from the cortical surface and depth"
track: neurotechnology-neural-engineering
level: L1
status: complete
curriculum_node: NNE-N-0017
concepts_introduced: ["NNE-C-0020"]
concepts_deepened: ["NNE-C-0010", "NNE-C-0011", "NNE-C-0012", "NNE-C-0015", "NNE-C-0016", "NNE-C-0018", "NNE-C-0019"]
concepts_used: ["NNE-C-0009"]
examples_added: ["NNE-EX-079", "NNE-EX-080", "NNE-EX-081", "NNE-EX-082", "NNE-EX-083"]
references_used: ["NNE-REF-041", "NNE-REF-077", "NNE-REF-078", "NNE-REF-079", "NNE-REF-080", "NNE-REF-081", "NNE-REF-082", "NNE-REF-083"]
last_reviewed: 2026-08-30
version_sensitive: false
review_after: null
---
# ECoG and intracranial EEG: recording from the cortical surface and depth

## If you landed here directly

The direct prerequisite is `NNE-0016 — Microelectrode arrays and high-channel-count invasive recording`.

That lesson established five distinctions that remain essential here:

```text
physical recording site
≠
acquisition channel
≠
inferred neural source
```

and:

```text
same channel count
≠
same spatial sampling geometry
```

You should also remember the extracellular measurement boundary from `NNE-0015`:

> an electrode does not read "the brain's voltage" at one absolute point. It participates in a voltage-difference measurement shaped by neural sources, conductive tissue, contact geometry, reference, electronics, and analysis.

This lesson moves from penetrating microelectrode arrays toward a different family of invasive recordings used extensively in human clinical neurophysiology and neuroscience:

```text
intracranial EEG
├── cortical-surface recording
│   └── ECoG with grids or strips
└── stereotactic depth recording
    └── SEEG with multicontact depth electrodes
```

The core question is:

> if both ECoG and SEEG record intracranial electrical potentials, what exactly changes when the contacts lie on the cortical surface versus along trajectories through the brain?

The answer is not simply "depth is better" or "surface is better."

The central mental model is:

```text
neural transmembrane currents
→ intracranial electric fields
→ electrode placement geometry
→ contact and reference potentials
→ voltage channels
→ spatially incomplete samples
→ clinical or scientific inference
```

The sentence to keep throughout the lesson is:

> intracranial EEG is closer to neural sources than scalp EEG, but it is still a selective field measurement rather than direct access to every neuron or every brain region.

---

# Part I — What does "intracranial EEG" mean?

**Intracranial EEG**, abbreviated **iEEG**, is an umbrella term for electrical recordings made using electrodes placed inside the skull.

Two major recording geometries are:

1. **subdural surface electrodes**, commonly arranged as grids or strips and often discussed as electrocorticography;
2. **stereotactically implanted depth electrodes**, used for stereoelectroencephalography.

The terminology is not perfectly uniform across every laboratory or clinical center.

For this lesson, we will use:

```text
ECoG
→ recording from contacts lying on or very near the cortical surface

SEEG
→ recording from contacts distributed along stereotactically planned depth-electrode trajectories

iEEG
→ the broader family containing both
```

This terminology matches the operational distinction used in major reviews of human intracranial electrophysiology.

---

# Part II — ECoG is not "EEG without the skull"

It is tempting to think:

```text
scalp EEG
- scalp
- skull
= ECoG
```

That is too simple.

Moving an electrode from the scalp to the cortical surface changes:

- distance to cortical generators;
- intervening tissues;
- attenuation and spatial smoothing;
- contact size and spacing;
- practical signal-to-noise ratio;
- spatial sampling pattern;
- invasiveness;
- accessible anatomy;
- referencing choices;
- clinical context.

So ECoG and scalp EEG are related field-potential measurements, but they are not interchangeable versions of one sensor.

The next lesson, `NNE-N-0018`, will make the scalp comparison explicit.

---

# Part III — The voltage-difference rule still applies

Let the electric potential at intracranial contact $i$ be $\phi_i(t)$.

Let the reference potential be $\phi_{\mathrm{ref}}(t)$.

The recorded channel is:

$$ V_i(t)=\phi_i(t)-\phi_{\mathrm{ref}}(t). $$

This is exactly the same measurement principle introduced earlier.

The electrode placement changed.

The fact that the instrument records a **difference** did not.

This immediately gives an important warning:

```text
channel waveform
≠
absolute voltage of one cortical location
```

and:

```text
waveform polarity
depends partly on montage and reference
```

---

# Part IV — One event, two geometries

Imagine a transient cortical event generated near the lateral temporal cortex.

A subdural grid may sample it with many neighboring surface contacts.

A depth electrode may encounter the same region along one trajectory, with only a few contacts near the relevant gray matter.

These are different spatial questions.

The surface grid asks approximately:

```text
how does the field vary across this exposed cortical surface?
```

The depth electrode asks approximately:

```text
how does the field vary along this planned path through superficial,
sulcal, white-matter, deep, or mesial structures?
```

The same biological event can therefore produce different channel patterns in the two systems.

---

# Part V — The physical geometry is the first thing to understand

A subdural grid is physically unlike a depth electrode.

That difference is explanatory, not decorative.

![Subdural electrodes and stereo-EEG depth electrodes](https://www.frontiersin.org/files/Articles/611291/xml-images/fnhum-14-611291-g0002.webp)

*Visual anchor — Figure 2 from Grande, Ihnen, and Arya (2020). The left side illustrates subdural electrodes covering the cortical surface; the right side illustrates a stereo-EEG depth electrode traversing brain tissue along a planned trajectory. The lower panel shows representative forms of a subdural grid and a depth electrode. Use the figure to inspect geometry, not to memorize one universal dimension or implantation pattern. Source: [Electrical Stimulation Mapping of Brain Function: A Comparison of Subdural Electrodes and Stereo-EEG](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2020.611291/full), Krista M. Grande, Sarah K. Z. Ihnen, and Ravindra Arya, Frontiers in Human Neuroscience, CC BY 4.0. Registry: `NNE-REF-081`.*

The contrast to notice is:

```text
subdural grid or strip
→ contacts distributed over a surface

SEEG depth electrode
→ contacts distributed along a penetrating trajectory
```

That geometric difference drives much of the rest of the lesson.

---

# Part VI — Surface ECoG: grids and strips

A **grid** places many contacts in a two-dimensional arrangement.

A **strip** places contacts along a narrower flexible carrier.

Conceptually:

```text
grid

o o o o o o
o o o o o o
o o o o o o
o o o o o o

strip

o o o o o o o o
```

For extraoperative recordings in epilepsy evaluation, these contacts are commonly placed subdurally on the cortical surface.

The grid geometry provides relatively contiguous sampling across exposed gyri.

This can be useful when the question requires:

- mapping a superficial cortical region;
- following activity across neighboring surface locations;
- defining boundaries near eloquent cortex;
- stimulating neighboring surface contacts for functional mapping.

But the same geometry has important limits.

---

# Part VII — What surface grids do not naturally reach

A surface grid does not automatically provide dense access to:

- deep sulcal walls;
- insula;
- mesial temporal structures;
- deep medial cortex;
- deep bilateral targets.

A strip can sometimes reach around a margin or into a selected surface region, but surface recording remains constrained by surgical access and geometry.

Therefore:

```text
dense surface coverage
≠
dense whole-brain coverage
```

and:

```text
large grid
≠
complete sampling of the underlying lobe
```

This is a recurring theme in iEEG:

> what you do not sample remains an inference problem.

---

# Part VIII — SEEG: multicontact depth electrodes

A stereotypical SEEG electrode is a thin shaft carrying multiple conductive contacts along its length.

Conceptually:

```text
entry
  ↓
──o──o──o──o──o──o──o──o──
  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑
contacts along one trajectory
```

Several depth electrodes can be implanted along different stereotactically planned trajectories.

A set of trajectories can sample:

- superficial cortex;
- sulcal cortex;
- mesial structures;
- insula;
- deep nuclei or deep cortical targets;
- both hemispheres.

The exact targets are patient- and hypothesis-specific.

---

# Part IX — SEEG is three-dimensional but not dense everywhere

A common overstatement is:

> SEEG gives three-dimensional coverage of the brain.

A safer statement is:

> SEEG can sample a hypothesis-driven three-dimensional set of locations.

The distinction matters.

SEEG samples only where its trajectories and contacts are placed.

Between those contacts can be large unsampled regions.

So:

```text
3D access
≠
continuous 3D measurement
```

The coverage is sparse relative to the full brain volume.

---

# Part X — The implantation plan is part of the measurement

In many clinical cases, invasive monitoring is performed because noninvasive evidence has not been sufficient to define a safe and useful treatment plan.

The implantation is therefore not random.

It is based on a prior hypothesis involving information such as:

- seizure semiology;
- scalp EEG;
- structural imaging;
- functional imaging;
- neuropsychology;
- prior recordings;
- suspected seizure network;
- vascular and anatomical constraints.

That means the electrode layout itself contains prior assumptions.

This is scientifically important.

---

# Part XI — Sampling is hypothesis-driven

Suppose the clinical hypothesis is:

```text
possible mesial temporal onset
with possible spread to lateral temporal cortex
```

A depth-electrode plan may deliberately sample:

```text
hippocampus
amygdala region
temporal pole
lateral temporal cortex
insula
```

Another patient with suspected frontal onset may receive a completely different layout.

Therefore:

```text
patient A channel 12
and
patient B channel 12
```

have no shared anatomical meaning merely because the numbers match.

---

# Part XII — Worked example NNE-EX-079: same 64 contacts, different coverage

Consider two hypothetical 64-contact systems.

### System A — surface ECoG

```text
8 × 8 grid
64 contacts
contiguous lateral cortical surface coverage
```

### System B — SEEG

```text
8 depth electrodes
8 contacts per electrode
64 contacts total
multiple three-dimensional trajectories
```

Both have:

```text
64 physical contacts
```

But they answer different spatial questions.

System A emphasizes:

```text
dense two-dimensional surface relationships
```

System B emphasizes:

```text
sparse three-dimensional access to selected trajectories
```

The correct conclusion is:

```text
same contact count
≠
same anatomy sampled
≠
same spatial density
≠
same inference capability
```

This is the intracranial-EEG version of the geometry lesson from `NNE-0016`.

---

# Part XIII — A depth-electrode contact is not automatically "deep gray matter"

A depth electrode passes through multiple tissue compartments.

Along one trajectory, different contacts may lie near:

```text
cortical gray matter
white matter
sulcal cortex
deep gray matter
ventricle or CSF boundary
another cortical surface
```

So the phrase:

```text
depth contact
```

describes hardware geometry.

It does not guarantee that the contact lies in one particular neural tissue.

Anatomical localization must be established separately.

---

# Part XIV — Gray matter and white matter matter

Neural transmembrane currents are generated mainly by excitable cellular membranes and their synaptic/cellular organization.

A contact located near active gray matter can therefore have a different signal composition from one located primarily in white matter.

But white-matter contacts are not automatically silent.

They can still record volume-conducted fields from nearby or more distant generators.

So:

```text
weak local generator
≠
zero recorded potential
```

This is another reason that contact location and signal interpretation must be separated.

---

# Part XV — Worked example NNE-EX-080: one depth electrode crosses different tissues

Imagine an eight-contact SEEG electrode.

Postimplant localization suggests:

```text
contact 1  superficial cortical gray matter
contact 2  cortical gray matter
contact 3  white matter
contact 4  white matter
contact 5  hippocampal gray matter
contact 6  hippocampal gray matter
contact 7  white matter
contact 8  deep cortical gray matter
```

During a task, contacts 5 and 6 show the largest local high-frequency response.

What can you conclude?

A reasonable statement is:

> the largest measured response along this sampled trajectory occurs at contacts localized to the hippocampal gray-matter segment.

What can you **not** conclude?

You cannot conclude that:

```text
the hippocampus is the only active structure
```

or:

```text
white-matter contacts contain no brain-generated signal
```

or:

```text
unsampled neighboring tissue is inactive
```

The electrode provides samples, not a complete volumetric map.

---

# Part XVI — iEEG measures population field potentials

Clinical ECoG and SEEG contacts are generally much larger than single-cell microelectrodes.

Their signals reflect the superposition of extracellular fields generated by populations of neural elements.

The exact contribution depends on:

- source geometry;
- synchrony;
- distance;
- orientation;
- tissue conductivity;
- contact size;
- contact location;
- reference.

Therefore:

```text
one iEEG channel
≠
one neuron
```

and:

```text
large iEEG amplitude
≠
large number of action potentials by itself
```

The same field-generation principles from `NNE-0015` still apply.

---

# Part XVII — There is no universal "recording radius"

You will sometimes hear statements such as:

> this contact records from X millimeters around it.

Treat such fixed-radius language cautiously.

The observable contribution of a source depends on:

- geometry;
- synchrony;
- frequency;
- conductivity;
- orientation;
- cancellation;
- contact configuration;
- reference.

A synchronized distributed source can remain visible farther away than a small incoherent source.

So:

```text
contact location
does not define
a hard spherical recording boundary
```

---

# Part XVIII — ECoG can be more spatially specific than scalp EEG without being perfectly local

Removing the skull and scalp from between the cortical generator and electrode changes the measurement substantially.

ECoG commonly provides:

- higher signal amplitudes;
- better signal-to-noise ratio;
- access to spatial structure smoothed at the scalp;
- useful higher-frequency information.

But intracranial placement does not abolish volume conduction.

A surface contact can still receive contributions from more than the cortex directly beneath it.

Thus:

```text
closer to cortex
→ usually greater spatial specificity

but

closer to cortex
≠
one-contact-one-patch isolation
```

---

# Part XIX — SEEG can be spatially selective without being continuous

A depth contact close to a local source can strongly reflect that source.

Adjacent contacts can show rapid changes along the electrode trajectory.

That provides useful localization evidence.

But a sparse set of depth trajectories can miss important activity between electrodes.

Therefore two statements can both be true:

```text
SEEG can have high local spatial specificity
```

and:

```text
SEEG can have sparse global coverage
```

These are not contradictory.

---

# Part XX — Surface and depth are complementary geometries

A useful comparison is:

| Property | Subdural ECoG grid/strip | SEEG depth electrodes |
| --- | --- | --- |
| Primary geometry | two-dimensional cortical surface | selected three-dimensional trajectories |
| Superficial contiguous coverage | often strong | usually sparser |
| Deep and mesial access | limited | strong when targeted |
| Sulcal access | limited from surface | possible when targeted |
| Bilateral distributed sampling | surgically more demanding | often feasible with planned trajectories |
| Functional surface mapping | geometrically intuitive | possible but spatial interpretation differs |
| Anatomical completeness | incomplete | incomplete |
| Typical surgical access | craniotomy for large subdural grids | stereotactic burr/twist-drill trajectories |
| Main strength | dense surface sampling | deep/distributed hypothesis-driven access |

Do not turn this table into a universal ranking.

Clinical selection depends on the specific problem, anatomy, center, expertise, and risk-benefit judgment.

---

# Part XXI — The reference can change the waveform

Return to the basic channel equation:

$$ V_i=\phi_i-\phi_{\mathrm{ref}}. $$

Suppose two contacts have potentials:

```text
contact A: 120 μV
contact B:  80 μV
reference: 20 μV
```

Then:

$$ V_A=120-20=100\ \mu\mathrm{V}. $$

and:

$$ V_B=80-20=60\ \mu\mathrm{V}. $$

Now form a bipolar difference:

$$ V_{A-B}=V_A-V_B. $$

Because both channels used the same original reference:

$$ V_{A-B}=\phi_A-\phi_B=40\ \mu\mathrm{V}. $$

This is a different channel representation.

It emphasizes differences between neighboring contacts.

---

# Part XXII — Worked example NNE-EX-081: change the reference, change the channel

Use the same physical contact potentials:

```text
φA = 120 μV
φB = 80 μV
```

### Reference 1

```text
φref = 20 μV
```

Then:

```text
VA = 100 μV
VB = 60 μV
```

### Reference 2

```text
φref = 50 μV
```

Then:

```text
VA = 70 μV
VB = 30 μV
```

The physical potentials at A and B did not change.

The displayed referential channels did.

Now calculate the bipolar difference:

```text
A - B = 40 μV
```

under either shared reference.

The lesson is:

> montage is not a cosmetic plotting choice. It changes the mathematical signal being analyzed.

Detailed referencing belongs later in `NNE-N-0024`.

---

# Part XXIII — Referential and bipolar recordings answer different spatial questions

A referential channel asks:

```text
how different is this contact from the chosen reference?
```

A bipolar channel asks:

```text
how different are these two contacts?
```

If both contacts contain a strong shared field, subtraction may reduce that shared component.

If the source is highly local to one contact, the difference may remain large.

But bipolar derivations can also:

- invert apparent polarity when contact order changes;
- attenuate broad signals;
- create spatial derivatives that are harder to compare across geometries.

So:

```text
bipolar
≠
automatically more correct
```

It is one measurement representation.

---

# Part XXIV — Polarity is not a universal biological label

Suppose an ECoG deflection is negative at one contact.

Do not immediately translate:

```text
negative voltage
→ inhibition
```

or:

```text
negative voltage
→ inward current at one fixed cortical layer
```

The recorded polarity depends on:

- source-sink geometry;
- orientation;
- reference;
- contact placement;
- conduction.

The same biological process can look different under different montages.

This is inherited directly from the extracellular-field logic of `NNE-0015`.

---

# Part XXV — What signals appear in iEEG?

Intracranial recordings can contain several classes of activity, including:

- slow fluctuations;
- oscillatory rhythms;
- evoked potentials;
- broadband high-frequency activity;
- interictal epileptiform discharges;
- ictal activity during seizures;
- artifacts from movement or equipment;
- stimulation artifacts when stimulation is used.

These are not independent physical substances.

They are analysis-level descriptions of features present in voltage recordings.

---

# Part XXVI — Frequency bands are analysis conventions

Terms such as:

```text
delta
theta
alpha
beta
gamma
high gamma
high-frequency broadband
```

are useful.

But their numerical boundaries vary across studies.

Do not turn one paper's band definitions into universal physiology.

Formal spectral analysis belongs to:

`NNE-N-0028 — Spectra, rhythms, time-frequency representations, and oscillatory features`.

Here we only need the measurement interpretation.

---

# Part XXVII — High-frequency broadband is useful but not a direct spike counter

Human ECoG research often uses increases in broadband high-frequency power as a marker of local population engagement.

That feature can correlate with population firing.

But the relationship is not a one-to-one identity.

Experimental work has demonstrated components of broadband high-frequency activity that dissociate from local multi-unit firing.

Therefore:

```text
larger high-frequency broadband
≠
exactly N more spikes
```

A safer statement is:

> broadband high-frequency activity is an informative population-level electrophysiological feature whose physiological contributors can include processes correlated with, but not reducible to, local spike count.

This distinction prevents a common overinterpretation.

---

# Part XXVIII — Normal iEEG varies across anatomy

Different brain regions can have different characteristic spectral patterns even in physiological recordings.

That means:

```text
one "normal EEG shape"
```

does not exist uniformly across all intracranial locations.

The multicenter intracranial EEG atlas by Frauscher and colleagues demonstrates regional variation in physiological wakeful iEEG activity.

Therefore anatomical localization is not optional metadata.

It is part of interpretation.

---

# Part XXIX — iEEG is a clinical measurement before it becomes a research dataset

Most human chronic iEEG recordings exist because a patient needs clinical evaluation.

A common context is drug-resistant focal epilepsy when noninvasive data are insufficient to define the suspected epileptogenic network and a safe treatment plan.

Clinical goals can include:

- identifying the earliest recorded ictal activity;
- determining seizure propagation;
- testing competing localization hypotheses;
- mapping functional tissue;
- supporting later therapeutic decisions.

Research use is often secondary to clinical need.

That creates important sampling constraints.

---

# Part XXX — "Seizure onset zone" and "epileptogenic zone" are not identical by definition

A recording may identify contacts at which the earliest electrographic seizure changes are observed.

Call that evidence about the **sampled seizure onset zone**.

The broader clinical concept of an **epileptogenic zone** concerns tissue whose treatment is necessary for seizure freedom.

Those concepts should not be collapsed casually.

Why?

Because iEEG does not sample every possible site.

The earliest recorded activity may not be the absolute biological origin if an earlier generator lies in unsampled tissue.

---

# Part XXXI — Absence of recorded onset is not proof of absence

Suppose no seizure onset is observed on any implanted contact in region X.

What can you conclude?

Only that:

> the implanted contacts did not record a convincing onset pattern from the sampled locations in region X under the recorded conditions.

You cannot automatically conclude:

```text
all of region X is not involved
```

if region X was incompletely sampled.

This is the logic of partial observation.

---

# Part XXXII — Worked example NNE-EX-082: earliest recorded activity depends on coverage

Imagine a synthetic seizure.

True distributed evolution:

```text
deep mesial structure
→ temporal pole
→ lateral temporal cortex
```

### Recording plan A — surface grid only

The first measured ictal change appears on lateral temporal contacts.

### Recording plan B — depth plus surface coverage

The first measured ictal change appears 600 ms earlier on mesial depth contacts.

What changed?

Not necessarily the biology.

The observation geometry changed.

The lesson is:

```text
earliest recorded contact
depends on
where electrodes were placed
```

Therefore the phrase:

> "the seizure started here"

should be interpreted within the sampled electrode network and the full clinical evidence.

---

# Part XXXIII — Propagation is not the same as origin

When a seizure spreads, channels can become involved sequentially.

A later large-amplitude signal may be more visually dramatic than the earliest subtle change.

So:

```text
largest ictal amplitude
≠
earliest recorded onset
```

and:

```text
first channel with obvious clinical waveform
≠
guaranteed biological source
```

Temporal order is evidence.

It still requires spatial and physiological interpretation.

---

# Part XXXIV — Interictal spikes are not seizures

Interictal epileptiform discharges occur between seizures.

They can provide important localization evidence.

But:

```text
frequent interictal spikes
≠
proof that the same contact is the ictal onset
```

Different markers answer different questions.

A robust clinical interpretation integrates:

- interictal activity;
- ictal onset;
- spread;
- anatomy;
- functional mapping;
- other diagnostic evidence.

This lesson does not teach epilepsy diagnosis.

It teaches the measurement boundary.

---

# Part XXXV — Human iEEG research is anatomically biased by clinical necessity

Suppose a research group wants to study memory.

They cannot implant electrodes arbitrarily throughout healthy brains simply to improve research coverage.

Electrodes are placed for clinical reasons.

Therefore research sampling is constrained by:

- the patient's disease;
- the clinical hypothesis;
- safety;
- anatomy;
- the surgical plan;
- available contacts.

This creates a strong selection bias.

---

# Part XXXVI — Electrode coverage differs across participants

Participant A may have:

```text
left temporal SEEG
```

Participant B may have:

```text
bilateral frontal and insular SEEG
```

Participant C may have:

```text
right temporal subdural grid
```

A group study cannot treat these as if every participant contributed the same brain locations.

Common strategies include:

- anatomical localization;
- coordinate registration;
- region-of-interest grouping;
- coverage maps;
- mixed-effects or hierarchical analyses;
- reporting how many participants contribute data to each region.

Those details become more important in later neural-data lessons.

---

# Part XXXVII — A beautiful activation map can hide sparse sampling

Suppose a figure shows colored dots across a standard brain.

The colors may represent electrode responses.

Before interpreting the spatial pattern, ask:

1. where were electrodes actually implanted?
2. how many participants contributed contacts there?
3. were unsampled regions displayed as zero or simply absent?
4. were surface and depth contacts mixed?
5. how were coordinates normalized across brains?

This is a powerful habit for reading iEEG papers.

---

# Part XXXVIII — Electrode localization is a separate inference step

The hardware manufacturer may specify contact positions along a lead.

But after implantation, the scientific question is:

> where is each contact relative to this person's anatomy?

Localization commonly combines imaging such as:

- preimplant MRI;
- postimplant CT;
- radiography;
- image coregistration;
- anatomical segmentation.

Exact workflows vary by center.

The key concept is:

```text
contact number
→ physical electrode
→ imaging localization
→ anatomical label
```

not:

```text
contact number
→ anatomy by assumption
```

---

# Part XXXIX — Surface electrodes can move the anatomy they are measuring

Subdural grids often require craniotomy.

Opening the skull and placing a grid can alter cortical geometry through:

- brain shift;
- swelling;
- CSF loss;
- mechanical interaction with the grid.

Therefore preoperative anatomy and postimplant contact location may not align perfectly.

This is one reason electrode localization requires careful imaging and registration.

---

# Part XL — SEEG also requires localization

SEEG trajectories are stereotactically planned.

But planned coordinates are not enough.

One still needs to verify:

- actual electrode trajectory;
- actual contact locations;
- relation to gray and white matter;
- relation to vascular structures;
- relation to the hypothesis being tested.

The word **stereotactic** means the procedure uses a spatial targeting framework.

It does not mean localization uncertainty disappears.

---

# Part XLI — Surface contiguity and depth access create different blind spots

A grid can provide dense coverage of exposed cortex while missing:

```text
deep sulci
insula
mesial structures
deep network nodes
```

SEEG can access those structures but may miss:

```text
large contiguous areas between trajectories
fine two-dimensional boundaries across exposed cortex
```

So each geometry creates blind spots.

A good measurement plan makes those blind spots explicit.

---

# Part XLII — No modality is globally "higher resolution"

The word **resolution** needs qualification.

Possible meanings include:

- contact spacing;
- source localization precision;
- temporal resolution;
- ability to distinguish neighboring cortical sites;
- coverage density;
- anatomical access.

ECoG and SEEG can trade these dimensions differently.

Therefore:

```text
SEEG has higher resolution
```

or:

```text
ECoG has higher resolution
```

is incomplete without saying:

> resolution of what, in which direction, over which anatomical region?

---

# Part XLIII — Temporal resolution is excellent, spatial completeness is not

Intracranial electrophysiology measures electrical activity on millisecond time scales.

That is a major strength.

But high temporal resolution does not imply full spatial coverage.

This combination is characteristic:

```text
excellent temporal sampling
+
selective spatial sampling
```

The two axes must be evaluated separately.

---

# Part XLIV — iEEG can reveal network timing

If contacts sample multiple network nodes, iEEG can reveal:

- relative timing;
- phase relationships;
- evoked responses;
- task-related changes;
- seizure propagation;
- functional interactions.

But simultaneous observation of two nodes does not prove direct causal communication between them.

A common cause can drive both.

Volume conduction can also create correlation.

Connectivity inference requires additional assumptions and methods.

---

# Part XLV — Correlation between contacts has several explanations

Two iEEG channels can be correlated because of:

```text
shared neural source
true interaction
common input
volume conduction
shared reference
artifact
```

These mechanisms are not equivalent.

Therefore:

```text
high correlation
≠
direct anatomical connection
```

This is an important general neural-data caution.

---

# Part XLVI — The contact spacing does not equal source spacing

Suppose adjacent ECoG contacts are separated by several millimeters.

That is the **sampling pitch**.

It does not mean:

```text
each contact represents an independent several-millimeter cortical tile
```

because neighboring contacts can share field contributions.

Likewise, adjacent SEEG contacts can record overlapping source mixtures.

Physical pitch is not the same as biological independence.

---

# Part XLVII — Contact size changes spatial averaging

A larger conductive contact integrates potential over a larger interface region.

A smaller contact samples a more localized interface but can alter:

- impedance;
- noise;
- signal amplitude;
- manufacturing constraints.

So:

```text
smaller contact
≠
automatically better recording
```

This reconnects to the electrode-tissue interface from `NNE-0013`.

---

# Part XLVIII — Macro-ECoG and micro-ECoG occupy different design regimes

Clinical ECoG commonly uses millimeter-scale contacts.

Research systems can use much smaller and denser contacts, often called **micro-ECoG** or **μECoG**.

Reducing contact size and pitch can reveal finer spatial structure.

But the same distinctions remain:

```text
site ≠ channel ≠ source
```

and:

```text
higher density
≠
complete cortical coverage
```

Detailed advanced array design belongs later in the curriculum.

---

# Part XLIX — ECoG is not always chronic extraoperative monitoring

The word **electrocorticography** can also refer to acute intraoperative recording from the exposed cortex.

That use differs from days-long extraoperative subdural monitoring.

So when reading a paper, ask:

```text
intraoperative ECoG?
or
implanted extraoperative ECoG?
```

The physiological measurement is related, but:

- duration;
- behavioral state;
- anesthesia;
- electrode layout;
- clinical goal

can differ substantially.

---

# Part L — SEEG is not just a depth version of scalp EEG

SEEG contacts are inside the brain.

That changes:

- source distance;
- anatomical selectivity;
- signal amplitude;
- available spatial patterns;
- frequency content;
- safety constraints.

So calling it "deep EEG" can be a useful first intuition but becomes misleading if it hides the invasive geometry.

A better model is:

> SEEG is intracranial extracellular field recording using stereotactically placed multicontact depth electrodes.

---

# Part LI — Intracranial recordings can still contain artifacts

Being inside the skull does not eliminate artifact.

Possible artifact sources include:

- cable movement;
- amplifier saturation;
- stimulation;
- muscle activity;
- cardiac activity;
- line-frequency interference;
- poor contact behavior;
- surgical hardware;
- reference contamination.

Detailed artifact analysis belongs to `NNE-N-0025`.

The present lesson only establishes:

```text
intracranial
≠
artifact-free
```

---

# Part LII — More signal amplitude is not automatically more neural information

Compared with scalp EEG, intracranial recordings often have larger amplitudes and better signal-to-noise ratio for nearby sources.

But scientific value depends on:

- target placement;
- anatomical coverage;
- reference;
- signal quality;
- task;
- analysis.

A large signal from the wrong location may be less useful than a smaller signal from the relevant structure.

---

# Part LIII — ECoG and SEEG can both be used for stimulation

The same implanted contacts can often be used not only to record but also to deliver electrical stimulation for functional mapping or other clinical tests.

That creates a bidirectional interface:

```text
record
↔
stimulate
```

But recording and stimulation are different operating modes.

Detailed stimulation waveform, charge transfer, recruitment, and safety belong to:

- `NNE-N-0044 — Electrical neural stimulation: waveform, charge transfer, recruitment, and spatial spread`;
- `NNE-N-0045 — Stimulation safety as a systems problem: tissue, electrode, charge, heat, and unintended activation`.

This lesson does not teach stimulation protocols.

---

# Part LIV — Functional mapping does not mean one contact equals one function

Electrical stimulation can evoke or disrupt behavior.

But:

```text
contact produces language disruption
≠
one tiny point contains "language"
```

Responses depend on:

- current spread;
- network organization;
- task;
- stimulation parameters;
- contact geometry;
- individual anatomy.

Functional mapping is evidence about network necessity or perturbability under a specific stimulation condition.

It is not a literal one-contact-one-function atlas.

---

# Part LV — Surgical risk is part of the modality tradeoff

Both subdural ECoG and SEEG are invasive procedures.

Potential complications include categories such as:

- hemorrhage;
- infection;
- neurological injury;
- edema;
- hardware complications.

Comparative studies often report lower complication rates for SEEG than for subdural-grid approaches in selected modern cohorts.

But a careful learner should not turn that population-level observation into:

```text
SEEG is always safer for every patient
```

Risk depends on:

- anatomy;
- trajectories;
- procedure;
- center;
- patient;
- number of electrodes;
- duration;
- definitions used in the study.

---

# Part LVI — Different invasiveness profiles are not the same as "invasive" versus "noninvasive"

Both methods cross the skull boundary.

Subdural grids commonly require a craniotomy.

SEEG commonly uses multiple stereotactically planned small openings and penetrating electrodes.

So the comparison is:

```text
two different invasive geometries
```

not:

```text
invasive versus noninvasive
```

That distinction matters when discussing safety and ethics.

---

# Part LVII — Clinical outcome evidence does not isolate hardware alone

Suppose one study finds different seizure outcomes after SEEG-guided versus subdural-grid-guided surgery.

That does not mean the electrode type alone caused the outcome.

The groups can differ in:

- disease anatomy;
- lesion visibility;
- center expertise;
- selection criteria;
- surgical strategy;
- target complexity.

Modern comparative-effectiveness studies try to control these differences statistically, but residual confounding remains possible.

This is a good example of evidence interpretation in neural engineering.

---

# Part LVIII — Worked example NNE-EX-083: high-frequency broadband is not spike count

Imagine an ECoG contact during a movement task.

Baseline:

```text
broadband high-frequency power = low
```

Movement epoch:

```text
broadband high-frequency power = strongly elevated
```

A careless interpretation is:

> firing rate increased by the same factor as broadband power.

That is not justified.

A better interpretation is:

> the local population-level high-frequency electrophysiological feature increased during movement.

To convert that into a statement about firing, you need independent evidence about the relationship between broadband activity and spiking in that preparation.

The lesson is:

```text
useful correlate
≠
identical physical variable
```

---

# Part LIX — A complete iEEG channel needs metadata

A useful channel record should connect the voltage trace to context.

Conceptually:

```text
channel
→ contact or contact pair
→ electrode
→ grid / strip / depth lead
→ anatomical location
→ reference or montage
→ sampling parameters
→ clinical state
→ event annotations
```

Without this metadata, the waveform can be impossible to interpret correctly.

Formal dataset organization belongs to `NNE-N-0029`.

---

# Part LX — The same contact can become different derived channels

Suppose contact A is used in:

```text
A - reference
A - B
A - C
common-average-referenced A
```

These are not four physical electrodes.

They are four mathematical channel representations involving the same physical contact.

Therefore:

```text
physical-contact count
≠
derived-channel count
```

This distinction becomes important in shared datasets.

---

# Part LXI — Electrode naming conventions are local

Labels such as:

```text
LAH1
RA1
LTG23
B'4
```

may encode:

- hemisphere;
- target;
- electrode;
- contact number.

But conventions vary across centers.

Never decode an unfamiliar channel label by guessing.

Use the dataset's electrode table or metadata.

---

# Part LXII — Contact order on a depth lead matters

Depth-electrode contacts are ordered along the shaft.

But whether:

```text
contact 1
```

is deepest or most superficial is a naming convention, not a universal physical law.

Again:

> metadata beats assumption.

This is a small but common practical source of error.

---

# Part LXIII — The same brain region can be sampled with different orientations

A depth trajectory can cross a cortical structure at different angles.

A surface contact is oriented approximately with the cortical surface.

Source geometry relative to the contact therefore differs.

That can alter:

- amplitude;
- polarity;
- spatial gradient;
- apparent local specificity.

The physical arrangement matters beyond anatomical labels alone.

---

# Part LXIV — Cortical folding complicates "under the contact"

A surface grid lies over a folded cortical sheet.

A contact positioned over a gyrus can receive contributions from:

- gyral crown;
- nearby sulcal walls;
- distributed synchronized sources.

Therefore a two-dimensional surface coordinate is not equivalent to a flat cortical patch.

Cortical geometry remains three-dimensional even when the array is planar.

---

# Part LXV — SEEG contacts can sample both banks of a sulcus

A depth electrode trajectory can cross folded cortex.

Adjacent contacts may lie in different cortical banks or tissue compartments.

That is one reason depth recordings can provide access to sulcal cortex that surface grids cannot sample directly.

But it also means neighboring contact numbers can belong to anatomically different structures.

---

# Part LXVI — Spatial specificity depends on frequency and source synchrony

A distributed low-frequency field can be visible across many contacts.

A high-frequency local feature can sometimes be more spatially confined.

But this is a tendency, not a universal law.

Do not infer:

```text
high frequency
→ always local

low frequency
→ always global
```

Source synchrony and geometry matter.

Formal spectral reasoning is deferred to `NNE-N-0028`.

---

# Part LXVII — Clinical iEEG is not a random sample of healthy brain physiology

This limitation deserves repetition.

Most long-duration human iEEG data come from people with neurological disease, commonly epilepsy.

Possible confounds include:

- pathology;
- medication changes;
- sleep disruption;
- seizures;
- recent surgery;
- electrode implantation;
- hospital environment.

That does not make the data useless.

It means generalization requires care.

---

# Part LXVIII — "Normal contacts" require criteria

A contact far from the seizure onset zone may still be affected by:

- pathology;
- network effects;
- medication;
- volume conduction.

Studies such as the normal iEEG atlas use explicit criteria to select contacts considered likely to sample relatively healthy tissue.

That is stronger than simply calling every non-seizure contact "normal."

---

# Part LXIX — iEEG gives millisecond timing, but task timing still matters

A neural response may be aligned to:

- stimulus onset;
- movement onset;
- speech onset;
- memory retrieval;
- seizure onset;
- stimulation pulse.

Accurate event timing is essential.

A 1-ms-capable signal does not help if behavioral timestamps are uncertain by 200 ms.

Temporal resolution is an end-to-end system property.

---

# Part LXX — The recording chain for iEEG

A useful system diagram is:

```mermaid
flowchart LR
    A["Neural transmembrane currents"] --> B["Intracranial electric fields"]
    B --> C["Surface or depth contacts"]
    C --> D["Reference and front end"]
    D --> E["Digitized iEEG channels"]
    E --> F["Montage and preprocessing"]
    F --> G["Events, spectra, or spatial patterns"]
    G --> H["Clinical or research inference"]
```

Every arrow can distort, filter, omit, or transform information.

This is the measurement-chain perspective from `NNE-0009`.

---

# Part LXXI — A second mental model: coverage as a mask

Think of the brain as containing a distributed field $\phi(\mathbf{r},t)$.

An implanted contact samples only selected spatial locations.

Conceptually:

```text
full field in brain
→ implanted spatial mask
→ measured contact potentials
→ channel derivations
```

The key word is **mask**.

The implant does not reveal the entire field.

It reveals the part made observable by the chosen geometry.

---

# Part LXXII — Coverage and localization are different

**Coverage** asks:

> where did we place contacts?

**Localization** asks:

> where exactly are those contacts anatomically?

**Inference** asks:

> what do the recorded signals imply about the underlying neural process?

These are three different problems.

Do not collapse them.

---

# Part LXXIII — A contact can be well localized but still measure a mixture

Suppose imaging localizes one ECoG contact perfectly over left motor cortex.

That does not mean every microvolt in that channel came only from neurons directly underneath the contact.

Localization describes the sensor.

Source attribution describes the generators.

Those are related but distinct.

---

# Part LXXIV — A local signal can still be network-driven

Suppose a task causes a strong local ECoG response in motor cortex.

Possible interpretations include:

- local synaptic input;
- local recurrent processing;
- output-related population activity;
- input arriving from another network node.

The recording localizes the field measurement better than it localizes causal origin.

This distinction becomes important in network neuroscience.

---

# Part LXXV — Spatial sampling creates an inverse problem

The forward problem is:

```text
neural sources
→ fields
→ contact voltages
```

The inverse problem is:

```text
contact voltages
→ infer neural sources
```

Many different source configurations can produce similar recorded voltages.

Intracranial placement constrains the inverse problem more strongly than scalp EEG in many situations.

It does not make the inverse unique.

---

# Part LXXVI — Why iEEG can be powerful for cognitive neuroscience

When clinically implanted contacts happen to sample a relevant network, researchers gain:

- direct millisecond-scale human electrophysiology;
- access to deep structures unavailable to scalp sensors;
- spatial specificity unavailable to many noninvasive modalities;
- the possibility of stimulation;
- within-human links between anatomy, timing, and behavior.

These are extraordinary strengths.

They coexist with equally important sampling limitations.

---

# Part LXXVII — Why iEEG can mislead if coverage is ignored

Imagine a memory task.

Only temporal and frontal contacts were implanted.

The experiment finds no parietal response.

That statement is meaningless if no parietal contacts existed.

The correct report is:

```text
no parietal measurement was available
```

not:

```text
parietal cortex was inactive
```

This seems obvious, but coverage mistakes can hide inside group figures and statistical summaries.

---

# Part LXXVIII — The next lesson deliberately moves outside the skull

The next canonical lesson is:

`NNE-N-0018 — Scalp EEG: potentials, montages, volume conduction, and spatial ambiguity`.

The transition will be:

```text
intracranial contacts close to neural tissue
→
scalp contacts separated by brain, CSF, meninges, skull, and scalp
```

The same voltage-difference rule will remain.

The source-to-sensor physics and spatial ambiguity will change substantially.

---

# Part LXXIX — What we are deliberately not doing yet

## Full scalp EEG theory

Montages, scalp topography, reference choices, and the severe spatial ambiguity of scalp measurements belong to `NNE-N-0018`.

---

## Sampling and digitization

We assume the voltage has already reached a usable acquisition system.

Sampling theory, aliasing, quantization, and dynamic range belong to `NNE-N-0023`.

---

## Front-end referencing and common-mode rejection

We used referential and bipolar equations to establish interpretation.

Circuit-level referencing, grounding, and differential amplification belong to `NNE-N-0024`.

---

## Artifact engineering

Detailed mains pickup, movement, electrode noise, and biological artifacts belong to `NNE-N-0025`.

---

## Filtering

We did not choose high-pass, low-pass, notch, or zero-phase filters.

That belongs to `NNE-N-0026`.

---

## Spectral analysis

We named high-frequency broadband and conventional bands without teaching Fourier or time-frequency methods.

That belongs to `NNE-N-0028`.

---

## Dataset architecture

We introduced channel-to-contact-to-anatomy metadata.

Formal dataset schemas and alignment belong to `NNE-N-0029`.

---

## Electrical stimulation

We noted that iEEG contacts can also stimulate.

Waveform physics and safety belong to `NNE-N-0044` and `NNE-N-0045`.

---

# Part LXXX — Common failure modes

## Failure mode 1 — "iEEG means ECoG"

Why it fails:

iEEG is broader.

ECoG is one intracranial recording geometry.

SEEG is another.

---

## Failure mode 2 — "ECoG is scalp EEG with the skull removed"

Why it fails:

Placement, geometry, contact size, reference, spatial sampling, and clinical context all change.

---

## Failure mode 3 — "SEEG gives continuous 3D coverage"

Why it fails:

It gives sparse samples along selected three-dimensional trajectories.

---

## Failure mode 4 — "A surface grid covers the whole lobe"

Why it fails:

It only samples the contacted surface and remains limited for deep, mesial, and sulcal structures.

---

## Failure mode 5 — "One iEEG contact records one neuron"

Why it fails:

Clinical intracranial contacts record population field potentials.

---

## Failure mode 6 — "A depth contact is automatically in deep gray matter"

Why it fails:

Contacts along the same shaft can traverse gray matter, white matter, and other compartments.

---

## Failure mode 7 — "White-matter contacts should be zero"

Why it fails:

Volume-conducted fields can remain visible even where local generators are weak.

---

## Failure mode 8 — "Every contact has a fixed recording radius"

Why it fails:

Source geometry, synchrony, frequency, conductivity, and reference determine spatial contribution.

---

## Failure mode 9 — "ECoG is perfectly local because it is on the cortex"

Why it fails:

Volume conduction remains.

Nearby and distributed sources can contribute.

---

## Failure mode 10 — "SEEG is always more spatially precise"

Why it fails:

Precision depends on the spatial question.

SEEG is sparse between trajectories; grids can be dense across exposed surface cortex.

---

## Failure mode 11 — "More contacts means better coverage"

Why it fails:

Coverage depends on where the contacts are placed and how densely they sample the relevant anatomy.

---

## Failure mode 12 — "Bipolar montage is the true signal"

Why it fails:

It is one derived difference between contacts.

Other montages answer different questions.

---

## Failure mode 13 — "Negative voltage means inhibition"

Why it fails:

Polarity depends on source geometry and reference.

---

## Failure mode 14 — "High gamma equals firing rate"

Why it fails:

Broadband high-frequency activity can correlate with firing but is not identical to spike count.

---

## Failure mode 15 — "The largest ictal signal is the seizure origin"

Why it fails:

Amplitude and onset timing are different properties.

Propagation can produce larger later signals.

---

## Failure mode 16 — "The first recorded contact is the absolute biological origin"

Why it fails:

An earlier generator can exist in unsampled tissue.

---

## Failure mode 17 — "Interictal spikes prove the seizure onset zone"

Why it fails:

Interictal and ictal markers answer related but distinct questions.

---

## Failure mode 18 — "No signal means the brain region is inactive"

Why it fails:

Poor sampling, reference, noise, source geometry, and unsampled subregions can all defeat that inference.

---

## Failure mode 19 — "Electrode coverage in research is random"

Why it fails:

Human iEEG placement is clinically driven and therefore strongly biased.

---

## Failure mode 20 — "Contact 1 means the same physical direction on every depth electrode"

Why it fails:

Contact-number conventions vary.

---

## Failure mode 21 — "Planned coordinates are final localization"

Why it fails:

Postimplant verification and anatomical registration are still needed.

---

## Failure mode 22 — "SEEG is noninvasive compared with ECoG"

Why it fails:

Both are invasive.

They have different surgical geometries and risk profiles.

---

## Failure mode 23 — "A lower complication rate in one cohort proves one method is always safer"

Why it fails:

Selection, anatomy, center, and procedure influence observed outcomes.

---

## Failure mode 24 — "A functional stimulation response assigns one function to one contact"

Why it fails:

Stimulation perturbs a network volume, not an isolated labeled neuron population.

---

## Failure mode 25 — "An anatomical label identifies the neural source"

Why it fails:

A localized sensor can still record a mixture of nearby and distributed generators.

---

# Part LXXXI — Active work

## Exercise A — classify the geometry

For each statement, choose:

```text
surface ECoG
SEEG
both
neither
```

1. contacts lie on a grid over exposed cortical surface;
2. contacts lie along several stereotactic penetrating trajectories;
3. recording is a voltage difference;
4. every contact directly identifies one neuron;
5. the system can be used for functional electrical stimulation;
6. deep mesial targets can be sampled when specifically targeted.

### Check

1. surface ECoG;
2. SEEG;
3. both;
4. neither;
5. both;
6. SEEG.

---

## Exercise B — coverage versus density

System A:

```text
96 contacts in one dense lateral temporal grid
```

System B:

```text
96 contacts spread across 12 depth electrodes targeting both hemispheres
```

Answer:

1. Which has denser contiguous surface sampling?
2. Which can more naturally access selected deep bilateral structures?
3. Which samples more total brain tissue?
4. Can question 3 be answered from contact count alone?

### Check

1. System A.
2. System B.
3. Not determined.
4. No.

---

## Exercise C — reference dependence

Suppose:

```text
φA = 150 μV
φB = 100 μV
φref = 40 μV
```

Calculate:

```text
VA
VB
VA-B
```

### Check

$$ V_A=110\ \mu\mathrm{V}. $$

$$ V_B=60\ \mu\mathrm{V}. $$

$$ V_{A-B}=50\ \mu\mathrm{V}. $$

---

## Exercise D — gray versus white matter

A depth contact in white matter shows a 30-μV rhythm coherent with nearby cortical contacts.

Is this impossible?

### Check

No.

A white-matter contact can record volume-conducted field activity even if local gray-matter generators are weak.

---

## Exercise E — missing coverage

A study reports:

> "No hippocampal response was observed."

But the participant had only lateral frontal and temporal surface electrodes.

What is wrong?

### Check

There was no direct hippocampal measurement.

The correct statement is that hippocampal activity was not sampled by the implant.

---

## Exercise F — earliest recorded seizure activity

A deep temporal contact changes first, followed by a surface temporal grid 800 ms later.

What can be said safely?

### Check

The earliest recorded ictal change among the sampled contacts occurred on the deep temporal contact.

That does not by itself prove the absolute biological origin of the seizure.

---

## Exercise G — high-frequency broadband

During speech, high-frequency broadband power doubles at one ECoG contact.

Can you conclude that firing rate doubled?

### Check

No.

Broadband high-frequency activity is a population-level electrophysiological correlate, not a calibrated one-to-one spike-count measurement.

---

## Exercise H — choose a recording geometry

### Question 1

You need dense coverage over a superficial cortical patch near language cortex.

### Question 2

You need to test a hypothesis involving insula and bilateral mesial temporal structures.

### Check

1. A subdural grid may offer useful contiguous surface coverage.
2. SEEG trajectories can be better suited to targeted deep and bilateral sampling.

These are conceptual matches, not clinical recommendations.

---

# Part LXXXII — Retrieval practice

Answer without looking back.

1. What does iEEG mean?
2. What is ECoG in this lesson?
3. What is SEEG?
4. Why is ECoG not just scalp EEG minus the skull?
5. Write the basic intracranial channel equation.
6. Why is a channel not an absolute potential?
7. What is a grid?
8. What is a strip?
9. What is a depth electrode?
10. Why is SEEG called three-dimensional but still sparse?
11. Why is an implantation plan hypothesis-driven?
12. Why does equal contact count not imply equal coverage?
13. Why can a depth electrode contain both gray- and white-matter contacts?
14. Why can a white-matter contact still show brain-generated signal?
15. Why is there no universal recording radius?
16. Why can ECoG be more spatially specific than scalp EEG?
17. Why is ECoG still affected by volume conduction?
18. What spatial advantage do subdural grids have?
19. What spatial advantage does SEEG have?
20. Why is neither modality globally "higher resolution"?
21. What does a referential channel measure?
22. What does a bipolar channel measure?
23. Why can montage change waveform amplitude and polarity?
24. Why does negative voltage not mean inhibition?
25. Name four kinds of features that can appear in iEEG.
26. Why are frequency-band boundaries conventions?
27. Why is high-frequency broadband not identical to firing rate?
28. Why does physiological iEEG vary across brain regions?
29. Why is human iEEG electrode coverage clinically biased?
30. Why does a group iEEG study need a coverage map?
31. Why is postimplant localization necessary?
32. What is brain shift?
33. Why is the earliest recorded seizure contact not necessarily the absolute origin?
34. Why are interictal spikes not identical to ictal onset?
35. What is the difference between seizure onset evidence and the broader epileptogenic-zone concept?
36. Why can intracranial channels remain correlated without direct connectivity?
37. Why does contact spacing not equal source independence?
38. What is micro-ECoG?
39. Why is SEEG still invasive?
40. Which next lesson moves to scalp EEG?
41. Which later lesson owns detailed referencing?
42. Which later lesson owns artifacts?
43. Which later lesson owns spectra and rhythms?
44. Which later lesson owns neural dataset metadata?
45. Which later lessons own stimulation physics and safety?
46. Finish the sentence: iEEG is closer to neural sources, but it is still a ______ field measurement rather than complete access to the brain.

---

# Part LXXXIII — Backward connections

## Connection backward: NNE-0006

Synaptic and transmembrane currents generate extracellular fields.

ECoG and SEEG observe population-level consequences of those currents.

---

## Connection backward: NNE-0007

The move from neurons to populations and circuits becomes concrete here.

Clinical iEEG contacts observe mixtures of population activity rather than isolated neurons.

---

## Connection backward: NNE-0008

`NNE-0008` introduced neural signal modalities.

This lesson deepens one branch:

```text
intracranial electrical field potentials
```

and distinguishes surface from depth geometry.

---

## Connection backward: NNE-0009

The neural measurement chain remains:

```text
source
→ tissue
→ electrode
→ electronics
→ data
→ inference
```

The present lesson emphasizes electrode location and spatial coverage.

---

## Connection backward: NNE-0012

ECoG and SEEG demonstrate coupled tradeoffs:

```text
surface density
deep access
bilateral coverage
invasiveness
surgical burden
localization
sampling completeness
```

No single method maximizes all of them.

---

## Connection backward: NNE-0013

Contact size and interface properties still matter.

Intracranial macroelectrodes remain electrode-tissue interfaces, not abstract points.

---

## Connection backward: NNE-0015

The extracellular-field interpretation carries directly forward.

ECoG and SEEG record spatially filtered mixtures of extracellular fields.

---

## Connection backward: NNE-0016

`NNE-0016` taught:

```text
site ≠ channel ≠ unit
```

This lesson adds:

```text
contact layout ≠ anatomical completeness
```

and:

```text
equal contact count ≠ equal surface/depth coverage
```

---

# Part LXXXIV — Forward connections

## NNE-N-0018 — Scalp EEG

The next lesson will add the skull and scalp back into the source-to-sensor path.

It will focus on:

- scalp potentials;
- montages;
- volume conduction;
- spatial ambiguity.

---

## NNE-N-0023 — Sampling and digitization

The high temporal resolution of iEEG only becomes digital data through sampling and quantization.

---

## NNE-N-0024 — Biopotential front ends

The simple reference equations used here will become a full treatment of:

- differential amplification;
- grounding;
- common mode;
- reference choice.

---

## NNE-N-0025 — Noise and artifacts

Intracranial data are not artifact-free.

The next instrumentation layer will separate:

- electrode noise;
- movement;
- mains pickup;
- biological artifacts.

---

## NNE-N-0028 — Spectra and rhythms

Terms such as alpha, beta, gamma, and broadband high-frequency activity will receive proper spectral treatment.

---

## NNE-N-0029 — Neural datasets

The metadata chain:

```text
channel
→ contact
→ electrode
→ anatomy
→ event
```

will become part of formal dataset design.

---

## NNE-N-0044 and NNE-N-0045 — Stimulation

Recording contacts can also become stimulation contacts.

Later lessons will treat the stimulation mode as its own physical and safety problem.

---

# Compact summary

```text
1. Intracranial EEG is a family of invasive electrical recordings made inside the skull.

2. ECoG samples cortical-surface field potentials with grids or strips; SEEG samples along stereotactically planned depth-electrode trajectories.

3. Surface and depth geometries answer different spatial questions.

4. Equal contact count does not mean equal density, coverage, or anatomical access.

5. SEEG can provide deep, sulcal, mesial, and bilateral access, but its 3D sampling remains sparse.

6. Subdural grids can provide dense contiguous surface coverage, but they do not sample the whole underlying brain.

7. A depth contact is not automatically located in deep gray matter; contacts along one shaft can cross several tissue compartments.

8. iEEG is still a voltage-difference measurement: V_i = φ_i - φ_ref.

9. Reference and montage can change amplitude, polarity, and spatial interpretation.

10. Intracranial contacts record population field potentials, not single neurons.

11. There is no universal fixed recording radius for an iEEG contact.

12. ECoG can be more spatially specific than scalp EEG while still being affected by volume conduction.

13. Broadband high-frequency activity is a useful population feature but is not identical to spike count.

14. Human iEEG electrode placement is clinically driven and therefore strongly biased spatially.

15. The earliest recorded seizure contact is the earliest among sampled contacts, not guaranteed absolute biological origin.

16. Anatomical localization and coverage maps are essential to interpretation.

17. Both ECoG and SEEG are invasive and carry different procedural tradeoffs.

18. Intracranial EEG is closer to neural sources than scalp EEG, but it remains a selective field measurement rather than complete access to the brain.
```

---

# References used in this lesson

- **NNE-REF-041** — György Buzsáki, Costas A. Anastassiou, and Christof Koch, *The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes*, Nature Reviews Neuroscience 13, 407–420 (2012), DOI 10.1038/nrn3241. Reused for extracellular-field generation, volume conduction, geometry, and the relationship among spikes, LFP, ECoG, and EEG.
- **NNE-REF-077** — Josef Parvizi and Sabine Kastner, *Promises and limitations of human intracranial electroencephalography*, Nature Neuroscience 21, 474–483 (2018), DOI 10.1038/s41593-018-0108-2, PMID 29507407, PMCID PMC6476542. Review used for the ECoG/SEEG distinction, millisecond temporal access, clinically constrained electrode placement, spatial sampling, and limitations of human iEEG research.
- **NNE-REF-078** — Prasanna Jayakar et al., *Diagnostic utility of invasive EEG for epilepsy surgery: Indications, modalities, and techniques*, Epilepsia 57(11), 1735–1747 (2016), DOI 10.1111/epi.13515, PMID 27677490. ILAE Neurophysiology Task Force special report used for clinical indications, modalities, limitations, and interpretation of invasive EEG.
- **NNE-REF-079** — Shasha Wu et al., *Depth versus surface: A critical review of subdural and depth electrodes in intracranial electroencephalographic studies*, Epilepsia 65(7), 1868–1878 (2024), DOI 10.1111/epi.18002, PMID 38722693, CC BY-NC 4.0. Critical review used for two-dimensional surface versus three-dimensional depth sampling, sulcal/deep access, and modality tradeoffs.
- **NNE-REF-080** — Lara Jehi et al., *Comparative Effectiveness of Stereotactic Electroencephalography Versus Subdural Grids in Epilepsy Surgery*, Annals of Neurology 90(6), 927–939 (2021), DOI 10.1002/ana.26238, PMID 34590337, PMCID PMC9438788. Comparative primary study used for cautious discussion of differences in procedural complications and outcomes between SEEG and subdural-grid cohorts.
- **NNE-REF-081** — Krista M. Grande, Sarah K. Z. Ihnen, and Ravindra Arya, *Electrical Stimulation Mapping of Brain Function: A Comparison of Subdural Electrodes and Stereo-EEG*, Frontiers in Human Neuroscience 14:611291 (2020), DOI 10.3389/fnhum.2020.611291, CC BY 4.0. Review used for surface-versus-depth geometry, contact forms, functional-mapping context, and the verified Figure 2 static visual anchor embedded in this lesson.
- **NNE-REF-082** — Birgit Frauscher et al., *Atlas of the normal intracranial electroencephalogram: neurophysiological awake activity in different cortical areas*, Brain 141(4), 1130–1144 (2018), DOI 10.1093/brain/awy035, PMID 29506200. Multicenter primary study used to support anatomical variation in physiological intracranial EEG and the importance of rigorous contact localization and selection.
- **NNE-REF-083** — Marcin Leszczyński et al., *Dissociation of broadband high-frequency activity and neuronal firing in the neocortex*, Science Advances 6(33), eabb0977 (2020), DOI 10.1126/sciadv.abb0977, PMID 32851172, PMCID PMC7423365, CC BY-NC 4.0. Primary study used to prevent the oversimplification that broadband high-frequency activity is identical to local multi-unit firing.
