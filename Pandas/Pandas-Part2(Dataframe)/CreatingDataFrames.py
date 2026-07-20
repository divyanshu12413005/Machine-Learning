import numpy as np
import pandas as pd




# using list
student_data=[[100,80,10], 
    [90,70,15], 
    [80,60,20], 
    [70,50,25]]

# print(pd.DataFrame(student_data,columns=['Iq','Marks','Package'],index=['Ravi','Kiran','Suresh','Ramesh']))


# using dictionary

student_dict={'Iq':[100,90,80,70],
    'Marks':[80,70,60,50],
    'Package':[10,15,20,25]
    }

print(pd.DataFrame(student_dict,index=['Ravi','Kiran','Suresh','Ramesh']))