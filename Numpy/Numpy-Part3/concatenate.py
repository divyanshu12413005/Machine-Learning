import numpy as np

a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)
print(a)
print(b)

print(np.concatenate((a,b),axis=0))  #concatenate along the rows
print(np.concatenate((a,b),axis=1))  #concatenate along the columns