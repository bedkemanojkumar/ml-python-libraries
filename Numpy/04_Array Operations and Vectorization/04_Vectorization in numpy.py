import numpy as np
# adding a number to each element
a = np.array([2,3,4,5,6,6])
num = 2
res=num+a
print(res)
# Add  and mul two arrays element wise
m = np.array([1,2,3])
n = np.array([4,5,6])
res = m+n
print(res)
res1=m*n
print(res1)
# Logical operators on arrays
m1 = np.array([100,20,36])
res2 = np.where(m1>25)#gives the index who is greater than 25
print(res2)
res3=m1>25# Gives Boolean value
print(res3)
