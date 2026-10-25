import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")


# How BIG is the dataset?
print(df.shape)

# how doea data look like?
print(df.head())

# what is the data type of columns?
print(df.info())

# are there any missing values?
print(df.isnull().sum())

# how does the data look mathematicaly?
print(df.describe())


# are there any duplicate ?
print(df.duplicated().sum())

# how is the correlation between the columns?
print(df.corr(numeric_only=True))



