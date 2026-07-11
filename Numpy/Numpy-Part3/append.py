import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)

print(np.append(a,300))

print(np.append(b,np.ones((b.shape[0],1)),axis=1))  #append a column of 1s to b