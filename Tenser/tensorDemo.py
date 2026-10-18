import numpy as np

#  0-D tensor   // also called scalar
a= np.array(42)
print(a)
print(a.ndim)

# 1-D tensor  // also called vector
b= np.array([1,2,3,4,5])  
# print(b)
print(b.ndim)

# 2-D tensor  // also called matrix
c= np.array([[1,2,3],[4,5,6]])
# print(c)
print(c.ndim)

# N-D tensor
d= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(d)
print(d.ndim)    #3-D
