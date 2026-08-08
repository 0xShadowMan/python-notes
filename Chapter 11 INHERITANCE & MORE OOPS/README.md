# Chapter 11 - Inheritance & More OOP

## Overview
This chapter covers advanced object-oriented programming features in Python, including inheritance, multiple inheritance, multilevel inheritance, `super()`, class methods, property decorators, and operator overloading.

## Files
- `01_Inheritance.py`
  - Demonstrates single inheritance using a base class and a derived class.
- `02_multiple_inheritance.py`
  - Shows multiple inheritance from two parent classes.
- `03_multilevel_inheritance.py`
  - Demonstrates multilevel inheritance with a chain of three classes.
- `04_super_method.py`
  - Uses `super()` to call the parent class constructor in a derived class.
- `05_class_methods.py`
  - Demonstrates a `@classmethod` and how it accesses class attributes.
- `06_property_decorators.py`
  - Shows `@property` and setter usage for creating computed attributes.
- `07_operator_overloading.py`
  - Demonstrates operator overloading by defining `__add__` for a custom class.

## Problems
The `Problems/` folder contains practice examples:

- `01_problem.py`
  - Implements 2D and 3D vector classes to demonstrate inheritance and method overriding.
- `02_problem.py`
  - Uses multilevel inheritance with an `Animals`, `Pets`, and `Dog` class.
- `03_problem.py`
  - Uses `@property` and a setter to compute a salary after increment.
- `04_problem.py`
  - Implements complex number addition and multiplication with operator overloading.
- `05_problem.py`
  - Implements vector addition and dot product using operator overloading.
- `06_problem.py`
  - Adds a string representation for a vector class with `i`, `j`, and `k` unit notation.
- `07_problem.py`
  - Demonstrates overloading `__len__` for a custom vector-like object.

## Key Concepts
- Inheritance allows a class to inherit attributes and methods from a parent class.
- Multiple inheritance allows a class to derive from more than one parent class.
- Multilevel inheritance chains classes in a parent-child-grandchild hierarchy.
- `super()` calls methods from the parent class, especially constructors.
- `@classmethod` methods receive the class object instead of the instance.
- `@property` creates managed attributes with getter and setter behavior.
- Operator overloading enables custom behavior for operators like `+`, `*`, and `len()`.

## Usage
Run examples from the chapter folder:
- `python 01_Inheritance.py`
- `python 02_multiple_inheritance.py`
- `python 03_multilevel_inheritance.py`
- `python 04_super_method.py`
- `python 05_class_methods.py`
- `python 06_property_decorators.py`
- `python 07_operator_overloading.py`
- `python Problems\01_problem.py`
- `python Problems\02_problem.py`
- `python Problems\03_problem.py`
- `python Problems\04_problem.py`
- `python Problems\05_problem.py`
- `python Problems\06_problem.py`
- `python Problems\07_problem.py`

## Notes
- Use inheritance to reuse code and model relationships between classes.
- Use property decorators to simplify the interface of computed or managed attributes.
- Operator overloading makes custom classes behave more like built-in types.
