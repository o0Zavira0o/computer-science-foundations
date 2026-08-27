---
id: NNE-0005
title: "Action potentials, thresholds, refractory periods, and propagation"
track: neurotechnology-neural-engineering
level: L0
status: complete
curriculum_node: NNE-N-0005
concepts_introduced: ["NNE-C-0008"]
concepts_deepened: ["NNE-C-0007", "NNE-C-0006"]
concepts_used: ["NNE-C-0005", "NNE-C-0002", "NNE-C-0004"]
examples_added: ["NNE-EX-021", "NNE-EX-022", "NNE-EX-023", "NNE-EX-024", "NNE-EX-025"]
references_used: ["NNE-REF-025", "NNE-REF-026", "NNE-REF-027", "NNE-REF-028"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Action potentials, thresholds, refractory periods, and propagation

## If you landed here directly

This lesson assumes the membrane-potential foundations from `NNE-0004`.

You should already know that:

- neurons maintain ion concentration gradients;
- membrane voltage is a potential difference across the membrane;
- each ion has an equilibrium potential;
- ionic current depends on both driving force and available conductance;
- resting membrane potential is a metabolically maintained steady state;
- resting voltage is often strongly influenced by K+ permeability;
- Na+ usually has a strong inward electrochemical driving force at rest.

You do **not** need the Hodgkin-Huxley equations yet.

You do not need differential equations.

The goal is to build the correct mechanism before formal modeling.

By the end, you should be able to explain:

- why action potentials require voltage-dependent conductances;
- what threshold really means;
- why opening Na+ channels can create regenerative positive feedback;
- why Na+ channel inactivation and delayed K+ activation terminate the spike;
- what depolarization, repolarization, and afterhyperpolarization mean;
- what absolute and relative refractory periods are;
- why action potentials propagate instead of simply fading away;
- why propagation is normally directional;
- how myelination and axon diameter affect conduction;
- why "all-or-none" does not mean stimulus intensity is irrelevant;
- why extracellular spikes are consequences of propagating membrane currents rather than direct copies of intracellular voltage.

---

## The problem worth understanding

Passive voltage changes decay with distance.

If you depolarize one small region of a long axon and nothing regenerates the signal, the disturbance spreads only so far before becoming smaller.

But neurons can transmit signals over long distances.

How?

They do not send one passive voltage bump from one end to the other.

Instead, they repeatedly regenerate the electrical event along the axon.

A useful first model is:

```text
local depolarization
→ voltage-gated Na+ channels open
→ inward Na+ current
→ more depolarization
→ neighboring membrane reaches threshold
→ new local action potential
→ process repeats
```

The action potential is therefore not a traveling packet of sodium.

It is a **traveling regeneration of membrane state**.

---

## From rest to excitability

At rest, membrane conductance is relatively stable.

Now imagine a local depolarizing input.

The membrane voltage becomes less negative.

If the depolarization is small, the membrane may simply relax back toward rest.

If it is large enough, voltage-gated Na+ channels begin opening rapidly enough to create a self-reinforcing process.

That transition is what threshold is about.

---

## Voltage-gated channels

A **voltage-gated ion channel** changes its probability of being open as membrane voltage changes.

For the classic fast neuronal action potential, two conductance families are central:

- voltage-gated Na+ channels;
- voltage-gated K+ channels.

They do not respond with identical timing.

That timing difference creates the waveform.

A high-level sequence is:

```text
depolarization
→ fast Na+ activation
→ strong inward Na+ current
→ further depolarization
→ Na+ inactivation + delayed K+ activation
→ outward K+ current
→ repolarization
→ temporary afterhyperpolarization
→ recovery
```

---

## Threshold is a dynamical tipping point

Introductory diagrams often label one threshold voltage.

For example:

```text
rest ≈ -70 mV
threshold ≈ -55 mV
```

Those values can be pedagogically useful.

But threshold is not a universal fixed number for every neuron.

A more useful concept is:

> threshold is the membrane state at which regenerative inward current becomes strong enough to overcome opposing currents and drive a self-sustaining spike.

So threshold depends on:

- channel density;
- channel state;
- recent firing history;
- membrane location;
- temperature;
- cell type;
- ongoing synaptic input.

Think of threshold as a **dynamical condition**, not merely a painted line on a graph.

---

## Why Na+ activation creates positive feedback

At rest:

$$ V_m \ll E_{Na}. $$

Therefore Na+ has strong inward electrochemical driving force.

Now suppose depolarization opens some voltage-gated Na+ channels.

Then:

```text
more Na+ conductance
→ more inward Na+ current
→ V_m becomes more positive
→ more voltage-gated Na+ channels activate
→ still more inward current
```

This is positive feedback.

```mermaid
flowchart LR
    D["Depolarization"] --> N["More Na+ channels activate"]
    N --> I["More inward Na+ current"]
    I --> D
```

Without another mechanism, positive feedback would not stop appropriately.

The action potential needs termination mechanisms too.

---

## The rising phase

Once threshold is crossed, Na+ conductance rises rapidly.

Membrane voltage moves toward the Na+ equilibrium potential.

It normally does not reach `E_Na` exactly because:

- Na+ channels begin inactivating;
- K+ conductance rises;
- membrane capacitance and other conductances matter.

The rapid positive-going part of the spike is the **depolarizing upstroke**.

---

## Overshoot

During many neuronal action potentials, membrane voltage crosses 0 mV and becomes positive.

This is called the **overshoot**.

It does not mean the entire intracellular fluid becomes massively positive.

As before, membrane voltage arises from a tiny charge separation near the membrane.

The bulk solutions remain approximately electroneutral.

---

## Na+ channel inactivation is different from closing after rest

Voltage-gated Na+ channels are often described with at least two functional processes:

- activation;
- inactivation.

At rest, channels are generally available but not activated.

During depolarization:

1. activation occurs rapidly;
2. the channel opens;
3. after a brief delay, inactivation develops;
4. the channel becomes temporarily unavailable even if the membrane is still depolarized.

This distinction matters because an inactivated channel cannot simply reopen immediately.

Recovery requires repolarization and time.

That mechanism is central to the refractory period.

---

## Delayed K+ activation

Voltage-gated K+ conductance typically rises more slowly than fast Na+ conductance.

As K+ channels open, K+ usually has an outward electrochemical driving force during the positive phase of the action potential.

So:

```text
K+ conductance rises
→ outward positive current rises
→ membrane voltage moves back negative
```

This contributes strongly to repolarization.

The delay is crucial.

If K+ conductance rose with exactly the same rapid kinetics as Na+ conductance, the waveform would be very different.

---

## Repolarization

**Repolarization** is the return of membrane voltage toward its negative resting range after the spike peak.

Mechanistically it reflects a combination of:

- reduced inward Na+ current because Na+ channels inactivate;
- increased outward K+ current because K+ channels are activated.

So repolarization is not simply:

> the pump pushes sodium back out.

That is a common misconception.

The rapid downstroke occurs mostly because membrane conductances change.

The Na+/K+ pump maintains gradients over longer timescales.

---

## Afterhyperpolarization

K+ conductance may remain elevated briefly after the membrane has returned near rest.

As a result, `V_m` can move closer to `E_K` and become more negative than the usual resting value.

This is the **afterhyperpolarization**.

It contributes to temporary reduced excitability after a spike.

Not every neuron has the same afterhyperpolarization waveform.

Different K+ channels and other conductances shape it.

---

## Example NNE-EX-021 — trace one spike phase by phase

Start with:

```text
V_rest = negative
```

Then trace:

### Phase 1 — local depolarization

A stimulus makes the membrane less negative.

### Phase 2 — threshold crossing

Regenerative Na+ activation begins.

### Phase 3 — upstroke

Na+ conductance rises rapidly.

Inward current depolarizes the membrane.

### Phase 4 — peak transition

Na+ channels inactivate.

Delayed K+ conductance becomes large.

### Phase 5 — repolarization

Outward K+ current drives voltage negative.

### Phase 6 — afterhyperpolarization

K+ conductance remains temporarily elevated.

### Phase 7 — recovery

Voltage and channel availability return toward resting conditions.

The action potential is therefore a **sequence of conductance states**, not one instantaneous voltage jump.

---

## All-or-none: what it actually means

A classic action potential is described as **all-or-none**.

That means:

> once regenerative threshold is crossed in a given excitable membrane region, the spike develops as a stereotyped event rather than scaling continuously with stimulus amplitude.

A stronger suprathreshold stimulus does not usually produce a proportionally taller action potential in the same axon under fixed conditions.

But do not overgeneralize.

Stimulus intensity can still affect:

- whether threshold is reached;
- firing rate;
- number of spikes;
- timing;
- number of recruited axons in a nerve;
- which neurons are activated.

So:

```text
all-or-none single spike
≠
all-or-none nervous-system response
```

---

## Stronger stimulus can change firing frequency

If a sustained input becomes stronger, the neuron may fire action potentials more frequently.

The individual spike amplitude may remain approximately stereotyped while the **spike train** changes.

That gives one important coding dimension:

```text
input intensity
→ firing timing / firing rate
```

This is one reason neural information is often represented in spike timing and rate rather than spike height alone.

---

## Threshold is local

A neuron is spatially extended.

The action potential often initiates near the axon initial segment because that region has specialized channel density and excitability.

Threshold at that site does not imply every membrane patch simultaneously reaches the same state.

Propagation then recruits adjacent membrane.

---

## Graded potential versus action potential

A **graded potential** changes amplitude with input strength and generally decays with distance.

An action potential is regenerative.

Useful contrast:

```text
graded:
local
variable amplitude
passive decay important

action potential:
thresholded
regenerative
propagates over distance
```

This distinction becomes especially important in the next synapse lesson.

Synaptic potentials are usually graded.

Axonal action potentials are regenerative.

---

## Passive spread comes first

Action potential propagation still uses passive electrical spread.

When one axonal segment depolarizes, local current flows into neighboring regions.

That local current depolarizes adjacent membrane.

If it reaches threshold there:

```text
new voltage-gated Na+ channels activate
→ a new local spike is generated
```

So propagation requires both:

- passive local current spread;
- active regenerative membrane conductance.

---

## Regeneration prevents amplitude decay

Pure passive signals decay with distance.

Action potentials avoid progressive amplitude loss because each adjacent segment regenerates the event.

Think:

```text
not:
one spike travels unchanged like a rigid object

but:
segment 1 triggers segment 2
segment 2 triggers segment 3
segment 3 triggers segment 4
...
```

The waveform observed at different locations can therefore maintain similar amplitude.

---

## Example NNE-EX-022 — passive decay versus regenerative propagation

Imagine injecting a small subthreshold current into an axon.

At increasing distance:

```text
voltage change gets smaller
```

Now increase the local depolarization enough to trigger an action potential.

At the first region:

```text
threshold crossed
→ local spike
```

The local current from that spike reaches the next region.

There:

```text
threshold crossed again
→ new spike
```

So the system converts a decaying passive influence into a sequence of regenerated events.

That is the engineering reason action potentials can support long-distance signaling.

---

## Why propagation is normally directional

Local current from an action potential can spread both forward and backward.

So why does the spike normally travel toward the terminal rather than immediately re-exciting the region behind it?

Because the membrane just behind the advancing spike is refractory.

Its Na+ channels are:

- inactivated;
- not yet fully recovered.

And K+ conductance may still be elevated.

Therefore backward-going local current encounters less excitable membrane.

Directional propagation emerges from:

```text
regenerative current ahead
+
refractory membrane behind
```

---

## The absolute refractory period

During the **absolute refractory period**, another normal action potential cannot be initiated in that membrane region, regardless of ordinary stimulus strength.

The primary reason is Na+ channel inactivation.

Many channels are temporarily unavailable.

This period:

- limits maximal firing frequency;
- helps maintain directional propagation;
- prevents immediate spike re-triggering.

---

## The relative refractory period

After the absolute refractory period, some Na+ channels have recovered.

But the membrane may still be:

- hyperpolarized;
- experiencing elevated K+ conductance;
- not fully restored to baseline excitability.

A stronger-than-usual stimulus may be required.

This is the **relative refractory period**.

So:

```text
absolute refractory:
cannot normally fire another spike

relative refractory:
can fire, but threshold is effectively harder to reach
```

---

## Refractory period is a state, not a timer pasted onto the neuron

Introductory diagrams often show fixed time windows.

But the biological refractory state emerges from channel kinetics.

Different neurons can have different:

- Na+ channel recovery rates;
- K+ conductance kinetics;
- maximum firing frequencies.

So refractory duration is a property of membrane dynamics.

---

## Example NNE-EX-023 — two stimuli separated in time

Stimulus A triggers an action potential.

Now consider Stimulus B.

### B arrives immediately

Most fast Na+ channels are inactivated.

No second normal spike can occur.

This is absolute refractoriness.

### B arrives slightly later

Some Na+ channels have recovered.

But K+ conductance remains elevated and the membrane may be hyperpolarized.

A stronger stimulus may produce a spike.

This is relative refractoriness.

### B arrives much later

Channel states have substantially recovered.

The neuron is closer to its baseline excitability.

This example shows that neural response depends on **history**.

---

## Firing rate has a biological ceiling

Because membranes need time to recover, neurons cannot fire infinitely fast.

Refractory dynamics impose an upper limit.

Different neuron types have different practical firing capabilities because they express different channel types and densities.

This is one reason a neural model should not treat spike events as arbitrarily dense independent impulses.

---

## Axon diameter and conduction speed

Larger axons generally conduct action potentials faster.

Why?

A larger diameter reduces internal axial resistance to passive current spread.

So depolarizing current can influence downstream membrane more effectively.

This does not make an axon identical to a metal wire.

But the resistance analogy is useful within limits.

---

## Myelination changes passive spread

Myelin wraps axonal membrane between nodes.

It:

- reduces current leakage through internodal membrane;
- changes membrane capacitance;
- allows passive current to spread farther and faster between active regions.

Voltage-gated Na+ channels are concentrated at nodes of Ranvier.

So active regeneration occurs mainly at nodes.

---

## Saltatory conduction

In myelinated axons:

```text
node 1 spike
→ passive current spreads under myelin
→ node 2 reaches threshold
→ node 2 regenerates spike
→ process repeats
```

This is **saltatory conduction**.

The word suggests jumping.

But no action potential object literally teleports between nodes.

Passive current spreads through the internode.

The regenerative membrane event is renewed at the next node.

---

## Continuous conduction

In unmyelinated axons, active regeneration occurs along closely adjacent membrane regions.

This is often called **continuous conduction**.

Comparison:

```text
unmyelinated:
regeneration distributed along axon

myelinated:
regeneration concentrated at nodes
```

Myelination usually increases conduction velocity dramatically.

---

## Example NNE-EX-024 — why myelin speeds conduction

Compare two axons of similar functional purpose.

### Unmyelinated axon

Each neighboring membrane segment must:

- charge;
- reach threshold;
- open voltage-gated channels;
- regenerate the spike.

### Myelinated axon

Internodal membrane has reduced leak and different capacitance.

Local current spreads farther.

Regeneration occurs mainly at nodes.

Therefore fewer membrane regions need to undergo full spike-generation dynamics per unit length.

Result:

> conduction can be much faster.

This connects the glial biology of `NNE-0003` to information transmission.

---

## Myelin does not merely make the signal "stronger"

Myelin improves the efficiency and speed of propagation.

It does not create an indefinitely larger action-potential amplitude.

At each node, the spike is regenerated by local conductances.

The relevant effect is on passive spread and timing between regenerative sites.

---

## Nodes of Ranvier are active specializations

A node is not simply a gap where myelin is missing.

It is a specialized membrane region with high concentrations of voltage-gated channels and organized molecular structure.

The distribution of channels is part of the propagation design.

---

## Demyelination can disrupt propagation

If myelin is lost:

- current leakage increases;
- passive depolarization may not reach the next node effectively;
- conduction can slow;
- propagation can fail.

This is a systems lesson:

> tissue structure and membrane-channel distribution jointly determine signal transmission.

The lesson is not a clinical guide.

---

## Propagation velocity is not the same as firing rate

These are different quantities.

### Conduction velocity

How fast one action potential travels along the axon.

Often expressed in:

```text
meters per second
```

### Firing rate

How often action potentials occur.

Often expressed in:

```text
spikes per second
```

A neuron can have:

- fast conduction but low firing rate;
- slower conduction but relatively high firing rate.

Do not mix them.

---

## Spike amplitude is not propagation speed

A taller recorded extracellular spike does not automatically mean:

- the axon conducts faster;
- the neuron fires more strongly;
- the stimulus was larger.

Recorded amplitude depends heavily on:

- electrode distance;
- geometry;
- cell size;
- orientation;
- tissue conductivity;
- reference;
- filtering.

This becomes crucial in extracellular recording.

---

## Intracellular versus extracellular spike shape

An intracellular recording shows membrane voltage relative to extracellular reference.

An extracellular electrode measures local field changes caused by transmembrane currents.

Therefore extracellular spikes often:

- have much smaller amplitude;
- can be biphasic or triphasic;
- depend strongly on electrode position;
- do not look like the classic intracellular action-potential curve.

Same underlying neural event.

Different measurement geometry.

---

## Example NNE-EX-025 — one action potential, two electrodes

Imagine:

```text
electrode A:
inside axon

electrode B:
outside axon
```

### Electrode A

Measures a large transmembrane voltage change:

```text
rest
→ rapid depolarization
→ overshoot
→ repolarization
→ afterhyperpolarization
```

### Electrode B

Measures extracellular voltage caused by changing membrane currents nearby.

The waveform may be:

- much smaller;
- polarity dependent on geometry;
- multiphasic.

Therefore:

```text
extracellular spike
is not
a scaled copy of intracellular V_m
```

That distinction will matter later for spike detection and sorting.

---

## Stimulus artifact is not an action potential

During electrical stimulation, electrodes may record a large electrical artifact caused directly by the stimulus pulse.

That artifact can occur before or overlap with neural responses.

Do not automatically interpret every large transient as a propagated spike.

Neural engineering requires separating:

- applied stimulus;
- electrode polarization;
- amplifier recovery;
- biological response.

---

## Compound action potentials

A peripheral nerve contains many axons.

If many axons are activated, an extracellular nerve electrode may record a **compound action potential**.

That waveform is a sum of contributions from many fibers.

Fibers can differ in:

- diameter;
- myelination;
- conduction velocity;
- recruitment threshold.

So a compound waveform is not one giant single-neuron action potential.

---

## Recruitment during stimulation

Electrical stimulation of a nerve can recruit different axons at different stimulus levels.

Therefore increasing stimulus amplitude can increase the number and types of recruited fibers.

This is another reason:

```text
single-axon all-or-none
≠
whole-nerve all-or-none
```

The population response can grow even though each recruited axon's spike is regenerative.

---

## Threshold in stimulation is not one universal voltage

External stimulation changes electric fields around cells.

The resulting transmembrane polarization depends on:

- electrode geometry;
- axon orientation;
- position;
- tissue conductivity;
- pulse waveform;
- axon diameter;
- myelination;
- initial membrane state.

So neural-stimulation threshold is a system property, not simply:

> membrane threshold = -55 mV.

The intracellular threshold concept and engineering stimulation threshold are related but not identical.

---

## Threshold varies with channel history

Suppose a neuron has recently fired.

Even if its membrane voltage has returned close to rest, not all channels may have fully recovered.

Therefore the next spike threshold can differ from baseline.

This creates history dependence.

The same input at two different moments can produce different results.

---

## Adaptation and firing dynamics

Many neurons show changes in firing rate during sustained stimulation.

Action-potential generation can interact with:

- slow K+ conductances;
- Ca2+-dependent conductances;
- persistent Na+ currents;
- other channels.

The simple Na/K spike is a foundation.

Real neuronal excitability is richer.

Do not mistake the introductory action-potential model for a complete neuron model.

---

## The Hodgkin-Huxley lesson

Hodgkin and Huxley showed that action-potential waveforms can be reconstructed from time- and voltage-dependent Na+ and K+ conductances.

The deep lesson is not merely the specific equations.

It is:

> membrane voltage and channel state form a coupled dynamical system.

Conceptually:

```text
V_m changes
→ channel gates respond

channel gates respond
→ conductances change

conductances change
→ ionic currents change

ionic currents change
→ V_m changes
```

This feedback loop generates the spike.

---

## Voltage clamp as a reasoning tool

A voltage clamp experimentally holds membrane voltage at a commanded value while measuring the current required to do so.

This lets researchers separate:

```text
change voltage
from
observe ionic current
```

It was essential for identifying voltage-dependent conductances underlying action potentials.

At this stage, remember the measurement logic:

> control one electrical variable to reveal another.

Later instrumentation lessons will revisit feedback measurement.

---

## Current clamp is different

In current clamp, the experimenter injects current and observes membrane voltage.

So:

```text
voltage clamp:
control voltage, measure current

current clamp:
control/inject current, measure voltage response
```

Classic action-potential voltage traces are often understood in current-clamp terms.

These are experimental modes, not two different kinds of neurons.

---

## Threshold depends on rate of depolarization

Because channel activation and inactivation evolve over time, two stimuli reaching similar voltages with different time courses can have different effects.

A slow depolarization can partially inactivate channels before a regenerative spike begins.

Therefore:

> threshold can depend on trajectory, not only instantaneous voltage.

This is another reason to think dynamically.

---

## Action-potential width matters

Spikes can differ across neuron types in:

- duration;
- peak;
- afterhyperpolarization;
- channel composition.

Even within one neuron, waveform can vary with:

- temperature;
- recent activity;
- pharmacology;
- recording location.

"All-or-none" does not mean every neuron has the same spike.

It refers to regenerative behavior within a given excitable system.

---

## Axonal versus somatic spikes

Action potentials can be recorded at:

- soma;
- axon initial segment;
- axon;
- terminals.

Waveforms can differ across compartments.

Propagation is an active spatial process.

A neuron is not an isopotential point.

---

## Branch points create propagation challenges

Axons can branch.

At a branch point, current must depolarize additional membrane.

Normally axonal geometry and channel organization support reliable propagation.

But propagation is not guaranteed by abstract logic alone.

Biophysical conditions matter.

---

## Conduction delay matters for circuits

If an axon conducts over a long distance, arrival is delayed.

Conduction velocity therefore affects:

- timing between neurons;
- synchronization;
- reflex latency;
- sensorimotor control;
- closed-loop neural-interface timing.

Neural engineering cares not only whether a spike propagates, but **when it arrives**.

---

## Closed-loop systems care about latency

A closed-loop neurotechnology system may contain:

```text
neural event
→ propagation
→ electrode
→ amplifier
→ digitizer
→ algorithm
→ decision
→ stimulation
→ neural propagation
```

Axonal conduction is one component of total latency.

For some systems, millisecond-scale timing matters.

---

## Spike train versus single spike

One spike is an event.

A spike train is a sequence of events over time.

Important spike-train features include:

- count;
- firing rate;
- interspike intervals;
- burst structure;
- precise timing.

Later neural-data lessons will represent these mathematically.

The action potential supplies the discrete event.

The spike train supplies temporal structure.

---

## Refractory period shapes spike trains

Because a second spike cannot occur immediately after the first, interspike intervals have a lower biological bound.

This affects:

- firing-rate distributions;
- point-process models;
- spike detection validation.

A recorded sequence with impossible interspike intervals may indicate:

- sorting error;
- detection artifact;
- multiple neurons mixed together.

This becomes an important engineering quality check.

---

## Refractory violations in spike sorting

Suppose a putative single-neuron cluster has many spikes separated by less than the expected absolute refractory interval.

That can suggest the cluster contains spikes from more than one neuron.

This is not a perfect rule.

But refractory biology becomes a data-quality diagnostic.

Biophysics informs algorithms.

---

## Why action potentials are energy consuming

During spikes:

- Na+ enters;
- K+ leaves.

These fluxes slightly perturb the maintained ion gradients.

Pumps later restore the long-term distribution.

Therefore repeated spiking creates metabolic demand.

This connects firing activity to:

- ATP consumption;
- oxygen demand;
- blood flow.

---

## The pump does not create each spike waveform

This deserves repetition.

The rapid action-potential phases are caused mainly by passive ionic movement through voltage-gated channels down electrochemical gradients.

The Na+/K+ pump:

- maintains those gradients over longer times;
- does not generate the millisecond upstroke by cycling fast enough.

Confusing these mechanisms destroys the temporal model.

---

## Local current is not sodium ions racing to the terminal

Propagation diagrams sometimes tempt people to imagine Na+ entering at one point and then physically traveling down the entire axon.

That is wrong.

Local charge redistribution passively affects adjacent membrane.

Then local channels at the next region open.

The spike is regenerated.

The same individual Na+ ions do not need to traverse the whole axon.

---

## Common failure mode: threshold is always -55 mV

No.

That is a common teaching value.

Real threshold depends on cell type, channel state, location, and history.

---

## Common failure mode: all-or-none means stronger stimuli do nothing

No.

Stronger inputs can alter:

- firing rate;
- timing;
- recruitment;
- population response.

---

## Common failure mode: the Na+/K+ pump repolarizes each spike

Not on the spike timescale.

Rapid repolarization mainly reflects Na+ inactivation and K+ conductance.

---

## Common failure mode: an action potential is sodium traveling down the axon

No.

Propagation is local passive spread plus repeated regenerative channel activation.

---

## Common failure mode: refractory period is arbitrary dead time

No.

It emerges from channel inactivation and conductance recovery.

---

## Common failure mode: propagation uses no passive current

Wrong.

Passive local current is essential for depolarizing downstream membrane.

Active regeneration prevents long-distance decay.

---

## Common failure mode: myelin blocks all current

No.

Myelin reduces internodal leak and changes capacitance.

Current spreads under myelin and regeneration occurs at nodes.

---

## Common failure mode: myelinated action potentials literally teleport between nodes

No.

Saltatory conduction still relies on passive current spread through the internode.

---

## Common failure mode: faster firing means faster conduction

Different concepts.

Firing rate describes event frequency.

Conduction velocity describes propagation speed.

---

## Common failure mode: extracellular spike equals intracellular action potential

No.

Extracellular waveform depends on transmembrane currents and measurement geometry.

---

## Common failure mode: every large stimulation transient is neural

No.

Stimulus artifact can be much larger than the biological signal.

---

## Active work

### Exercise 1 — build the feedback loop

Write the sequence:

```text
depolarization
→ ...
→ ...
→ more depolarization
```

using voltage-gated Na+ channels.

Then identify why this is positive feedback.

### Exercise 2 — stop the spike

Explain why the upstroke terminates.

Your answer must mention:

- Na+ channel inactivation;
- delayed K+ activation;
- outward K+ current.

### Exercise 3 — phase labeling

Draw a generic action-potential waveform.

Label:

- rest;
- threshold region;
- upstroke;
- overshoot;
- repolarization;
- afterhyperpolarization;
- recovery.

For each phase, write the dominant conductance logic.

### Exercise 4 — refractory reasoning

Compare a second stimulus arriving:

1. during absolute refractory period;
2. during relative refractory period;
3. after full recovery.

Do not describe the difference only with time.

Describe channel state.

### Exercise 5 — propagation

Explain why a passive voltage perturbation decays but an action potential can maintain amplitude over long distance.

Use the words:

- local current;
- threshold;
- regeneration.

### Exercise 6 — directionality

Why can current spread backward while the spike still propagates mainly forward?

Your answer must mention refractory membrane behind the spike.

### Exercise 7 — myelin

Explain saltatory conduction without using the phrase:

> the signal magically jumps.

Include:

- internodal passive spread;
- nodes of Ranvier;
- regenerated action potentials.

### Exercise 8 — recording geometry

Compare the waveform expected from:

- intracellular electrode;
- nearby extracellular microelectrode.

Explain why they differ even when produced by the same action potential.

---

## Retrieval check

Without looking back:

1. What makes an action potential regenerative?
2. What does a voltage-gated channel do?
3. Why does Na+ entry depolarize a resting neuron?
4. What is threshold conceptually?
5. Why is threshold not a universal fixed voltage?
6. What creates the positive-feedback phase?
7. What is the upstroke?
8. What is overshoot?
9. What is Na+ channel inactivation?
10. How is inactivation different from simple closure at rest?
11. Why does K+ current increase later?
12. What produces repolarization?
13. What produces afterhyperpolarization?
14. Why does the pump not generate the rapid downstroke?
15. What does all-or-none mean?
16. What does all-or-none **not** mean?
17. How can stimulus strength change firing without changing single-spike amplitude much?
18. What is a graded potential?
19. How is passive spread involved in propagation?
20. Why do action potentials not progressively shrink along a healthy axon?
21. What is the absolute refractory period?
22. What causes it?
23. What is the relative refractory period?
24. Why is the membrane less excitable then?
25. Why does refractoriness support directionality?
26. Why does axon diameter influence conduction velocity?
27. What does myelin change electrically?
28. What is saltatory conduction?
29. What is continuous conduction?
30. Why are nodes of Ranvier important?
31. How can demyelination impair propagation?
32. What is the difference between firing rate and conduction velocity?
33. Why can extracellular spikes be multiphasic?
34. What is a compound action potential?
35. Why can refractory biology help detect spike-sorting errors?
36. Why do action potentials consume metabolic energy indirectly?
37. What did Hodgkin-Huxley modeling demonstrate conceptually?
38. What does voltage clamp control and measure?
39. What does current clamp control and measure?
40. Why can threshold depend on recent history?

---

## Connection backward: NNE-0004

NNE-0004 gave you the resting operating point:

```text
ion gradients
+
equilibrium potentials
+
resting conductances
→
resting V_m
```

This lesson adds voltage-dependent conductances:

```text
V_m changes
→ channel state changes
→ conductance changes
→ ionic currents change
→ V_m changes again
```

That feedback creates excitability.

---

## Connection forward: NNE-0006

The next canonical lesson is:

`NNE-N-0006 — Synapses, neurotransmitters, excitation, inhibition, and integration`.

Action potentials carry signals along axons.

Synapses transfer influence between cells.

The next transformation is:

```text
presynaptic action potential
→ terminal depolarization
→ Ca2+ entry
→ transmitter release
→ postsynaptic conductance change
→ graded postsynaptic potential
→ integration
→ possible new action potential
```

So action potentials and synapses form alternating regenerative and graded stages of neural signaling.

---

## Connection forward: extracellular recording

Later recording lessons will study:

- single-unit spikes;
- multi-unit activity;
- spike detection;
- spike sorting.

The extracellular waveform is a measurement consequence of the transmembrane currents introduced here.

Understanding the biology prevents treating a detected spike as an abstract digital bit detached from tissue.

---

## Connection forward: peripheral neural interfaces

Peripheral nerve interfaces often record or stimulate propagating axonal activity.

Relevant variables include:

- fiber diameter;
- myelination;
- conduction velocity;
- recruitment threshold;
- direction of travel.

The action-potential mechanism becomes directly measurable engineering structure.

---

## Connection forward: stimulation

Electrical stimulation changes membrane polarization.

If a region crosses the regenerative threshold, an action potential can be initiated.

Then the action potential propagates away from the activation site.

Depending on geometry, stimulation can generate:

- orthodromic propagation;
- antidromic propagation;
- multiple recruited fibers.

Later stimulation lessons will formalize these concepts.

---

## Connection to Linear Algebra

A multi-electrode recording at one instant can be represented as a vector.

A propagating action potential creates a sequence of spatial patterns across electrodes.

Those patterns can later be modeled with:

- vectors;
- linear combinations;
- subspaces;
- time-dependent state models.

The biology tells you what those vectors represent.

---

## What this unlocks

You should now be able to reason through:

```text
resting membrane
→ local depolarization
→ threshold
→ fast Na+ activation
→ regenerative upstroke
→ Na+ inactivation + delayed K+ activation
→ repolarization
→ refractory recovery
```

and then:

```text
local action potential
→ passive current spread
→ adjacent threshold crossing
→ regenerated action potential
→ long-distance propagation
```

For myelinated axons:

```text
node
→ internodal passive spread
→ next node
→ regeneration
```

This is enough to move from electrical signaling within one cell to communication between cells.

---

## References

- **NNE-REF-025** — Purves et al., *Neuroscience*, 2nd ed., “Voltage-Dependent Membrane Permeability,” NCBI Bookshelf.
- **NNE-REF-026** — Purves et al., *Neuroscience*, 2nd ed., “Ion Channels Underlying Action Potentials,” NCBI Bookshelf.
- **NNE-REF-027** — Purves et al., *Neuroscience*, 2nd ed., “The Refractory Period,” NCBI Bookshelf.
- **NNE-REF-028** — Purves et al., *Neuroscience*, 2nd ed., “Long-Distance Signaling by Means of Action Potentials” and “Increased Conduction Velocity as a Result of Myelination,” NCBI Bookshelf.
