import numpy as np

a=np.random.randint(1,100,20)
print(a)

print(np.where(a>50))  #return the indices of the elements greater than 50


# replace the elements greater than 50 with 0


print(np.where(a>50,0,a))  