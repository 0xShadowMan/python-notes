# Chapter 9 - File I/O

## Overview
This chapter covers Python file input/output operations, including reading, writing, appending, using `with`, and working with files in real tasks.

## Files
- `01_file_io.py`
  - Reads and prints the contents of `note.txt` using manual file open and close.
- `02_file_write.py`
  - Writes a string to `Chapter 9/myfile.txt` using write mode.
- `03_more_file_funtions.py`
  - Reads all lines from `file.txt` using `readlines()`.
- `04_append.py`
  - Opens `note.txt` in append mode and adds a new line.
- `05_with.py`
  - Demonstrates the `with` statement to open and read a file safely without calling `close()`.
- `note.txt`
  - Example text file used in file I/O demonstrations.
- `myfile.txt`
  - Generated or used by file write operations.

## Problems
The `Problems/` folder contains file-based practice exercises:

- `01_problem.py`
  - Reads `poems.txt` and checks if the word `twinkle` appears.
- `02_problem.py`
  - Reads and updates a high score in `Hi-score.txt`.
- `03_problem.py`
  - Generates multiplication tables from 2 to 20 and saves them to `Multiplication_Tables/`.
- `04_problem.py`
  - Replaces the word `Donkey` with `#####` in `pass.txt`.
- `05_problem.py`
  - Censors multiple words in `pass.txt` by replacing them with `#` characters.
- `06_problem.py`
  - Searches `log.txt` for the word `python` and reports presence.
- `07_problem.py`
  - Finds the line number where `python` appears in `log.txt`.
- `08_problem.py`
  - Copies the contents of `this.txt` to `this_copy.txt`.
- `09_problem.py`
  - Compares `this.txt` and `this_copy.txt` to verify they are identical.
- `10_problem.py`
  - Clears the contents of `this.txt` by opening it in write mode.
- `11_problem.py`
  - Copies `old.txt` to `renamed_by_python.txt` and deletes `old.txt`.

## Key Concepts
- Use `open(filename, mode)` for reading (`r`), writing (`w`), and appending (`a`).
- Use `read()`, `readlines()`, and `write()` for file operations.
- Prefer `with open(...) as file:` to auto-close files.
- Writing in `w` mode overwrites existing content.
- Use file operations for search, update, copy, and rename-style tasks.

## Usage
Run examples from the chapter folder:
- `python 01_file_io.py`
- `python 02_file_write.py`
- `python 03_more_file_funtions.py`
- `python 04_append.py`
- `python 05_with.py`
- `python Problems\01_problem.py`
- `python Problems\02_problem.py`
- `python Problems\03_problem.py`
- `python Problems\04_problem.py`
- `python Problems\05_problem.py`
- `python Problems\06_problem.py`
- `python Problems\07_problem.py`
- `python Problems\08_problem.py`
- `python Problems\09_problem.py`
- `python Problems\10_problem.py`
- `python Problems\11_problem.py`

## Notes
- Ensure the referenced files such as `poems.txt`, `Hi-score.txt`, `pass.txt`, `log.txt`, `this.txt`, and `old.txt` exist before running problem scripts.
- Use `with` to handle files safely and avoid forgetting `close()`.
