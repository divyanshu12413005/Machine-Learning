import numpy as np
import pandas as pd



from data import kohli,bollywood, subs


# astype

# print(kohli.astype(np.int16))


# /between
# print(kohli[kohli.between(50, 100)].size)

# clips
# print(subs.clip(lower=50, upper=100))

# drop_duplicates
# temp=pd.Series([1,2,3,4,5,6,7,8,9,10,1,2,3,4])
# print(temp.drop_duplicates())


# isnull
temp=pd.Series([1,2,3,4,np.nan,6,7,np.nan,9,10,np.nan])

# print(temp.isnull().sum())

# dropna
# print(temp.dropna())    

# fillna
# print(temp.fillna(0))

# isin
# print(kohli[kohli.isin([50, 100, 150, 200])])

# apply
# print(subs.apply(lambda x: "Good day" if x > subs.mean() else "Bad day!"))

# copy

new=kohli.head().copy()
print(kohli)
new[1]=1000
print(new)
print(kohli)
