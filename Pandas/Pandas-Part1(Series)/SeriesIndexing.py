import pandas as pd
import numpy as np

x=pd.Series([1,13,26,39,52,65,78,91])

# integer indexing'


# print(x[0])  # Access the first element of the series



# negative indexing

# print(x[-1])  # give error because negative indexing is not supported in pandas Series for number index 


# slicing

# print(x[2:5])  # Access elements from index 2 to 4 (slicing)

# negative slicing
# print(x[-5:-2])  # Access elements from index -5 to -3 (negative slicing)

# print(x[::2])  # Access every second element of the series (step slicing)

# fancy indexing
# print(x[[0, 2, 4]])  # Access elements at index 0, 2, and 4 (fancy indexing)

# indexing with labels

y=pd.Series([1,13,26,39,52,65,78,91],index=['a','b','c','d','e','f','g','h'])

print(y['d'])  # Access the element with label 'd'



