# Chapter 1 - Modules, Comments & Pip

## Overview
This chapter covers Python basics for working with modules, comments, and simple file examples.

## Files
- `fast.py`
  - Prints `Hello World!`.
- `module.py`
  - Demonstrates importing a module (`pyjokes`) and printing a joke.
  - Shows a multiline comment using triple quotes.
- `note.txt`
  - Contains chapter notes about REPL, modules, and comment types.

## Problems
The `Problems/` folder contains example practice files:

- `Problem_1.py`
  - Prints the poem `Twinkle, twinkle, little star` using a multiline string.
- `problem_2.py`
  - Demonstrates file I/O with `os.listdir()` and writing text to `test.txt`.
- `test.txt`
  - Contains sample text written by `problem_2.py`.

## Key Concepts
- Python REPL: run `python` in terminal to execute expressions interactively.
- Modules: use `import <module_name>` to reuse code from libraries.
- Comments:
  - Single-line comments begin with `#`.
  - Multiline comments can be written with triple quotes (`""" ... """`).

## Usage
1. Open a terminal in this folder.
2. Run examples like:
   - `python fast.py`
   - `python module.py`
   - `python Problems\Problem_1.py`
   - `python Problems\problem_2.py`

## Notes
- `module.py` requires the `pyjokes` package to be installed.
- To install it, run:
  - `pip install pyjokes`
