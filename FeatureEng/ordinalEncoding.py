
import numpy as np
import pandas as pd

df = pd.read_csv(
    r"D:\Sem 5th\MachineLearning\FeatureEng\customer.csv"
)

print("Original Data:")
print(df.head())

# Select columns from index 2 to the end
df = df.iloc[:, 2:]

print("\nAfter removing first two columns:")
print(df.head())

from sklearn.preprocessing import OrdinalEncoder

# Select all columns except the last column
x_train = df.iloc[:, :-1]

print("\nCategorical Features:")
print(x_train.head())

# Define category order
oe = OrdinalEncoder(
    categories=[
        ['Poor', 'Average', 'Good'],
        ['School', 'UG', 'PG']
    ]
)

# Learn the encoding
oe.fit(x_train)

# Convert categorical values into numerical values
x_train_encoded = oe.transform(x_train)

print("\nEncoded Array:")
print(x_train_encoded)

# Convert encoded array back into DataFrame
x_train_encoded = pd.DataFrame(
    x_train_encoded,
    columns=x_train.columns
)

print("\nFinal Encoded DataFrame:")
print(x_train_encoded)
