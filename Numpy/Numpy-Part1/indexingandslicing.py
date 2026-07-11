import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)

# print(a1)
# print(a2)
print(a3)


# indexing 

# print(a1[-1])  # Accessing the last element of a1

# print(a2[1,2])  # Accessing the element at row 1, column 2 of a2

# print(a3[1,0,1])  # Accessing the element at index [1,0,1] of a3


# slicing

# print(a1[2:5])  # Accessing elements from index 2 to 4 of a1
# print(a2[0,:])   #accessing first row of a2
# print(a2[:,1:3])  # Accessing columns 1 and 2 of a2
# print(a2[1:,1:3])  # Accessing rows 1 and 2, columns 1 and 2 of a2
# print(a2[::2,::3])  # Accessing every second row and every third column of a2


# print(a3[1])  # Accessing the second 2D array (matrix) in a3

# print(a3[::2])  # Accessing every second 2D array (matrix) in a3
# print(a3[0,1,:])  # Accessing the second row of the first 2D array (matrix) in a3

# print(a3[1,:,1])  # Accessing the second column of the second 2D array (matrix) in a3
# print(a3[2,1:,1:])  # Accessing the second and third rows, second column of the third 2D array (matrix) in a3


print(a3[::2,0,::2])  # Accessing every second 2D array (matrix) in a3, the first row, and every second column of those matrices
