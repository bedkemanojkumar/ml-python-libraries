# heaavly used in ML ( feature scaling , statistics)
import numpy as np
arr=np.array([10,20,29,25,30])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.reciprocal(arr))
print(np.power(arr,2))
arr1 = np.array([20,40,50,60,68])
print(np.power(arr,arr1))
# 2 D aggrregations
arr = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr,axis=0))# Coloumn wise
print(np.sum(arr,axis=1))#Row wise