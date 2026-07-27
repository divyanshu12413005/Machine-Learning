import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import deaths,confirm

# can we have multiple indexe? let's try

index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a=pd.Series([1,2,3,4,5,6,7,8],index=index_val)
# print(a)


# how to create a multiindex
# 1. pd.MultiIndex.from_tuples()

multi_index=pd.MultiIndex.from_tuples(index_val)
# print(multi_index)

# 2. pd.MultiIndex.from_product()

multi_index2=pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])
# print(multi_index2)


# creating a series with multiindex object
s=pd.Series([1,2,3,4,5,6,7,8],index=multi_index2)
# print(s)

# how to fetch items from multiindex series


# print(s['cse',2020])         #this gives the value of cse department for year 2020
# print(s['ece'])              #this gives all the values of ece department for all years



# unstack

temp=s.unstack()  #this will convert the series into a dataframe with first index as row and second index as column
# print(temp)

# stack
temp2=temp.stack()  #this will convert the dataframe back into series
# print(temp2)


# multiindex dataframe

branch_df1=pd.DataFrame(
    [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
    [11,12],
    [13,14],
    [15,16]
    ],
    index=multi_index2,
    columns=['avg_package','students']
)
# print(branch_df1)
# print(branch_df1.loc['cse',2020])  #this will give the row of cse department for year 2020
# print(branch_df1.loc['cse'])  #this will give all the rows of cse department for all years


# Unstacking and Stacking

# print(branch_df1.unstack().stack())  

# Extracting rows
# single rows

# print(branch_df1.loc[('cse',2020)])  

# multiple rows
# print(branch_df1.loc[[('cse',2020),('ece',2021)]]) 

# using iloc
# print(branch_df1.iloc[[1,5]])  #this will give the rows of index 1 and 5


# Extracting columns
# single column

# print(branch_df1['avg_package'])  

# multiple columns
# print(branch_df1[['avg_package','students']]) 

# Extracting rows and columns
# print(branch_df1.loc[('cse',2020),'avg_package'])  


# sort index
# print(branch_df1.sort_index(level=0, ascending=False))  #this will sort the dataframe based on first index

# transpose
# print(branch_df1.T)  

# swapping levels
# print(branch_df1.swaplevel(0,1)) 


# melt -> simple example branch
# wide to long format
m=pd.DataFrame({'cse':[120]}).melt()
# print(m)

# melt -> branch with year
m2=pd.DataFrame({'cse':[120],'ece':[130],'mec':[50]}).melt(var_name='branch',value_name='students')
# print(m2)


# melt -> real world example

# print(deaths.head(10))
# print(confirm.head(10))

# make table where country,date,confirm,deaths are columns and each row is a record

deaths=deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='deaths')
confirm=confirm.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')
# print(deaths.head(10))
# print(confirm.head(10))

l=confirm.merge(deaths,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','deaths']]
print(l.tail(25))  