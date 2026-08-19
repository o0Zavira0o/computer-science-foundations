---
id: LNX-EXR-0001
title: Build the Linux System Map
track: linux-systems
level: L0
status: complete
curriculum_nodes: ["LNX-N-0001"]
concepts_used: ["LNX-C-0001"]
references_used: ["LNX-REF-001"]
last_reviewed: 2026-08-19
---

## Task

Create a one-page system map for the Linux machine you are currently using. It may be a physical Fedora workstation, a virtual machine, WSL, a cloud host, or another safe environment.

Your map must identify, without changing system state:

1. the kernel release;
2. the distribution/operating-system identity;
3. the shell process you are interacting with;
4. the terminal environment if one exists;
5. one userspace utility and the package that provides it, if your package manager can answer safely;
6. one example of a kernel-mediated resource that utility uses.

Suggested read-only probes include:

```bash
uname -r
cat /etc/os-release
printf '%s\n' "$SHELL"
ps -p $$ -o pid,ppid,comm,args
command -V ls
```

Do not run commands you do not understand with `sudo` for this exercise.

## Evidence of success

A successful answer is not a screenshot of commands. It is a labeled diagram plus a short explanation that distinguishes kernel, distribution, shell, terminal, and userspace utility. For at least one action, write a four-step causal chain from your input to a kernel-mediated effect.

## Hints

If `command -V ls` says `ls` is aliased or otherwise wrapped, that is useful evidence: the string you type and the executable eventually invoked are not always identical.
