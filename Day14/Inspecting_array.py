
import numpy as np

# Create a sample array of float64
arr = np.array([1.2, 2.3, 3.4, 4.5, 5.6], dtype=np.float64)

# Find the shape, size, and dtype of the array
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)

# Change the dtype of the array from float64 to int32
arr_int32 = arr.astype(np.int32)
print("Dtype after conversion:", arr_int32.dtype)
print("Array after conversion:", arr_int32)

# Find the number of dimensions (ndim) of the array
print("Number of dimensions:", arr.ndim)

# Change the dtype from float64 to int32
arr_int32 = arr.astype(np.int32)
print("Array after conversion (int32):", arr_int32)



