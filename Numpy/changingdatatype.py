import numpy as np

a1=np.arange(10)                                  
a2=np.arange(12,dtype='float').reshape(3,4)       
a3=np.arange(8).reshape(2,2,2)

# before changing the data type of an array
print(a3.dtype)

# changing the data type of an array using astype() method
a3_new=a3.astype('float')
print(a3_new.dtype)
