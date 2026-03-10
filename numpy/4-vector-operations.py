import numpy as np

# Scalar multiplication
v = np.array([[1],[3]])
print("scalar multiplication by 2 \n", 2*v)
print("scalar multiplication by 2 \n", -2*v)


# Vector addition

v = np.array([[1],[3]])
w = np.array([[4],[-1]])

print("adding vectors v & w: \n", v+w)
print("adding vectors v & w: \n", np.add(v, w))


# L2 norm -> magnitude of a vector
print("Norm of a vector v is", np.linalg.norm(v))

# Dot product

x = [1, -2, -5]
y = [4, 3, -1]

def dot(x, y):
    s = 0
    for xi, yi in zip(x,y):
        s += xi * yi
    
    return s

print("The dot product of x.y is", dot(x, y))
print("The dot product of x and y using np.dot(x,y)", np.dot(x, y)) 
print("The dot product of x and y using @: ", np.array(x) @ np.array(y))

# As both np.dot() and @ operators are commonly used, 
# it is recommended to define vectors as NumPy arrays to avoid errors.
# Let's redefine vectors 𝑥 and 𝑦 as NumPy arrays to be safe:
x = np.array(x)
y = np.array(y)

# Orthogonal dot is zero
i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
print("The dot product of i and j is", dot(i, j))
