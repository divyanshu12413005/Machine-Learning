import numpy as np

a=np.random.randint(1,100,20)

print(a)


print(a[np.isin(a,[10,20,30])])  #return the elements of a that are in the list [10,20,30]
