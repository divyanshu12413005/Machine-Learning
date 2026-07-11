import numpy as np

a=np.array([1,2,3,4])
print(a)
print(type(a))

# 2D and #3D arrays
b=np.array([[1,2,3],[4,5,6]])
# print(b)

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])   
# print(c)

# data type of array
d=np.array([1,2,3],dtype='float')
# print(d)

# arrange function in numpy
e=np.arange(0,10,2)              # creates an array with values from 0 to 10 (exclusive 10) with a step of 2
# print(e)

# reshape function in numpy 
f=np.arange(1,13).reshape(3,4)   #i.e creates an array with values from 1 to 12 and reshapes it into a 3x4 array
# print(f)

# np.ones and np.zeros functions in numpy
g=np.ones((2,3))                 # creates a 2x3 array filled with ones it is use ful for initializing weights in neural networks
# print(g)

h=np.zeros((2,3))                # creates a 2x3 array filled with zeros it is useful for initializing biases in neural networks
# print(h)

# np.random.rand and np.random.randn functions in numpy 
i=np.random.rand(2,3)             # creates a 2x3 array with random values between 0 and 1
# print(i)

j=np.random.randn(2,3)            # creates a 2x3 array with random values from a standard normal distribution
# print(j)

# np.linspace function in numpy
k=np.linspace(-10,10,5)              # creates an array with 5 evenly spaced values between -10 and 10
# print(k)

# np.identity function in numpy
l=np.identity(3)                  # creates a 3x3 identity matrix
# print(l)