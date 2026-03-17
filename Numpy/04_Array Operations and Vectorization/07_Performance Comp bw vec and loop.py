import numpy as np
import time

arr = np.arange(1_000_000)
# Loop
t1 = time.time()
loop_res = [x * 2 for x in arr]
t2 = time.time()

# Vectorized
t3 = time.time()
vec_res = arr * 2
t4 = time.time()

print("Loop Time:", t2 - t1)
print("Vectorized Time:", t4 - t3)