import numpy as np

a1 = np.array([1, 2, 3, 4])
vec = np.vectorize(lambda x: x**2 + 2*x + 1)
res = vec(a1)
print(res)