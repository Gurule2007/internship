import numpy as np

# Create a 5x5 array of random integers between 1 and 100
arr = np.random.randint(1, 101, (5, 5))
print("Original array:-\n", arr)

# Find the min, max, mean, and sum of the array
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

# Replace all numbers > 50 with -1
arr[arr > 50] = -1
print("numbers > 50 with -1:-\n", arr)

# Save the array to a .npy file
np.save('array.npy:-\n', arr)

# Load the array from the .npy file and print its contents
loaded_arr = np.load('array.npy')
print("Loaded array:-\n", loaded_arr)