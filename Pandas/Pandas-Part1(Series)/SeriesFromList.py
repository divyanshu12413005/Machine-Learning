import pandas as pd 
import numpy as np 

# country list
country_list = ['USA', 'Canada', 'Germany', 'UK', 'France']

# print(country_list)


# create a pandas series from the country list


# print(pd.Series(country_list))    


    

# from integer list to pandas series

runs=[100, 200, 300, 400, 500]
# print(pd.Series(runs))



# cutoms index 

marks = [90, 80, 70, 60, 50]
subjects = ['Maths', 'Physics', 'Chemistry', 'Hindi', 'English']

# print(pd.Series(marks, index=subjects))        # in this case we are passing the index as subjects list and values as marks list.


# add new attribute name  
print(pd.Series(marks, index=subjects, name='Student Marks'))        # in this case we are passing the index as subjects list and values as marks list.