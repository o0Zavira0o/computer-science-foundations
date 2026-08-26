---
id: PHL-0004
title: "Truth, validity, and soundness"
track: philosophy-and-logic
level: L0
status: complete
curriculum_node: PHL-N-0004
concepts_introduced: ["PHL-C-0004"]
concepts_deepened: ["PHL-C-0003"]
concepts_used: ["PHL-C-0001", "PHL-C-0002"]
examples_added: ["PHL-EX-010", "PHL-EX-011", "PHL-EX-012", "PHL-EX-013", "PHL-EX-014"]
references_used: ["PHL-REF-003", "PHL-REF-004", "PHL-REF-007"]
last_reviewed: 2026-08-26
version_sensitive: false
review_after: null
---
# PHL-0004 — Truth, validity, and soundness

## If you landed here directly

The direct prerequisite is [`PHL-0003 — Premises, conclusions, and argument indicators`](PHL-0003-premises-conclusions-and-argument-indicators.md).

You should already be able to:

- identify the conclusion an argument is trying to support;
- identify explicit premises;
- distinguish argument indicators from mechanical rules;
- rewrite a short argument into premise–conclusion form.

This lesson asks a new question:

> once we know what the premises and conclusion are, how do we evaluate a deductive argument without mixing together three different issues?

Those three issues are:

1. whether particular claims are true;
2. whether the conclusion follows from the premises;
3. whether the argument combines good logical structure with true premises.

The corresponding ideas are **truth**, **validity**, and **soundness**.

---

## The problem worth understanding

Consider:

1. All squares are rectangles.
2. All rectangles have four sides.
3. Therefore, all squares have four sides.

This looks good in more than one way.

The premises are true.

The conclusion is true.

And the conclusion follows from the premises.

Now consider:

1. All planets are made of glass.
2. Earth is a planet.
3. Therefore, Earth is made of glass.

Something is wrong.

But **what** is wrong?

The inferential pattern is still structurally strong:

```text
All A are B.
x is A.
Therefore, x is B.
```

If both premises were true, the conclusion could not be false.

The defect is not the inference.

The defect is that a premise is false.

That distinction is the reason logic needs separate vocabulary.

---

## Three questions, not one

When evaluating a deductive argument, ask:

### Question 1 — Are the premises true?

This concerns the truth values of the premises.

### Question 2 — If the premises were true, would the conclusion have to be true?

This concerns validity.

### Question 3 — Is the argument valid and are its premises in fact true?

This concerns soundness.

Do not collapse these into:

> “Is the argument good?”

That phrase hides several logically distinct questions.

---

## Truth belongs to claims

A proposition or statement can be true or false.

For example:

> Paris is in France.

is true.

> Paris is in Japan.

is false.

At this level, truth is a property of the claim being asserted.

Arguments are different objects.

An argument contains premises offered in support of a conclusion.

We therefore need vocabulary for the **support relation** between those claims.

---

## Validity belongs to deductive arguments

A deductive argument is **valid** when it is impossible for all its premises to be true while its conclusion is false.

Equivalent beginner-friendly wording:

> if the premises were all true, the conclusion would have to be true.

Validity does **not** initially ask whether the premises actually are true.

It asks what follows **under the assumption** that they are true.

That conditional perspective is central.

---

## The forbidden pattern for a valid argument

A valid deductive argument cannot have this combination:

| Premises | Conclusion |
|---|---|
| all true | false |

That is the one truth-status pattern validity rules out.

If you can produce even one coherent case in which all the premises are true and the conclusion is false, the argument is invalid.

Later lessons will turn that idea into more formal countermodels and truth-table methods.

---

## Validity is not the same as having a true conclusion

A conclusion can be true for reasons that have nothing to do with the premises.

Consider:

1. Paris is in France.
2. $2+2=4$.
3. Therefore, Earth orbits the Sun.

All three statements are true.

But the premises do not logically force the conclusion.

The argument is invalid.

A true conclusion does not repair a broken inference.

---

## Validity is not the same as having true premises

The same example also shows:

- premise 1 is true;
- premise 2 is true;
- conclusion is true;
- the argument is still invalid.

Truth of the individual claims and validity of the inferential connection are different dimensions of evaluation.

---

## Worked example PHL-EX-010 — true premises plus valid inference

Consider:

1. Every square is a rectangle.
2. Every rectangle has four sides.
3. Therefore, every square has four sides.

### Truth check

Premise 1 is true.

Premise 2 is true.

### Validity check

If both premises are true, there is no possible square that could fail to have four sides while those premises remain true.

So the inference is valid.

### Soundness check

The argument is valid and its premises are true.

Therefore it is sound.

This is the ideal deductive case.

---

## Soundness

A deductive argument is **sound** exactly when:

1. it is valid;
2. every premise is true.

In compact form:

```text
sound = valid + true premises
```

Because a valid argument cannot have true premises and a false conclusion, a sound argument must have a true conclusion.

That does **not** mean soundness is defined as:

> “an argument with a true conclusion.”

The conclusion's truth is a consequence of soundness, not its definition.

---

## Worked example PHL-EX-011 — valid but unsound

Consider:

1. Every planet is made of glass.
2. Earth is a planet.
3. Therefore, Earth is made of glass.

The pattern is:

```text
All A are B.
x is A.
Therefore, x is B.
```

If the premises were true, the conclusion would have to be true.

So the argument is valid.

But premise 1 is false.

Therefore the argument is unsound.

The failure is **premise truth**, not validity.

---

## A valid argument can contain false premises

This often feels strange at first.

Students sometimes think:

> “If a premise is false, the argument must be invalid.”

No.

Validity asks about what follows **if** the premises are true.

It does not certify their actual truth.

This separation lets logic study inferential structure without pretending that logic alone can settle every factual question.

---

## Worked example PHL-EX-012 — true statements do not guarantee validity

Consider:

1. Paris is in France.
2. $2+2=4$.
3. Therefore, Earth orbits the Sun.

Each claim is true.

But imagine a situation in which premises 1 and 2 remain true while the conclusion is false.

There is no contradiction in the premises themselves that forces Earth's orbit.

So the premises do not entail the conclusion.

The argument is invalid.

This example is deliberately obvious because it isolates the logical point:

> truth can line up accidentally without inferential support.

---

## A valid argument may have a true conclusion even when its premises are false

Consider:

1. All birds are mammals.
2. All whales are birds.
3. Therefore, all whales are mammals.

Premise 1 is false.

Premise 2 is false.

The conclusion is true.

Yet the argument form is valid:

```text
All A are B.
All C are A.
Therefore, all C are B.
```

If the two premises were true, the conclusion would have to be true.

So we have:

- false premises;
- true conclusion;
- valid inference;
- unsound argument.

This is another reason you cannot classify validity by looking only at actual truth values.

---

## Worked example PHL-EX-013 — valid, unsound, true conclusion

Using the argument:

1. All birds are mammals.
2. All whales are birds.
3. Therefore, all whales are mammals.

we can classify each layer.

| Question | Answer |
|---|---|
| Are all premises true? | No |
| Is the conclusion true? | Yes |
| Is the inference valid? | Yes |
| Is the argument sound? | No |

The table contains an important lesson:

> valid does not mean true-premised, and true conclusion does not mean sound.

---

## Invalidity needs only one countercase

To show that a deductive argument is invalid, you do not need to list every possible failure.

You need one case with:

- all premises true;
- conclusion false.

That single countercase proves that the premises do not logically guarantee the conclusion.

This idea becomes a major tool in later logic.

---

## Worked example PHL-EX-014 — finding a countercase

Consider:

1. If a whole number is divisible by $4$, then it is even.
2. $6$ is even.
3. Therefore, $6$ is divisible by $4$.

Premise 1 is true.

Premise 2 is true.

The conclusion is false.

We have directly found the forbidden validity pattern:

| Premises | Conclusion |
|---|---|
| true | false |

Therefore the argument is invalid.

Notice how decisive this is.

We do not need to say the argument merely “feels weak.”

The truth pattern itself demonstrates failure of deductive guarantee.

---

## Validity concerns guarantee, not probability

Suppose an argument makes its conclusion highly likely but not certain.

That may be excellent reasoning.

But if the argument is intended as deductive, “highly likely” is not enough for validity.

Deductive validity is all-or-nothing in this sense:

> there is no possible case with all true premises and a false conclusion.

Later, the track distinguishes deduction from induction and abduction.

Those ampliative forms of reasoning are not defective merely because they lack deductive guarantee.

They are evaluated differently.

---

## Validity is not persuasiveness

An argument can be psychologically persuasive and logically invalid.

An argument can also be logically valid and psychologically unconvincing.

Persuasiveness can depend on:

- rhetoric;
- framing;
- prior beliefs;
- emotional response;
- trust in the speaker;
- familiarity;
- social context.

Validity is narrower.

It concerns the inferential relation between premises and conclusion.

---

## Validity is not importance

A valid argument can concern something trivial.

An invalid argument can concern something morally urgent.

Logical validity does not rank the importance of topics.

It evaluates a specific inferential property.

This distinction matters because logical vocabulary should not become a general-purpose compliment.

---

## Do not call a statement “valid”

In ordinary conversation, people sometimes say:

> “Your point is valid.”

That can mean reasonable, acceptable, or worthy of consideration.

In deductive logic, we use terminology more precisely.

Usually:

- statements are true or false;
- deductive arguments are valid or invalid;
- deductive arguments are sound or unsound.

Keeping these categories separate prevents confusion.

---

## Do not call an argument “true”

Similarly, saying:

> “This argument is true”

mixes levels.

The premises and conclusion can be true or false.

The argument can be valid or invalid.

And a deductive argument can be sound or unsound.

Precision in the nouns helps precision in the reasoning.

---

## A diagnostic grid

For a deductive argument, these combinations are possible:

| Validity | Premises | Sound? | What can we say about conclusion? |
|---|---|---|---|
| valid | all true | yes | must be true |
| valid | one or more false | no | may be true or false |
| invalid | all true | no | may be true or false |
| invalid | one or more false | no | may be true or false |

The key row is the first one.

Only validity plus true premises gives the soundness guarantee.

---

## Why soundness matters philosophically

Philosophical reasoning often involves two different jobs.

### Job 1 — inferential evaluation

Does the conclusion follow from the premises?

### Job 2 — premise evaluation

Should we accept the premises?

Logic helps with the first job.

The second can require:

- conceptual analysis;
- empirical evidence;
- ethical argument;
- epistemology;
- metaphysics;
- philosophy of science;
- interpretation of texts;
- further argument.

A sound philosophical argument needs both jobs to succeed.

---

## A valid argument can still be useless

Suppose:

1. If consciousness is entirely physical, then consciousness is entirely physical.
2. Consciousness is entirely physical.
3. Therefore, consciousness is entirely physical.

The inference may be trivially valid, but it gives no independent reason for someone who doubts the key premise.

Validity does not guarantee:

- informativeness;
- non-circularity;
- dialectical usefulness;
- relevance to an opponent's concerns.

Those are additional standards.

---

## Soundness is powerful but demanding

To establish soundness, you must establish two things:

1. validity;
2. truth of every premise.

In real philosophy, premise truth is often the hard part.

That is why philosophical disagreement can remain even after people agree on the logical structure.

They may dispute:

- definitions;
- background assumptions;
- evidence;
- modal claims;
- moral principles;
- causal claims;
- conceptual commitments.

Logic organizes the disagreement.

It does not automatically eliminate it.

---

## Formal structure and ordinary language

At L0, we can often judge simple validity by understanding the meaning and structure of the claims.

Later, formal logic will make the structure explicit with symbolic languages.

That formalization helps us distinguish:

- logical form;
- content;
- semantics;
- proof rules.

But formalization also requires care.

Ordinary language contains ambiguity, context, and pragmatic meaning.

So “extract the form” is itself an analytical task.

---

## A useful evaluation workflow

When facing a deductive argument:

1. identify the conclusion;
2. identify the premises;
3. clarify ambiguous claims;
4. ask whether all premises could be true while the conclusion is false;
5. if yes, classify the argument as invalid;
6. if no, classify it as valid;
7. separately investigate whether each premise is actually true;
8. if valid and all premises are true, classify it as sound;
9. do not infer premise truth merely from validity;
10. do not infer validity merely from a true conclusion.

This workflow keeps structural and factual evaluation separate.

---

## Failure mode: “the conclusion is false, so the argument is invalid”

Not necessarily.

A valid argument can have a false conclusion when at least one premise is false.

Example:

1. All planets are glass.
2. Earth is a planet.
3. Therefore Earth is glass.

The conclusion is false.

The argument is still valid.

Its problem is unsoundness.

---

## Failure mode: “the conclusion is true, so the argument is valid”

No.

Example:

1. Paris is in France.
2. $2+2=4$.
3. Therefore Earth orbits the Sun.

The conclusion is true.

The argument is invalid.

Truth of the conclusion does not establish inferential support.

---

## Failure mode: “a false premise makes an argument invalid”

No.

False premises can occur inside valid arguments.

Validity asks what follows from the premises under the supposition that they are true.

Soundness is the concept that additionally demands true premises.

---

## Failure mode: “valid means convincing”

No.

Validity is a logical property.

Persuasiveness is psychological and rhetorical.

A person may fail to be convinced by a valid argument because they reject a premise.

That does not by itself show invalidity.

---

## Failure mode: “sound means the conclusion happens to be true”

No.

A sound argument is:

- valid;
- based entirely on true premises.

A true conclusion reached by an invalid route does not make the argument sound.

---

## Failure mode: treat validity as a label you can see from wording

Indicator words such as:

- therefore;
- because;
- since;
- thus;

can help identify argument structure.

They do not determine validity.

Validity depends on the inferential relationship, not the presence of vocabulary.

This connects directly back to `PHL-0003`.

---

## Active work

### Exercise 1 — classify the property

For each item, say whether the relevant property is truth, validity, or soundness.

A. “The premise `7 is prime` is correct.”

B. “There is no case in which these premises are all true and the conclusion false.”

C. “The argument is valid and every premise is true.”

### Exercise 2 — valid or invalid

1. All dogs are mammals.
2. Luna is a dog.
3. Therefore Luna is a mammal.

Classify validity first.

Then ask what additional facts you would need for soundness.

### Exercise 3 — false premise

1. All metals are transparent.
2. Iron is a metal.
3. Therefore iron is transparent.

Is the argument valid?

Is it sound?

### Exercise 4 — accidental true conclusion

1. Rome is in Italy.
2. Water contains hydrogen.
3. Therefore $11$ is prime.

All three claims are true.

Does that make the argument valid?

Explain.

### Exercise 5 — find the forbidden pattern

Can a valid deductive argument have:

- all true premises;
- a false conclusion?

Explain using the definition of validity.

### Exercise 6 — valid but unsound with true conclusion

Construct your own argument that has:

- a valid form;
- at least one false premise;
- a true conclusion.

Then explain why the true conclusion does not make it sound.

### Exercise 7 — premise dispute versus logic dispute

Two people agree that:

```text
If P, then Q.
P.
Therefore Q.
```

is valid, but they disagree about whether $P$ is true.

Are they disagreeing about validity or soundness?

Be precise.

### Exercise 8 — countercase

Give one case showing that this pattern is invalid:

```text
If P, then Q.
Q.
Therefore P.
```

Your case must make both premises true and the conclusion false.

---

## Retrieval check

Without looking back:

1. What kinds of things are true or false?
2. What kinds of things are valid or invalid?
3. What is deductive validity?
4. What truth-value combination is impossible for a valid argument?
5. Can a valid argument have a false premise?
6. Can a valid argument have a false conclusion?
7. Under what condition can that happen?
8. What is soundness?
9. Why must a sound argument have a true conclusion?
10. Can an invalid argument have a true conclusion?
11. Why does a true conclusion not prove validity?
12. What does one true-premises/false-conclusion countercase establish?
13. Why are premise evaluation and inference evaluation separate jobs?
14. Why should validity not be confused with persuasiveness?

---

## Connections

### Backward: PHL-0003

`PHL-0003` identified premises and conclusions.

This lesson asks how to evaluate the relation between them.

You cannot reliably judge validity until you know which claims are supposed to support which conclusion.

### Forward: PHL-N-0005

The next sequential core lesson distinguishes:

- deduction;
- induction;
- abduction.

This lesson gives the benchmark for deductive support: guarantee rather than mere probability.

### Forward branch: PHL-N-0006

`PHL-N-0006` develops counterexamples more directly.

The seed has already appeared here:

> one true-premises/false-conclusion case is enough to refute deductive validity.

### Long-range: formal logic

Later lessons formalize validity with:

- truth-functional semantics;
- valuations;
- truth tables;
- proof systems;
- first-order interpretations.

The notation becomes more rigorous.

The core idea remains the same.

### Long-range: epistemology

Much later, epistemology asks questions about:

- truth;
- belief;
- justification;
- knowledge.

The word “truth” will then appear in a broader philosophical setting.

Do not confuse those epistemic questions with deductive validity.

---

## What this unlocks

You should now be able to:

- distinguish truth from validity;
- distinguish validity from soundness;
- state the definition of deductive validity;
- explain why false premises do not automatically imply invalidity;
- explain why a true conclusion does not prove validity;
- classify valid-but-unsound arguments;
- identify the truth-pattern that refutes validity;
- explain why sound arguments guarantee true conclusions;
- separate premise evaluation from inference evaluation;
- avoid using `true`, `valid`, and `sound` as interchangeable compliments.

---

## References

- **PHL-REF-003** — MIT OpenCourseWare, *Logic I*.
- **PHL-REF-004** — The Open Logic Project.
- **PHL-REF-007** — Stanford Encyclopedia of Philosophy, *Classical Logic*.
