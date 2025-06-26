import numpy as np

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7,])

# Extract the first 5 elements
first_5 = arr_1d[:5]
print("First 5 elements:", first_5)

# Extract the last 3 elements
last_3 = arr_1d[-3:]
print("Last 3 elements:", last_3)

# Change every second element
arr_1d[1::2] = 0
print("Array after changing every second element:", arr_1d)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extract an element from a 2D array
element = arr_2d[2,2]
print("Element at row 1, column 1:", element)

# Slice a 2D array to get its first 2 rows and first 2 columns
slice_2d = arr_2d[:2, :2]
print("First 2 rows and first 2 columns:\n", slice_2d)

