#The np.newaxis keyword adds a new axis to
# the array which helps in converting a 1D array into a row or column vector.
import numpy as np

arr = np.array([1, 2, 3])

print(arr[:, np.newaxis])#Here it adds a new axis helps in converting the 1D
# array into a 2D column vector with shape (3,1).