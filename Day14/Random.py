import numpy as np

# Create an array of 5 random numbers between 1 and 100
arr1 = np.random.randint(1, 101, 5)
print("1 and 100:-", arr1)

# Create a 3x3 array with random floats between 0 and 1
arr2 = np.random.rand(3, 3)
print("3x3 array:-", arr2)

# Create a 4x4 array of random integers between 10 and 50
arr3 = np.random.randint(10, 51, (4, 4))
print("4x4 array:-", arr3)
