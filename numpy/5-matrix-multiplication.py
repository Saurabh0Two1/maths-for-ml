import numpy as np

A = np.array([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
print("Matrix A (3 by 3):\n", A)

B = np.array([[2, 2], [5, 7], [4, 4]])
print("Matrix B (3 by 2):\n", B)

print("A x B using np.matmul \n", np.matmul(A, B))

print("A x B using python @ \n", A @ B)

try:
    np.matmul(B, A)
except ValueError as err:
    print("error mismatching dims np matmul ",err)

try:
    B @ A
except ValueError as err:
        print("error mismatching dims @",err)


x = np.array([1, -2, -5])
y = np.array([4, 3, -1])

print("Shape of vector x:", x.shape)
print("Number of dimensions of vector x:", x.ndim)

print("Shape of vector y:", y.shape)
print("Number of dimensions of vector y:", y.ndim)

print("two vectors can by np.matmul ed even if dimensions do not match", np.matmul(x, y))

x1 = x.reshape(3, 1)
y1 = y.reshape(3, 1)


try:
    np.matmul(x1, y1)
except ValueError as err:
    print("error mismatching dims np on reshape",err)   

# matrix multplication can also be done using np.dot using broadcasting of dot product
print("matrix multiply A x B using np.dot", np.dot(A, B))