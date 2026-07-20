import numpy as np
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import matches, movies

# shape
# print(movies.shape)    #it will give the number of rows and columns in the dataframe

# dtypes
# print(movies.dtypes)   #it will give the data type of each column in the dataframe

# index
# print(movies.index)    


# columns
# print(movies.columns)  #it will give the name of each column in the dataframe

# values
# print(matches.values)   #it will give the values of each column in the dataframe

# head/tail
# print(matches.head())  
# print(matches.tail(3))


# sample
# print(matches.sample(8))  


# info
# print(matches.info())   #it will give the information about the dataframe like number of rows

# describe
# print(matches.describe())  #it will give the statistical information about the dataframe like mean, std, min, max, etc


# isnull
# print(matches.isnull().sum())  #it will give the number of null values in each column

# duplicated
# print(movies.duplicated().sum())  #it will give the number of duplicated rows

# rename
# print(movies.rename(columns={'movie':'Movie Name'}))  #it will rename the column name 'movie' to 'Movie Name' in the dataframe