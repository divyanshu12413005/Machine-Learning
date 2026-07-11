import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

# Stacking arrays vertically (row-wise)
print(np.vstack((a1, a2)))


# Stacking arrays horizontally (column-wise)
print(np.hstack((a1, a2)))
