# Slicing in 1 D array
# syntax  arr[start:end:step]
import numpy as np
arr =np.array([0,1,2,3,4,5])
print(arr[1:4])
print(arr[0:8:2]) # step slicing
print(arr[::-1]) # reverse the array
# Slicing in 2 D array
# slicing can be applied to each dimension separetly
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0:2, 1:3])