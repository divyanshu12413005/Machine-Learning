import numpy as np

a=np.random.randint(1,100,20)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)

print(np.cumsum(a))  #return the cumulative sum of the elements
print(np.cumsum(b,axis=0))  #return the cumulative sum along the columns

# cumprod() returns the cumulative product of the elements along the specified axis
print(np.cumprod(a))  #return the cumulative product of the elements