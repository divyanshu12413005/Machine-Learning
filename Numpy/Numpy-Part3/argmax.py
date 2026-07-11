import numpy as np

a=np.random.randint(1,100,20)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)

print(np.argmax(a))  #return the index of the maximum element
print(np.argmax(b,axis=0))  #return the indices of the maximum elements along the columns


# np.argmin() returns the indices of the minimum elements along the specified axis
print(np.argmin(a))  #return the index of the minimum element