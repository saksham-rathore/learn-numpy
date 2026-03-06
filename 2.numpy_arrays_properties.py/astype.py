import numpy as np

arr = np.array([1.2, 5.2, 7.5])
print(arr.dtype)
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)