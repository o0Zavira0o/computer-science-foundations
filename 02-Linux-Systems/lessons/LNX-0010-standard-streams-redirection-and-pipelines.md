---
id: LNX-0010
title: Standard streams, redirection, and pipelines
track: linux-systems
level: L0
status: complete
curriculum_node: LNX-N-0010
concepts_introduced: ["LNX-C-0010"]
concepts_deepened: ["LNX-C-0003", "LNX-C-0009"]
concepts_used: ["LNX-C-0004", "LNX-C-0005", "LNX-C-0007", "LNX-C-0008"]
examples_added: ["LNX-EX-028", "LNX-EX-029", "LNX-EX-030", "LNX-EX-031"]
references_used: ["LNX-REF-001", "LNX-REF-003", "LNX-REF-005"]
last_reviewed: 2026-08-26
version_sensitive: true
review_after: 2027-02-19
---

# Standard streams, redirection, and pipelines

## If you landed here directly

The formal prerequisite is:

- **[`LNX-0009 — Quoting, globbing, and expansion`](LNX-0009-quoting-globbing-and-expansion.md).**

That lesson established a crucial boundary:

> the shell interprets syntax and constructs the command environment before the target program begins ordinary execution.

This lesson applies the same idea to input and output.

When you type:

```bash
wc -l < notes.txt
```

the characters `< notes.txt` are not normally passed to `wc` as ordinary arguments.

The shell interprets the redirection, opens the file, connects that open stream to the command's standard input, and then runs the command with that connection already in place.

Likewise:

```bash
producer | consumer
```

does not mean "write a temporary file and then run the next program."

The shell creates a pipe and arranges two command environments so that bytes written by one command can become bytes read by another.

This lesson stays at the user-and-shell boundary. Later **LNX-N-0037 — File descriptors and the system-call boundary** will connect these ideas to descriptor tables and calls such as `open`, `dup`, `read`, and `write`.

---

## The problem worth understanding

A terminal can make several different data paths look like one thing.

Run:

```bash
printf 'hello\n'
```

You see:

```text
hello
```

Now run a command that fails:

```bash
ls /definitely-not-a-real-csf-path
```

You see a diagnostic.

Both appeared in the same terminal window.

It is tempting to conclude:

> "Commands have one output."

That model is too weak.

Unix-style programs normally begin with three conventional streams:

```text
standard input   stdin    descriptor 0
standard output  stdout   descriptor 1
standard error   stderr   descriptor 2
```

The terminal may be connected to all three, so their effects can appear in one place.

But they remain distinct channels.

That distinction becomes visible when you redirect them separately.

---

## Mental model: a command starts with connected streams

For a simple interactive command, imagine:

```text
keyboard / terminal input
          │
          ▼
      stdin (0)
          │
          ▼
       PROGRAM
        │    │
        │    └────────► stderr (2) ───────► terminal
        │
        └─────────────► stdout (1) ───────► terminal
```

The numbers `0`, `1`, and `2` are conventional file-descriptor numbers.

At this level you do not need to know how the kernel represents them internally.

You do need the following operational idea:

> a process reads and writes through open channels; the shell can arrange where those channels point before the command runs.

That is what redirection changes.

---

## Standard input is a data source

A program that reads standard input does not need to know whether the bytes came from:

- your keyboard;
- a file;
- another process through a pipe;
- a terminal emulator;
- some other compatible source.

For example:

```bash
wc -l
```

can read lines interactively until end-of-file.

But:

```bash
wc -l < notes.txt
```

connects `notes.txt` to standard input.

And:

```bash
printf 'one\ntwo\nthree\n' | wc -l
```

connects the output of `printf` to the input of `wc`.

The `wc` program can use the same ordinary input interface in all three cases.

The source changed.

The program's basic reading role did not.

---

## Standard output is the ordinary result channel

Programs commonly write their normal result to standard output.

For example:

```bash
printf 'result\n'
```

writes its ordinary data to stdout.

A successful command may write nothing at all, or it may write many megabytes.

"Standard output" does not mean:

- text only;
- success only;
- terminal only;
- human-readable only.

It is a conventional output channel.

Whether a particular program uses it well is a property of that program's interface.

---

## Standard error is a separate diagnostic channel

Programs commonly write diagnostics to standard error.

For example:

```bash
ls /definitely-not-a-real-csf-path
```

normally emits an error message to stderr.

Why have a separate channel?

Because ordinary output may itself be data that another command or file should receive.

Suppose a program is producing a list of names on stdout.

If diagnostics were mixed into that same byte stream, a downstream program could mistake the diagnostic text for valid data.

Separate stdout and stderr make it possible to say:

```text
ordinary result  ─────► data destination
diagnostics      ─────► terminal or log
```

That is a compositional design feature, not merely a cosmetic convention.

---

## Redirection is shell syntax

Consider:

```bash
printf 'hello\n' > hello.txt
```

A useful high-level sequence is:

```text
shell parses command
        ↓
shell recognizes > as redirection syntax
        ↓
shell resolves/expands the redirection target
        ↓
shell opens hello.txt for the requested redirection mode
        ↓
shell arranges stdout to refer to that open destination
        ↓
command runs
        ↓
printf writes stdout
        ↓
bytes go to hello.txt
```

The command does not normally receive these arguments:

```text
">"
"hello.txt"
```

The redirection is handled by the shell layer.

This directly extends the parsing model from LNX-0009.

---

## `>` redirects stdout and normally truncates the destination

Example:

```bash
printf 'first\n' > result.txt
```

Then:

```bash
cat result.txt
```

shows:

```text
first
```

Now:

```bash
printf 'second\n' > result.txt
```

The file now contains:

```text
second
```

not both lines.

The ordinary `>` output redirection opens the destination in a way that replaces/truncates its prior contents.

That makes `>` potentially destructive.

A safe habit is:

> verify the pathname and decide whether replacement is intended before pressing Enter.

Quoting still matters:

```bash
printf 'report\n' > "quarterly report.txt"
```

The shell must still construct the destination pathname correctly.

---

## `>>` appends instead of replacing

Example:

```bash
printf 'first\n' > log.txt
printf 'second\n' >> log.txt
```

Now:

```bash
cat log.txt
```

contains:

```text
first
second
```

The distinction is conceptual:

```text
>    open stdout destination for replacement/truncating output
>>   open stdout destination for appending output
```

Do not reduce this to "single arrow versus double arrow."

Think about the destination state.

---

## `<` redirects stdin from a file

Create a disposable input file:

```bash
printf 'alpha\nbeta\ngamma\n' > input.txt
```

Then:

```bash
wc -l < input.txt
```

The shell connects the file to descriptor 0.

`wc` reads from standard input.

Notice the difference from:

```bash
wc -l input.txt
```

In the second command, `input.txt` is an ordinary argument naming a file.

In the first, the filename belongs to shell redirection syntax and `wc` reads from stdin.

The visible result may be similar, but the interface is different.

That difference matters when a program:

- has no filename argument;
- reports filenames when given operands;
- behaves differently for seekable files versus streams;
- is used inside a pipeline.

---

## Worked example LNX-EX-028 — separate ordinary output from diagnostics

Use a disposable directory:

```bash
mkdir -p ~/csf-labs/streams
cd ~/csf-labs/streams
```

Run:

```bash
printf 'normal result\n' > output.txt
ls /definitely-not-a-real-csf-path 2> errors.txt
```

Now inspect:

```bash
printf '%s\n' '--- output.txt ---'
cat output.txt

printf '%s\n' '--- errors.txt ---'
cat errors.txt
```

The point is not the exact wording of the `ls` diagnostic.

The point is the routing:

```text
printf stdout ─────► output.txt
ls stderr      ─────► errors.txt
```

The terminal did not magically "capture output."

The shell changed where specific descriptors pointed.

---

## Why `2>` means stderr

The general redirection form can include a descriptor number.

For output:

```bash
2> errors.txt
```

means:

```text
redirect descriptor 2
```

and descriptor 2 is conventionally stderr.

Similarly:

```bash
1> output.txt
```

explicitly names stdout.

Because stdout is the default for `>`, these are equivalent in the ordinary case:

```bash
command > output.txt
command 1> output.txt
```

The shorter form is usually clearer.

---

## Redirecting both stdout and stderr

A common Bash pattern is:

```bash
command > all.txt 2>&1
```

This deserves careful reading.

Do not read `2>&1` as "send two things to one file."

At the moment that redirection is processed, it means roughly:

> make descriptor 2 refer to the same destination descriptor 1 currently refers to.

Because redirections are processed from left to right in Bash, order matters.

---

## Worked example LNX-EX-029 — redirection order changes topology

Compare:

```bash
command > all.txt 2>&1
```

with:

```bash
command 2>&1 > out.txt
```

In the first:

```text
1. stdout -> all.txt
2. stderr -> where stdout now points
```

Result:

```text
stdout ─┐
        ├──► all.txt
stderr ─┘
```

In the second:

```text
1. stderr -> where stdout points now, usually terminal
2. stdout -> out.txt
```

Result:

```text
stdout ─────► out.txt
stderr ─────► original stdout destination, often terminal
```

The characters are similar.

The connection graph is different.

This is one of the clearest examples of why shell syntax should be read as an ordered transformation, not as decorative punctuation.

GNU Bash documents that redirections are processed in the order they appear, from left to right.

---

## `2>&1` duplicates a connection; it is not a filename

This is an easy misconception.

In:

```bash
2>&1
```

the `&1` part refers to descriptor 1 in this redirection context.

It does not mean:

```text
write stderr into a file literally named 1
```

Later descriptor lessons will explain the underlying duplication mechanism more formally.

For now, retain the topology idea:

```text
descriptor 2
     │
     └── make it point where descriptor 1 points now
```

---

## A pipeline connects processes

Consider:

```bash
printf 'alpha\nbeta\ngamma\n' | wc -l
```

A useful mental model is:

```text
printf process
    stdout
      │
      ▼
   [ pipe ]
      │
      ▼
    stdin
   wc process
```

The pipe is a kernel-managed byte channel.

The shell creates the pipeline structure and launches the commands with appropriate connections.

The left command and right command can run during overlapping time.

This is not fundamentally:

```text
run command A completely
save output to a hidden file
run command B on that file
```

A pipe is a stream connection.

---

## Worked example LNX-EX-030 — compose two simple programs

Run:

```bash
printf 'alpha\nbeta\ngamma\n' | wc -l
```

Predict before running:

1. What does `printf` write?
2. Which stream does it write to?
3. Where does that stream go?
4. What does `wc -l` read?
5. What does `wc -l` write?
6. Where does the final output appear?

A correct model is:

```text
literal data in printf arguments
        ↓
printf
        ↓ stdout
pipe
        ↓ stdin
wc -l
        ↓ stdout
terminal
```

Each program has a small job.

The shell connects them.

That is the core of Unix stream composition.

---

## A pipeline normally carries stdout, not stderr

Now run:

```bash
ls /definitely-not-a-real-csf-path | wc -l
```

You will typically still see an `ls` diagnostic in the terminal.

And `wc -l` may report:

```text
0
```

Why?

Because the pipe normally connects:

```text
left stdout -> right stdin
```

not:

```text
left stderr -> right stdin
```

So:

```text
ls stdout ─────► pipe ─────► wc stdin
ls stderr ─────────────────► terminal
```

This distinction prevents diagnostics from automatically contaminating a data pipeline.

If you deliberately want to merge stderr into stdout, you must request that routing.

---

## Pipeline data is bytes, not "lines" in the kernel abstraction

Many command-line programs treat input as lines.

That can make pipelines feel like "line channels."

At a lower level, a pipe transports bytes.

Line interpretation belongs to the programs or libraries reading those bytes.

This matters later for:

- binary data;
- partial reads;
- buffering;
- long records;
- programs that do not flush output when you expect.

At L0, remember:

> the pipe supplies a byte stream; "line" is a higher-level interpretation.

---

## Pipeline commands can run concurrently

Suppose:

```bash
producer | consumer
```

A simplistic picture says:

```text
producer finishes
        ↓
consumer starts
```

That is generally wrong.

The shell can launch both sides and connect them through the pipe.

Conceptually:

```text
time ─────────────────────────►

producer:  write write write ...
                 │
                 ▼
              pipe buffer
                 │
                 ▼
consumer:       read read read ...
```

This overlapping behavior is one reason pipelines can process large streams without storing the entire intermediate result.

It also creates failure modes that are different from ordinary sequential commands.

---

## Pipeline exit status can hide an earlier failure

Consider Bash:

```bash
false | true
```

`false` exits unsuccessfully.

`true` exits successfully.

By default, the pipeline's status in Bash is based on the last command, so the pipeline can appear successful even though an earlier component failed.

Check:

```bash
false | true
printf 'status=%s\n' "$?"
```

In default Bash behavior, the reported status is normally `0`.

This does **not** mean every stage succeeded.

Bash provides the `pipefail` option to change pipeline-status behavior.

Inspect your current setting:

```bash
set -o | grep '^pipefail'
```

In a disposable shell, you can compare:

```bash
set -o pipefail
false | true
printf 'status=%s\n' "$?"
set +o pipefail
```

Do not turn this into a slogan that `pipefail` "fixes pipelines."

It changes which failure becomes visible in the pipeline status.

Later shell-programming lessons will treat robust error handling in more depth.

---

## Worked example LNX-EX-031 — the output can look fine while the pipeline failed

Imagine a pipeline:

```bash
producer | formatter
```

The formatter might successfully format whatever bytes it received.

But the producer may have failed halfway through.

If you inspect only:

- the final text;
- the final command's status;

you can miss the upstream failure.

The lesson is broader than `pipefail`:

> composition creates multiple failure locations.

When debugging a pipeline, ask:

```text
Which stage produced this data?
Which stage failed?
Which stream carried the diagnostic?
Which exit status am I actually inspecting?
```

This is the beginning of systems-oriented pipeline debugging.

---

## Redirection can fail before the intended program meaningfully runs

Consider:

```bash
printf 'important result\n' > /directory/you-cannot-write/result.txt
```

If the shell cannot open the redirection target, command execution cannot proceed normally with the requested connection.

The diagnostic may come from the shell rather than from `printf`.

That distinction matters.

The apparent command line contains a program name, but the failure occurred while establishing the shell-managed environment.

This gives you a debugging question:

> Did the target program fail, or did the shell fail while preparing its redirections?

---

## Path expansion still applies to redirection targets

LNX-0009 still matters.

For example:

```bash
name='quarterly report.txt'
printf 'done\n' > "$name"
```

The variable is expanded by the shell.

The quotes protect the result as one pathname field.

If you instead write:

```bash
printf 'done\n' > $name
```

you are combining redirection syntax with unquoted expansion.

That can produce unintended field splitting or pathname expansion.

So shell topics are not isolated chapters.

They compose.

---

## A redirection target is not ordinary command output syntax

Beginners sometimes reason:

```text
command prints >
then file receives output
```

No.

`>` is not something the command prints.

It is syntax that changes the command's output destination.

Similarly:

```bash
cat < file.txt
```

does not cause `<` to flow through stdin.

The shell removes redirection syntax from the ordinary command-argument interface after using it to configure the command.

---

## Pipeline versus redirection

Compare:

```bash
producer > data.txt
consumer < data.txt
```

with:

```bash
producer | consumer
```

They are not interchangeable in every respect.

### File-mediated version

```text
producer
   │
   ▼
data.txt
   │
   ▼
consumer
```

The file persists.

It can be inspected later.

The two commands can be run at different times.

### Pipeline version

```text
producer stdout
       │
       ▼
     pipe
       │
       ▼
consumer stdin
```

The intermediate channel is transient.

The commands can overlap.

There is no ordinary persistent intermediate file to inspect afterward.

Choose based on the task, not because pipes look more advanced.

---

## Why pipelines are powerful

A pipeline lets small programs expose narrow interfaces.

For example, a later text-processing workflow might look like:

```text
generate data
    │
    ▼
filter
    │
    ▼
transform
    │
    ▼
sort
    │
    ▼
count
```

The programs do not all need to understand one another's full implementation.

They need compatible stream formats.

This is an architectural idea:

> composition works when components agree on interfaces.

Unix command-line pipelines are one concrete example of that broader systems principle.

---

## But "everything is a pipeline" is also a bad model

Pipelines are excellent for stream-shaped transformations.

They are less suitable when you need:

- random access to intermediate data;
- transactional updates;
- rich structured protocols;
- multiple bidirectional communication channels;
- persistent intermediate artifacts;
- large stateful interactions;
- complex error coordination.

The lesson is not "pipes are superior."

The lesson is "pipes are a simple, composable interface for a specific class of data flow."

---

## Where intuition breaks

### 1. "Whatever I see in the terminal is stdout"

False.

The terminal may be displaying stdout and stderr from the same process or from several processes.

Redirection reveals the distinction.

---

### 2. "`>` is an argument to the program"

Usually false in ordinary shell syntax.

The shell interprets it.

Use the shell model before asking what `argv` the program receives.

---

### 3. "`>` means save without danger"

False.

`>` can truncate an existing file.

Treat output redirection as a filesystem mutation.

---

### 4. "`>>` is always safer"

Not necessarily.

Appending to the wrong file can also be harmful.

The operation is different, not automatically correct.

---

### 5. "A pipe sends every output stream to the next command"

False.

Ordinary `|` connects stdout of the left command to stdin of the right command.

Stderr remains separate unless you explicitly route it.

---

### 6. "A pipeline runs one program after another"

Not as a general execution model.

Stages can run concurrently.

---

### 7. "If the pipeline's final command succeeds, the whole computation succeeded"

Not necessarily.

Earlier stages can fail.

Inspect the failure semantics you actually need.

---

### 8. "`2>&1` means stderr goes to stdout forever"

It changes a descriptor connection at that point in the redirection sequence.

Later redirections can change the topology again.

Order matters.

---

### 9. "The program opens every file named after `>`"

The shell commonly opens the redirection target as part of preparing the command.

This is why permission or pathname errors can occur before the program performs its intended work.

---

### 10. "stdin/stdout/stderr are the only file descriptors"

No.

They are merely the conventional initial descriptors 0, 1, and 2.

Processes can have many more.

LNX-N-0037 will make that model explicit.

---

## A safe disposable lab

Create:

```bash
mkdir -p ~/csf-labs/redirection
cd ~/csf-labs/redirection
```

Check:

```bash
pwd
ls -la
```

Create input:

```bash
printf 'red\nblue\ngreen\n' > colors.txt
```

### Experiment A — stdin from file

Predict, then run:

```bash
wc -l < colors.txt
```

### Experiment B — stdout to file

Predict, then run:

```bash
wc -l < colors.txt > count.txt
cat count.txt
```

### Experiment C — stderr to file

Predict, then run:

```bash
ls definitely-missing 2> errors.txt
cat errors.txt
```

### Experiment D — stdout through pipe

Predict, then run:

```bash
printf 'red\nblue\ngreen\n' | wc -l
```

### Experiment E — stderr does not enter ordinary pipe

Predict, then run:

```bash
ls definitely-missing | wc -l
```

Ask after every experiment:

```text
What did the shell interpret?
What did the program receive as arguments?
Where did stdin point?
Where did stdout point?
Where did stderr point?
Which component could have produced the diagnostic?
```

That question set is more reusable than memorizing punctuation.

---

## Active work

### Exercise 1 — draw the channels

For:

```bash
wc -l < colors.txt > count.txt
```

draw:

```text
source of stdin:
destination of stdout:
destination of stderr:
```

Then explain which component opens `colors.txt` and `count.txt` at the shell-model level.

---

### Exercise 2 — predict truncation

Suppose `report.txt` already contains important data.

What happens to its old contents in the ordinary successful case after:

```bash
printf 'new\n' > report.txt
```

How is that different from:

```bash
printf 'new\n' >> report.txt
```

Do not answer with punctuation names only.

Describe file state.

---

### Exercise 3 — separate streams

Predict which file receives which bytes:

```bash
printf 'normal\n' > normal.txt
ls definitely-missing 2> diagnostic.txt
```

Then verify.

---

### Exercise 4 — explain `2>&1`

In words, explain:

```bash
command > all.txt 2>&1
```

without saying merely "redirect both."

Your explanation must include the left-to-right ordering.

---

### Exercise 5 — reverse the order

Explain why:

```bash
command 2>&1 > out.txt
```

can leave stderr going to the terminal while stdout goes to `out.txt`.

Draw the descriptor destinations after each redirection.

---

### Exercise 6 — pipeline topology

For:

```bash
printf 'a\nb\nc\n' | wc -l
```

identify:

- producer;
- consumer;
- producer stdout destination;
- consumer stdin source;
- consumer stdout destination.

---

### Exercise 7 — stderr bypass

Why can:

```bash
ls definitely-missing | wc -l
```

display a diagnostic and still give `wc` zero lines?

Answer using stream names.

---

### Exercise 8 — hidden pipeline failure

Run in Bash:

```bash
false | true
printf 'status=%s\n' "$?"
```

Then:

```bash
set -o pipefail
false | true
printf 'status=%s\n' "$?"
set +o pipefail
```

Explain what changed and what did **not** change.

---

### Exercise 9 — distinguish filename argument from stdin redirection

Compare:

```bash
wc -l colors.txt
wc -l < colors.txt
```

What information can the program receive differently in these two interfaces?

---

### Exercise 10 — debug the layer

You run:

```bash
printf 'hello\n' > /some/unwritable/path/out.txt
```

and receive a permission-related diagnostic.

Which layer should you investigate first:

- `printf` formatting;
- shell redirection setup;
- network routing;
- terminal rendering?

Explain why.

---

## Retrieval / self-explanation

Close the lesson and answer from memory.

1. What are stdin, stdout, and stderr?
2. What conventional descriptor numbers correspond to them?
3. Why can stdout and stderr look merged in an interactive terminal?
4. Who normally interprets `>` in a Bash command line?
5. What is the ordinary difference between `>` and `>>`?
6. What does `< file` change?
7. What does `2> file` change?
8. Why is `2>&1` sensitive to order?
9. What does ordinary `|` connect?
10. Does ordinary `|` also carry stderr?
11. Why is a pipe not best modeled as a hidden temporary file?
12. Can pipeline stages run concurrently?
13. Why can a pipeline hide an upstream failure?
14. What does Bash `pipefail` change?
15. Why can a redirection error occur before the target program meaningfully runs?
16. Why does quoting still matter in a redirection pathname?
17. When might a persistent intermediate file be preferable to a pipeline?
18. What deeper topic will later explain descriptor duplication and system calls?

If you cannot clearly answer 4, 8, 9, and 13, revisit the shell-topology examples before moving on.

---

## Connections

### Backward: command invocation

LNX-0003 introduced stdin, stdout, stderr, arguments, and exit status as distinct parts of command execution.

This lesson makes the stream side operational.

---

### Backward: quoting and shell interpretation

LNX-0009 showed that the shell transforms syntax before the program sees final arguments.

Redirection operators and pipeline operators are another category of shell syntax.

This is why:

```bash
command > file
```

cannot be understood by looking only at the target program's command-line options.

---

### Forward: text-processing composition

The immediate next core lesson is:

**LNX-N-0011 — Search, filter, count, sort, and transform text.**

That lesson will use pipelines to build transparent text-processing chains.

Without today's stream model, those chains would become recipes to memorize.

With the stream model, you can ask what each stage consumes and produces.

---

### Forward: shell environment and exit status

LNX-N-0017 will deepen:

- exit status;
- shell variables;
- exported environment;
- `PATH`;
- startup files.

Pipeline-status behavior belongs to that larger shell-execution model.

---

### Forward: file descriptors and system calls

LNX-N-0037 will explain what this lesson deliberately keeps conceptual:

- process descriptor tables;
- `open`;
- `read`;
- `write`;
- `close`;
- `dup`;
- shell redirection at the system-call boundary.

The L0 topology model is preparation for that mechanism.

---

## What this unlocks

You should now be able to:

- distinguish stdin, stdout, and stderr even when one terminal displays them together;
- explain redirection as shell-managed connection setup;
- use `>`, `>>`, `<`, and `2>` deliberately;
- explain why `2>&1` is order-sensitive;
- predict which stream ordinary pipelines connect;
- explain why stderr can bypass a pipeline;
- model a pipeline as concurrently connected processes rather than a hidden file;
- recognize that pipeline status may hide upstream failure;
- use a disposable lab to verify stream routing;
- distinguish a shell-preparation error from a target-program error;
- connect shell parsing, filesystem paths, streams, and process composition into one mental model.

The immediate next core lesson is:

**LNX-0011 — Search, filter, count, sort, and transform text.**

---

## References

- **LNX-REF-001** — IEEE / The Open Group, *POSIX.1-2024*, for standard input/output concepts, shell redirection, pipelines, and portable shell semantics.
- **LNX-REF-003** — Linux man-pages project, for Linux file-descriptor and pipe terminology that later lessons will deepen.
- **LNX-REF-005** — GNU Project, *Bash Reference Manual*, especially Redirections, Pipelines, and command execution semantics. Bash documents that redirections are processed left to right.
