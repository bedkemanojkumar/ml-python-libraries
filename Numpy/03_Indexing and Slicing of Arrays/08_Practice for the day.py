import numpy as np
# Task 01 Basic indexing
a = np.array([1,2,4,5,6])
# print 1st,last element
print(a[0])
print(a[-1])

# Task 02 Slicing
arr = np.arange(2,11)
print(arr[2:7])
print(arr[1:11:2])
print(arr[: :-1])

# Task 03 2 D indexing
arr = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])
print(arr[1,1])
print(arr[1])
print(arr[:,2])

# Task 04 Modify Using Mask
# change values greater than 30
arr = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])
print(arr[arr>30])
arr[arr>30]=0
print(arr)
 # Task 05 Real ML  style practice
arr = np.array([12,55,23,89,34,90,10])
print(arr[arr>50]) # Extract values greater than 50
arr[arr>80] = -1 # Replace number gtreater than 80 with -1
print(arr)
m=arr[arr%2==0] # print all the even numbers
print(m)
