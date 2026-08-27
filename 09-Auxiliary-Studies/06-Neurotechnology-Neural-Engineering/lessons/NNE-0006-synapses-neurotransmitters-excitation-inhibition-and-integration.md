---
id: NNE-0006
title: "Synapses, neurotransmitters, excitation, inhibition, and integration"
track: neurotechnology-neural-engineering
level: L0
status: complete
curriculum_node: NNE-N-0006
concepts_introduced: ["NNE-C-0009"]
concepts_deepened: ["NNE-C-0008", "NNE-C-0007"]
concepts_used: ["NNE-C-0006", "NNE-C-0005", "NNE-C-0002", "NNE-C-0004"]
examples_added: ["NNE-EX-026", "NNE-EX-027", "NNE-EX-028", "NNE-EX-029", "NNE-EX-030"]
references_used: ["NNE-REF-029", "NNE-REF-030", "NNE-REF-031", "NNE-REF-032"]
last_reviewed: 2026-08-27
version_sensitive: false
review_after: null
---

# Synapses, neurotransmitters, excitation, inhibition, and integration

## If you landed here directly

This lesson assumes the electrical-signaling foundations from `NNE-0004` and `NNE-0005`.

You should already know that:

- a neuron's membrane voltage depends on ion gradients and membrane conductances;
- an action potential is a regenerative electrical event;
- action potentials propagate along axons;
- voltage-gated Ca2+ channels can respond to terminal depolarization;
- a neuron's firing probability depends on its membrane state and threshold dynamics.

This lesson asks the next question:

> once an action potential reaches the end of an axon, how does one cell influence another?

The answer is **synaptic transmission**.

By the end, you should be able to explain:

- what a synapse is;
- how chemical and electrical synapses differ;
- why presynaptic Ca2+ entry matters;
- how vesicles release neurotransmitter;
- why a neurotransmitter is not automatically "excitatory" or "inhibitory" by name alone;
- how postsynaptic receptors change membrane conductance;
- what EPSPs and IPSPs are;
- why reversal potential matters;
- how ionotropic and metabotropic receptors differ;
- how temporal and spatial summation work;
- how a neuron integrates many simultaneous inputs;
- why inhibition can work by hyperpolarization or by shunting;
- why synaptic transmission is probabilistic and state dependent;
- what synaptic signals look like from an engineering measurement perspective.

---

## The problem worth understanding

An action potential reaches a presynaptic terminal.

The spike itself cannot simply leap across a fluid-filled gap into the next neuron.

At a typical chemical synapse, the signal changes physical form:

```text
electrical
→ chemical
→ electrical
```

More explicitly:

```text
presynaptic action potential
→ terminal depolarization
→ voltage-gated Ca2+ channels open
→ Ca2+ enters
→ vesicles fuse
→ neurotransmitter is released
→ transmitter binds postsynaptic receptors
→ postsynaptic conductance changes
→ postsynaptic current changes
→ membrane voltage / excitability changes
```

This is a transduction chain.

Each step has its own timescale, uncertainty, and failure modes.

---

## What is a synapse?

A **synapse** is a specialized junction through which one cell influences another.

The communicating cells can be:

- neuron to neuron;
- neuron to muscle;
- neuron to gland;
- in some cases, neuron to other specialized target cells.

At L0, we will focus mainly on neuron-to-neuron communication.

Two broad synapse classes matter:

- chemical synapses;
- electrical synapses.

---

## Chemical synapses

A typical chemical synapse includes:

```text
presynaptic terminal
synaptic vesicles
synaptic cleft
postsynaptic membrane
postsynaptic receptors
```

The presynaptic terminal contains vesicles loaded with neurotransmitter.

The postsynaptic membrane contains receptors that detect the released transmitter.

The two membranes are separated by a small extracellular cleft.

---

## Electrical synapses

Electrical synapses use gap junction channels to connect cells electrically.

Current can pass relatively directly between cells through these intercellular channels.

Compared with chemical synapses, electrical synapses can be:

- very fast;
- often bidirectional, though rectifying examples exist;
- useful for synchronization.

The key contrast is:

```text
chemical:
electrical → chemical messenger → postsynaptic electrical effect

electrical:
direct intercellular current path
```

Both are biological communication mechanisms.

---

## Chemical synapses introduce a synaptic delay

Chemical transmission requires several sequential events:

1. terminal depolarization;
2. Ca2+ channel opening;
3. Ca2+ entry;
4. vesicle fusion;
5. transmitter diffusion;
6. receptor binding;
7. channel or signaling response.

Therefore chemical synapses have a finite synaptic delay.

This delay is small on ordinary human timescales.

But millisecond-scale delays matter in neural circuits and closed-loop neurotechnology.

---

## Presynaptic action potential arrival

When an action potential invades the presynaptic terminal, membrane voltage changes rapidly.

That depolarization opens voltage-gated Ca2+ channels.

This creates the key link:

```text
action potential
→ Ca2+ influx
```

Why calcium?

Because intracellular free Ca2+ is normally kept very low.

When Ca2+ channels open, Ca2+ has a strong electrochemical tendency to enter.

---

## Ca2+ is the release trigger

The rise in presynaptic Ca2+ concentration promotes synaptic-vesicle fusion with the presynaptic membrane.

The vesicle membrane becomes continuous with the plasma membrane.

The vesicle contents are released into the synaptic cleft.

This is **exocytosis**.

A useful causal chain is:

```mermaid
flowchart LR
    AP["Presynaptic action potential"] --> DEP["Terminal depolarization"]
    DEP --> CA["Voltage-gated Ca2+ channels open"]
    CA --> CIN["Ca2+ enters terminal"]
    CIN --> VF["Vesicle fusion"]
    VF --> NT["Neurotransmitter release"]
```

---

## Vesicles make release packet-like

Neurotransmitter is packaged into synaptic vesicles.

This creates a natural unit of release.

Historically, synaptic physiology revealed **quantal** transmitter release: postsynaptic responses can reflect discrete vesicular packets rather than an infinitely divisible continuous stream.

At L0, keep this mental model:

> chemical synaptic release is built from vesicle-release events.

The exact number of vesicles released can vary.

---

## Release is not perfectly deterministic

The arrival of one presynaptic action potential does not guarantee that every release site releases a vesicle.

Synaptic release can be probabilistic.

Relevant factors include:

- presynaptic Ca2+ entry;
- release machinery state;
- vesicle availability;
- recent activity;
- neuromodulation.

So:

```text
presynaptic spike
does not always imply
identical postsynaptic response
```

This is one source of biological variability.

---

## The synaptic cleft is not an empty wire gap

After release, neurotransmitter molecules diffuse through extracellular space across the synaptic cleft.

They then bind to specific receptors.

The cleft is a biochemical signaling compartment.

Its geometry and clearance mechanisms help shape transmitter concentration over time.

---

## Neurotransmitter

A **neurotransmitter** is a chemical signaling molecule released from presynaptic terminals that acts on receptors in target cells.

Important transmitter families include:

- glutamate;
- GABA;
- glycine;
- acetylcholine;
- dopamine;
- norepinephrine;
- serotonin;
- neuropeptides;
- others.

Do not turn this into a memorization list yet.

The more important question is:

> what receptor does the transmitter activate, and what does that receptor do to the postsynaptic cell?

---

## A neurotransmitter is not the whole synaptic effect

A dangerous oversimplification is:

```text
glutamate = excitation
GABA = inhibition
```

Those statements are often useful first approximations in the mature central nervous system.

But the actual postsynaptic effect depends on:

- receptor subtype;
- ion selectivity;
- ionic concentration gradients;
- reversal potential;
- postsynaptic membrane voltage;
- intracellular signaling pathways.

So:

> transmitter identity alone does not fully specify the effect.

---

## Receptors translate chemical information

Postsynaptic receptors bind neurotransmitters.

Their activation changes the target cell.

Two broad receptor families are especially important:

- ionotropic receptors;
- metabotropic receptors.

They differ in mechanism and timescale.

---

## Ionotropic receptors

An **ionotropic receptor** is directly associated with an ion channel.

Neurotransmitter binding changes channel opening.

That rapidly changes membrane conductance.

Typical chain:

```text
transmitter binds
→ channel opens
→ ions flow
→ postsynaptic current
→ membrane voltage changes
```

These responses are often fast.

---

## Metabotropic receptors

A **metabotropic receptor** affects cellular signaling indirectly, commonly through G proteins and intracellular signaling cascades.

Typical chain:

```text
transmitter binds receptor
→ intracellular signaling
→ channel / enzyme / cellular process changes
```

Responses can be:

- slower;
- longer lasting;
- modulatory;
- more spatially distributed.

So the phrase "neurotransmitter receptor" does not imply one universal response speed.

---

## Postsynaptic current comes before postsynaptic voltage

When synaptic receptors change conductance, ions flow according to electrochemical driving force.

That creates a synaptic current.

The current then changes membrane voltage according to the electrical properties of the postsynaptic membrane.

So:

```text
receptor activation
→ conductance change
→ ionic current
→ postsynaptic voltage response
```

This preserves the membrane-physics logic from `NNE-0004`.

---

## Postsynaptic potentials are usually graded

A postsynaptic potential, or PSP, is generally a graded voltage response.

Its amplitude depends on factors such as:

- amount of transmitter released;
- receptor number;
- synaptic conductance;
- driving force;
- membrane resistance;
- location;
- other simultaneous inputs.

Unlike an action potential, a PSP is not normally all-or-none.

---

## EPSP

An **excitatory postsynaptic potential**, or EPSP, increases the probability that the postsynaptic neuron will generate an action potential.

Often this means depolarizing the cell toward threshold.

But the more precise definition is functional:

> excitation increases spike probability under the relevant conditions.

Do not define EPSP only as:

> membrane becomes more positive.

That is often true, but it is not the deepest rule.

---

## IPSP

An **inhibitory postsynaptic potential**, or IPSP, decreases the probability that the postsynaptic neuron will generate an action potential.

Often this involves:

- hyperpolarization;
- conductance changes that stabilize membrane voltage;
- shunting of excitatory current.

So inhibition does not require a dramatic negative-going voltage deflection.

---

## Reversal potential determines synaptic direction

For a synaptic conductance, a useful current relation is:

$$ I_{\text{syn}}\approx g_{\text{syn}}(V_m-E_{\text{rev}}). $$

Where:

- `g_syn` is synaptic conductance;
- `V_m` is membrane voltage;
- `E_rev` is the synaptic reversal potential.

The sign and magnitude of:

$$ V_m-E_{\text{rev}} $$

help determine synaptic current direction.

This is the same driving-force logic from `NNE-0004`.

---

## Excitation and inhibition depend on threshold too

Suppose a synaptic reversal potential is:

```text
E_rev = 0 mV
```

and the neuron is near:

```text
V_m = -70 mV.
```

Opening that conductance pulls membrane voltage upward toward 0 mV.

That is strongly depolarizing and usually excitatory.

Now imagine another synaptic conductance with:

```text
E_rev ≈ -70 mV.
```

Opening it may produce little visible voltage change at rest.

But it can still strongly increase membrane conductance and reduce the effect of simultaneous excitatory currents.

That is **shunting inhibition**.

---

## Example NNE-EX-026 — same transmitter, receptor determines the effect

Imagine transmitter `T` can bind two receptor subtypes.

### Receptor A

Opens a cation channel with reversal potential near 0 mV.

At:

```text
V_m = -70 mV
```

current tends to depolarize the cell.

Spike probability increases.

### Receptor B

Activates a K+-selective pathway with a much more negative reversal potential.

The postsynaptic effect tends to make firing less likely.

Same transmitter.

Different receptor machinery.

Therefore:

> neurotransmitter identity is not enough to infer synaptic effect.

---

## Glutamate

Glutamate is the major excitatory neurotransmitter in much of the mature central nervous system.

Many glutamatergic receptors increase cation conductance and depolarize the postsynaptic neuron.

Important receptor families include:

- AMPA;
- NMDA;
- metabotropic glutamate receptors.

At L0, do not memorize every subtype.

Remember:

> glutamate commonly participates in fast excitation, but receptor properties define the precise effect.

---

## GABA

GABA is the major inhibitory neurotransmitter in much of the mature brain.

Common GABA receptor mechanisms include:

- ionotropic Cl--related conductance;
- metabotropic pathways influencing K+ and other channels.

But the effect depends on ionic gradients.

During development or altered chloride regulation, the same transmitter can produce different voltage effects.

Again:

```text
transmitter name
≠
complete electrical prediction
```

---

## Glycine

Glycine is an important inhibitory transmitter in parts of the spinal cord and brainstem.

Many glycine receptors are ligand-gated Cl- channels.

This is another example of inhibition through receptor-controlled ionic conductance.

---

## Acetylcholine

Acetylcholine acts at:

- neuromuscular junctions;
- autonomic synapses;
- central synapses.

It can activate:

- nicotinic ionotropic receptors;
- muscarinic metabotropic receptors.

So one transmitter can participate in very different signaling modes.

---

## Dopamine, serotonin, and neuromodulation

Some transmitters often act through metabotropic receptors and can modify:

- excitability;
- channel state;
- synaptic strength;
- network dynamics.

Their effects may not resemble a simple fast EPSP or IPSP.

This is one reason the nervous system uses the broader concept of **neuromodulation**.

---

## Signal termination matters

If neurotransmitter remained in the cleft indefinitely, synaptic signaling would not be temporally precise.

Synaptic effects are terminated by mechanisms such as:

- reuptake;
- enzymatic degradation;
- diffusion away;
- receptor desensitization and downstream termination.

The exact mechanism depends on transmitter and synapse.

---

## Reuptake

Transporters can move neurotransmitter out of the synaptic cleft.

Reuptake can involve:

- presynaptic terminals;
- surrounding glial cells.

This is another place where glia participate directly in neural signaling.

---

## Example NNE-EX-027 — trace one chemical synaptic event

Start with one presynaptic action potential.

Trace:

```text
action potential reaches terminal
→ Ca2+ channels open
→ Ca2+ enters
→ vesicle fusion
→ transmitter release
→ diffusion
→ receptor binding
→ conductance change
→ postsynaptic current
→ PSP
```

Now identify three places where variability can arise:

1. amount of Ca2+ entry;
2. vesicle release probability;
3. postsynaptic receptor / membrane state.

This is a biological communication channel with multiple stochastic elements.

---

## Synaptic strength

A stronger synapse can produce a larger influence on the postsynaptic neuron.

"Strength" can depend on:

- release probability;
- number of release sites;
- amount of transmitter;
- receptor density;
- receptor conductance;
- dendritic location;
- membrane state.

So synaptic strength is not one physical knob.

It is an emergent property of several mechanisms.

---

## Dendritic location matters

A synapse far out on a dendrite does not necessarily have the same effect at the axon initial segment as an equally large local conductance near the soma.

Passive cable properties cause synaptic voltage signals to:

- attenuate;
- spread;
- interact with dendritic geometry.

Therefore:

> synaptic influence depends on both synapse strength and synapse location.

---

## The neuron receives many inputs

A typical neuron receives many synapses.

At any moment, some may be:

- excitatory;
- inhibitory;
- modulatory;
- inactive.

The postsynaptic neuron combines these influences.

This process is **integration**.

---

## Spatial summation

**Spatial summation** means that postsynaptic effects from different synaptic locations overlap in time and combine.

Example:

```text
synapse A active
+
synapse B active
+
synapse C active
→ combined postsynaptic effect
```

If two EPSPs overlap, their combined depolarization can be larger than either alone.

---

## Temporal summation

**Temporal summation** means repeated inputs from the same or nearby synapses arrive close enough in time that their postsynaptic responses overlap.

Example:

```text
EPSP 1 has not fully decayed
when
EPSP 2 arrives
→ responses sum
```

Timing therefore matters.

---

## Example NNE-EX-028 — temporal summation

Suppose one synapse generates a small EPSP that is individually subthreshold.

### Slow presynaptic firing

Each EPSP decays before the next arrives.

Result:

```text
little summation
```

### Faster presynaptic firing

A second EPSP arrives before the first has disappeared.

A third arrives before the combined response decays.

Result:

```text
temporal summation
→ larger depolarization
→ threshold becomes more likely
```

The presynaptic spike amplitude did not change.

The **timing pattern** changed.

---

## Example NNE-EX-029 — spatial excitation plus inhibition

Suppose a postsynaptic neuron receives:

```text
E1 = excitatory synapse
E2 = excitatory synapse
I1 = inhibitory synapse
```

If E1 and E2 are active together:

```text
EPSP + EPSP
→ stronger depolarization
```

Now activate I1 at the same time.

The inhibitory conductance may:

- hyperpolarize the membrane;
- increase total membrane conductance;
- reduce the voltage effect of excitatory current.

So the final membrane response is not simply:

```text
E1 + E2 - one fixed inhibitory number
```

Synaptic integration depends on conductance and timing.

---

## Shunting inhibition

Suppose an inhibitory synapse opens channels with reversal potential near the current resting voltage.

The membrane voltage may barely move.

But membrane conductance increases.

Now an excitatory current arrives.

Because the membrane is more conductive, the same excitatory current produces a smaller voltage change.

This is **shunting**.

Important lesson:

> inhibition can be strong even without obvious hyperpolarization.

---

## Conductance means inputs can interact nonlinearly

Introductory explanations often say:

$$ \text{PSP total}=\text{EPSP}_1+\text{EPSP}_2+\text{IPSP}. $$

That can be a useful approximation for small signals.

But synaptic inputs change conductances.

Conductance changes alter how other currents affect voltage.

Therefore real integration is not always a perfect arithmetic sum.

This becomes important in computational neuroscience.

---

## Integration at the axon initial segment

Dendritic and somatic inputs influence the membrane state near the axon initial segment.

If the integrated state crosses the regenerative action-potential condition:

```text
action potential begins
```

If not:

```text
no output spike at that moment
```

So the neuron performs a physical transformation:

```text
many graded inputs
→ integrated membrane state
→ threshold dynamics
→ spike output
```

---

## The neuron is not a simple binary logic gate

It is tempting to say:

```text
enough excitation = 1
not enough = 0
```

That loses important biology.

Neural output depends on:

- timing;
- dendritic location;
- inhibition;
- channel state;
- recent history;
- neuromodulation;
- intrinsic membrane dynamics.

Binary abstractions can be useful later.

But they are models, not literal cellular behavior.

---

## Presynaptic versus postsynaptic

Always identify which side you mean.

### Presynaptic

The cell sending transmitter at a particular synapse.

### Postsynaptic

The target cell receiving transmitter at that synapse.

A neuron can be:

- postsynaptic at one connection;
- presynaptic at another.

These are relational roles, not permanent neuron types.

---

## Axodendritic, axosomatic, and axoaxonic contacts

Synapses can occur at different target regions.

Examples include:

- axon onto dendrite;
- axon onto soma;
- axon onto another axon or terminal.

Location changes functional influence.

A synapse near spike initiation can have different leverage from a distal dendritic synapse.

---

## Presynaptic inhibition

Not all inhibition acts by directly hyperpolarizing the postsynaptic soma.

Some synapses regulate transmitter release from another presynaptic terminal.

This is **presynaptic inhibition**.

It can modify:

- Ca2+ entry;
- vesicle release;
- transmitter amount.

The nervous system can therefore regulate information flow before the postsynaptic PSP is generated.

---

## Electrical synapses and synchronization

Because current can pass directly through gap junctions, electrical synapses can synchronize populations of cells.

They can transmit:

- subthreshold voltage fluctuations;
- sometimes action-potential-related current.

Electrical coupling therefore differs from chemical synaptic event transmission.

---

## Electrical synapses are not simply "better"

They are faster and direct.

But chemical synapses offer powerful capabilities:

- amplification;
- sign changes;
- receptor diversity;
- modulation;
- plasticity;
- biochemical control.

The nervous system uses both.

---

## Chemical synapses are typically directional

A typical chemical synapse has:

- release machinery presynaptically;
- receptor machinery postsynaptically.

This creates directional transmission.

Electrical synapses can be more symmetric, though not always.

---

## Synaptic latency contributes to circuit timing

Suppose a circuit contains several sequential chemical synapses.

Each adds delay.

Therefore pathway latency includes:

```text
axonal conduction delay
+
synaptic delay
+
postsynaptic integration delay
```

Closed-loop neural systems must respect all three.

---

## Synapses are filters

A synapse does not merely relay a presynaptic spike.

It transforms spike timing into a postsynaptic waveform.

Depending on receptor kinetics:

- response can be fast or slow;
- response can outlast the presynaptic spike;
- repeated spikes can accumulate;
- short-term dynamics can change amplitude.

So a synapse behaves partly like a biological temporal filter.

---

## Short-term synaptic dynamics

Repeated presynaptic activity can change synaptic effectiveness over short times.

Examples include:

- facilitation;
- depression.

Mechanisms can involve:

- residual presynaptic Ca2+;
- vesicle depletion;
- receptor state.

A synapse therefore can have memory of recent activity.

---

## Synaptic plasticity preview

Synaptic strength can also change over longer timescales.

This is **synaptic plasticity**.

Later lessons will revisit plasticity in:

- learning;
- adaptation;
- neural interfaces;
- closed-loop coadaptation.

At L0, remember:

> a synapse is not necessarily a fixed weight.

---

## A machine-learning weight is only an analogy

Artificial neural networks often represent connections using scalar weights.

Biological synapses can indeed strengthen or weaken influence.

But one biological synapse has:

- transmitter-release probability;
- receptor dynamics;
- conductance;
- timing;
- nonlinear state;
- biochemical modulation.

So:

```text
biological synapse
≠
one static scalar multiplication
```

The analogy is useful only at a chosen modeling level.

---

## Example NNE-EX-030 — engineering view of a synapse

Suppose we model one chemical synapse as a signal-processing block.

Input:

```text
presynaptic spike train
```

Hidden state:

```text
release probability
vesicle availability
receptor state
postsynaptic V_m
```

Output:

```text
postsynaptic current / conductance waveform
```

Then:

```text
spike timing
→ release events
→ synaptic current
→ PSP
→ integration with other inputs
```

This reveals why the mapping from presynaptic spikes to postsynaptic voltage is:

- dynamic;
- noisy;
- state dependent;
- history dependent.

---

## Synaptic current versus field potential

A synaptic current crosses a neuronal membrane locally.

That transmembrane current contributes to extracellular electrical fields.

When many synaptic currents are spatially organized and synchronized, they can contribute strongly to:

- local field potentials;
- ECoG;
- EEG.

So extracellular field recordings often reflect synaptic and dendritic currents more strongly than they directly reflect single axonal spikes.

---

## Why EEG is strongly linked to postsynaptic currents

A single action potential is brief and spatially small.

By contrast, synchronized postsynaptic currents can occur across large populations of aligned neurons.

Their fields can sum.

This makes organized synaptic activity especially important for macroscopic electrophysiology.

Later signal lessons will formalize this.

---

## Synaptic events are not directly visible in every recording modality

An extracellular microelectrode may capture:

- spikes;
- local field potentials.

EEG captures larger-scale field mixtures.

fMRI does not measure neurotransmitter release directly.

It reflects hemodynamic consequences of neural activity.

So:

```text
synapse
→ biological event

recorded signal
→ modality-dependent consequence
```

Do not confuse mechanism with measurement.

---

## Pharmacology changes synaptic transfer functions

A drug can alter:

- transmitter synthesis;
- vesicle release;
- receptor activation;
- reuptake;
- degradation;
- ion-channel conductance.

Therefore pharmacology can change neural-system behavior without directly changing axon anatomy.

This is a useful systems insight.

It is not a medication guide.

---

## Neurotransmitter concentration is not the same as neural "information"

A transmitter molecule has a biochemical identity.

Information is carried through patterns of:

- release;
- timing;
- location;
- receptor effects;
- circuit state.

Do not treat one molecule as one semantic symbol.

---

## Excitation is not "good" and inhibition is not "bad"

These words are dynamical.

Excitation increases the chance of postsynaptic firing.

Inhibition decreases it.

Healthy computation requires both.

Inhibition supports:

- stability;
- timing;
- gain control;
- competition;
- oscillations;
- selective routing.

---

## Balance does not mean equal numbers

"Excitation-inhibition balance" does not necessarily mean:

```text
same number of excitatory and inhibitory synapses
```

It concerns the net functional interaction of currents and conductances.

Synapses differ in:

- strength;
- location;
- timing;
- reversal potential;
- kinetics.

Counting alone is insufficient.

---

## Integration is continuous in time

A neuron does not collect all inputs into a bag and then decide once.

Its membrane state evolves continuously.

Inputs arrive:

- asynchronously;
- at different locations;
- with different kinetics.

The membrane is always integrating.

---

## Common failure mode: neurotransmitter crosses the synapse as electrical current

At a chemical synapse, transmitter is a chemical messenger.

Ionic current occurs through membrane channels before and after release.

The transmitter itself is not the same thing as the postsynaptic ionic current.

---

## Common failure mode: action potential jumps across the cleft

No.

The presynaptic action potential triggers a chemical release process.

The postsynaptic cell generates its own electrical response.

---

## Common failure mode: transmitter release happens because Na+ enters the terminal

Terminal depolarization is produced by the action potential.

But fast transmitter release is triggered primarily by presynaptic Ca2+ entry through voltage-gated Ca2+ channels.

---

## Common failure mode: every presynaptic spike causes identical transmitter release

No.

Release is probabilistic and state dependent.

---

## Common failure mode: glutamate is always excitatory and GABA is always inhibitory

That is too absolute.

Receptors, reversal potentials, ionic gradients, developmental state, and cellular context matter.

---

## Common failure mode: IPSP always means visible hyperpolarization

No.

Inhibition can be shunting with little voltage deflection.

---

## Common failure mode: one EPSP usually triggers an action potential

At many central synapses, individual PSPs are small and subthreshold.

Integration across space and time matters.

---

## Common failure mode: spatial summation means signals physically merge into one synapse

No.

Inputs at different synapses influence the same postsynaptic membrane state.

---

## Common failure mode: temporal summation means spike amplitudes become taller

It is the overlap of postsynaptic responses over time, not the height of presynaptic action potentials.

---

## Common failure mode: a biological synapse is one fixed scalar weight

No.

Its effect has dynamics, stochastic release, receptor kinetics, conductance, and plasticity.

---

## Common failure mode: inhibition subtracts a fixed number from excitation

Conductance-based inhibition can change how excitatory currents translate into voltage.

It is not always simple arithmetic subtraction.

---

## Common failure mode: chemical synapses are always slower in every useful sense

They introduce synaptic delay relative to direct electrical coupling, but receptor kinetics vary widely.

Some chemical responses are fast.

Others are slow and modulatory.

---

## Common failure mode: synaptic current equals recorded EEG voltage

No.

Synaptic current contributes to extracellular fields through tissue geometry and population summation.

EEG is a remote mixture of many sources.

---

## Active work

### Exercise 1 — chemical synaptic chain

Without looking back, write:

```text
presynaptic spike
→ ...
→ postsynaptic PSP
```

Include:

- terminal depolarization;
- Ca2+ channels;
- vesicle fusion;
- neurotransmitter;
- receptor;
- conductance.

### Exercise 2 — receptor dependence

A transmitter activates:

```text
receptor A:
E_rev = 0 mV

receptor B:
E_rev = -90 mV
```

At:

```text
V_m = -65 mV
```

predict the qualitative direction of each effect.

Do not label the transmitter itself excitatory or inhibitory before considering the receptor.

### Exercise 3 — temporal summation

Draw three small EPSPs.

Case A:

```text
far apart in time
```

Case B:

```text
close together
```

Explain why Case B can produce a larger peak membrane response.

### Exercise 4 — spatial integration

A neuron receives:

```text
two excitatory synapses
one inhibitory synapse
```

Construct two timing patterns that produce different outputs even though the same three synapses are involved.

### Exercise 5 — shunting

Explain how opening an inhibitory conductance with reversal potential near rest can reduce excitation without producing a large hyperpolarization.

### Exercise 6 — electrical versus chemical synapse

Build a comparison table with:

- physical connection;
- directionality;
- delay;
- modulation;
- receptor dependence;
- synchronization.

### Exercise 7 — recording interpretation

Explain why a synchronized population of postsynaptic currents can contribute strongly to a field potential even though each individual PSP is small.

### Exercise 8 — synapse as system block

For one chemical synapse, list:

- input;
- hidden state;
- output;
- sources of stochasticity;
- sources of memory.

---

## Retrieval check

Without looking back:

1. What is a synapse?
2. What are the two broad synapse classes?
3. What separates cells at a chemical synapse?
4. What is a synaptic vesicle?
5. What happens when a presynaptic action potential reaches a terminal?
6. Why does Ca2+ enter?
7. What does Ca2+ trigger?
8. What is exocytosis?
9. What is a neurotransmitter?
10. Why is release described as quantal?
11. Why can synaptic release be probabilistic?
12. What does a postsynaptic receptor do?
13. What is an ionotropic receptor?
14. What is a metabotropic receptor?
15. Which is usually faster?
16. What is a postsynaptic current?
17. What is a postsynaptic potential?
18. What is an EPSP?
19. What is an IPSP?
20. Why is reversal potential important?
21. Why is transmitter identity alone insufficient to predict effect?
22. What is shunting inhibition?
23. Why can inhibition occur without strong hyperpolarization?
24. What is temporal summation?
25. What is spatial summation?
26. Why does dendritic location matter?
27. What does integration mean?
28. Where does action-potential initiation usually enter the integration story?
29. What is presynaptic inhibition?
30. How are electrical synapses different?
31. Why can electrical synapses synchronize cells?
32. What is synaptic delay?
33. What is synaptic strength?
34. Why is synaptic strength not one single molecular quantity?
35. What is short-term facilitation?
36. What is short-term depression?
37. Why is a biological synapse not equivalent to one fixed neural-network weight?
38. Why can postsynaptic currents contribute to EEG/LFP?
39. Why does excitation not mean "good"?
40. Why does inhibition not mean "bad"?

---

## Connection backward: NNE-0005

`NNE-0005` gave:

```text
action potential
→ axonal propagation
→ presynaptic terminal
```

This lesson adds:

```text
presynaptic terminal
→ Ca2+ entry
→ transmitter release
→ postsynaptic conductance
→ graded PSP
→ integration
→ possible new action potential
```

So a neural pathway alternates between:

```text
regenerative spikes
and
graded synaptic influences
```

---

## Connection backward: NNE-0004

Synaptic effects depend on:

- `V_m`;
- conductance;
- reversal potential;
- ion gradients.

Those were the core concepts of resting membrane potential.

So excitation and inhibition are applications of the same electrochemical driving-force logic.

---

## Connection forward: NNE-0007

The next canonical lesson is:

`NNE-N-0007 — From single neurons to populations, circuits, systems, and behavior`.

One neuron receives many synapses.

Many neurons form circuits.

Circuits produce:

- population activity;
- computation;
- sensorimotor transformations;
- behavior.

This lesson supplies the connection rule from which networks are built.

---

## Connection forward: field potentials

Synaptic currents are important sources of extracellular fields.

Later lessons on:

- LFP;
- ECoG;
- EEG

will rely on the distinction between:

```text
local transmembrane current
and
remote measured field
```

---

## Connection forward: neural interfaces

A neural interface may:

- record consequences of synaptic activity;
- stimulate neurons and alter synaptic release;
- trigger plasticity;
- interact with neuromodulatory state.

Closed-loop interfaces therefore influence networks through synapses, not only through action potentials.

---

## Connection to Linear Algebra

Suppose a neuron receives `n` modeled synaptic inputs.

At one simplified time point, their strengths can be represented as a vector:

```text
[x1, x2, ..., xn]
```

A linearized model may combine them using weights.

But the biology learned here warns that real integration can be:

- conductance based;
- nonlinear;
- time dependent;
- state dependent.

Linear algebra is a modeling language, not a claim that dendrites literally perform static dot products.

---

## What this unlocks

You should now be able to reason through:

```text
presynaptic spike
→ Ca2+-dependent transmitter release
→ receptor activation
→ conductance change
→ synaptic current
→ graded postsynaptic potential
```

and then:

```text
many synaptic inputs
+
timing
+
location
+
inhibition
+
membrane state
→ integration
→ probability of postsynaptic spike
```

The next step is to scale this from one neuron to populations, circuits, systems, and behavior.

---

## References

- **NNE-REF-029** — Purves et al., *Neuroscience*, 2nd ed., Chapter 5, “Synaptic Transmission,” including electrical and chemical synapses, NCBI Bookshelf.
- **NNE-REF-030** — Purves et al., *Neuroscience*, 2nd ed., “Excitatory and Inhibitory Postsynaptic Potentials,” NCBI Bookshelf.
- **NNE-REF-031** — Purves et al., *Neuroscience*, 2nd ed., “Summation of Synaptic Potentials,” NCBI Bookshelf.
- **NNE-REF-032** — Purves et al., *Neuroscience*, 2nd ed., “Neurotransmitters” and chapter summary material on transmitter synthesis, release, receptor action, and clearance, NCBI Bookshelf.
