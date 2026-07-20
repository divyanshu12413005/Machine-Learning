import numpy as np
import pandas as pd


student_dict={'name':['Amit','Rohit','Saurav','Virat'],
    'Iq':[100,90,80,70],
    'Marks':[80,70,60,50],
    'Package':[10,15,20,25]
    }
df = pd.DataFrame(student_dict)

df = df.set_index('name')

# iloc -> integer location based indexing
# loc -> label based indexing

# single row
# print(df.iloc[0])  # it will give the first row of the dataframe

# multiple rows
# print(df.iloc[0:3])  # it will give the first to third row of the dataframe

# loc
# print(df.loc['Amit'])  # it will give the row of Amit


# both rows and columns
print(df.iloc[0:3, 0:2])  # it will give the first to third row and first to second column of the dataframe
