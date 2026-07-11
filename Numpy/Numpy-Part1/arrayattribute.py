import numpy as np

a1=np.arange(10)                                   # creates an array with values from 0 to 9
a2=np.arange(12,dtype='float').reshape(3,4)        # creates an array with values from 0 to 11 and reshapes it into a 3x4 array of float type
a3=np.arange(8).reshape(2,2,2)                     # creates a 3D array with values from 0 to 7 and reshapes it into a 2x2x2 array
# print(a1)
# print(a2)
# print(a3)

# ndim attribute of numpy array
# print(a1.ndim)                                     # prints the number of dimensions of the array 
print(a2.ndim)                                     
# print(a3.ndim)                                    

# shape attribute of numpy array  it returns a tuple representing the dimensions of the array
# print(a1.shape)                                
print(a2.shape)
# print(a3.shape)

# size attribute of numpy array  it returns the total number of elements in the array
# print(a1.size)
# print(a2.size)
# print(a3.size)

# itemsize attribute of numpy array  it returns the size in bytes of each element in the array
# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)


# dtype attribute of numpy array  it returns the data type of the elements in the array
# print(a1.dtype)