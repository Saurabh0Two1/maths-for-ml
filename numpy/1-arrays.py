import numpy as np

# 1D arrays
one_dimensional_arr = np.array([10, 12])
print(f"one_dimensional_arr - {one_dimensional_arr}")

# ========================================= #
# ============ Creating Arrays ============ #
# ========================================= #

# You can create a 1-D array by simply using the function array() which takes in a 
# list of values as an argument and returns a 1-D array.
a = np.array([1, 2, 3])
print(f"a - {a}")

# Another way to implement an array is using np.arange(). 
# This function will return an array of evenly spaced values within a given interval
b = np.arange(3)
print(f"b - {b}")

c = np.arange(1, 20, 3)
print(f"c - {c}")

lin_spaced_arr = np.linspace(0, 100, 5)
print(f"lin_spaced_arr - {lin_spaced_arr}")

# Default element type using linspace is float. We can specify type using dtype
lin_spaced_arr_int = np.linspace(0, 100, 5, dtype=int)
print(f"lin_spaced_arr_int - {lin_spaced_arr_int}")

# Character arrays
char_arr = np.array(['Welcome to Math for ML!'])
print(f"char_arr - {char_arr}")
print(f"char_arr.dtype - {char_arr.dtype}")

# ========================================= #
# ========= BUILT IN Functions ============ #
# ========================================= #


# One of the advantages of using NumPy is that you can easily create arrays with built-in functions.
# Returns a new array setting values to one.
ones_arr = np.ones(3)
print(f"ones_arr - {ones_arr}")

#  Returns a new array setting values to zero.
zeros_arr = np.zeros(3)
print(f"zeros_arr - {zeros_arr}")

# Returns a new uninitialized array. 
empty_arr = np.empty(3)
print(f"empty_arr - {empty_arr}")

# Returns a new array with values chosen at random.
rand_arr = np.random.rand(3)
print(f"rand_arr - {rand_arr}")

# ==================================================== #
# ============ Multidimensional arrays =============== #
# ==================================================== #

# Create a 2 dimensional array (2-D)
two_dim_arr = np.array([[1,2,3], [4,5,6]])
print(f"two_dim_arr \n {two_dim_arr}")

# An alternative way to create a multidimensional array is by reshaping the initial 1-D array.
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])
multi_dim_arr = np.reshape(one_dim_arr, (2, 3))
# Print the new 2-D array with two rows and three columns
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
                one_dim_arr, # the array to be reshaped
               (2,3) # dimensions of the new array
            )
# Print the new 2-D array with two rows and three columns
print(f"multi_dim_arr \n {multi_dim_arr}")

# Finding size, shape and dimension
# Dimension of the 2-D array multi_dim_arr
print(f"multi_dim_arr.ndim - {multi_dim_arr.ndim}")

# Shape of the 2-D array multi_dim_arr
# Returns shape of 2 rows and 3 columns
print(f"multi_dim_arr.shape - {multi_dim_arr.shape}")

# Size of the array multi_dim_arr
# Returns total number of elements
print(f"multi_dim_arr.size - {multi_dim_arr.size}")

# ==================================================== #
# ============== Array math operations =============== #
# ==================================================== #

arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

# Adding two 1-D arrays
addition = arr_1 + arr_2
print(f"addition - {addition}")

# Subtracting two 1-D arrays
subtraction = arr_1 - arr_2
print(f"subtraction - {subtraction}")

# Multiplying two 1-D arrays elementwise
multiplication = arr_1 * arr_2
print(f"multiplication - {multiplication}")

# Multiplying vector with a scalar (broadcasting)
vector = np.array([1, 2])
vector = vector * 1.6
print(f"vector - {vector}")

# ==================================================== #
# =============== Indexing and slicing =============== #
# ==================================================== #

# Select the third element of the array. Remember the counting starts from 0.
a = ([1, 2, 3, 4, 5])
print("a[2] - ", a[2])

# Indexing on a 2-D array
two_dim = np.array(([1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]))

# Select element number 8 from the 2-D array using indices i, j.
print("two_dim[2][1] - ", two_dim[2][1])

# slice - array[start:end:step]
# Slice the array a to get the array [1,3,5]
sliced_arr = a[::2]
print("sliced_arr - ", sliced_arr)

# Slice MultiDimensions arrays
# Slice the two_dim array to get the first two rows
sliced_arr_1 = two_dim[0:2]
print("sliced_arr_1 \n", sliced_arr_1)

sliced_two_dim_cols = two_dim[:,1]
print("sliced_two_dim_cols", sliced_two_dim_cols)

# ==================================================== #
# ===================== Stacking ======================#
# ==================================================== #
# Finally, stacking is a feature of NumPy that leads to increased customization of 
# arrays. It means to join two or more arrays, either horizontally or vertically,
# meaning that it is done along a new axis. 
# - `np.vstack()` - stacks vertically
# - `np.hstack()` - stacks horizontally
# - `np.hsplit()` - splits an array into several smaller arrays

a1 = np.array([[1,1], 
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])

# Stack the arrays vertically
vert_stack = np.vstack((a1, a2))
print("vert_stack \n", vert_stack)

# Stack the arrays horizontally
horz_stack = np.hstack((a1, a2))
print("horz_stack \n", horz_stack)

# Vector vs matrix representations

b1 = np.array([7, 1]) 
b2 =  np.array([[7], [1]])


print(f"Shape of b1 vactor: {b1.shape}")
print(f"Shape of b2 matrix: {b2.shape}")