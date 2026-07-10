import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

print("Original a1:", a1)
print("Reshaped a1 (2x5):\n", a1.reshape(2,5))

print("Original a2:\n", a2)
print("Transpose of a2:\n", a2.transpose())

print("Original a3:\n", a3)
print("Ravel of a3:", a3.ravel())   # ravel converts the any multi-dimensional array into a 1D array