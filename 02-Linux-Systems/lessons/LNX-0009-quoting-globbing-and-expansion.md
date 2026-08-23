---
id: LNX-0009
title: Quoting, globbing, and expansion
track: linux-systems
level: L0
status: complete
curriculum_node: LNX-N-0009
concepts_introduced: ["LNX-C-0009"]
concepts_deepened: ["LNX-C-0003"]
concepts_used: ["LNX-C-0004", "LNX-C-0005", "LNX-C-0007"]
examples_added: ["LNX-EX-025", "LNX-EX-026", "LNX-EX-027"]
references_used: ["LNX-REF-001", "LNX-REF-005"]
last_reviewed: 2026-08-23
version_sensitive: true
review_after: 2027-02-19
---

# Quoting, globbing, and expansion

## If you landed here directly

The formal prerequisite is:

- **LNX-0003 — Shell, terminal, command, and argument are different things.**

That distinction matters because this lesson answers a question that is almost invisible when you first use a terminal:

> when you type a command line, which text reaches the program unchanged, and which text does the shell transform first?

The small lab also uses familiar navigation and file-creation commands. You do not need deep knowledge of them; they are only there to give the shell filenames to work with.

This lesson focuses on Bash on a typical Linux system while separating Bash-specific behavior from portable POSIX shell ideas where that distinction matters.

---

## The problem worth understanding

Imagine you type:

```bash
printf '<%s>\n' *.txt
```

Did `printf` receive the characters `*.txt`?

Usually, no.

The shell may replace `*.txt` with matching filenames **before** `printf` starts.

Now type:

```bash
printf '<%s>\n' '*.txt'
```

This time `printf` receives the literal characters `*.txt`.

The program did not suddenly learn a different wildcard rule. The shell changed its own behavior because you quoted the text.

That one distinction explains a surprising amount of command-line behavior:

- filenames with spaces becoming several arguments;
- `*` unexpectedly touching many files;
- variables disappearing or splitting into words;
- command substitutions producing arguments you did not intend;
- a command appearing to "understand wildcards" even though the program never sees the wildcard;
- scripts that work with simple filenames and fail on real ones.

The shell is not merely forwarding your keystrokes.

It parses a language, performs expansions, removes quoting syntax, and then launches commands with an argument vector.

---

## Mental model: source text becomes arguments

Use this pipeline:

```text
text you type
    ↓
shell parsing
    ↓
expansions controlled by quote context
    ↓
field/word formation
    ↓
pathname expansion where applicable
    ↓
quote removal
    ↓
final argv passed to the program
```

For a simple external command, the program ultimately receives something conceptually like:

```text
argv[0] = "printf"
argv[1] = "<%s>\n"
argv[2] = "alpha.txt"
argv[3] = "report 1.txt"
```

It does **not** normally receive one raw string containing your original command line.

That is why quoting is not cosmetic punctuation.

Quoting changes how the shell constructs the arguments.

A useful debugging question is therefore:

> "What exact fields will exist after the shell finishes?"

not:

> "What does the command line look like to me?"

---

## Precise concepts

### 1. Quoting

Quoting tells the shell to preserve some characters from their usual special interpretation.

The three mechanisms you will use most often are:

1. single quotes: `'...'`
2. double quotes: `"..."`
3. backslash: `\`

They are not interchangeable.

---

### 2. Single quotes: preserve everything inside literally

Inside ordinary single quotes, characters lose their special shell meanings.

```bash
printf '%s\n' '$HOME'
```

prints:

```text
$HOME
```

The variable is not expanded.

Likewise:

```bash
printf '%s\n' '*.txt'
```

passes the literal string `*.txt`.

A single quote cannot be represented by simply placing `\'` inside an already single-quoted string. The shell's single-quote syntax must end and resume around it.

At this level, remember the simpler contract:

> single quotes are the strongest ordinary "take this literally" quoting form.

---

### 3. Double quotes: allow selected expansion but protect the result

Double quotes preserve most text while still allowing important expansions such as:

- parameter/variable expansion: `$name`, `${name}`
- command substitution: `$(command)`
- arithmetic expansion: `$((expression))`

For example:

```bash
name='two words'
printf '<%s>\n' "$name"
```

passes **one** argument containing a space:

```text
<two words>
```

The variable expanded, but the double quotes prevented the expanded value from being split into multiple fields and from undergoing pathname expansion.

This is the source of a high-value shell habit:

> when a variable is intended to become one ordinary argument, expand it as `"$variable"`.

There are advanced exceptions and special parameters, especially `"$@"`, but this rule is an excellent default for scalar variables.

---

### 4. Backslash: quote the next character in context

Outside single quotes, a backslash can remove the special meaning of the next character.

For example:

```bash
printf '%s\n' \*
```

passes a literal `*`.

And:

```bash
printf '%s\n' hello\ world
```

passes one argument containing a space.

Backslash has context-sensitive details, especially inside double quotes. Do not build a mental model in which backslash is a universal "escape everything" operator.

For ordinary interactive use, single or double quotes are often easier to read.

---

### 5. Expansion

**Expansion** is the shell transforming shell-language constructs into other text or fields before command execution.

Bash has several expansion mechanisms. The important ones for this lesson are:

- parameter and variable expansion;
- command substitution;
- word splitting;
- filename expansion, often called globbing.

Bash also supports brace, tilde, arithmetic, and process substitution mechanisms. Those matter, but we do not need to master all of them here.

The order matters.

In Bash, the documented broad order is:

1. brace expansion;
2. tilde expansion, parameter/variable expansion, arithmetic expansion, and command substitution;
3. word splitting;
4. filename expansion;
5. quote removal.

POSIX specifies a closely related staged model for portable shell word expansions.

You do not need to memorize the entire list yet.

You **do** need to understand this consequence:

> an unquoted expansion can produce text that is then split and globbed before the program receives it.

Double quotes often stop those later transformations for the expanded value.

---

### 6. Parameter and variable expansion

A shell variable can be assigned like this:

```bash
name='report 1.txt'
```

The assignment itself does not run `report 1.txt` as a command. It binds text to a shell variable.

You request its value with parameter expansion:

```bash
printf '%s\n' "$name"
```

The `$name` is shell syntax.

`printf` receives the expanded value, not the characters `$name`.

Braces can make the boundary explicit:

```bash
prefix='report'
printf '%s\n' "${prefix}-final.txt"
```

Without braces,

```bash
"$prefix-final.txt"
```

still works here because `-` cannot be part of the variable name.

But compare:

```bash
name='log'
printf '%s\n' "${name}file"
```

with:

```bash
printf '%s\n' "$namefile"
```

The second asks for a different variable named `namefile`.

Use `${...}` when the variable-name boundary would otherwise be ambiguous.

---

### 7. Word splitting

After certain **unquoted** expansions, the shell can split the resulting text into multiple fields.

Consider:

```bash
value='alpha beta'
printf '<%s>\n' $value
```

In normal Bash settings, the unquoted expansion produces text that is then split, so `printf` receives two arguments after its format string:

```text
<alpha>
<beta>
```

Now quote it:

```bash
printf '<%s>\n' "$value"
```

and the result is one field:

```text
<alpha beta>
```

This is one reason the advice "quote your variables" exists.

But the deeper rule is better:

> decide how many arguments you intend, then quote expansions so the shell constructs that number.

Sometimes deliberate splitting is wanted. In robust shell code, however, using arrays is usually clearer than relying on accidental splitting of a scalar string.

---

### 8. Filename expansion: globbing

After word splitting, an unquoted field containing pattern characters may undergo pathname expansion.

The three basic glob pattern forms are:

- `*` — matches any string of characters within one pathname component;
- `?` — matches one character;
- `[...]` — matches one character from a set or class described by the bracket expression.

Suppose the current directory contains:

```text
alpha.txt
beta.txt
notes.md
report 1.txt
```

Then:

```bash
printf '<%s>\n' *.txt
```

may become arguments equivalent to:

```text
alpha.txt
beta.txt
report 1.txt
```

Notice something subtle:

`report 1.txt` contains a space, but pathname expansion produces it as one pathname field. The shell does not take each matched filename and split it again on spaces after globbing.

This is why globs can handle spaces in matched names better than an unquoted variable containing a space-separated filename list.

---

### 9. A glob is not a regular expression

This is a major conceptual trap.

Shell glob:

```text
*.log
```

roughly means:

> any filename whose final characters are `.log`

A regular expression such as:

```text
.*\.log
```

belongs to a different pattern language.

They use some of the same punctuation but with different grammars and meanings.

Do not transfer regex rules into shell globbing.

A future lesson will study regular expressions explicitly.

---

### 10. Command substitution

Command substitution runs a command and substitutes its standard output into the surrounding shell word.

Modern syntax:

```bash
$(command)
```

Example:

```bash
kernel=$(uname -r)
printf 'kernel: %s\n' "$kernel"
```

The shell runs `uname -r`, captures its standard output, removes trailing newline characters from the substitution result, assigns the text to `kernel`, and later expands the variable.

You can also substitute directly:

```bash
printf 'kernel: %s\n' "$(uname -r)"
```

The double quotes are important if you intend the command output to become one argument.

The older backtick syntax:

```bash
`command`
```

still exists, but `$(...)` is easier to read and nest and is the preferred form for new code.

---

## How it actually works

### The shell parses before the program runs

Take:

```bash
printf '<%s>\n' "$HOME" '*.txt' *.txt
```

The shell first recognizes words and quote context.

Conceptually, it sees four command words before expansion:

1. `printf`
2. `'<%s>\n'`
3. `"$HOME"`
4. `'*.txt'`
5. `*.txt`

Then different rules apply.

- The format string is protected by single quotes.
- `$HOME` expands inside double quotes but remains one field.
- `'*.txt'` stays literal.
- unquoted `*.txt` is eligible for filename expansion.

By the time `printf` runs, the quote characters themselves are no longer part of ordinary arguments. They were shell syntax.

This is **quote removal**.

So if you type:

```bash
printf '<%s>\n' "hello"
```

the program gets `hello`, not `"hello"` with quote characters.

---

### Quoting does not "turn text into a string"

People often say quotes "make a string."

That is too vague for shell reasoning.

All command arguments are already byte/string-like data at the process interface.

Quotes are primarily **syntax interpreted by the shell**.

Compare:

```bash
printf '<%s>\n' hello
```

and:

```bash
printf '<%s>\n' "hello"
```

Both normally pass the same argument `hello`.

The quotes matter when the content contains characters the shell would otherwise treat specially:

```bash
printf '<%s>\n' "hello world"
printf '<%s>\n' '$HOME'
printf '<%s>\n' "*.txt"
```

Each quotation choice changes which shell transformations remain possible.

---

### Double quotes and unquoted expansion are not equivalent

Let:

```bash
x='*.txt'
```

Now compare:

```bash
printf '<%s>\n' $x
```

with:

```bash
printf '<%s>\n' "$x"
```

The unquoted version may:

1. expand `$x` to `*.txt`;
2. treat that result as subject to word splitting;
3. perform filename expansion;
4. pass matching filenames.

The quoted version expands `$x` but protects the result from those later splitting and pathname-expansion steps.

`printf` may therefore receive completely different argument vectors from two command lines that differ only by quotes.

---

### Empty values expose the same rule

Let:

```bash
empty=''
```

Compare:

```bash
printf '[%s]\n' $empty
```

and:

```bash
printf '[%s]\n' "$empty"
```

In the unquoted case, the empty expansion can result in no field at that position.

In the quoted case, an explicit empty argument is preserved.

This matters when argument position carries meaning.

For example, "no argument" and "one empty argument" are not necessarily the same API call to a command or script.

---

### Globbing is performed by the shell, not by most commands

Suppose:

```bash
ls *.txt
```

If matching files exist, `ls` usually receives their names as separate arguments.

This means it is misleading to say:

> "`ls` expands `*.txt`."

The shell expands it.

You can observe the distinction with `printf`, which makes argument boundaries visible:

```bash
printf 'ARG=<%s>\n' *.txt
```

This technique is safer for learning than using a command that changes files.

---

### What if a glob matches nothing?

This is an important portability and Bash-configuration edge case.

In default Bash behavior, if a filename pattern has no matches, the pattern normally remains unchanged.

So:

```bash
printf '<%s>\n' no-such-*.xyz
```

often prints:

```text
<no-such-*.xyz>
```

But Bash options can change this.

For example:

- `nullglob` can make a nonmatching pattern disappear;
- `failglob` can turn a nonmatching pattern into an expansion error.

Therefore, "a glob always becomes filenames" is false.

Robust scripts should know which shell and options they rely on.

---

### Why `*` usually does not match hidden names

On typical Bash defaults, filename expansion patterns do not match a leading `.` at the beginning of a filename component unless the pattern itself begins appropriately or shell options alter the behavior.

So:

```bash
*
```

does not normally include:

```text
.hidden
```

This is why a directory can appear empty-ish under a simple glob while still containing dotfiles.

Again, shell options such as `dotglob` can change Bash behavior.

Do not turn one interactive observation into a universal law without checking the shell's configuration.

---

## Worked examples

### LNX-EX-025 — Make the argument vector visible

Create a disposable lab:

```bash
lab="$HOME/csf-shell-0009"
mkdir -p "$lab"
cd "$lab"
touch alpha.txt beta.txt 'report 1.txt' notes.md
```

Now ask `printf` to expose each argument boundary:

```bash
printf 'ARG=<%s>\n' *.txt
```

Expected shape:

```text
ARG=<alpha.txt>
ARG=<beta.txt>
ARG=<report 1.txt>
```

The exact ordering follows the shell's pathname expansion and locale rules, so do not make the lesson depend on one universal order.

Now quote the pattern:

```bash
printf 'ARG=<%s>\n' '*.txt'
```

Output:

```text
ARG=<*.txt>
```

Now use a question mark:

```bash
touch a1.log a2.log abc.log
printf 'ARG=<%s>\n' a?.log
```

Likely matches:

```text
a1.log
a2.log
```

but not:

```text
abc.log
```

because `?` matches exactly one character.

#### Predict first

Before running each command, write down what you think the final arguments will be.

Then compare your prediction to `printf`.

That habit is more valuable than memorizing a wildcard table.

---

### LNX-EX-026 — One variable, one argument or several?

Stay in the lab and run:

```bash
value='alpha beta'
printf 'ARG=<%s>\n' $value
```

Observe the two arguments.

Then:

```bash
printf 'ARG=<%s>\n' "$value"
```

Observe the single argument.

Now use a filename:

```bash
file='report 1.txt'
printf 'ARG=<%s>\n' $file
```

The unquoted expansion does **not** magically know that the original string was intended as one filename. It is just text in a scalar variable, and ordinary unquoted splitting can make multiple fields.

Quoted:

```bash
printf 'ARG=<%s>\n' "$file"
```

passes the intended filename as one argument.

Now make the variable contain a glob:

```bash
pattern='*.txt'
printf 'ARG=<%s>\n' $pattern
```

The unquoted result may be pathname-expanded.

Quoted:

```bash
printf 'ARG=<%s>\n' "$pattern"
```

passes literal `*.txt`.

This gives one compact chain:

```text
unquoted variable
    ↓
parameter expansion
    ↓
possible word splitting
    ↓
possible filename expansion
    ↓
argv
```

while:

```text
double-quoted variable
    ↓
parameter expansion
    ↓
one protected field
    ↓
argv
```

for the ordinary scalar-variable cases we are studying.

---

### LNX-EX-027 — Command substitution and the boundary between text and arguments

First inspect a simple substitution:

```bash
printf 'ARG=<%s>\n' "$(printf 'alpha\nbeta\n')"
```

The inner `printf` writes two lines plus a trailing newline.

Command substitution removes trailing newlines from the captured result, so the quoted outer substitution becomes one argument containing an embedded newline.

Your terminal may display it as:

```text
ARG=<alpha
beta>
```

Now remove the outer double quotes:

```bash
printf 'ARG=<%s>\n' $(printf 'alpha\nbeta\n')
```

With ordinary splitting rules, the result becomes multiple fields, commonly:

```text
ARG=<alpha>
ARG=<beta>
```

This is not `printf` deciding to split output.

It is the shell processing the unquoted substitution result.

Now capture a real system value:

```bash
kernel="$(uname -r)"
printf 'kernel=<%s>\n' "$kernel"
```

The pattern to notice is:

1. inner command runs;
2. stdout is captured;
3. trailing newline characters are removed by command substitution;
4. quote context determines what later splitting/globbing is allowed;
5. final fields become command arguments.

---

## A safe default: quote scalar expansions

When a shell variable represents one path, one username, one option value, one message, or one other scalar argument, prefer:

```bash
"$variable"
```

rather than:

```bash
$variable
```

Examples:

```bash
printf '%s\n' "$file"
cd "$directory"
cp -- "$source" "$destination"
```

The `--` in the final example is a different safety mechanism: many commands use it to mark the end of options, so a filename beginning with `-` is less likely to be misread as an option.

Quoting solves shell expansion problems.
`--` solves an option-parsing ambiguity in commands that support it.

They address different layers.

Do not confuse them.

---

## Why storing "a command" in a scalar string is fragile

A common beginner attempt is:

```bash
cmd='printf "%s\n" hello world'
$cmd
```

This does not ask Bash to reparse the variable's contents as if you had typed the original source code.

Expansion, splitting, quoting, and syntax do not compose that way.

The quote characters stored inside the variable are ordinary data at that stage; they do not automatically regain their earlier syntactic role.

If you need multiple arguments in Bash, arrays are usually the right structure:

```bash
args=(printf '%s\n' 'hello world')
"${args[@]}"
```

Arrays are beyond the formal scope of this lesson, but the design principle matters now:

> represent an argument list as an argument list, not as one string that you hope the shell will reinterpret.

Avoid reaching for `eval` as a repair. `eval` deliberately reparses text as shell code and introduces a much larger correctness and security surface.

---

## Expansion order: enough detail to reason, not enough to drown

For Bash, a useful simplified sequence is:

```text
parse shell syntax and quote context
        ↓
brace expansion
        ↓
tilde / parameter / arithmetic / command substitution
        ↓
word splitting
        ↓
filename expansion
        ↓
quote removal
        ↓
command execution
```

Some categories have special cases, and process substitution is an additional Bash feature on supporting systems.

The key causal relationship is this:

```text
unquoted expansion result
        ↓
can be split
        ↓
split fields can contain glob patterns
        ↓
patterns can expand to pathnames
```

That is why the shell's transformation pipeline matters more than any isolated "always quote" slogan.

---

## Quoting table

| Source form | Variable expansion? | Word splitting of expanded scalar? | Filename expansion from expanded scalar? | Typical intent |
|---|---:|---:|---:|---|
| `$x` | yes | yes | yes | deliberate shell splitting/globbing, or a bug |
| `"$x"` | yes | no | no | one ordinary argument |
| `'$x'` | no | no | no | literal characters `$x` |
| `\*` | not relevant | not relevant | no | literal `*` |
| `*.txt` | not variable expansion | n/a | yes | matching pathnames |
| `'*.txt'` | no | no | no | literal pattern text |

This table is intentionally scoped to the ordinary scalar cases in this lesson. Shell arrays, `"$@"`, pattern contexts, arithmetic contexts, and other syntax add rules of their own.

---

## Where intuition breaks

### 1. "Spaces separate arguments"

Sometimes.

Literal unquoted shell syntax spaces separate words during parsing.

But a space inside quotes can remain inside one argument:

```bash
printf '<%s>\n' "two words"
```

And a pathname produced by globbing can contain spaces while still being one field.

So the real model is not "every space means a new argument."

---

### 2. "Quotes are passed to the program"

Usually not.

In:

```bash
printf '%s\n' "hello"
```

the quote characters are shell syntax and are removed.

The program receives `hello`.

If you want literal quote characters in an argument, you must construct them as data.

---

### 3. "The command understands `*`"

Often false.

The shell usually expands an unquoted glob before launching the command.

Some programs also implement their own pattern languages, but that is a separate layer.

---

### 4. "Single and double quotes are interchangeable"

False.

```bash
printf '%s\n' '$HOME'
```

prints literal `$HOME`.

```bash
printf '%s\n' "$HOME"
```

prints the value of the parameter while protecting the result as one ordinary field.

---

### 5. "If a variable contains quotes, those quotes will protect spaces"

False in ordinary expansion.

```bash
x='"two words"'
```

does not recreate original shell quoting when you later write:

```bash
printf '<%s>\n' $x
```

The stored quote characters are data, not automatically active parser syntax.

---

### 6. "A glob with no matches becomes nothing"

Not in default Bash.

It normally remains literal, unless options such as `nullglob` or `failglob` alter behavior.

This is exactly the kind of shell-specific state that can make scripts behave differently.

---

### 7. "`*` includes every file"

Not necessarily.

Leading-dot names are normally excluded by default Bash pathname expansion unless the pattern or shell options account for them.

---

### 8. "Unquoted command substitution is harmless if the command prints one thing"

You are relying on properties of the output you may not control.

Whitespace can create fields.
Glob characters in those fields can trigger pathname expansion.

Quoted command substitution:

```bash
"$(command)"
```

is the safer default when the output is intended as one argument.

---

### 9. "Globs and regexes are basically the same"

They are different languages.

`*.txt` is a shell glob.
`.*\.txt` is a regex-like pattern.

They belong to different parsers and match under different rules.

---

## Active work

Use a disposable directory and `printf` so that you can inspect arguments without modifying important files.

### Exercise 1 — predict `argv`

Assume the current directory contains:

```text
a.txt
b.txt
two words.txt
notes.md
```

Predict what follows the format argument in each command:

```bash
printf '<%s>\n' *.txt
printf '<%s>\n' '*.txt'
printf '<%s>\n' "*.txt"
printf '<%s>\n' \*.txt
```

Then explain why the last three can all pass literal `*.txt` even though they use different shell syntax.

---

### Exercise 2 — variable boundary

Run:

```bash
x='alpha beta'
printf '<%s>\n' $x
printf '<%s>\n' "$x"
```

Explain the transformation pipeline for each.

Do not answer only "quotes preserve spaces." Name the stages that are suppressed or allowed.

---

### Exercise 3 — empty argument

Run:

```bash
x=''
printf 'counted=<%s>\n' $x
printf 'counted=<%s>\n' "$x"
```

Explain why "zero fields from this expansion" and "one empty field" are different states.

Think of one command-line interface where that distinction could matter.

---

### Exercise 4 — glob from a variable

Create:

```bash
touch one.log two.log
pattern='*.log'
```

Predict:

```bash
printf '<%s>\n' $pattern
```

and:

```bash
printf '<%s>\n' "$pattern"
```

Then verify.

Which line treats `*.log` as a filename pattern?
Which passes it as literal data?

---

### Exercise 5 — no-match behavior

Choose a deliberately impossible pattern:

```bash
printf '<%s>\n' definitely-no-file-*.csf
```

Observe your Bash behavior.

Then inspect, without changing anything:

```bash
shopt -p nullglob failglob dotglob
```

Your result is evidence about your current shell configuration, not a universal statement about every shell.

---

### Exercise 6 — command substitution

Predict how many arguments are produced after the format string:

```bash
printf '<%s>\n' "$(printf 'red\nblue\n')"
```

and:

```bash
printf '<%s>\n' $(printf 'red\nblue\n')
```

Then run both.

Explain separately:

- what command substitution did;
- what quoting did;
- what word splitting did.

---

### Exercise 7 — distinguish shell pattern from regex

Explain why:

```bash
printf '<%s>\n' *.log
```

and a future command such as:

```bash
grep -E '.*\.log'
```

do not use the same pattern language even though both contain `*`.

Do not focus on `grep` behavior yet. Focus on **which component parses each pattern**.

---

### Exercise 8 — debug a fragile snippet

A script contains:

```bash
file='quarterly report.txt'
printf 'opening %s\n' $file
```

The author expects one filename.

1. What arguments can `printf` receive?
2. What is the smallest correction?
3. If `file` contained `*.txt`, what additional transformation could happen unquoted?
4. Why is storing literal quote characters inside `file` not the right fix?

---

## Retrieval / self-explanation

Close the lesson and answer from memory.

1. Does a typical program receive your original raw shell command line?
2. What role does the shell play before a command starts?
3. What is the main difference between single and double quotes?
4. What does `"$x"` protect against in the ordinary scalar-variable case?
5. What is word splitting?
6. What is pathname expansion?
7. Who usually expands `*.txt`: the shell or `ls`?
8. Why can a globbed filename containing a space still arrive as one argument?
9. What happens to quote characters used as shell syntax?
10. What does `$(command)` use from the inner command?
11. What happens to trailing newlines in command substitution?
12. Why can unquoted command substitution produce more than one argument?
13. Why is a shell glob not a regular expression?
14. What can `nullglob`, `failglob`, and `dotglob` change?
15. Why is "always quote everything" less useful than "decide the intended argument boundaries"?

If you cannot answer 1, 4, 7, and 15 clearly, revisit the mental model and worked examples before moving on.

---

## Connections

### Backward connection: shell, terminal, command, argument

LNX-0003 separated the terminal interface from the shell language and separated a command from its arguments.

This lesson makes that distinction operational.

The shell constructs the arguments.

The program receives the result.

---

### Backward connection: pathnames

Earlier file-navigation lessons treated pathnames as names of filesystem objects.

Now we see that pathnames can also be **generated by shell expansion**.

A glob is therefore not a special kind of path stored by the filesystem. It is shell syntax that may produce pathnames.

---

### Forward connection: redirection and pipelines

The next core lesson is **LNX-N-0010 — Standard streams, redirection, and pipelines**.

Redirection operators are also shell syntax.

Understanding that the shell interprets syntax before launching commands will make this much easier:

```bash
command > file
```

does not normally mean the program receives `>` and `file` as ordinary arguments.

The shell handles the redirection layer.

---

### Forward connection: environment and startup state

Later, **LNX-N-0017** deepens shell variables, exported environment variables, `PATH`, startup files, and exit status.

This lesson deliberately does not collapse shell variables and environment variables into one concept.

For now, the important idea is parameter expansion and quote context.

---

### Forward connection: safe automation

Future lessons on `find`, `xargs`, scripting, and text processing will depend on correct argument-boundary reasoning.

Many shell bugs that look like "weird filename problems" are actually failures to model fields and expansions.

---

## What this unlocks

You should now be able to:

- explain why the shell can transform text before a program runs;
- distinguish literal source text from final command arguments;
- use single quotes, double quotes, and backslash deliberately;
- predict ordinary variable expansion with and without quotes;
- explain word splitting rather than merely fearing spaces;
- use basic globs and distinguish them from regular expressions;
- understand that commands usually receive expanded pathnames rather than glob syntax;
- use quoted command substitution when one result should become one argument;
- recognize shell-option edge cases around unmatched and hidden-file globbing;
- debug shell behavior by making argument boundaries visible with `printf`.

The immediate next core lesson is:

**LNX-0010 — Standard streams, redirection, and pipelines.**

---

## References

- **LNX-REF-001** — IEEE / The Open Group, *POSIX.1-2024 Shell Command Language*, especially quoting and word expansion.
- **LNX-REF-005** — GNU Project, *Bash Reference Manual*, especially Quoting and Shell Expansions.
