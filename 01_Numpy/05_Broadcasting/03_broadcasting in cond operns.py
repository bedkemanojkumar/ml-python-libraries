import numpy as np
# using np.where to pick varibles instead of boolean values

a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)
#ages > 18 creates a Boolean array by checking every value at once (broadcasting).
#np.where() picks "Adult" for True and "Minor" for False without any loop.
#The result is an array labeling each age correctly.