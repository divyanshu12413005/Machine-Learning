import pandas as pd

url = 'https://raw.githubusercontent.com/CourseMaterial/DataWrangling/main/flowerdataset.csv'

df = pd.read_csv(url)

print(df.head())