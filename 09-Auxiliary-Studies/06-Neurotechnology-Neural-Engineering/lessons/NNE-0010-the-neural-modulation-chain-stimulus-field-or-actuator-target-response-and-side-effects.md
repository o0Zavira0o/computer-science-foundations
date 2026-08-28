---
id: NNE-0010
title: "The neural modulation chain: stimulus, field or actuator, target, response, and side effects"
track: neurotechnology-neural-engineering
level: L0
status: complete
curriculum_node: NNE-N-0010
concepts_introduced: ["NNE-C-0013"]
concepts_deepened: ["NNE-C-0012", "NNE-C-0010", "NNE-C-0008", "NNE-C-0009"]
concepts_used: ["NNE-C-0001", "NNE-C-0002", "NNE-C-0003", "NNE-C-0004", "NNE-C-0005", "NNE-C-0006"]
examples_added: ["NNE-EX-046", "NNE-EX-047", "NNE-EX-048", "NNE-EX-049"]
references_used: ["NNE-REF-045", "NNE-REF-046", "NNE-REF-047", "NNE-REF-048", "NNE-REF-049"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# The neural modulation chain: stimulus, field or actuator, target, response, and side effects

## If you landed here directly

This lesson assumes `NNE-0009 — The neural measurement chain: source, tissue, sensor, electronics, data, and inference`.

You should already understand that a neural measurement is not the biological event itself.

A recording chain looks like:

```text
biology
→ tissue / medium
→ sensor
→ electronics
→ data
→ inference
```

Now we turn the engineering direction around.

Instead of asking:

> how did a biological event become a measurement?

we ask:

> how does an engineered command become a biological perturbation, and how does that perturbation become a useful effect or an unwanted side effect?

The central model of this lesson is:

```text
engineering goal
→ command and stimulation parameters
→ actuator / interface
→ physical stimulus or field
→ propagation through tissue
→ biological target
→ immediate neural response
→ circuit / system response
→ functional effect

                         ↘ off-target response
                         ↘ side effects
                         ↘ safety constraints
```

By the end, you should be able to:

- distinguish a device command from the physical stimulus actually delivered to tissue;
- distinguish the actuator from the field or energy distribution it produces;
- explain why tissue geometry and material properties affect the delivered stimulus;
- distinguish an intended anatomical target from the full set of neural elements that respond;
- explain why stimulation does not simply mean "make neurons fire more";
- separate immediate cellular or axonal responses from network and behavioral effects;
- distinguish desired effects from off-target and side effects;
- explain why dose, selectivity, and safety are end-to-end properties;
- trace electrical, magnetic, acoustic, and sensory-neuroprosthetic examples through the same chain;
- prepare for open-loop and closed-loop neural systems.

---

# The problem worth understanding

Suppose a stimulator is set to:

```text
amplitude = 2 mA
pulse width = 60 microseconds
frequency = 130 Hz
```

What exactly has been delivered to the nervous system?

A careless answer is:

> 2 mA of stimulation.

That answer mixes several different levels.

The device has generated a commanded electrical waveform.

But the biological effect depends on a longer chain:

```text
programmed settings
→ current or voltage waveform
→ electrode-tissue interface
→ electric potential and field in tissue
→ membrane polarization of nearby neural elements
→ changes in action-potential timing or probability
→ propagation through connected pathways
→ network response
→ functional effect
```

The number displayed on the device is therefore not identical to the neural response.

This distinction is the foundation of neuromodulation engineering.

---

# Part I — Recording and modulation are related but not symmetric

## Recording asks what happened

A measurement system begins with biology and ends with data or inference:

```text
biological event
→ physical consequence
→ sensor
→ electronics
→ digital data
→ estimate
```

The central uncertainty is:

> what biological process produced this observation?

---

## Modulation asks what we caused

A modulation system begins with an engineering decision and sends energy toward biological tissue:

```text
desired effect
→ command
→ actuator
→ physical stimulus
→ tissue
→ neural response
→ observed outcome
```

The central uncertainty is:

> what biological changes did this intervention actually produce?

---

## Why "recording in reverse" is not enough

It is tempting to imagine:

```text
recording:
neuron → electrode

stimulation:
electrode → neuron
```

That picture is too simple.

In recording, the electrode senses a physical consequence of biological activity.

In stimulation, the electrode or other actuator creates a physical perturbation that may affect:

- axons;
- cell bodies;
- dendrites;
- synaptic terminals;
- glia;
- passing fibers;
- nearby or downstream circuits.

The sensitive biological elements are not necessarily the same elements that would dominate a recording at the same location.

So the two directions are related, but they are not mirror images.

---

# Part II — Start with the engineering goal

## A modulation system should begin with an intended effect

Possible goals include:

- restore hearing;
- reduce pathological movement;
- interrupt a seizure;
- evoke a sensation;
- activate a muscle through a peripheral nerve;
- alter cortical excitability;
- investigate causal involvement of a neural pathway.

The correct first question is therefore not:

> what stimulation amplitude should I use?

It is:

> what biological or functional effect is the system trying to produce?

---

## Goal, target, and actuator are different

Consider deep brain stimulation.

One might say:

```text
goal:
reduce a movement-disorder symptom

anatomical target:
a selected deep brain region

actuator:
implanted electrode contacts
```

Those are three different objects.

The target is not the device.

The device is not the therapeutic outcome.

Keeping these layers separate prevents many reasoning errors.

---

# Part III — Command and waveform

## The command is the device-level instruction

A stimulation command may specify quantities such as:

- amplitude;
- pulse width;
- pulse frequency;
- waveform shape;
- polarity;
- electrode contact configuration;
- burst duration;
- duty cycle;
- spatial pattern;
- timing relative to another event.

For a simplified current-controlled pulse, one might describe:

```text
current amplitude
pulse duration
inter-pulse interval
```

These parameters specify what the stimulator is instructed to produce.

They do not yet specify the complete biological dose.

---

## A waveform has time structure

Two stimuli can deliver similar total charge while having different timing.

For example:

```text
one long pulse
```

and:

```text
several shorter pulses
```

can interact differently with excitable tissue.

Neural membranes and axons are dynamic systems.

Timing matters because ion channels and membrane polarization evolve over time.

---

## Charge per phase

For an ideal rectangular current pulse:

$$ Q = I T. $$

Here:

- $Q$ is charge delivered during the phase;
- $I$ is current amplitude;
- $T$ is phase duration.

This equation is useful for bookkeeping.

But equal $Q$ does not imply equal neural effect.

Waveform shape, geometry, electrode properties, repetition rate, and neural state still matter.

---

## Biphasic stimulation

Many implanted electrical stimulators use charge-balanced or approximately charge-balanced biphasic waveforms.

Conceptually:

```text
phase 1
→ phase 2 of opposite polarity
```

The engineering reason is not that the second phase "undoes" the neural response.

Its major role is to manage electrode polarization and charge transfer at the interface.

Electrical safety requires reasoning about the electrode-tissue interface, not only the target neurons.

---

# Part IV — The actuator is not the field

## Actuator

An **actuator** is the engineered component that converts device power and commands into a physical perturbation.

Examples:

- an implanted electrode;
- a peripheral nerve cuff;
- a TMS coil;
- an ultrasound transducer;
- an optical emitter in an experimental preparation;
- a cochlear-implant electrode array.

The actuator is a physical object.

The stimulus experienced by tissue is a field, force, current distribution, acoustic pressure pattern, optical intensity distribution, or another physical quantity produced by that object.

---

## Electrical stimulation

An electrode can drive current into conductive tissue.

The tissue then develops a spatial voltage distribution and electric field.

Conceptually:

```text
stimulator
→ electrode
→ current flow through interface
→ electric potential in tissue
→ electric field
→ neural membrane polarization
```

The electrode contact itself is therefore not the "volume of stimulation."

---

## Magnetic stimulation

In TMS:

```text
brief current in coil
→ time-varying magnetic field
→ induced electric field in tissue
→ neural response
```

The coil current is not directly a neuronal current.

The magnetic field is an intermediate physical stage, and the induced electric field is the quantity more directly coupled to excitable neural tissue.

This is a clean example of why actuator and biological stimulus must be separated.

---

## Acoustic stimulation

In focused ultrasound neuromodulation:

```text
electrical drive
→ ultrasound transducer
→ acoustic field
→ interaction with tissue
→ neural effect
```

Again:

```text
transducer setting
≠ acoustic field everywhere in the brain
≠ neural response
```

The physical mechanism of low-intensity ultrasound neuromodulation is still an active research topic.

A responsible model therefore separates what is measured or controlled from what is mechanistically inferred.

---

# Part V — Tissue is part of the actuator-to-target path

## Tissue reshapes what is delivered

Biological tissue is not an empty space between actuator and neuron.

For electrical stimulation, relevant properties include:

- conductivity;
- geometry;
- anisotropy;
- electrode placement;
- encapsulation or scar tissue in chronic implants;
- boundaries between tissues.

For magnetic stimulation, geometry and conductivity influence the induced electric field.

For ultrasound, skull and tissue affect transmission, focusing, reflection, and absorption.

---

## Same device command can produce different tissue fields

Imagine two otherwise identical electrodes:

```text
electrode A:
close to a large myelinated axon

electrode B:
farther from that axon and oriented differently
```

Both receive the same command.

The neural response need not be the same.

Therefore:

```text
same programmed amplitude
≠ same spatial field
≠ same neural recruitment
```

---

## Geometry is part of dose

In ordinary language, "dose" may sound like one scalar number.

In neural stimulation, the biologically relevant dose can have:

- spatial structure;
- temporal structure;
- orientation;
- repetition;
- history dependence.

A single amplitude cannot summarize all of this.

---

# Part VI — What exactly is the target?

## Anatomical target

An anatomical target is a named physical region or pathway selected for intervention.

Examples:

- a deep brain nucleus;
- motor cortex;
- auditory nerve fibers;
- a peripheral nerve;
- a spinal cord region.

This is useful for surgical and experimental planning.

But anatomy alone does not tell us which neural elements are recruited.

---

## Functional target

Sometimes the intended target is better described functionally:

```text
pathological beta-band circuit activity
```

or:

```text
auditory nerve patterns that can carry speech information
```

The functional target can extend beyond one anatomical location.

---

## Biophysical target

The elements directly sensitive to the applied field may include:

- axonal segments;
- axon bends or branch points;
- cell membranes;
- synaptic terminals;
- populations with particular orientations.

The exact sensitive elements depend on the modality.

---

## Target is not the same as response volume

A clinical or experimental protocol may name one target.

But the physical field can extend beyond it.

Connected pathways can carry the effect farther.

So:

```text
named target
≠ directly affected elements
≠ downstream affected network
```

These sets can overlap without being identical.

---

# Part VII — From field to neural response

## Excitable membrane responds to perturbation

Neurons maintain voltage differences across their membranes.

External electric fields can alter membrane polarization.

If the perturbation is sufficient at sensitive neural elements, it can change action-potential initiation or propagation.

But the result depends on:

- field strength;
- spatial gradient;
- fiber orientation;
- membrane state;
- axon diameter and myelination;
- pulse duration;
- repetition;
- recent activity.

---

## "Stimulation" does not mean "excitation everywhere"

The everyday word *stimulate* can suggest "increase activity."

That is not a safe engineering interpretation.

A neural stimulation protocol can produce:

- action-potential initiation in some axons;
- suppression of some local firing patterns;
- altered timing;
- desynchronization;
- entrainment;
- synaptic effects;
- downstream inhibition through inhibitory circuitry;
- mixed excitation and inhibition across a network.

The system-level outcome depends on the circuit.

---

## Local cell-body activity is not the whole output

A particularly important lesson from DBS is that somatic firing near the electrode does not completely describe what the stimulated network is doing.

Axons can propagate stimulation-induced activity to distant regions.

Local inhibition and downstream activation can coexist.

Therefore:

```text
local firing rate
≠ complete stimulated-system state
```

This is the modulation version of a lesson you already learned in measurement:

```text
one observed variable
≠ complete biological truth
```

---

# Part VIII — From local response to network response

## Neural systems are connected

`NNE-0007` established:

```text
neuron
→ population
→ circuit
→ system
→ behavior
```

Neuromodulation enters somewhere inside that hierarchy.

The perturbation then propagates through existing connectivity and dynamics.

---

## Immediate effect versus downstream effect

Suppose electrical stimulation triggers spikes in a set of axons.

That is an immediate response.

Those spikes may then:

- release neurotransmitter at distant terminals;
- recruit excitatory pathways;
- recruit inhibitory pathways;
- alter oscillatory synchrony;
- influence motor output;
- change sensory perception.

The final effect can therefore be many synapses away from the actuator.

---

## Network state matters

The same perturbation can produce different outcomes when the network state differs.

Examples of state variables include:

- sleep versus wake;
- ongoing oscillatory phase;
- recent stimulation history;
- movement versus rest;
- medication state;
- attention;
- adaptation.

This is one reason a fixed stimulus does not guarantee a fixed response.

---

# Part IX — Desired effect, off-target effect, and side effect

## Desired effect

A desired effect is the outcome the intervention is intended to produce.

Examples:

- reduced tremor;
- useful auditory perception;
- muscle activation;
- interruption of pathological activity;
- a reproducible experimental perturbation.

---

## Off-target response

An off-target response is a biological effect outside the intended target.

It may occur because:

- the physical field spreads;
- adjacent fibers are recruited;
- connected pathways propagate activity;
- current returns through an unintended path;
- the actuator is imperfectly positioned.

An off-target response is not automatically harmful.

It is simply outside the intended target.

---

## Side effect

A **side effect** is an unintended functional or biological consequence relevant to the intervention.

A side effect may arise from an off-target response.

But it may also arise from changing the intended target in an unwanted way.

Therefore:

```text
off-target response
and
side effect
```

are related but not identical concepts.

---

## Therapeutic window

A useful engineering idea is:

```text
too weak
→ insufficient desired effect

useful range
→ desired effect with acceptable side effects

too strong or poorly shaped
→ unwanted recruitment, discomfort, tissue risk, or other adverse effect
```

The useful range depends on the complete system.

---

# Part X — Selectivity

## Spatial selectivity

Spatial selectivity asks:

> how narrowly can the intervention affect the intended region or pathways?

It depends on:

- actuator geometry;
- field spread;
- tissue properties;
- target depth;
- current return path;
- focusing method.

---

## Neural selectivity

Even inside one spatial region, different neural elements can have different thresholds.

Electrical stimulation may preferentially recruit some axons before nearby cell bodies.

Fiber diameter and orientation matter.

So spatial precision does not guarantee cell-type precision.

---

## Temporal selectivity

Timing can also create selectivity.

A system can choose:

- when to stimulate;
- how pulses are grouped;
- phase relative to neural activity;
- whether stimulation is continuous or intermittent.

This prepares an important question for the next lesson:

> what if measured neural activity determines when or how the next stimulus is delivered?

---

# Part XI — Safety is part of the chain

## Safety cannot be added at the end

A modulation system must respect constraints at several layers.

Possible limits include:

```text
device electrical limits
electrode polarization limits
charge-injection limits
tissue heating limits
mechanical limits
acoustic exposure limits
unintended neural recruitment
behavioral or clinical adverse effects
```

Different modalities have different safety mechanisms.

---

## Electrical interface safety

An electrode transfers charge through an electrochemical interface.

Excessive or poorly controlled stimulation can drive undesirable electrochemical reactions or tissue damage.

Therefore electrical stimulation safety involves quantities such as:

- current;
- charge per phase;
- charge density;
- waveform balance;
- electrode material;
- electrode area;
- pulse repetition;
- chronic interface condition.

No single scalar captures every relevant limit.

---

## Safety constraint is not biological proof

If a waveform is inside an engineering safety envelope, that does not prove it produces the intended biological effect.

Likewise, observing a desired neural response does not prove the interface is safe long term.

Efficacy and safety require separate evidence.

---

# Part XII — Example NNE-EX-046: trace DBS from command to outcome

Suppose a clinician programs an implanted DBS system.

A complete chain is:

```text
therapeutic goal
→ programmed amplitude / pulse width / frequency
→ implantable pulse generator
→ selected electrode contacts
→ electrode-tissue charge transfer
→ electric field in surrounding tissue
→ recruitment of susceptible neural elements
→ local and axonal responses
→ changes across connected networks
→ clinical effect
```

Now add the parallel unintended path:

```text
field spread or pathway recruitment
→ unintended neural response
→ side effect
```

The important conclusion is not:

> DBS excites the target.

The stronger conclusion is:

> DBS applies an electrical perturbation whose effects can include local and distributed neural responses, and the clinically useful result depends on how those responses interact with the pathological network.

---

# Part XIII — Example NNE-EX-047: TMS separates actuator from field

Consider one TMS pulse.

Device-level description:

```text
capacitor discharge
→ high current in stimulation coil
```

Physical-field description:

```text
changing coil current
→ changing magnetic field
→ induced electric field in conductive tissue
```

Biological description:

```text
induced electric field
→ membrane polarization of susceptible cortical elements
→ altered neural activity
```

Measurement description might then include:

```text
neural response
→ motor-evoked potential measured in muscle
```

Notice how many layers exist between:

```text
coil current
```

and:

```text
measured muscle response
```

The motor-evoked potential is not the magnetic field.

It is a downstream measurement of a neural and neuromuscular response.

---

# Part XIV — Reuse example: cochlear implant as a modulation chain

Earlier lessons used the cochlear implant to show that a sensory neuroprosthesis does not simply amplify sound.

Reuse that example with a new purpose.

A simplified chain is:

```text
sound
→ microphone
→ signal processing
→ encoded stimulation command
→ implanted electrode array
→ electric field in cochlear tissue
→ auditory-nerve recruitment
→ central auditory processing
→ perception
```

The implant does not write "sound" directly into the brain.

It creates patterned electrical stimulation that the surviving auditory pathway and brain must interpret.

This distinction is essential:

```text
encoded command
≠ neural code produced by biology
≠ final percept
```

---

# Part XV — Example NNE-EX-048: same amplitude, different recruitment

Imagine two electrode contacts programmed with the same current amplitude.

Contact A lies near a bundle of myelinated fibers.

Contact B lies farther away and with different local geometry.

Even if:

```text
command A = command B
```

we should not assume:

```text
field A = field B
```

or:

```text
recruited neural elements A = recruited neural elements B
```

The example teaches a general rule:

> a device parameter is not a universal biological dose.

---

# Part XVI — Example NNE-EX-049: focused ultrasound and mechanism uncertainty

Suppose an ultrasound neuromodulation experiment reports:

```text
acoustic frequency
pulse repetition frequency
duty cycle
estimated intensity
target coordinates
```

A careful chain is:

```text
electrical drive
→ transducer
→ acoustic field
→ skull and tissue transmission
→ local mechanical / biophysical interaction
→ neural response
→ measured physiological effect
```

The chain contains stages that may be modeled with different degrees of confidence.

If the experiment measures an EEG or motor response after sonication, that response is evidence of an effect.

It is not, by itself, proof of one specific microscopic mechanism.

This is a reusable scientific discipline:

```text
effect observed
≠ mechanism uniquely identified
```

---

# Part XVII — Modality comparison

| Modality | Actuator | Main physical intermediary | Example target | Important caution |
|---|---|---|---|---|
| implanted electrical stimulation | electrode contact | electric potential / field and current flow | deep brain or peripheral nerve | contact location is not identical to recruited volume |
| TMS | coil | magnetic field then induced electric field | cortex | coil output is not neural dose |
| focused ultrasound | transducer | acoustic field | superficial or deep neural tissue | biological mechanism depends on regime and remains an active research topic |
| cochlear implant | intracochlear electrode array | electric field / current distribution | auditory nerve population | electrode command is not the final percept |

The common architecture matters more than the modality-specific hardware:

```text
command
→ actuator
→ physical field
→ tissue
→ neural response
→ functional effect
```

---

# Part XVIII — Failure modes

## Failure mode 1: equating programmed amplitude with biological effect

Incorrect:

> twice the amplitude means twice the therapeutic effect.

Why it fails:

- recruitment can be nonlinear;
- thresholds exist;
- geometry matters;
- different neural elements have different sensitivity;
- side effects may appear before the desired effect scales proportionally.

---

## Failure mode 2: equating actuator location with stimulated tissue

Incorrect:

> the electrode is in region X, so only region X is affected.

Why it fails:

- fields spread;
- passing fibers can be recruited;
- connected pathways carry effects away from the site.

---

## Failure mode 3: assuming stimulation always increases firing

Incorrect:

> stimulation means excitation.

Why it fails:

- local and downstream effects can differ;
- inhibitory circuits can be recruited;
- timing and synchrony can change without a simple firing-rate increase.

---

## Failure mode 4: treating a measured response as the complete biological effect

Incorrect:

> the evoked potential increased, therefore the entire target response increased.

Why it fails:

`NNE-0009` already showed that measurements are partial and transformed observations.

The modulation chain can create a complex biological response that a single sensor only samples incompletely.

---

## Failure mode 5: confusing target with mechanism

Incorrect:

> because stimulation of region X improves symptom Y, neurons in region X must be the sole causal mechanism.

Why it fails:

- fibers of passage may be involved;
- downstream networks may contribute;
- the intervention can perturb multiple biological elements.

---

## Failure mode 6: assuming no immediate side effect means long-term safety

Acute tolerance does not establish chronic safety.

Chronic interfaces can change because of:

- tissue response;
- electrode degradation;
- encapsulation;
- adaptation;
- long-term network plasticity.

---

# Part XIX — Active work

## Exercise 1 — identify the layers

For each item, classify it as:

```text
goal
command
actuator
physical field
biological target
neural response
functional outcome
measurement
```

Items:

1. TMS coil current.
2. Induced cortical electric field.
3. Motor-evoked potential recorded from a hand muscle.
4. Reduction in tremor.
5. DBS electrode contact.
6. Auditory-nerve spikes after cochlear-implant stimulation.
7. Programmed pulse width.
8. Intended subthalamic target.

---

## Exercise 2 — command is not dose

Two patients receive the same programmed DBS amplitude.

Give at least four reasons why the neural recruitment may differ.

---

## Exercise 3 — trace a peripheral nerve stimulator

Build a chain with at least seven stages for:

> an implanted cuff electrode intended to activate a muscle through a peripheral motor nerve.

Mark:

- actuator;
- physical intermediary;
- direct neural target;
- downstream biological response;
- functional output.

---

## Exercise 4 — stimulation versus excitation

Give three different ways a stimulation protocol could alter a neural system without producing a simple uniform increase in firing rate.

---

## Exercise 5 — target versus side effect

A stimulation protocol improves the desired motor output but also produces tingling.

Propose two distinct chain locations where the unintended sensation might arise.

---

## Exercise 6 — TMS reasoning

Explain why the statement:

> the coil delivers current into cortex

is physically misleading.

Replace it with a more accurate three-stage description.

---

## Exercise 7 — ultrasound evidence

An experiment finds a behavioral change after focused ultrasound.

What can be concluded directly?

What additional evidence would be needed before claiming one unique microscopic mechanism?

---

## Exercise 8 — build an end-to-end neuromodulation specification

Choose one modality.

List:

- intended effect;
- command variables;
- actuator;
- relevant physical field;
- target;
- expected immediate response;
- downstream response;
- measurement of efficacy;
- one side effect;
- one safety constraint.

---

# Retrieval check

Without looking back:

1. What is the central neural modulation chain?
2. Why is modulation not simply recording run backward?
3. What is an actuator?
4. Why is an actuator not the same as the physical field?
5. Give three examples of actuators.
6. What is a stimulation command?
7. Why does the device setting not fully specify biological dose?
8. Why does waveform timing matter?
9. For a rectangular current pulse, what does $Q=IT$ describe?
10. Why does equal charge not guarantee equal neural response?
11. What does tissue do to an applied physical field?
12. Why does geometry matter?
13. What is an anatomical target?
14. What is a functional target?
15. What is a biophysical target?
16. Why is the named target not identical to the full response volume?
17. Why can axons be important in electrical stimulation?
18. Why does "stimulation" not mean uniform excitation?
19. How can local inhibition coexist with downstream activation?
20. Why does network state matter?
21. What is an off-target response?
22. What is a side effect?
23. Why are off-target response and side effect not identical?
24. What is a therapeutic window?
25. What is spatial selectivity?
26. Why does spatial selectivity not guarantee cell-type selectivity?
27. What is temporal selectivity?
28. Why is safety an end-to-end property?
29. Why is electrical charge balance relevant to electrode interfaces?
30. Why does safe operation not prove efficacy?
31. Trace the TMS chain from coil current to neural response.
32. Trace the cochlear-implant chain from sound to perception.
33. Why is focused ultrasound a useful example of mechanism uncertainty?
34. Why can two equal device commands produce different responses?
35. Why is a measured evoked response not the complete biological response?
36. Why can downstream networks matter in DBS?
37. What distinction from `NNE-0009` remains important during modulation?
38. What new question does this lesson create for closed-loop systems?

---

# Connection backward: NNE-0009

`NNE-0009` taught:

```text
biology
→ tissue
→ sensor
→ electronics
→ data
→ inference
```

This lesson adds the engineering direction:

```text
command
→ actuator
→ field
→ tissue
→ neural response
→ outcome
```

The two chains share an important discipline:

> every arrow is a transformation, not an identity.

In measurement:

```text
recorded value
≠ biological truth
```

In modulation:

```text
device setting
≠ biological effect
```

---

# Connection backward: NNE-0007 and NNE-0005

`NNE-0007` moved from single neurons to populations, circuits, systems, and behavior.

That hierarchy explains why a local perturbation can produce a distributed outcome.

`NNE-0005` introduced action potentials, thresholds, refractory periods, and propagation.

Those concepts explain why neural elements respond dynamically rather than as passive wires.

---

# Connection to Linear Algebra

Many modulation systems use spatial models.

A simplified linear field model may be written:

$$ \mathbf{e}=A\mathbf{u}. $$

Here:

- $\mathbf{u}$ is a vector of actuator commands;
- $A$ is a model mapping commands to field samples;
- $\mathbf{e}$ is the resulting modeled field.

`LA-0010` explains the matrix-vector structure of such a model.

This equation is only a simplified model.

It does not mean neural response is universally linear in stimulation amplitude.

The biological transformation after the field can be nonlinear and state dependent.

---

# Connection forward: NNE-N-0011

The next canonical lesson is:

`NNE-N-0011 — Open-loop and closed-loop neural systems`.

We now have two chains:

```text
measurement chain:
biology → sensor → data → inference

modulation chain:
command → actuator → field → biology
```

Place a decision process between them:

```text
measurement
→ estimate
→ decision
→ stimulation command
→ modulation
```

Now ask:

> does the next stimulation command depend on what the system just measured?

If no, the system is open-loop with respect to that measured variable.

If yes, a feedback path exists.

That is the next lesson.

---

# What this unlocks

You should now be able to examine a neuromodulation system and ask:

```text
What is the actual engineering goal?
What is commanded?
What physical object is the actuator?
What physical field reaches tissue?
How does tissue reshape that field?
What biological elements are intended targets?
What other elements may respond?
What is the immediate neural response?
How does the response propagate through circuits?
What counts as the desired effect?
What counts as an off-target response?
What side effects are plausible?
How is efficacy measured?
What safety constraints apply?
Which claims are measured, modeled, or inferred?
```

That is the foundation for reasoning about neural stimulation as an engineered biological intervention rather than as a single device setting.

---

# References

- **NNE-REF-045** — Stuart F. Cogan, “Neural stimulation and recording electrodes,” *Annual Review of Biomedical Engineering* 10, 275–309 (2008). DOI: `10.1146/annurev.bioeng.10.061807.160518`.
- **NNE-REF-046** — Mark Hallett, “Transcranial magnetic stimulation: a primer,” *Neuron* 55(2), 187–199 (2007). DOI: `10.1016/j.neuron.2007.06.026`.
- **NNE-REF-047** — Todd M. Herrington, Jennifer J. Cheng, and Emad N. Eskandar, “Mechanisms of deep brain stimulation,” *Journal of Neurophysiology* 115(1), 19–38 (2016). DOI: `10.1152/jn.00281.2015`.
- **NNE-REF-048** — Lazzaro di Biase, Emma Falato, and Vincenzo Di Lazzaro, “Transcranial Focused Ultrasound (tFUS) and Transcranial Unfocused Ultrasound (tUS) Neuromodulation: From Theoretical Principles to Stimulation Practices,” *Frontiers in Neurology* 10, 549 (2019). DOI: `10.3389/fneur.2019.00549`.
- **NNE-REF-049** — Nicholas L. Deep, Eric M. Dowling, Daniel Jethanamest, and Matthew L. Carlson, “Cochlear Implantation: An Overview,” *Journal of Neurological Surgery Part B: Skull Base* 80(2), 169–177 (2019). DOI: `10.1055/s-0038-1669411`.
