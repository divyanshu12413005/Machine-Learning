import numpy as np

# list
a = [i for i in range(10000000)]
import sys

print(sys.getsizeof(a))


# numpy
a = np.arange(10000000, dtype=np.float32)   #we use here datatype for reducing the memory size of the  array in numpy
print(a.nbytes)


#conclusion is that numpy uses less memory than list in python.

# convience is  that we can use the datatype to reduce the memory size of the array in numpy and also it is faster than list in python.
