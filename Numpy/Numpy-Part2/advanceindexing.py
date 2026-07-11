import numpy as np

a= np.arange(24).reshape(6,4)
# print(a)

# fancy indexing (ye tab use hota hai jab hume kisi array ke specific rows ya columns ko select karna ho jaise hume array ke rows me se 0,2,3 rows ko select karna ho to hum fancy indexing ka use karenge)

# print(a[[0,2,3]])   # prints rows at indices 0, 2, and 3

# print(a[:, [0,2,3]])   # prints columns at indices 0, 2, and 3


# Boolean indexing (ye tab use hota hai jab hume kisi condition ke basis pe array ke elements ko select karna ho jaise hume array ke elements me se even numbers ko select karna ho to hum boolean indexing ka use karenge)

a1=np.random.randint(1,100,24).reshape(6,4)  #it will create a 6x4 array with random integers between 1 and 100
print(a1)

# find all numbers greater than 50

# print(a1[a1 > 50])

# find all even numbers

# print(a1[a1 % 2 == 0])

# find all numbers greater than 50 and even

# print(a1[(a1 > 50) & (a1 % 2 == 0)])

# find all numbers not divisible by 7

print(a1[a1 % 7 != 0])