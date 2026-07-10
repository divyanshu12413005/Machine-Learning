import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

# for i in a1:
#     print(i)  # Iterating over elements of a1
    
# for i in a2:
#     print(i)  # Iterating over rows of a2
        

# for i in a3:
#     print(i)  # Iterating over 2D arrays (matrices) in a3

for i in np.nditer(a3):
    print(i)  # Iterating over all elements of a3 using nditer
        