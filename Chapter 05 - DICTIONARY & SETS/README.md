# Chapter 5 - Dictionary & Sets

## Overview
This chapter covers Python dictionaries and sets, illustrating how dictionaries store key-value pairs and how sets store unique values.

## Files
- `01_dist.py`
  - Demonstrates a simple dictionary with string keys and values, and accessing values by key.
- `02_dict_methods.py`
  - Shows dictionary operations like `.items()`, `.keys()`, `.values()`, `.update()`, and `.get()`.
- `03_sets.py`
  - Demonstrates set creation and shows how sets automatically remove duplicate values.
- `04_union_intersection.py`
  - Shows set union and intersection operations.
- `note.txt`
  - Includes chapter notes on dictionary and set concepts.

## Problems
The `Problem/` folder contains practice files for dictionaries and sets:

- `01_Problem.py`
  - Bangla-to-English dictionary example with user input.
- `02_problem.py`
  - Builds a set from user-entered numbers and prints the unique values.
- `03_problem.py`
  - Demonstrates that sets can hold mixed types but preserve uniqueness.
- `04_problem.py`
  - Shows that numeric values and strings are treated differently in a set.
- `05_problem.py`
  - Demonstrates that `{}` creates an empty dictionary, not a set.
- `06_problem.py`
  - Collects friend names and languages into a dictionary.
- `07_problem.py`
  - Notes that later dictionary entries overwrite earlier values for duplicate keys.
- `08_problem.py`
  - Notes that sets allow duplicate values without error but store only unique elements.
- `09_problem.py`
  - Shows that sets cannot contain mutable elements like lists.

## Key Concepts
- Dictionaries store data as key-value pairs and are indexed by keys.
- Use `{}` or `dict()` to create a dictionary.
- Sets store only unique elements.
- Use `{}` for set literals with values inside, and `set()` for an empty set.
- Set operations include `.union()` and `.intersection()`.

## Usage
Run the chapter examples from this folder:
- `python 01_dist.py`
- `python 02_dict_methods.py`
- `python 03_sets.py`
- `python 04_union_intersection.py`
- `python Problem\01_Problem.py`
- `python Problem\02_problem.py`
- `python Problem\03_problem.py`
- `python Problem\04_problem.py`
- `python Problem\05_problem.py`
- `python Problem\06_problem.py`
- `python Problem\07_problem.py`
- `python Problem\08_problem.py`
- `python Problem\09_problem.py`

## Notes
- `01_dist.py` and `06_problem.py` require interactive input.
- Use `dictionary.get(key, default)` to avoid errors when a key does not exist.
- Remember that tuples and lists cannot be elements of a set if they are mutable.
