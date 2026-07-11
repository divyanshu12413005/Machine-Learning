import numpy as np

a=np.array([1,2,3,np.nan,5])
print(a)

print([np.isnan(a)])  # [True  True  True False  True]
print(a[~np.isnan(a)])  # [1. 2. 3. 5.]