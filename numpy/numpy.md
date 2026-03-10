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

## Vectors vs Matrices numpy

In NumPy, the shape of a vector (a 1-dimensional array) is a tuple with a single element, representing the number of elements it contains. This can be accessed using the .shape attribute.

Examples of Vector Shapes

| Array Definition       | Code                   | Shape | Output    | Dimensions (.ndim) |
| ---------------------- | ---------------------- | ----- | --------- | ------------------ |
| 1-D array (4 elements) | np.array([1, 2, 3, 4]) | (4,)  | [1 2 3 4] | 1                  |
| 1-D array (3 elements) | np.array([1, 2, 3])    | (3,)  | [1 2 3]   | 1                  |
| Scalar (0-D array)     | np.array(5)            | ()    | 5         | 0                  |

Trailing comma: The comma in (4,) is Python's way of indicating a tuple with a single element, not an empty second dimension.

Difference from matrices: A true 1D vector with shape (n,) is different from a 2D row vector with shape (1, n) or a 2D column vector with shape (n, 1). Transposing a (n,) vector does not change its shape, while transposing (1, n) results in (n, 1).

# Numpy linalg sub library

```
See solving-linear-equations.py for code
```

1 - Representing and Solving a System of Linear Equations using Matrices
1.1 - System of Linear Equations
1.2 - Solving Systems of Linear Equations using Matrices
1.3 - Evaluating the Determinant of a Matrix
1.4 - What happens if the system has no unique solution?

# Vector Operations: Scalar Multiplication, Sum and Dot Product of Vectors

## Topics [see vector-operations.py]

1 - Scalar Multiplication
2 - Sum of Vectors
3 - Norm of a vector
4 - Dot product

### loop vs np.dot vs @

loop version: 123.25286865234375 ms
np.dot() function: 1.1188983917236328 ms
@ function: 7.949590682983398 ms

# Matrix Multiplication

## Topics [see 5-matrix-multiplication.py]

1 - matrix multiplication in numpy and python
