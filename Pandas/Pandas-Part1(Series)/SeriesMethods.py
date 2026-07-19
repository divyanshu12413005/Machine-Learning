import pandas as pd
import numpy as np



df = pd.read_csv("D:/Sem 5th/MachineLearning/Pandas/Database/bollywood.csv", index_col='movie')
series = df.squeeze()

# head and tails


# print(series.head())  # Display the first 5 rows  default 5 
# print(series.tail(6))  # Display the last 6 rows


# sample  display random sample of rows from the series

# print(series.sample())  


# value_counts()  Display the count of unique values in the series

# print(series.value_counts())  

# sort_values()  Sort the series by its values

# print(series.sort_values(ascending=False))  # Sort the series in descending order
# print(series.sort_values(ascending=True))  # Sort the series in ascending order


# if we use inplace=True, it will modify the original series



# sort_index()  Sort the series by its index

# print(series.sort_index(ascending=False))  # Sort the series in descending order by index


