# 4.	Change the dtype of an array from float64 to int32.
print("\nChanging data type of array")
import numpy as np

arr2 = np.array([1.5, 2.5, 3.5], dtype=np.float64)
arr2_int32 = arr2.astype(np.int32)
print(arr2_int32.dtype)