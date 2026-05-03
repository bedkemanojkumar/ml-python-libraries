#Simple Feature + Target
import numpy as np
x= np.random.rand(100,1)*100 # feature
noise=np.random.normal(0,1,(100,1)) # noise
y = 3*x+5+noise# Target
print(x[:5])
print("now Y")
print(y[:5])
