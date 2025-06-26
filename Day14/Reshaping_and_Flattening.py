import numpy as np
# Create an array with numbers from 1 to 12
arr = np.arange(1, 13)

# Reshape the array into (3, 4)
arr_reshaped = arr.reshape(3, 4)
print(arr_reshaped)

# Flatten the array back into a 1D array
arr_flattened = arr_reshaped.flatten()
print(arr_flattened)
