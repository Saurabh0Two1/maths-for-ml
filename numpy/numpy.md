# install numpy

## initialize package manager and virtual environment

```bash
uv venv
source .venv/bin/activate

uv init --bare
uv pip install numpy
uv add numpy
```

# Basics of NumPy

NumPy is the main package for scientific computing in Python. It performs a wide variety of advanced mathematical operations with high efficiency.

## Arrays

Learn more at arrays.py

Arrays are one of the core data structures of the NumPy library, essential for organizing your data. You can think of them as a grid of values, all of the same type. If you have used Python lists before, you may remember that they are convenient, as you can store different data types. However, Python lists are limited in functions and take up more space and time to process than NumPy arrays.

NumPy provides an array object that is much faster and more compact than Python lists. Through its extensive API integration, the library offers many built-in functions that make computing much easier with only a few lines of code. This can be a huge advantage when performing math operations on large datasets.

The array object in NumPy is called ndarray meaning 'n-dimensional array'. To begin with, you will use one of the most common array types: the one-dimensional array ('1-D'). A 1-D array represents a standard list of values entirely in one dimension. Remember that in NumPy, all of the elements within the array are of the same type.
