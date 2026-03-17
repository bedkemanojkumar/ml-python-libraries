import numpy as np
# Example 1
# Let fd array contains the fat ,protein,carbs in grps for 4 nutrinets and
# #[9,4,4] be a array which give calories per grame 9->fat,4->proetin,4->carbs calories per gram
fd = np.array([ [0.8, 2.9, 3.9],
                [52.4, 23.6, 36.5],
                [55.2, 31.7, 23.9],
                [14.4, 11.0, 4.9] ])

cpg = np.array([9, 4, 4])
res1 = fd * cpg#broadcasting pg array on d array to get Result is a matrix showing calorie
# contribution from fats, proteins and carbs for each food item.

print(res1)

# Example 2  Adjusting Temperature Data Across Multiple Locations
# taking temperatures of different locations and updating them
import numpy as np

temp = np.array([ [30, 32, 34, 33, 31],
                  [25, 27, 29, 28, 26],
                  [20, 22, 24, 23, 21] ])

corr = np.array([1.5, -0.5, 2.0])# updation value
res2 = temp + corr[:, None]
print(res2)


# Example 3   Normalizing Image Data
#Normalization is important in many real-world scenarios like image processing and machine learning because it:

#1.Centers data by subtracting the mean by ensuring features have zero mean.
#2.Scales data by dividing by the standard deviation by ensuring features have unit variance.
#3.Improves numerical stability and performance of algorithms like gradient descent.

import numpy as np

img = np.array([ [100, 120, 130],
                 [90, 110, 140],
                 [80, 100, 120] ])

m = img.mean(axis=0)
s = img.std(axis=0)
res3 = (img - m) / s
print(res3) # we get normalized values


# Example  4 Centering Data in Machine Learning
import numpy as np
#Centering data is an important step in many machine learning workflows.
# Broadcasting helps center the data efficiently by subtracting the mean from each feature.
# This example centers each feature by subtracting its mean using NumPy broadcasting.

data = np.array([ [10, 20],
                  [15, 25],
                  [20, 30] ])
m = data.mean(axis=0)
res = data - m
print(res)
