.. spx documentation master file, created by
   sphinx-quickstart on Tue Feb  4 08:29:21 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

spx documentation
=================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

====================
Python Cheat Sheet
====================

Basic Syntax
------------

- ``print("Hello, World!")``
- Comments: ``# single-line`` or ``'''multi-line'''``

Variables & Data Types
----------------------

- ``x = 5`` (int), ``3.14`` (float), ``"Hello"`` (str)
- Lists: ``[1, 2, 3]``
- Tuples: ``(a, b)``
- Dicts: ``{"key": "value"}``
- Sets: ``{1, 2, 3}``

Control Flow
------------

- ``if x > 0:``
- ``for i in range(5):``
- ``while condition:``

Functions
---------

.. code-block:: python

   def greet(name):
       return "Hi " + name

Lambda Functions: ``square = lambda x: x * x``

List Comprehensions
-------------------

- ``[x for x in range(10) if x % 2 == 0]``

String Methods
--------------

- ``"abc".upper()`` → ``'ABC'``
- ``" Hello ".strip()`` → ``'Hello'``
- ``"a,b,c".split(",")`` → ``['a', 'b', 'c']``
- ``"hello".replace("h", "H")`` → ``'Hello'``

Math & Modules
--------------

- ``import math`` → ``math.sqrt(16)``
- ``from random import randint`` → ``randint(1, 10)``

File I/O
--------

.. code-block:: python

   with open('file.txt') as f:
       data = f.read()

Writing to a file:

.. code-block:: python

   with open('file.txt', 'w') as f:
       f.write("Hello")

Exception Handling
------------------

.. code-block:: python

   try:
       x = 1 / 0
   except ZeroDivisionError:
       print("Error!")
   finally:
       print("Done")

Classes
-------

.. code-block:: python

   class Person:
       def __init__(self, name):
           self.name = name
       def greet(self):
           return "Hi " + self.name

Useful Built-in Functions
-------------------------

- ``len()``
- ``sum()``
- ``max()``
- ``min()``
- ``sorted()``

Common Data Structures
----------------------

- **Lists:** ``append()``, ``pop()``, ``extend()``
- **Dictionaries:** ``keys()``, ``values()``, ``get()``
- **Sets:** ``add()``, ``remove()``, ``union()``

Virtual Environments
--------------------

.. code-block:: bash

   python -m venv env
   source env/bin/activate  # On Unix/macOS
   env\Scripts\activate     # On Windows

Pip Commands
------------

.. code-block:: bash

   pip install package
   pip freeze > requirements.txt
   pip install -r requirements.txt

Quick Tips
----------

- Check Python version: ``python --version``
- Interactive mode: ``python -i script.py``
- REPL shortcut: ``python`` (starts an interactive shell)

.. list-table:: **Python String Functions**
   :header-rows: 1
   :widths: 20 80

   * - String Function
     - Explanation
   * - ``str.upper()``
     - Converts all characters in the string to uppercase.
   * - ``str.lower()``
     - Converts all characters in the string to lowercase.
   * - ``str.strip()``
     - Removes leading and trailing whitespace from the string.
   * - ``str.replace()``
     - Replaces occurrences of a substring with another string.
   * - ``str.split()``
     - Splits the string into a list based on a delimiter.
   * - ``str.find()``
     - Returns the index of the first occurrence of a substring.
   * - ``str.join()``
     - Joins elements of an iterable with the string as a separator.
   * - test
     - wheat