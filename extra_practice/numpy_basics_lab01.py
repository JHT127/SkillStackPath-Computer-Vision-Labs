
# numpy_basics_lab01.py
# Lab 1 — Section 3.2: Getting hands-on with NumPy


import numpy as np  # Load NumPy with the standard alias "np"



# ── 1. Create a 1D array ────────────────────────────────────────────────────
# np.array() converts a Python list into a NumPy array.
# NumPy arrays support fast math operations that plain lists don't.
x = np.array([1, 2, 3])
print(x)  # Output: [1 2 3]





# ── 2. Vectorized math  ───────────────────────────────────────
# Multiplying by a scalar applies the operation to every element at once.
# No for-loop needed — NumPy does it internally in fast C code.
y = x * 10
print(y)  # Output: [10 20 30]






# ── 3. Create a 2D vector ───────────────────────────────────────────────────
# A 1D array with two elements — think of it as a point (x=1, y=2) in 2D space.
A = np.array([1, 2])
print(A)  # Output: [1 2]






# ── 4. Create a rotation matrix ─────────────────────────────────────────────
# A 2×2 matrix is written as a list of rows.
# This specific matrix rotates any 2D point 90° counter-clockwise.
#   [ 0  -1 ]
#   [ 1   0 ]
R = np.array([[0, -1], [1, 0]])
print(R)







# ── 5. Apply the rotation with a dot product ────────────────────────────────
# np.dot(matrix, vector) multiplies them together (matrix × vector).
# Geometrically: this rotates point A = [1, 2] by 90° CCW → result [-2, 1].
B = np.dot(R, A)
print(B)  # Output: [-2  1]







# ── 6. Inverse rotation — undo the previous rotation ────────────────────────
# The inverse of a 90° CCW rotation is a 90° CW rotation.
#   [ 0   1 ]
#   [-1   0 ]
# Applying it to B should give back the original A = [1, 2].
R_invers = np.array([[0, 1], [-1, 0]])
B_prime = np.dot(R_invers, B)
print(B_prime)  # Output: [1 2]  ← back to the original point






# ── 7. Inspect the shape of an array ────────────────────────────────────────
# .shape returns the dimensions as a tuple.
# (2,) means 1D array with 2 elements.
# For images: (height, width) for grayscale, (height, width, 3) for color.
print(A.shape)  # Output: (2,)