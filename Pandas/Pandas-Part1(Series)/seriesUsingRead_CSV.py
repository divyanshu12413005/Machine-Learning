import pandas as pd
import numpy as np


# with one column(for one column dataframe is default) so will apply  squeeze() to convert it to a Series

df = pd.read_csv("D:/Sem 5th/MachineLearning/Pandas/Database/subs.csv")


series = df.squeeze()

# print(series)


# with two columns, squeeze() will return the DataFrame as is

vk= pd.read_csv("D:/Sem 5th/MachineLearning/Pandas/Database/kohli_ipl.csv",index_col='match_no')


series = vk.squeeze()

# print(series)


import pandas as pd

movies = pd.read_csv("D:/Sem 5th/MachineLearning/Pandas/Database/bollywood.csv", index_col='movie')

series = movies.squeeze()

print(series)



