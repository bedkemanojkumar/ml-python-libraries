import numpy as np
# Indexing in 1  D array
a = np.array([10,20,30,40,50])
print(a[0])
# Indexing in 2 D array
a = np.array([[1,2],
              [3,4],
              [5,6]])
print(a[0,1])
print(a[1])# accesing a row
print(a[:,1])#accesing a coloumn
print(a[2,1])
# Indexing in 3 D array
cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[1, 2, 0])# 1->Specifies the 2 D slice,#2->Specifies the row in  slice#0->Specifies the coloumns in  slice.