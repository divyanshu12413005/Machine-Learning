import numpy as np

a = np.random.randint(1, 100, 20)

print(a)

print(np.clip(a, 10, 50))  #return the elements of a that are between 10 and 50, if the element is less than 10, it will be replaced with 10, if it is greater than 50, it will be replaced with 50

