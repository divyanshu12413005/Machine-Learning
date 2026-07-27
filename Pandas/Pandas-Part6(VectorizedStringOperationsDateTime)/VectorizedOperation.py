import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import titanic


# what are vectorized operations?
a=np.array([1, 2, 3, 4, 5])
# print(a*2) 

# problem in vectorized operations in vanilla python
# In vanilla Python, you would need to use a loop to perform the same operation:
s=['cat', 'dog', 'bird','mat',None]
# [i.startswith('c') for i in s]  # This will raise an error because NoneType object has no attribute 'startswith'

# how pandas solve this issue

s=pd.Series(['cat', 'dog',None, 'bird','mat',None])
# print(s.str.startswith('c'))  # This will return a Series with True/False


# print(titanic['Name'])

# common function
# uppercase/lowercase/capalize/titlecase


# print(titanic['Name'].str.upper())     
# print(titanic['Name'].str.lower())    
# print(titanic['Name'].str.capitalize())        #it will convert the first character of each name in the 'Name' column to uppercase and the rest to lowercase.
# print(titanic['Name'].str.title())               #it will convert each name in the 'Name' column to title case.


# len/strip


# print(titanic['Name'].str.len())        #it will return the length of each name in the 'Name' column.
# print(titanic['Name'].str.strip())      #it will remove any leading or trailing whitespace from each name in the 'Name' column.


# split ->get


titanic['Last Name'] = titanic['Name'].str.split(',').str.get(0) #it will split each name in the 'Name' column by the comma and return the first part (the last name).

titanic['Title'] = titanic['Name'].str.split(',').str.get(1).str.split('.').str.get(0).str.strip() 
titanic['First Name'] = titanic['Name'].str.split(',').str.get(1).str.split('.').str.get(1).str.strip() 

# print(titanic[['Name', 'Last Name', 'Title', 'First Name']].head())

# total number of titles in the dataset
# print(titanic['Title'].value_counts())


# replace

titanic['Title'] = titanic['Title'].str.replace('Sir.', 'Mr.')
# print(titanic['Title'].value_counts())


# filtering 
# strartswith/endswith/contains
# print(titanic[titanic['First Name'].str.startswith('O')])  

# isDigit/isAlpha/isAlnum

# print(titanic[titanic['First Name'].str.isdigit()]) 


# find the last name strat wwith vowel and end with vowel

# print(
#     titanic[
#         (titanic["Last Name"].str.lower().str.startswith(("a", "e", "i", "o", "u"), na=False)) &
#         (titanic["Last Name"].str.lower().str.endswith(("a", "e", "i", "o", "u"), na=False))
#     ]
# )

# by contains method


# print(
#     titanic[
#         (titanic["Last Name"].str.lower().str.contains(r"^[aeiou].*[aeiou]$", na=False))
#     ]
# )

# slicing

print(titanic['First Name'].str[0:3])