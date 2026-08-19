# Linux Systems — Curriculum Reconnaissance (2026-08-19)

## Purpose

This document records why the Linux Systems curriculum has the shape it does. The roadmap is not copied from one book, certification, or distribution. It is a dependency spine synthesized from multiple evidence classes so that practical competence, portable interfaces, Linux-specific behavior, internals, and research literacy all remain visible.

## Evidence classes used

1. **Portable interface semantics:** POSIX.1-2024 / The Open Group Base Specifications Issue 8.
2. **Linux-specific canonical behavior:** Linux kernel documentation and the Linux man-pages project.
3. **Everyday command and shell semantics:** GNU Coreutils and Bash documentation.
4. **Administration practice:** Linux Foundation LFS101 and LFCS domains.
5. **System construction and integration:** Linux From Scratch 13.0-systemd and Beyond Linux From Scratch.
6. **Operating-system implementation:** MIT 6.1810 and UC Berkeley CS 162.
7. **Kernel contribution and research:** kernel development-process documentation and researcher guidelines.

## Scope decisions

Linux Systems owns the Linux-specific operating environment: shell and utilities, filesystems, processes, identity, administration, service management, observability, kernel-facing interfaces, Linux internals, kernel development, and Linux-oriented systems research.

General architecture concepts that deserve a complete hardware treatment belong to Computer Architecture. General OS mechanisms that are not Linux-specific can be canonically deepened in Computer Systems. C++ and Parallel Processor tracks own their full language/HPC treatments. Linux may introduce enough of a neighboring concept to keep a dependency chain understandable, then link rather than duplicate the canonical deep treatment.

## Depth policy

The 112 nodes are an audited **spine, not a ceiling**. L0 begins with the system mental model and safe experimentation; L1-L2 build operational competence; L3-L4 enter system-call, kernel, performance, security, virtualization, BPF, and subsystem internals; L5 trains source archaeology, patch review, experimental design, paper reading, and research ethics; L6 remains an open research frontier.

## Freshness policy

Version-sensitive operational references carry review dates in the reference registry. Stable conceptual interfaces and fixed historical papers/standards are not rewritten merely because a newer distribution release appears. Current kernel behavior must be rechecked when a lesson explicitly depends on it.
