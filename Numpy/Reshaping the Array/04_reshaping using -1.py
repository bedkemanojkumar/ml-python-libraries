# one dimension can be -1 ,letting numpy auto calculate it based on total elements
# returns : a new shaped ndarray
import numpy  as np
b = np.arange(6)
c=b.reshape(3,-1)
print(c)
a= np.array([1,2,3,4,5,6,7,8])
r = a.reshape(2,-1) # tells numpy to create 2 rows and compute dimension as 8/2=4 coloumns
print(r)