# used to select  all dimensions which are not explicity mentioned
import numpy as np
cube = np.random.rand(4, 4, 4)
print(cube[..., 0])#Here it selects all elements in the first
# two dimensions and 0 selects the first element along the last dimension for each.