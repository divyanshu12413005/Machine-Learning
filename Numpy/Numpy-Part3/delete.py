import numpy as np

a = np.random.randint(1, 100, 20)

print(a)

a = np.delete(a, [0, 1, 2])   #delete the elements at indices 0, 1, and 2

print(a)