import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)

# print(a)
print(b)

# print(np.sort(a))
print(np.sort(b,axis=0))  #sort along the columns
# print(np.sort(b,axis=1))  #sort along the rows

# in desceding order
# print(np.sort(a)[::-1]) 