# Chapter 13 - Advanced Python 2

## Overview
This chapter covers advanced Python features such as virtual environments, lambda functions, string joining, formatted strings, and functional programming tools like `map`, `filter`, and `reduce`.

## Files
- `01_venv.py`
  - Contains a short reference on creating and using virtual environments with `venv` and `pip`.
- `02_lambda.py`
  - Demonstrates a simple lambda function for squaring a number.
- `03_join.py`
  - Shows how to join a list of strings using the `join()` method.
- `04_format.py`
  - Demonstrates string formatting with the `.format()` method.
- `05_map_filter_reduce.py`
  - Demonstrates `map`, `filter`, and `reduce` for list transformation and aggregation.
- `requirements.txt`
  - Example package list used for reproducing virtual environments.

## Problems
The `Problems/` folder contains practice examples related to advanced Python usage:

- `01_problem.py`
  - Notes commands for creating and using virtual environments and requirements files.
- `02_problem.py`
  - Uses `.format()` with user input and handles invalid integer input with `try`/`except`.
- `03_problem.py`
  - Generates a multiplication table as a single joined string.
- `04_problem.py`
  - Filters a list for numbers divisible by 5 using `filter()`.
- `05_problem.py`
  - Finds the largest number in a list using `reduce()`.
- `06_problem.py`
  - Contains virtual environment setup commands for `shadowEnv` and `requirements.txt`.
- `07_problem.py`
  - Demonstrates a simple Flask web application.

## Key Concepts
- Virtual environments isolate project dependencies and avoid package conflicts.
- Lambda functions provide concise anonymous function syntax.
- `join()` constructs strings from sequences of strings.
- `.format()` formats values into string templates.
- `map()` applies a function to each item in a list.
- `filter()` selects items from a list using a predicate function.
- `reduce()` aggregates list values with a binary function.
- Flask can be used to build a minimal web application.

## Usage
Run examples from the chapter folder:
- `python 02_lambda.py`
- `python 03_join.py`
- `python 04_format.py`
- `python 05_map_filter_reduce.py`
- `python Problems\02_problem.py`
- `python Problems\03_problem.py`
- `python Problems\04_problem.py`
- `python Problems\05_problem.py`
- `python Problems\07_problem.py`

## Notes
- `01_venv.py` and `Problems/01_problem.py` explain how to create and manage virtual environments.
- `Problems/07_problem.py` requires Flask to be installed in the current environment.
- `requirements.txt` and `Problems\recurments.txt` contain package lists for environment setup.
