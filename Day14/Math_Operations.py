import numpy as np

# Perform element-wise addition, subtraction, multiplication, and division between two arrays.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   
print(a - b)   
print(a * b)  
print(a / b)

# Perform power and square root operations.
print(a ** 2)  
print(np.sqrt(a))  

# Use np.sum(), np.mean(), np.min(), np.max(), and np.std().
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Min:", np.min(a))
print("Max:", np.max(a))
print("Standard deviation:", np.std(a))