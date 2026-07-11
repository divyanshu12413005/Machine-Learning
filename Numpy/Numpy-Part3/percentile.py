import numpy as np

a=np.random.randint(1,100,20)

print(a)

print(np.percentile(a,100))  #return the 100th percentile of the elements
