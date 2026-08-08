# Chapter 10 - OOP

## Overview
This chapter introduces object-oriented programming (OOP) concepts in Python, including classes, instance attributes, class attributes, `self`, constructors, and methods.

## Files
- `01_class.py`
  - Defines a simple class with class attributes and adds instance attributes afterward.
- `02_instance_vs_class_attr.py`
  - Shows the difference between class attributes and instance attributes.
- `03_self.py`
  - Demonstrates using `self` inside class methods and includes a static method.
- `04_constructor.py`
  - Uses the constructor (`__init__`) to initialize object attributes and create instances.

## Problems
The `Problems/` folder contains practice examples for classes and objects:

- `01_problem.py`
  - Defines a `Programers` class and uses the constructor to display user-provided employee details.
- `02_problem.py`
  - Defines a `Calculator` class with methods for square, cube, and square root calculations.
- `03_problem.py`
  - Shows how class attributes can be overridden at the instance level.
- `04_problem.py`
  - Adds a static method to the `Calculator` class and calls it on an instance.
- `05_problem.py`
  - Implements a `Train` class with booking, status, and fare methods.
- `06_problem.py`
  - Confirms that objects can call class methods using `self` (or a custom name) in the method signature.

## Key Concepts
- Classes define templates for objects and can contain attributes and methods.
- Class attributes are shared by all instances unless overridden.
- Instance attributes are specific to each object.
- `__init__` is the constructor used to initialize new objects.
- `self` refers to the current instance inside class methods.
- Static methods do not require access to the instance and can be called on the class or instance.

## Usage
Run examples from the chapter folder:
- `python 01_class.py`
- `python 02_instance_vs_class_attr.py`
- `python 03_self.py`
- `python 04_constructor.py`
- `python Problems\01_problem.py`
- `python Problems\02_problem.py`
- `python Problems\03_problem.py`
- `python Problems\04_problem.py`
- `python Problems\05_problem.py`
- `python Problems\06_problem.py`

## Notes
- Use class attributes for values shared across all instances.
- Use instance attributes for values that vary per object.
- The constructor helps create objects with initial state.
