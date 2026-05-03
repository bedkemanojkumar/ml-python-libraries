# creation of 3 d array by grouping the original elements into bloscks containing equal 2-d sections
import numpy as np
a= np.array([1,2,3,4,5,6,7,8])
r = a.reshape(2,2,2)
print(r)
