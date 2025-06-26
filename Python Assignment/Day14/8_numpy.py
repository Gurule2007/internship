# 8.	Use NumPy to compute:
# o	Square root of every element in an array
# o	Square of every element in an array
import numpy as np
s_array = np.array([11, 5, 67, 34, 98])

s_root = np.sqrt(s_array)
print("Square root: ",s_root)

sqr = np.square(s_array)
print("Square: ",sqr)