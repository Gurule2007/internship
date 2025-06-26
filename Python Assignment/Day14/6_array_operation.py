# 6.	Elementwise operations:
# o	Create two arrays of the same shape (e.g., a = [[1,2],[3,4]], b = [[5,6],[7,8]])
# o	Perform elementwise:
# 	Addition
# 	Subtraction
# 	Multiplication
# 	Division

import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

add = arr1 + arr2
sub = arr1 - arr2
mul = arr1 * arr2
Div = arr1 / arr2

print("Element wise Addition: /n",add)
print("Element wise Subtraction: ",sub)
print("Element wise Multiplication: ",mul)
print("Element wise Division: ",Div)



