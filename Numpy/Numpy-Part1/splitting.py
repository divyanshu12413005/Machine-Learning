import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

print(a1)
print(a2)

# Splitting arrays vertically (row-wise)
print(np.vsplit(a1, 3))                    # Split a1 into 3 arrays vertically

# Splitting arrays horizontally (column-wise)
print(np.hsplit(a1, 2))                    # Split a1 into 2 arrays horizontally

