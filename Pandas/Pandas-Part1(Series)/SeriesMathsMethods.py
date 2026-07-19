import pandas as pd
import numpy as np

df = pd.read_csv("D:/Sem 5th/MachineLearning/Pandas/Database/subs.csv",)
series = df.squeeze()

# count()

# print(series.count())  # Count the number of non-null values in the series

# sum() -> product

# print(series.sum())  # Calculate the sum of the values in the series
# print(series.product())  # Calculate the product of the values in the series


# mean/median/mode/std/var

# print(series.mean()) 
# print(series.median())  
# print(series.mode())  
# print(series.std()) 
# print(series.var())  


# min()/max()

# print(series.min())  # Find the minimum value in the series
# print(series.max())  # Find the maximum value in the series

# describe()  Generate descriptive statistics of the series

print(series.describe()) 