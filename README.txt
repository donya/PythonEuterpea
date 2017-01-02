Python Euterpea
(c) Donya Quick 2016

Two versions of the PythonEuterpea are included:

- PythonEuterpea: a Python port of the Haskell Euterpea library. Haskell Euterpea 
  represents music as binary trees.

- PythonEuterpeaN: similar to the above but uses n-ary trees instead of binary trees 
  for representing music.

Functionality is otherwise the same for each.

To install:
1. Open a command prompt or terminal in the folder for the version you wish to install.
2. Run: python setup.py install

Both versions of PythonEuterpea require the python-midi and pygame libraries. If not installed automatically, you can install them with:
	pip install python-midi
	pip install pygame