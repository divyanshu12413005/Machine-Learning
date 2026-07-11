import numpy as np

a1=np.arange(12).reshape(3,4)                                    
a2=np.arange(12,24).reshape(3,4)  

# arithmetic operations +, -, *, /, **, % can be performed on numpy arrays
print(a1*2)

# relational operations <, >, <=, >=, ==, != can be performed on numpy arrays
print(a2>5)


# vector operations can be performed on numpy arrays
print(a1+a2)