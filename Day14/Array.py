import numpy as np
# Create a 1D array of numbers from 1–10.
arr1d = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(arr1d)

# Create an array of 10 zeros.
zeros = np.zeros((10)) 
print(zeros)

# Create an array of 5 ones.
ones = np.ones((5))  # 2x3x4 array of 1's
print(ones)

# Create an array of even numbers from 2–20.
even_no = np.arange(2,21,2)
print(even_no)

# Random float between 0 and 1
print(np.random.random())

# Create an array of shape (3, 3) filled with the number 7.
shape =np.full((3,3),7)
print(shape)

# Create an identity matrix of size 4x4.
i_matrix = np.eye(4)
print(i_matrix)