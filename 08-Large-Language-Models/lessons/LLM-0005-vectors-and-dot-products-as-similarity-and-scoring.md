---
id: LLM-0005
title: "Vectors and dot products as similarity and scoring"
track: large-language-models
level: L0
status: complete
curriculum_node: LLM-N-0005
concepts_introduced: ["LLM-C-0005"]
concepts_deepened: ["LLM-C-0004"]
concepts_used: ["LLM-C-0001", "LLM-C-0002", "LLM-C-0003"]
examples_added: ["LLM-EX-015", "LLM-EX-016", "LLM-EX-017", "LLM-EX-018", "LLM-EX-019"]
references_used: ["LLM-REF-023", "LLM-REF-024", "LLM-REF-025"]
last_reviewed: 2026-08-26
version_sensitive: false
review_after: null
---
# LLM-0005 — Vectors and dot products as similarity and scoring

## If you landed here directly

The direct prerequisite is [`LLM-0004 — Logits, softmax, and categorical prediction`](LLM-0004-logits-softmax-and-categorical-prediction.md).

You should already understand that:

- a language model can produce one real-valued logit for each candidate token;
- logits are not probabilities;
- softmax converts competing logits into a categorical probability distribution;
- relative score differences matter more than a common additive offset.

This lesson asks:

> where can useful scores come from?

We start with one of the most important mechanisms in machine learning:

> represent things with vectors, then combine vectors with dot products to produce scalar scores.

The lesson stays deliberately small.

We are not yet building a Transformer.

We are building the mathematical object that later appears inside:

- linear layers;
- output projections;
- embedding comparisons;
- attention scores;
- recommendation systems;
- retrieval systems.

---

## The problem worth understanding

Suppose a model has one representation of the current context and one representation associated with a candidate output.

We want a single number answering:

> how strongly do these two representations interact under the chosen coordinate system?

A vector gives us several numerical coordinates.

A dot product collapses two same-sized vectors into one scalar.

That scalar can act as:

- a weighted sum;
- a compatibility score;
- a ranking score;
- part of a logit;
- under additional assumptions, a similarity measure.

The phrase **under additional assumptions** matters.

A large dot product does not automatically mean two objects are semantically similar.

We will make the assumptions explicit.

---

## A vector is an ordered list of numbers

At this level, a vector can be written as:

$$ x=[x_1,x_2,\ldots,x_d]. $$

The number $d$ is the vector's dimension.

For example:

$$ x=[2,-1,3] $$

is a three-dimensional vector.

The coordinates are ordered.

So:

$$ [2,-1,3] $$

is not the same vector as:

$$ [-1,2,3]. $$

The coordinate positions matter because each position participates in operations with the corresponding position of another vector.

---

## Coordinates need a shared meaning or learned geometry

Suppose:

$$ x=[2,-1,3] $$

and:

$$ y=[4,0,1]. $$

We can mechanically compute a dot product.

But interpretation depends on what the coordinates represent.

In a hand-designed feature system, coordinates might mean:

```text
feature 1
feature 2
feature 3
```

In a learned neural representation, individual coordinates may not have simple human-readable meanings.

The vector still has mathematical structure.

But do not assume every coordinate corresponds to a named semantic concept.

---

## Shape compatibility comes first

A basic dot product combines two vectors of the same dimension.

For:

$$ x=[x_1,x_2,\ldots,x_d] $$

and:

$$ y=[y_1,y_2,\ldots,y_d], $$

the dot product is:

$$ x\cdot y=\sum_{i=1}^{d}x_i y_i. $$

If one vector has dimension $3$ and the other dimension $5$, the ordinary coordinatewise dot product is not defined.

This shape constraint will later become a practical tensor-programming rule.

---

## Dot product means multiply corresponding coordinates, then add

For:

$$ x=[x_1,x_2,x_3] $$

and:

$$ y=[y_1,y_2,y_3], $$

compute:

$$ x\cdot y=x_1y_1+x_2y_2+x_3y_3. $$

Two steps:

1. multiply matching coordinates;
2. sum the products.

That is the entire arithmetic rule.

Its power comes from how broadly that rule can be interpreted.

---

## Worked example LLM-EX-015 — dot product by hand

Take:

$$ x=[2,-1,3] $$

and:

$$ y=[4,0,1]. $$

Coordinatewise products are:

$$ 2\cdot4=8, $$

$$ (-1)\cdot0=0, $$

and:

$$ 3\cdot1=3. $$

Add them:

$$ x\cdot y=8+0+3=11. $$

The output is not another three-dimensional vector.

It is one scalar:

$$ 11. $$

This vector-to-scalar operation is exactly why dot products are useful for scoring.

---

## Dot product as a weighted sum

Let:

$$ x=[x_1,x_2,\ldots,x_d] $$

represent values.

Let:

$$ w=[w_1,w_2,\ldots,w_d] $$

represent weights.

Then:

$$ w\cdot x=w_1x_1+w_2x_2+\cdots+w_dx_d. $$

That is a weighted sum.

A linear scoring model can therefore produce:

$$ s=w\cdot x+b, $$

where $b$ is a bias.

This pattern appears throughout machine learning.

---

## Worked example LLM-EX-016 — a tiny scoring rule

Suppose an object has feature vector:

$$ x=[1,2,-1]. $$

A scoring vector is:

$$ w=[2,0.5,-3]. $$

Compute:

$$ w\cdot x=(2)(1)+(0.5)(2)+(-3)(-1). $$

Therefore:

$$ w\cdot x=2+1+3=6. $$

If the bias is:

$$ b=-1, $$

then:

$$ s=w\cdot x+b=5. $$

The vector $w$ defines how each coordinate contributes to the score.

Positive and negative weights can reward or penalize different directions in the representation.

---

## Dot products can compare two representations

Suppose we have:

- a context vector $h$;
- a candidate vector $v$.

We can compute:

$$ s=h\cdot v. $$

A larger score may be interpreted as greater compatibility.

This is especially natural when the vectors were learned so that dot products are useful for the task.

But this interpretation is not automatic from algebra alone.

The training objective and representation geometry matter.

---

## The geometric view

For nonzero vectors $x$ and $y$:

$$ x\cdot y=\lVert x\rVert\lVert y\rVert\cos\theta, $$

where:

- $\lVert x\rVert$ is the length of $x$;
- $\lVert y\rVert$ is the length of $y$;
- $\theta$ is the angle between them.

So the dot product depends on two things:

1. vector lengths;
2. directional alignment.

That gives a useful geometric mental model.

---

## What the sign tells you geometrically

For nonzero vectors:

### Positive dot product

If:

$$ x\cdot y>0, $$

the angle is less than $90^\circ$.

The vectors point partly in the same direction.

### Zero dot product

If:

$$ x\cdot y=0, $$

the vectors are perpendicular in Euclidean geometry.

### Negative dot product

If:

$$ x\cdot y<0, $$

the angle is greater than $90^\circ$.

The vectors point partly in opposing directions.

These statements concern the geometry of the vectors.

Semantic interpretation requires an additional learned or designed mapping from objects to those vectors.

---

## Worked example LLM-EX-017 — zero interaction in a toy geometry

Take:

$$ a=[1,1] $$

and:

$$ b=[1,-1]. $$

Then:

$$ a\cdot b=(1)(1)+(1)(-1)=0. $$

Geometrically, the two vectors are perpendicular.

But do not jump directly to:

> “The represented concepts are unrelated.”

That conclusion would require knowing how the representation space was constructed.

The algebra tells us the dot product is zero.

The model design tells us what that means for the task.

---

## Dot product is not the same as cosine similarity

Because:

$$ x\cdot y=\lVert x\rVert\lVert y\rVert\cos\theta, $$

a dot product grows when vector magnitudes grow, even if the angle stays the same.

Cosine similarity removes the magnitude terms:

$$ \mathrm{cosine}(x,y)=\frac{x\cdot y}{\lVert x\rVert\lVert y\rVert}. $$

For nonzero vectors, cosine similarity focuses on directional alignment.

The dot product combines direction and magnitude.

---

## Why magnitude can matter

Suppose two candidate vectors point in almost the same direction as a query.

One candidate has much larger norm.

Its dot product with the query can be much larger.

That may be desirable if norm encodes something useful.

It may be undesirable if you intended to compare only direction.

So “use dot product for similarity” is a modeling choice, not a universal law.

---

## Worked example LLM-EX-018 — dot product and cosine rank differently in strength

Let:

$$ q=[1,0]. $$

Candidate A:

$$ a=[2,0]. $$

Candidate B:

$$ b=[1,1]. $$

Dot products:

$$ q\cdot a=2 $$

and:

$$ q\cdot b=1. $$

So dot-product scoring prefers A.

Now compare direction.

Vector A points exactly in the same direction as $q$.

Its cosine similarity with $q$ is:

$$ 1. $$

Vector B forms a $45^\circ$ angle with $q$.

Its cosine similarity is approximately:

$$ \frac{1}{\sqrt{2}}\approx0.707. $$

Here both measures prefer A, but for different numerical reasons.

The example makes the decomposition visible:

- dot product sees alignment and magnitude;
- cosine removes magnitude.

---

## Scaling one vector changes dot-product scores

Suppose:

$$ x\cdot y=3. $$

If we replace $y$ by:

$$ 10y, $$

then:

$$ x\cdot(10y)=30. $$

The direction of $y$ did not change.

Its magnitude did.

So the dot product changed by a factor of $10$.

Cosine similarity would remain unchanged for positive scaling.

This is the most important warning against equating raw dot product with pure angular similarity.

---

## Normalized vectors make dot product equal cosine similarity

If both nonzero vectors are normalized to unit length:

$$ \lVert x\rVert=1 $$

and:

$$ \lVert y\rVert=1, $$

then:

$$ x\cdot y=\cos\theta. $$

In that special case, dot product and cosine similarity are the same number.

Normalization therefore changes the interpretation of dot-product scoring.

---

## From one score to many candidate scores

Suppose a context representation is:

$$ h\in\mathbb{R}^d. $$

Suppose each candidate token $t$ has a scoring vector:

$$ w_t\in\mathbb{R}^d. $$

A simple token score can be:

$$ z_t=h\cdot w_t+b_t. $$

The result $z_t$ is a scalar.

If we compute one such scalar for every token, we obtain a vector of logits.

That directly connects this lesson to `LLM-0004`.

---

## Worked example LLM-EX-019 — dot products become logits

Let the context vector be:

$$ h=[2,1]. $$

Candidate A has:

$$ w_A=[1,0],\qquad b_A=0. $$

Candidate B has:

$$ w_B=[0,2],\qquad b_B=-0.5. $$

Compute candidate A:

$$ z_A=h\cdot w_A+b_A=(2)(1)+(1)(0)+0=2. $$

Compute candidate B:

$$ z_B=h\cdot w_B+b_B=(2)(0)+(1)(2)-0.5=1.5. $$

The model has produced logits:

$$ z=[2,1.5]. $$

Softmax can then convert those logits into probabilities.

The conceptual pipeline is:

```text
context representation
        ↓
dot-product or linear scores
        ↓
logits
        ↓
softmax
        ↓
categorical probabilities
```

This is a mechanism, not a slogan.

---

## A bias changes the score without changing vector alignment

In:

$$ s=w\cdot x+b, $$

the bias $b$ is an additive offset.

It is not part of the dot product unless we deliberately augment the vectors with an extra coordinate.

The bias can shift a candidate's score even when the vector interaction stays unchanged.

So a complete linear score is not always pure similarity.

---

## Symmetry is another warning sign

The ordinary real dot product is symmetric:

$$ x\cdot y=y\cdot x. $$

But many learned relationships are not conceptually symmetric.

For example:

> “context predicts token”

is not necessarily the same relationship as:

> “token predicts context.”

Models can introduce separate transformations, biases, or roles for the two sides.

Therefore, even when a dot product appears inside a model, the overall scoring mechanism need not be symmetric.

---

## Vectors can encode features, states, or learned representations

A vector might represent:

- hand-designed numeric features;
- measurements;
- model parameters;
- hidden activations;
- a token representation;
- a sentence representation;
- a query;
- a candidate;
- a direction in parameter space.

The arithmetic is shared.

The semantics depend on the system.

This is why “a vector is a list of numbers” is necessary but not sufficient.

---

## Coordinate axes are part of the representation

Suppose:

$$ x=[3,1]. $$

If coordinate 1 means “feature A” and coordinate 2 means “feature B,” swapping them changes the represented object:

$$ [1,3]. $$

A dot product assumes corresponding coordinates are comparable.

You cannot safely dot arbitrary numeric lists merely because they have the same length.

The shared coordinate system is part of the model.

---

## Dot product versus distance

Similarity and distance answer related but different questions.

A Euclidean distance between $x$ and $y$ is:

$$ \lVert x-y\rVert. $$

Small distance usually means nearby points.

Large dot product can arise from:

- strong directional alignment;
- large norms;
- both.

So nearest-by-distance and highest-dot-product need not select the same candidate.

Later systems choose metrics based on the task.

---

## Dot product does not create probability by itself

A dot product can produce any real score.

For example:

$$ x\cdot y=-7.2. $$

That is allowed.

It is not a negative probability.

To obtain a categorical probability distribution over competing candidates, we need a normalization mechanism such as softmax.

This is exactly the distinction from `LLM-0004`:

- dot product can help produce logits;
- softmax turns logits into probabilities.

---

## Dot product does not make semantics by itself

You can assign random vectors to words and compute dot products.

The arithmetic will still work.

But the scores will not automatically encode useful linguistic relationships.

Useful geometry comes from:

- training objectives;
- data;
- architecture;
- constraints;
- normalization;
- optimization.

The mathematical operation provides capacity.

Learning gives it task-specific meaning.

---

## Same dimension does not guarantee meaningful comparison

These two vectors both have length three:

```text
[height, temperature, age]
[redness, price, battery level]
```

A dot product is numerically computable if you encode them as numbers.

But the coordinate systems do not match conceptually.

Meaningful vector operations require compatible representations.

This point becomes easy to forget once everything is stored as tensors.

---

## Common failure mode: treat a vector as an unordered bag

Wrong idea:

```text
[1,2,3] = [3,2,1]
```

No.

Coordinates have positions.

Reordering coordinates changes the vector unless you simultaneously redefine the coordinate system.

---

## Common failure mode: multiply two vectors elementwise and stop

The elementwise products are intermediate values.

For a dot product, you must sum them.

Example:

$$ [2,3]\cdot[4,5]=(2)(4)+(3)(5)=23. $$

The answer is:

$$ 23, $$

not:

$$ [8,15]. $$

---

## Common failure mode: assume large dot product means small angle

A large dot product can come from large magnitudes.

If you care only about angle, normalize the vectors or use cosine similarity.

Always ask what the metric is intended to encode.

---

## Common failure mode: zero dot product means “no semantic relationship”

Zero dot product means orthogonality in the represented geometry.

Whether that corresponds to semantic unrelatedness depends on how the representation was learned or designed.

Do not convert geometry into semantics without a modeling argument.

---

## Common failure mode: dot product output is already a probability

No.

A dot product is a scalar score.

Scores can be negative or arbitrarily large.

A probability distribution requires appropriate normalization.

---

## Common failure mode: a single coordinate must have a human-readable meaning

Learned vector spaces can distribute information across many coordinates.

A coordinate may not correspond cleanly to one named concept.

Interpretability is a separate problem.

---

## Common failure mode: dot-product scoring must be symmetric in the whole model

The primitive operation is symmetric for real vectors.

But the model can put different transformations on the two sides.

For example:

```text
score(context, token) = transformed_context · token_vector + bias
```

The full system need not represent a symmetric relationship.

---

## A practical scoring workflow

When you see vector scoring in an ML system:

1. identify what each vector represents;
2. check that dimensions match;
3. identify whether both vectors live in a compatible coordinate space;
4. compute the dot product as multiply-then-sum;
5. check whether a bias is added;
6. ask whether vector norms are intended to matter;
7. if not, check whether normalization or cosine similarity is used;
8. distinguish the scalar score from a probability;
9. if probabilities are needed, identify the normalization step;
10. interpret semantics only in light of the training objective and model design.

---

## A tiny implementation intuition

For one-dimensional tensors, a library call such as PyTorch's dot-product operation computes the same mathematics:

```text
sum of coordinatewise products
```

The important conceptual rule is independent of framework.

Framework APIs matter later because shape mistakes can silently become model bugs.

At this stage, understand the operation before memorizing syntax.

---

## Active work

### Exercise 1 — compute a dot product

Compute:

$$ [3,-2,1]\cdot[4,5,-1]. $$

Show the coordinatewise products before summing.

### Exercise 2 — shape check

Can you take the ordinary dot product of:

$$ [1,2,3] $$

and:

$$ [4,5]? $$

Explain.

### Exercise 3 — weighted score

Let:

$$ x=[2,1,4] $$

and:

$$ w=[0.5,-1,2]. $$

Compute:

$$ w\cdot x. $$

Then add bias:

$$ b=-2. $$

What is the final linear score?

### Exercise 4 — sign interpretation

Without invoking semantics, what does:

$$ x\cdot y<0 $$

tell you geometrically for nonzero vectors?

### Exercise 5 — scaling

If:

$$ q\cdot v=4, $$

what is:

$$ q\cdot(3v)? $$

What changed: direction, magnitude, or both?

### Exercise 6 — cosine versus dot product

Two candidates point in exactly the same direction but one has twice the norm.

How do their cosine similarities with the same query compare?

How can their dot products differ?

### Exercise 7 — logits

Let:

$$ h=[1,2] $$

and candidate vectors:

$$ w_1=[2,0], $$

$$ w_2=[0,1]. $$

With zero biases, compute both logits.

Which candidate has the larger pre-softmax score?

### Exercise 8 — modeling assumption

Someone says:

> “These two words have a large dot product, so they must mean the same thing.”

What additional information would you need before accepting that interpretation?

---

## Retrieval check

Without looking back:

1. What is a vector at this level?
2. Why does coordinate order matter?
3. What dimension requirement does an ordinary dot product have?
4. How is a dot product computed?
5. Why is a dot product useful as a score?
6. How is a dot product a weighted sum?
7. What does the geometric identity for a dot product depend on?
8. Why is raw dot product not identical to cosine similarity?
9. What happens to a dot product if one vector is scaled by $10$?
10. When does dot product equal cosine similarity?
11. Can a dot product be negative?
12. Why is a dot product not a probability?
13. How can dot-product scores become logits?
14. What does a bias contribute?
15. Why does vector geometry not automatically imply semantic meaning?
16. Why must two vectors share a compatible coordinate system?

---

## Connections

### Backward: LLM-0004

`LLM-0004` treated logits as real-valued scores and softmax as the probability-normalization step.

This lesson provides one concrete score-producing mechanism:

$$ z_t=h\cdot w_t+b_t. $$

So we now have a longer causal chain:

```text
numeric representations
        ↓
dot-product or linear scoring
        ↓
logits
        ↓
softmax
        ↓
probabilities
```

### Cross-track: Linear Algebra

The Linear Algebra track develops vectors as mathematical objects in much greater depth.

This LLM lesson uses only the minimum vector machinery needed to understand scoring.

Later LLM lessons will repeatedly reuse these operations in model-specific contexts.

### Forward: LLM-N-0006

The next canonical LLM lesson is:

`LLM-N-0006 — Matrices as organized linear transformations`.

A matrix can be viewed as organizing many compatible dot products at once.

That will let us move from:

> one vector score

to:

> many coordinated outputs.

### Long-range: attention

Much later, attention uses dot-product-style compatibility between queries and keys.

At that point we will add:

- learned projections;
- scaling;
- softmax across candidates;
- multiple heads;
- causal masking.

This lesson is only the arithmetic seed.

### Long-range: embeddings and retrieval

Embedding systems often compare vectors with:

- dot product;
- cosine similarity;
- Euclidean distance.

The choice changes ranking behavior.

That is why metric choice is part of model design, not a cosmetic implementation detail.

---

## What this unlocks

You should now be able to:

- define a vector as an ordered numeric representation;
- identify vector dimension;
- compute a dot product by hand;
- interpret a dot product as a weighted sum;
- explain why dot products produce scalar scores;
- connect dot-product scores to logits;
- distinguish dot product from cosine similarity;
- explain the role of vector magnitude;
- explain when normalized dot product equals cosine similarity;
- recognize shape incompatibility;
- avoid treating vector geometry as automatic semantics;
- separate scores from probabilities;
- prepare for matrix–vector products and linear transformations.

---

## References

- **LLM-REF-023** — *Dive into Deep Learning*, §2.3, *Linear Algebra*.
- **LLM-REF-024** — PyTorch documentation, `torch.dot`.
- **LLM-REF-025** — Google for Developers, *Measuring similarity from embeddings*.
