# Task 1 Create 1,2,3 D arrays
import numpy as np
a = np.array([1,2,3,4,5])
b=np.array([[2,3,4],[4,5,6]])
c = np.array([[[1,2],[3,4],[5,6]]])
print(a)
print(b)
print(c)
# Take 2  Checking the shape and type
c = np.array([[[1,2],[3,4],[5,6]]])
d=c.shape
print(d) #gives 1 layer,3 rows,2 coloumns
m = c.dtype
print(m)
# Task 3 Reshaping the array and print results
m =np.array([1,2,3,4,5,6,7,8])
n=m.reshape(2,4)
print(n)
i = m.reshape(2,2,2)
print(i)