# Allows us to filter elements from an array based om a condition and returns only those that meet it.
import numpy as np

arr = np.array([10, 15, 20, 25, 30])

print(arr[(arr > 10) & (arr < 30)])
print(arr[arr>20])