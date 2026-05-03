# Allows us access elements of an array by using another array or list of incicies
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])
# Integer array indexing
print(arr[[0,2,4]])