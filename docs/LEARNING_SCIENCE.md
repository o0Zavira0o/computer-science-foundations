# Learning Science Operating Notes

This repository is not a learning-science experiment, and no single technique works identically for every subject or learner. The following practices are used as defaults because they have substantial empirical support and map well to technical learning.

## Retrieval instead of rereading alone

A learner should regularly reconstruct knowledge without looking at the answer: explain a mechanism, predict output, derive a step, debug a failure, reproduce a diagram, or answer a question from memory.

Retrieval is used as a learning event, not merely as grading.

A classic study found better delayed retention from testing than from repeated study, and later work has repeatedly supported retrieval practice as a useful learning mechanism.

**Reference:** Roediger, H. L., & Karpicke, J. D. (2006). *Test-enhanced learning: Taking memory tests improves long-term retention*. Psychological Science, 17(3), 249–255. DOI: `10.1111/j.1467-9280.2006.01693.x`.

## Spacing

Review should be distributed over time rather than compressed into one session.

The repository does not hard-code one universal spacing interval. `LEARNER_STATE.json` supports `review_due` so the tutor can adapt review timing to difficulty, retention goals, and evidence.

**Reference:** Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed practice in verbal recall tasks: A review and quantitative synthesis*. Psychological Bulletin, 132(3), 354–380. DOI: `10.1037/0033-2909.132.3.354`.

## Worked examples that fade into independent work

For unfamiliar procedural or problem-solving material, complete worked examples can reduce unnecessary search. As competence grows, scaffolding should fade and the learner should take over more of the solution.

Do not keep an experienced learner trapped in fully solved examples.

**Reference:** Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). *From example study to problem solving: Smooth transitions help learning*. Journal of Experimental Education, 70(4), 293–315. DOI: `10.1080/00220970209599510`.

## Self-explanation

Lessons should sometimes ask the learner to explain **why** a step follows, why an alternative fails, or how a new result connects to an earlier model.

Self-explanation prompts should be substantive rather than repetitive "say this in your own words" filler.

**Reference:** Chi, M. T. H., Bassok, M., Lewis, M. W., Reimann, P., & Glaser, R. (1989). *Self-explanations: How students study and use examples in learning to solve problems*. Cognitive Science, 13, 145–182.

## Interleaving

Once multiple related problem types have been learned, practice should sometimes mix them so the learner must identify **which method applies**, not merely repeat the method from the immediately previous example.

Interleaving is not used to make first exposure needlessly chaotic.

**Reference:** Rohrer, D., & Taylor, K. (2007). *The shuffling of mathematics practice problems boosts learning*. Instructional Science, 35(6), 481–498. DOI: `10.1007/s11251-007-9015-8`.

## Mastery is evidence, not familiarity

Feeling that a lesson is familiar is not enough.

Where appropriate, the repository seeks evidence across several modes:

- explanation;
- prediction;
- application;
- transfer;
- debugging;
- counterexample;
- derivation/proof;
- design choice with justification;
- project performance;
- research critique.

The exact evidence must fit the discipline. A proof-oriented mathematics concept and a Linux operational skill should not be assessed identically.

## Calibration

Confidence is useful metadata but cannot replace performance evidence.

When confidence and demonstrated performance disagree, the system should surface the mismatch rather than hiding it.

## Pedagogical repetition policy

Repetition is allowed when its purpose is one of:

- spaced retrieval;
- deliberate deepening;
- contrast;
- interleaving;
- cross-domain transfer;
- correction of a diagnosed misconception.

Unlabeled same-depth restatement is duplication.
