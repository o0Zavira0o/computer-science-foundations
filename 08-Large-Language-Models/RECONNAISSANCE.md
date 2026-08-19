# Large Language Models — Curriculum Reconnaissance (2026-08-19)

## Purpose

This roadmap is designed to prevent two common failures in LLM education: beginning with fashionable product terminology before the learner has a computational model, and stopping at a Transformer diagram without understanding training, evaluation, systems, post-training, or research practice.

## Evidence classes used

- **Implementation-centered university curriculum:** Stanford CS336, Language Modeling from Scratch (Spring 2026).
- **Foundational architecture research:** *Attention Is All You Need*.
- **Scaling research:** Kaplan-style scaling laws and the Chinchilla compute-optimal study.
- **Post-training:** InstructGPT/RLHF, DPO, and reasoning-oriented reinforcement-learning case studies.
- **Evaluation:** HELM and capability/robustness evaluation literature.
- **Retrieval and agents:** RAG and ReAct primary papers.
- **Training systems:** current PyTorch autograd/distributed/FSDP documentation.
- **Inference systems:** FlashAttention, PagedAttention/vLLM, and current vLLM documentation.

## Scope and prerequisite closure

The track assumes zero LLM-specific knowledge. L0 contains compact bridges for probability, vectors, gradients, neural networks, PyTorch, data splits, loss, and compute/memory so that a learner is not forced to leave the track before understanding the first model. Those bridges do not replace full Linear Algebra, Computer Systems, Computer Architecture, or Parallel Processor tracks; when deeper treatment matters, the canonical track should own it.

## Progression

The 116-node spine progresses from a probabilistic language-model mental model to a tiny neural LM, then a Transformer built from known components, then data/scaling/distributed training, post-training, evaluation, retrieval/tools, inference systems, interpretability/safety, graduate research questions, replication, and an open L6 frontier.

This spine is deliberately revisable. It is not a claim that 116 lessons exhaust the field. Fast-moving frontier areas must be refreshed against primary/current sources before publication.
