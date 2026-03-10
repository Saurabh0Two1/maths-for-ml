import numpy as np

###############################################################
########## SOLVING A LINEAR EQUATION ###########
###############################################################

# 1. Represent coefficients as matrix
A = np.array([
        [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
    ], dtype=np.dtype(float))

# 2. Represent constant as a vector
b = np.array([-10, 0, 17], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

# 3. Solve
x = np.linalg.solve(A, b)

print(f"Solution: {x}")

###############################################################
##########   Evaluating the Determinant of a Matrix ###########
###############################################################

d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")

###############################################################
#####  What happens if the system has no unique solution ######
###############################################################

A_2= np.array([
        [1, 1, 1],
        [0, 1, -3],
        [2, 1, 5]
    ], dtype=np.dtype(float))

b_2 = np.array([2, 1, 0], dtype=np.dtype(float))

# Error
# print(np.linalg.solve(A_2, b_2))


# Check determinant (hint: its zero)

d_2 = np.linalg.det(A_2)

print(f"Determinant of matrix A_2: {d_2:.2f}")