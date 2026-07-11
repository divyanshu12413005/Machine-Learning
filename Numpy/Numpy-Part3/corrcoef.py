import numpy as np

salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,5])

print(np.corrcoef(salary,experience))  #return the correlation coefficient between salary and experience
