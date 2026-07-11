import numpy as np

a=np.random.randint(1,100,15)

print(np.expand_dims(a,axis=0))  #add a new axis along the rows
print(np.expand_dims(a,axis=1))  #add a new axis along the columns