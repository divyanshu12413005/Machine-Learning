import numpy as np

# union1d, intersect1d, setdiff1d, setxor1d, isin

m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])

print(np.union1d(m,n))  #return the unique values that are in either of the two arrays
print(np.intersect1d(m,n))  #return the unique values that are in both of the two arrays
print(np.setdiff1d(m,n))  #return the unique values that are in m but not in n
print(np.setxor1d(m,n))  #return the unique values that are in either of the two arrays but not in both
print(np.isin(m, 1))  # return a boolean array that indicates whether each element of m is 1
