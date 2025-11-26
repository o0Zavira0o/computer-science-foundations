# File Archiving and Compression in Linux

While Windows or macOS often handle "zipping" as one action, Linux historically separates this into two distinct tasks: **Compressing** (making small) and **Archiving** (grouping together).

---

## 1. Compressing Files with `gzip`
The `gzip` (GNU Zip) utility is used to reduce the size of a **single file**. Think of this like putting a fluffy sweater into a vacuum-seal bag to save space.

*   **Behavior:** When you run `gzip` on a file, it creates a new compressed file ending in `.gz` and **deletes the original file**.
*   **To Compress:**
    $$ \texttt{gzip filename} $$
*   **To Uncompress:**
    $$ \texttt{gunzip filename.gz} $$

## 2. Archiving Files with `tar`
A critical limitation of `gzip`: it cannot bundle multiple files into one folder. For that, we use `tar` (Tape ARchive).

Think of `tar` as a suitcase. It doesn't necessarily make things smaller, but it lets you carry 50 items as a single piece of luggage.

### Creating an Archive
To create a bundle, we use specific "flags" (letters that tell the command what to do):

$$ \texttt{tar cvf archive\_name.tar file1 file2 file3} $$

*   **`c` (Create):** Tells the system we are making a new archive.
*   **`v` (Verbose):** "Talkative" mode. It lists the files on the screen as it adds them, so you know it's working.
*   **`f` (File):** Crucial flag. It tells the command, "The very next word I type is the name of the new archive file."

### Unpacking an Archive
To open the suitcase and get your files back, we switch the `c` flag to an `x` flag.

$$ \texttt{tar xvf archive\_name.tar} $$

*   **`x` (Extract):** Takes files out of the archive.
*   **Note:** This does **not** delete the `.tar` file; it just copies the contents out of it.

---

# 🛠️ Hands-On Lab: GitHub Codespaces

### Part 1: Setup
First, let's create a playground folder and make some dummy files to work with.

```bash
# 1. Create a directory for this lab
mkdir archive_lab

# 2. Go into the directory
cd archive_lab

# 3. Create three dummy text files
echo "Hello World" > file1.txt
echo "Linux is fun" > file2.txt
echo "Archiving is useful" > file3.txt

# 4. Check that they exist
ls -l
```

### Part 2: Working with `gzip`
Let's try to compress just `file1.txt`.

```bash
# 1. Compress file1
gzip file1.txt

# 2. Check the directory now
ls -l
```
**Observation:** Notice that `file1.txt` is gone! It has been replaced by `file1.txt.gz`.

Now, let's bring it back.
```bash
# 3. Uncompress the file
gunzip file1.txt.gz

# 4. Verify it is back to normal
ls -l
```

### Part 3: Working with `tar`
Now we will bundle all three files into a single archive named `my_backup.tar`.

```bash
# 1. Create the archive (c = create, v = verbose, f = filename)
tar cvf my_backup.tar file1.txt file2.txt file3.txt
```
**Observation:** You will see the list of files printed on the screen because we used the `v` flag.

```bash
# 2. Check the directory
ls -l
```
**Observation:** You now have your three original text files **plus** the new `my_backup.tar`.

### Part 4: Unpacking the Archive
To prove that the archive works, let's delete the original text files and try to restore them from the tarball.

```bash
# 1. Delete the original text files (DANGER: Be careful with rm)
rm file1.txt file2.txt file3.txt

# 2. Confirm they are gone (only the .tar should remain)
ls -l

# 3. Extract the files from the archive (x = extract)
tar xvf my_backup.tar

# 4. Verify everything is back!
ls -l
```

# Mastering Compressed Archives (.tar.gz)

In the previous section, we learned that `tar` groups files (like a suitcase) and `gzip` shrinks files (like a vacuum bag).

In the real world of Linux, these two are almost always used together. You will frequently encounter files ending in **.tar.gz** (or sometimes **.tgz**). This means a group of files was put into a "suitcase" (`tar`), and then that suitcase was "vacuum sealed" (`gzip`).

Here is how to handle them efficiently.

---

## 1. The Beginner Way (Two Steps)
If you are just starting out, it is helpful to think of unpacking a `.tar.gz` file as a reverse process. You have to remove the "vacuum seal" first, and then open the "suitcase."

1.  **Decompress:** Use `gunzip` to remove the `.gz` layer.
    $$ \texttt{gunzip file.tar.gz} $$
    *(Result: You now have `file.tar`)*

2.  **Unpack:** Use `tar` to open the archive.
    $$ \texttt{tar xvf file.tar} $$
    *(Result: You now have your actual files)*

---

## 2. The Professional Way (The `z` Shortcut)
Doing two steps every time is tiresome and wastes disk space (because you temporarily have a huge uncompressed `.tar` file sitting on your drive).

Modern Linux `tar` commands have a built-in shortcut: the **`z`** flag.

The `z` flag tells the system: *"I know this is compressed. Please run it through gzip for me automatically."*

### To Extract (Unpack)
$$ \texttt{tar \textbf{z}xvf archive.tar.gz} $$
*   `z`: Decompress (Filter through gzip)
*   `x`: Extract
*   `v`: Verbose (Show me the files)
*   `f`: File (Here comes the filename)

### To Create (Pack)
$$ \texttt{tar \textbf{z}cvf archive.tar.gz file1 file2} $$
*   `c`: Create

---

## 3. The `zcat` Pipeline (Advanced)
 This command unzips a file and prints the contents directly to the screen (Standard Output) without creating a temporary file on your hard drive.

We can use the "Pipe" symbol (`|`) to pass this output directly to `tar`.

$$ \texttt{zcat file.tar.gz \quad | \quad tar xvf -} $$

*   **`zcat`**: Unzips the data stream.
*   **`|`**: Passes that stream to the next command.
*   **`tar xvf -`**: The dash (`-`) tells tar, "Don't look for a file on the hard drive; read the data coming from the pipe."

---

# 🛠️ Hands-On Lab: GitHub Codespaces

Let's try all three methods in your terminal.

### Setup: Create a Playground
```bash
# 1. Create a folder for this lesson
mkdir compression_lab
cd compression_lab

# 2. Create some dummy files to compress
echo "Report Data 1" > report.txt
echo "Image Data" > image.jpg
echo "Script Data" > script.sh
```

### Exercise 1: The "Pro" Way (Create a compressed archive)
We will bundle these three files into one compressed file using the `z` flag.

```bash
# c = create, z = use gzip, v = verbose, f = filename
tar zcvf work_backup.tar.gz report.txt image.jpg script.sh
```
**Result:** Run `ls -l`. You will see `work_backup.tar.gz`. It is much smaller than the sum of the individual files.

### Exercise 2: The "Beginner" Way (Decompressing in 2 steps)
First, let's delete our original files so we can prove we are restoring them.
```bash
rm report.txt image.jpg script.sh
```

Now, let's unpack using the slow, two-step method:
```bash
# Step 1: Unzip (Removes .gz)
gunzip work_backup.tar.gz

# Check: You now have work_backup.tar
ls -l

# Step 2: Untar (Extracts files)
tar xvf work_backup.tar
```
**Result:** Your files are back!

### Exercise 3: The `zcat` Pipeline
Let's clean up and try the pipe method.

1. Re-create the compressed file (since we unzipped it in step 2):
   ```bash
   gzip work_backup.tar
   ```
2. Delete the loose files again:
   ```bash
   rm report.txt image.jpg script.sh
   ```
3. Use `zcat` and `tar` together:
   ```bash
   zcat work_backup.tar.gz | tar xvf -
   ```

**Result:** You will see the file names print to the screen, and if you run `ls`, your files have been restored successfully.