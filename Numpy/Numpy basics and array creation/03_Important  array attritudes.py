import  numpy as np
x = np.array([[1,2,3],[4,5,6]])
m=x.shape # getting size of array in rows and coloumns
print(m)
n = x.ndim# gives dimension of array
print(n)
o =x.size # gives total no of elements
print(o)
p = x.dtype # gives the data type of an array
print(p)
q = x.nbytes
print(q)