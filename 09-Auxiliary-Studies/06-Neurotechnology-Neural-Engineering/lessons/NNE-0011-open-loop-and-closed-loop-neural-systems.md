---
id: NNE-0011
title: "Open-loop and closed-loop neural systems"
track: neurotechnology-neural-engineering
level: L0
status: complete
curriculum_node: NNE-N-0011
concepts_introduced: ["NNE-C-0014"]
concepts_deepened: ["NNE-C-0002", "NNE-C-0012", "NNE-C-0013"]
concepts_used: ["NNE-C-0001", "NNE-C-0004", "NNE-C-0010", "NNE-C-0011"]
examples_added: ["NNE-EX-050", "NNE-EX-051", "NNE-EX-052", "NNE-EX-053"]
references_used: ["NNE-REF-004", "NNE-REF-009", "NNE-REF-012", "NNE-REF-050", "NNE-REF-051", "NNE-REF-052"]
last_reviewed: 2026-08-28
version_sensitive: false
review_after: null
---
# Open-loop and closed-loop neural systems

## If you landed here directly

This lesson assumes `NNE-0010 — The neural modulation chain: stimulus, field or actuator, target, response, and side effects`.

You should already understand two separate engineering directions:

```text
measurement:
biology → sensor → electronics → data → inference

modulation:
command → actuator → physical field → tissue → neural response → outcome
```

The new question is:

> what happens when information from the measured response is allowed to influence a later command?

That question creates the distinction between **open-loop** and **closed-loop** neural systems.

The central mental model of this lesson is:

```text
reference / goal
      ↓
 decision or controller
      ↓
   command
      ↓
 modulation chain
      ↓
 neural system
      ↓
 measurement chain
      ↓
 estimate / feedback
      └──────────────→ back to the decision
```

By the end, you should be able to:

- define open-loop and closed-loop relative to an explicit measured variable;
- identify the plant, sensor, estimate, controller, actuator, command, and feedback path in a neural system;
- explain why sensing alone does not make a system closed-loop;
- explain why feedback alone does not guarantee good control;
- distinguish a target biological variable from a measured biomarker or proxy;
- reason about thresholds, delays, noise, artifacts, state changes, and safety constraints;
- compare fixed stimulation, responsive stimulation, adaptive DBS, and feedback-driven assistive BCIs;
- explain why a closed-loop system can fail even when every component works individually;
- prepare for system-level tradeoffs among resolution, selectivity, bandwidth, invasiveness, stability, latency, and safety.

---

# The problem worth understanding

Suppose two implanted stimulators deliver the same pulse pattern most of the day.

System A runs a schedule chosen in advance:

```text
09:00 → stimulation on
22:00 → stimulation off
```

System B continuously measures a neural feature and changes stimulation when the feature crosses a programmed criterion:

```text
measure
→ estimate biomarker
→ compare with criterion
→ choose command
→ stimulate
→ measure again
```

Both systems can contain sensors.

Both can store data.

Both can use sophisticated software.

But only the second system uses the measured state in the decision that determines a later stimulation command.

That feedback dependency is the key distinction.

---

# Part I — Open-loop does not mean primitive

## Open-loop definition

A system is **open-loop with respect to a variable** when its command does not depend on feedback from that variable during operation.

A simple example is fixed continuous stimulation:

```text
programmed settings
→ stimulator
→ tissue
→ neural response
```

The device may have been calibrated carefully before use.

A clinician may adjust it at appointments.

The system may record battery state or diagnostics.

It can still be open-loop with respect to the neural state being treated.

---

## Open-loop can still be adaptive across long timescales

Imagine a clinician reviews a patient's symptoms every month and reprograms stimulation.

At the human-system level there is feedback:

```text
patient outcome
→ clinical evaluation
→ reprogramming
```

But between visits, the implanted stimulation may remain open-loop with respect to moment-to-moment neural activity.

So always specify:

```text
closed-loop with respect to what variable?
closed over what timescale?
```

---

# Part II — Closed-loop means a feedback dependency exists

## The minimal closed loop

A minimal closed-loop system contains:

```text
1. something to control
2. a way to observe something about it
3. a rule for choosing an action
4. an actuator that applies the action
5. a feedback path from response to a later decision
```

For neural engineering:

```text
neural system
→ sensor
→ measurement
→ feature / estimate
→ decision rule
→ stimulation command
→ actuator
→ neural system
```

The circle is conceptual.

The physical signals can travel through electrodes, electronics, processors, wireless links, muscles, sensory pathways, or external devices.

---

## The plant

Control-system language often calls the system being influenced the **plant**.

In neural engineering the plant might include:

- a neural circuit;
- a brain region plus connected pathways;
- a peripheral nerve and muscle;
- the nervous system plus an assistive device;
- the person, prosthesis, and environment together.

The boundary must be stated.

A poor boundary can hide important feedback paths.

---

# Part III — Reference, output, error, and command

## Reference or goal

A controller needs some notion of desired behavior.

Examples include:

```text
keep a pathological biomarker below a threshold
maintain cursor velocity near the user's intended velocity
reduce seizure-like activity after detection
maintain a stimulation effect while limiting side effects
```

The reference is not necessarily a single number.

At L0, treat it as the desired condition against which the system decides what to do.

---

## Output

The **output** is the variable we care about observing or controlling.

Examples:

- estimated beta-band activity;
- detected seizure-like pattern;
- cursor position;
- muscle force;
- tremor amplitude.

The output may be directly measured or inferred through a proxy.

---

## Error

In a simple control model:

$$ e=r-y. $$

Here:

- $r$ is a desired reference;
- $y$ is the measured or estimated output;
- $e$ is their difference.

Not every neural controller literally computes this subtraction.

The equation is a mental model for the idea that the decision depends on how the current state differs from the desired state.

---

## Command

The controller converts information into a command.

A simple conceptual rule might be:

```text
if biomarker is below threshold:
    use low stimulation

if biomarker is above threshold:
    use stronger stimulation
```

Real systems can use richer rules, multiple biomarkers, hysteresis, state machines, predictive models, or learned policies.

Those details come later.

---

# Part IV — Sensing is not the same as feedback control

A device can sense neural activity while still operating open-loop.

Example:

```text
record neural signal
→ store for later analysis

fixed stimulation schedule
→ actuator
```

The recording does not alter the command.

Therefore the sensing path is observational, not a control feedback path.

To close the loop, the measured information must influence a later action inside the stated system boundary.

---

# Part V — Feedback can use a proxy rather than the true target state

## Biological target versus biomarker

Suppose the clinical goal is:

```text
improve movement
```

But the implanted device measures:

```text
local field-potential power in a selected frequency band
```

Those are not the same variable.

The measured feature is a **biomarker** or proxy used because the true desired state is not directly accessible at the required speed and location.

So the loop is really:

```text
biological state
→ measurement chain
→ biomarker estimate
→ controller
→ modulation chain
→ biological state
```

The controller acts on an estimate of the state, not on perfect biological truth.

---

## Proxy failure matters more in closed loop

In an open-loop experiment, a poor biomarker may produce a bad interpretation.

In a closed-loop system, a poor biomarker can also produce a bad action.

That changes the consequence:

```text
measurement error
→ decision error
→ actuation error
→ new biological response
```

The error can now circulate through the loop.

---

# Part VI — Example NNE-EX-050: fixed DBS versus adaptive DBS

Consider two simplified Parkinson's disease stimulation strategies.

## Fixed DBS

```text
clinician programs parameters
→ continuous or scheduled stimulation
→ neural system
```

The stimulation command does not change moment by moment according to the measured neural biomarker.

With respect to that biomarker, the system is open-loop.

---

## Adaptive DBS

A simplified adaptive design is:

```text
local field potential
→ estimate biomarker
→ compare with criterion
→ adjust stimulation
→ neural response
→ local field potential again
```

This is closed-loop with respect to the sensed biomarker because the measured feature influences later stimulation.

Adaptive DBS studies have demonstrated implementations in which neural activity is used to modify stimulation rather than maintaining one fixed command continuously.

The engineering lesson is broader than Parkinson's disease:

> a closed loop couples the measurement chain to the modulation chain through a decision rule.

---

# Part VII — Example NNE-EX-051: responsive neurostimulation for epilepsy

A responsive neurostimulation architecture can be simplified as:

```text
intracranial electrical activity
→ sensing electrodes
→ detection algorithm
→ detection of programmed electrocorticographic pattern
→ stimulation command
→ stimulation near seizure focus
→ continued sensing
```

This makes the feedback dependency explicit.

The system does not wait for a clinician to inspect every event before each stimulus.

A programmed detector links measured activity to responsive stimulation.

Important distinction:

```text
detected pattern
≠ seizure mechanism itself
```

The detector operates on a measurable feature selected as useful for control.

---

# Part VIII — Feedback timing

## A loop takes time

Every stage introduces delay:

```text
biology
→ sensing delay
→ filtering / windowing delay
→ feature computation
→ decision delay
→ command transmission
→ actuator delay
→ biological response delay
```

Call the total delay:

$$ \tau_{loop}. $$

If the phenomenon changes much faster than the loop can respond, feedback may arrive too late to be useful.

---

## Fast is not automatically better

Reducing latency can require tradeoffs:

- shorter feature windows can be noisier;
- faster updates consume more power;
- higher sampling rates generate more data;
- aggressive response rules can react to artifacts;
- wireless communication can add delay and energy cost.

So latency is one systems tradeoff, not the only objective.

This directly prepares the next lesson.

---

# Part IX — Noise and false decisions

Suppose a controller uses a threshold:

```text
if estimated biomarker > threshold:
    stimulate
```

Now imagine measurement noise briefly pushes the estimate above threshold even though the biological state has not meaningfully changed.

The result is:

```text
noise
→ false threshold crossing
→ unnecessary stimulation
```

The problem is no longer only measurement accuracy.

It is action selection under uncertain measurement.

---

## Hysteresis and persistence

One simple design idea is to require stronger evidence before switching states.

For example:

```text
turn stimulation on above a high threshold
turn stimulation off only below a lower threshold
```

Another idea is to require the condition to persist for a minimum duration.

These strategies reduce rapid switching caused by noise.

They also add delay.

Again, the design is a tradeoff.

---

# Part X — Example NNE-EX-052: artifact-driven feedback failure

Imagine a system that senses from an electrode while stimulation is occurring nearby.

The stimulation pulse produces a large electrical artifact in the recording.

Suppose the detector mistakes that artifact for the biological biomarker it is intended to control.

Then:

```text
stimulation
→ artifact
→ detector says "pathological activity"
→ controller increases stimulation
→ larger artifact
```

This is a dangerous conceptual pattern: **the actuator contaminates the sensor that controls the actuator**.

The exact engineering solution depends on the system, but possible strategies include:

- blanking or ignoring known stimulation intervals;
- improved sensing geometry;
- artifact rejection;
- independent sensing channels;
- controller rules that limit rapid escalation;
- hard safety bounds.

The important L0 lesson is:

> closing a loop creates new failure modes because actions can alter measurements as well as biology.

---

# Part XI — Stability as a systems idea

You do not need formal control theory yet.

At this level, **stability** means asking whether repeated feedback tends to keep the system in a useful bounded regime rather than causing growing oscillation, runaway action, or uncontrolled switching.

A crude conceptual example:

```text
controller sees error
→ overcorrects strongly
→ state crosses too far
→ controller reverses strongly
→ state crosses back too far
→ repeated oscillation
```

Feedback is therefore not automatically stabilizing.

Its sign, gain, delay, thresholds, and plant dynamics matter.

---

# Part XII — Positive and negative feedback intuition

## Negative-feedback intuition

Negative feedback acts in a direction intended to reduce deviation from a desired state.

Example conceptually:

```text
biomarker too high
→ stimulation change intended to lower it
```

This does not guarantee success.

It only describes the intended direction of correction.

---

## Positive-feedback intuition

Positive feedback reinforces a deviation.

In engineering, uncontrolled positive feedback can create runaway behavior.

But not every reinforcing biological process is an engineering mistake.

The important question is whether the loop behavior matches the system objective and remains safe.

---

# Part XIII — The controller is not the biology

A controller is an engineered decision mechanism.

It may contain:

- thresholds;
- lookup tables;
- finite-state rules;
- proportional rules;
- classifiers;
- predictive models;
- optimization algorithms;
- learned policies.

Do not confuse the controller's model with the neural mechanism.

A controller can work clinically even if its internal feature is only a useful proxy rather than a complete mechanistic explanation.

This repeats an important discipline from earlier lessons:

```text
model ≠ mechanism unless evidence supports the claim
```

---

# Part XIV — Human-in-the-loop systems

Not every closed loop is entirely inside implanted electronics.

Consider an assistive motor BCI:

```text
neural activity
→ decoder
→ cursor movement
→ user sees cursor
→ user changes neural strategy
→ new neural activity
```

The user is part of the feedback loop.

This reuses the systems idea introduced in `NNE-0001`.

The decoder does not simply read a fixed signal source.

User and decoder can adapt to each other over time.

---

# Part XV — Closed-loop relative to system boundary

Suppose a cochlear implant maps sound to stimulation using a fixed signal-processing strategy.

At one boundary:

```text
sound processor → stimulation
```

may be open-loop with respect to auditory-nerve feedback because the device does not measure the nerve to choose the next command.

But the person naturally uses sensory feedback to interpret and adapt behavior.

The broader human-environment system contains loops.

Therefore never label a complex technology simply:

```text
"closed-loop"
```

without stating the loop and boundary.

Prefer:

> closed-loop with respect to measured variable X and command Y inside boundary Z.

---

# Part XVI — Example NNE-EX-053: latency budget in a closed-loop cursor system

Suppose an assistive BCI aims to update a cursor every 50 ms.

A simplified timing budget might contain:

```text
neural feature window       20 ms
processing and decoding     10 ms
command communication        5 ms
device rendering             5 ms
remaining timing margin     10 ms
```

Total:

$$ 20+10+5+5+10=50\ \text{ms}. $$

Now suppose the feature window is lengthened to 60 ms to improve signal reliability.

The old 50 ms update requirement can no longer be satisfied without changing something else.

This is why closed-loop design is end-to-end.

A locally "better" signal-processing choice can violate the system-level feedback requirement.

---

# Part XVII — Safety supervisor

Clinical closed-loop systems should not let an unconstrained controller command arbitrary actuation.

A conceptual architecture is:

```text
controller proposal
→ safety supervisor
→ allowed command
→ actuator
```

Safety rules can limit:

- amplitude;
- pulse width;
- stimulation rate;
- duty cycle;
- charge or energy exposure;
- rate of parameter change;
- operating states;
- response to sensor failure.

The supervisor is not a substitute for clinical validation.

It is one layer in a safety architecture.

---

# Part XVIII — Fail-safe behavior

Ask:

> what should happen when the sensor fails?

Possible choices depend on risk:

- stop stimulation;
- revert to a known safe fixed setting;
- alert the user or clinician;
- disable only the adaptive component;
- enter a conservative mode.

A system is not fully designed until failure behavior is specified.

---

# Part XIX — Adaptation is not the same as feedback

A system can adapt parameters slowly based on historical data without responding moment by moment.

A system can also use immediate feedback without learning anything long term.

So separate:

```text
feedback:
current measurements influence later actions

adaptation:
parameters or policy change over time
```

They can coexist, but they are not synonyms.

---

# Part XX — Closed-loop does not automatically mean better

Closed-loop operation can offer potential advantages:

- act only when needed;
- tailor stimulation to state;
- reduce unnecessary actuation;
- respond to changing biomarkers;
- potentially reduce energy use or side effects.

But it adds requirements:

- reliable sensing;
- useful biomarkers;
- validated decision rules;
- bounded latency;
- artifact handling;
- computational power;
- additional verification;
- failure-safe behavior.

So the right engineering question is not:

> open-loop or closed-loop — which is better?

It is:

> which architecture meets the clinical or scientific objective under the real constraints?

---

# Part XXI — Three layers of validation

## 1. Measurement validation

Does the sensor and processing pipeline estimate the intended feature reliably?

## 2. Decision validation

Does the controller choose an appropriate action from that estimate?

## 3. End-to-end outcome validation

Does the complete loop produce useful and safe outcomes over relevant timescales?

Passing layer 1 does not guarantee layer 2.

Passing layer 2 in simulation does not guarantee layer 3 in people.

---

# Part XXII — Failure modes

## Failure mode 1: "There is a sensor, so the system is closed-loop"

False.

The sensor output must influence a later command inside the stated boundary.

---

## Failure mode 2: "Closed-loop means automatic"

Not necessarily.

A human can be part of the feedback path.

---

## Failure mode 3: "Feedback means the true biological state is known"

False.

The loop usually acts on measurements and estimates.

---

## Failure mode 4: "A correlated biomarker is automatically a good control signal"

False.

A useful control biomarker also needs sufficient reliability, timing, specificity, and robustness under intervention.

---

## Failure mode 5: "More controller gain means faster and therefore better control"

False.

Strong correction can amplify noise, overshoot, oscillate, or violate safety constraints.

---

## Failure mode 6: "Shorter latency is always better"

False.

Shorter windows can reduce feature reliability and increase sensitivity to noise.

---

## Failure mode 7: "The actuator only changes biology"

False.

Actuation can also change what the sensor measures, including through artifacts.

---

## Failure mode 8: "Closed-loop proves mechanism"

False.

A feedback controller can exploit a predictive biomarker without proving that biomarker is the unique causal mechanism of disease.

---

# Part XXIII — Active work

## Exercise 1 — classify the architecture

For each system, state whether it is open-loop or closed-loop **with respect to the named variable**.

1. DBS delivers fixed stimulation all day; no neural signal is sensed.
2. A device records neural activity but stores it only for next month's clinic visit while stimulation remains fixed.
3. A seizure detector triggers stimulation when a programmed intracranial pattern is detected.
4. A clinician changes stimulation monthly after reviewing symptoms.

State the system boundary and timescale for each answer.

---

## Exercise 2 — draw the loop

For adaptive DBS, label:

```text
plant
sensor
measured signal
biomarker
controller
command
actuator
feedback path
```

---

## Exercise 3 — proxy versus target

Suppose the clinical target is improved movement but the controller senses beta-band power.

Explain why:

```text
beta power
≠ movement itself
```

and list two ways this distinction could matter.

---

## Exercise 4 — artifact failure

A stimulation artifact causes a detector to fire falsely.

Trace the error through at least five stages of the loop.

Then propose two independent safety or signal-processing defenses.

---

## Exercise 5 — latency

A system has:

```text
30 ms feature window
8 ms processing
4 ms communication
3 ms actuator delay
```

What is the minimum loop latency before biological response delay is included?

Which stage would you change first, and what tradeoff might that create?

---

## Exercise 6 — human in the loop

Trace visual feedback in a cursor BCI from decoder output back to later neural activity generated by the user.

Why is the person part of the control system rather than just an external observer?

---

## Exercise 7 — fail-safe design

Choose one plausible response to loss of the biomarker signal in an implanted adaptive stimulator.

Explain why your response is safer than simply continuing arbitrary controller output.

---

## Exercise 8 — architecture decision

A treatment works well with stable fixed stimulation and the biomarker sensor is noisy and power hungry.

Give a reason why open-loop stimulation might remain the better engineering choice.

---

# Retrieval check

Without looking back:

1. What makes a system open-loop with respect to a variable?
2. What makes it closed-loop?
3. Why must the system boundary be stated?
4. Why can a system be open-loop on one timescale and closed-loop on another?
5. What is the plant?
6. What is a reference or desired state?
7. What is the role of a controller?
8. In the simple equation $e=r-y$, what are $r$, $y$, and $e$?
9. Why does sensing alone not close a loop?
10. What is a biomarker?
11. Why is a biomarker usually a proxy?
12. Why can measurement error be more consequential in closed-loop operation?
13. Trace the adaptive DBS loop.
14. Trace the responsive neurostimulation loop.
15. Why does total loop latency matter?
16. Why is shorter latency not the only objective?
17. How can noise create a false action?
18. What is hysteresis used for conceptually?
19. How can stimulation contaminate sensing?
20. What does stability mean at L0?
21. Why is feedback not automatically stabilizing?
22. What is the difference between feedback and adaptation?
23. Why is closed-loop not automatically better than open-loop?
24. What does a safety supervisor do?
25. Why must sensor-failure behavior be designed explicitly?
26. What are the three validation layers described here?
27. Why does successful control not prove one unique biological mechanism?
28. How can a human user be part of a neural-interface feedback loop?
29. What tradeoffs can arise when the feature window is shortened?
30. Which next lesson is prepared by the tradeoffs exposed here?

---

# Connection backward: NNE-0010

`NNE-0010` separated:

```text
command
actuator
field
biological target
response
outcome
```

This lesson adds a feedback dependency:

```text
response
→ measurement
→ estimate
→ decision
→ next command
```

The modulation chain still matters inside the loop.

Closing the loop does not remove uncertainty about field spread, target recruitment, side effects, or biological response.

It adds a new layer of decision making on top of those uncertainties.

---

# Connection backward: NNE-0009

`NNE-0009` taught:

```text
measurement
≠ biological truth
```

That distinction becomes operationally important here.

A closed-loop controller does not receive perfect neural state.

It receives a measured and processed estimate.

Therefore every limitation in the measurement chain can influence actuation decisions.

---

# Connection backward: NNE-0001

The first track lesson introduced the reusable loop:

```text
observe
→ infer
→ act
→ adapt
```

At that point it was a systems map.

Now you can identify the concrete engineering pieces that make such a loop open or closed.

---

# Connection to Linear Algebra

A simple controller or decoder may use a linear relation such as:

$$ \mathbf{u}=K\mathbf{x}. $$

Here:

- $\mathbf{x}$ can represent measured features;
- $K$ can represent an engineered linear rule;
- $\mathbf{u}$ can represent command variables.

Linear algebra helps describe that mapping.

But a matrix model does not prove that the nervous system itself is linear.

---

# Connection forward: NNE-N-0012

The next canonical lesson is:

`NNE-N-0012 — Resolution, selectivity, bandwidth, invasiveness, stability, and safety as coupled tradeoffs`.

This lesson has already exposed several coupled constraints:

```text
better temporal resolution
↔ more data / power / noise sensitivity

more sensing channels
↔ more bandwidth / hardware complexity

faster feedback
↔ shorter windows / potentially weaker estimates

more aggressive control
↔ faster response / potentially greater instability or side effects

more invasive sensing
↔ potentially richer signals / greater biological and surgical burden
```

The next lesson turns those tensions into an explicit design framework.

---

# What this unlocks

You should now be able to inspect a neural system and ask:

```text
What is the system boundary?
What variable is being controlled?
What is actually measured?
Is the measurement a proxy?
Does that measurement influence a later command?
What is the controller rule?
What is the actuator?
How long does the loop take?
How can noise or artifact change the decision?
What happens if the sensor fails?
What safety bounds constrain the controller?
Is the system stable enough for its intended use?
What is validated at component level versus end-to-end level?
```

That is the foundation for reasoning about neural interfaces as feedback systems rather than as disconnected sensors and stimulators.

---

# References

- **NNE-REF-004** — NIH BRAIN Initiative, *Neural Recording and Modulation*.
- **NNE-REF-009** — NIH BRAIN Initiative, *BRAIN 2.0 Neuroethics: Enabling and Enhancing Neuroscience Advances for Society*.
- **NNE-REF-012** — NIH BRAIN Initiative, *Therapeutic Human Neuroscience Program*.
- **NNE-REF-050** — Simon Little et al., “Adaptive deep brain stimulation in advanced Parkinson disease,” *Annals of Neurology* 74(3), 449–457 (2013). DOI: `10.1002/ana.23951`.
- **NNE-REF-051** — Gregory K. Bergey et al., “Long-term treatment with responsive brain stimulation in adults with refractory partial seizures,” *Neurology* 84(8), 810–817 (2015). DOI: `10.1212/WNL.0000000000001280`.
- **NNE-REF-052** — Ro'ee Gilron et al., “Long-term wireless streaming of neural recordings for circuit discovery and adaptive stimulation in individuals with Parkinson's disease,” *Nature Biotechnology* 39, 1078–1085 (2021). DOI: `10.1038/s41587-021-00897-5`.
