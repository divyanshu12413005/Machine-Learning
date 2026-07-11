import numpy as np

a = np.random.randint(1, 100, 20)

print(a)

np.put(a, [0, 1, 2], [100, 200, 300])   #replace the elements at indices 0, 1, and 2 with 100, 200, and 300 respectively

print(a)