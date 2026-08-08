# Chapter 12 - Advanced Python 1

## Overview
This chapter explores advanced Python features including the walrus operator, type hints, `match` statements, exception handling, module imports, global variables, `enumerate()`, and list comprehensions.

## Files
- `01_walrus.py`
  - Demonstrates the walrus operator (`:=`) to assign and evaluate in one expression.
- `02_types.py`
  - Shows Python type hints using `int`, `str`, and function return annotations.
- `03_match_case.py`
  - Demonstrates the `match` / `case` statement for pattern-like branching.
- `04_exception.py`
  - Shows `try` / `except` for handling `ValueError` and general exceptions.
- `05_raising_exceptions.py`
  - Shows how to raise a custom exception (`ZeroDivisionError`) manually.
- `06_try_else.py`
  - Demonstrates `try`, `except`, and `else` blocks.
- `07_try_finally.py`
  - Demonstrates `finally`, which runs regardless of success or exception.
- `08_main.py`
  - Imports `myFonc` from `module.py` to show module importing.
- `09_global.py`
  - Demonstrates the `global` keyword and modifying a global variable inside a function.
- `10_enumerate.py`
  - Uses `enumerate()` to loop with index and value.
- `11_list_comprehensions.py`
  - Demonstrates a list comprehension to square list values.
- `module.py`
  - Defines a function and shows the `if __name__ == "__main__"` pattern.

## Problems
The `Problems/` folder contains example practice files:

- `01_problem.py`
  - Attempts to read several files and handles missing files with exceptions.
- `02_problem.py`
  - Prints specific list items using `enumerate()` and index checks.
- `03_problem.py`
  - Creates a multiplication table using a list comprehension.
- `04_problem.py`
  - Demonstrates exception handling during division.
- `05_problem.py`
  - Generates a multiplication table and writes it to `tables.txt`.
- `2.txt`
  - Example text file used by problem scripts.
- `tables.txt`
  - Output file written by `05_problem.py`.

## Key Concepts
- The walrus operator saves repeated expressions by assigning inside conditions.
- Type hints improve code readability and tool support but are not enforced at runtime.
- `match` / `case` provides a modern alternative to chained `if` / `elif`.
- Use `try`, `except`, `else`, and `finally` for robust error handling.
- Raise exceptions intentionally when invalid conditions occur.
- Use `if __name__ == "__main__"` to separate module execution from import behavior.
- Global variables can be modified inside functions with the `global` keyword.
- `enumerate()` pairs each item with an index.
- List comprehensions offer concise list creation syntax.

## Usage
Run examples from the chapter folder:
- `python 01_walrus.py`
- `python 02_types.py`
- `python 03_match_case.py`
- `python 04_exception.py`
- `python 05_raising_exceptions.py`
- `python 06_try_else.py`
- `python 07_try_finally.py`
- `python 08_main.py`
- `python 09_global.py`
- `python 10_enumerate.py`
- `python 11_list_comprehensions.py`
- `python Problems\01_problem.py`
- `python Problems\02_problem.py`
- `python Problems\03_problem.py`
- `python Problems\04_problem.py`
- `python Problems\05_problem.py`

## Notes
- `03_match_case.py` requires Python 3.10+.
- `08_main.py` depends on `module.py` in the same folder.
- Several problem scripts are interactive and may require user input.
