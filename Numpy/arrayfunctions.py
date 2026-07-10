import numpy as np

a1=np.random.random((3,3))  # creates a 3x3 array with random values between 0 and 1
a1=np.round(a1*100)  # rounds the values in the array to 2 decimal places
print(a1)

# max/min/mean/sum/prod functions in numpy


# print(np.max(a1))                            
# print(np.mean(a1))  
# print(np.sum(a1))  
# print(np.prod(a1)) 


 #if we use axis=0 it will return the max value of each column and if we use axis=1 it will return the max value of each row
 
 
# print(np.max(a1,axis=0))
# print(np.max(a1,axis=1))



# mean/median/std/var functions in numpy
# print(np.mean(a1))
# print(np.median(a1))
# print(np.std(a1))
# print(np.var(a1))



# trigonometric functions in numpy
# print(np.sin(a1))
# print(np.cos(a1))
# print(np.tan(a1))


# dot product of two arrays in numpy
a2=np.arange(12).reshape(3,4) 
a3=np.arange(12,24).reshape(4,3)
# print(np.dot(a2,a3))  # dot product of a2 and a3 

# log/exponential functions in numpy
# print(np.log(a1)) 
# print(np.exp(a1))


# round/floor/ceil functions in numpy
print(np.round(a1))                  #it rounds the values in the array to the nearest integer
print(np.floor(a1))                  #it rounds the values in the array to the nearest integer towards minus infinity
print(np.ceil(a1))                   #it rounds the values in the array to the nearest integer towards plus infinity