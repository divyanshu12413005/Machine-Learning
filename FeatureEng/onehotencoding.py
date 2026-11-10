
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv(
    r"D:\Sem 5th\MachineLearning\FeatureEng\cars.csv"
)

print("Original Data:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())


# ==========================================
# 1. ONE-HOT ENCODING USING PANDAS
# ==========================================

df_encoded = pd.get_dummies(
    df,
    columns=['fuel', 'owner']
)

print("\nOne-Hot Encoding using Pandas:")
print(df_encoded.head())


# ==========================================
# 2. K-1 ONE-HOT ENCODING USING PANDAS
# ==========================================

df_encoded_k1 = pd.get_dummies(
    df,
    columns=['fuel', 'owner'],
    drop_first=True
)

print("\nK-1 One-Hot Encoding:")
print(df_encoded_k1.head())


# ==========================================
# 3. ONE-HOT ENCODING USING SKLEARN
# ==========================================

from sklearn.preprocessing import OneHotEncoder

# Select categorical columns
categorical_cols = ['fuel', 'owner']

# Create encoder
ohe = OneHotEncoder(
    drop='first',
    sparse_output=False,
    handle_unknown='ignore'
)

# Fit and transform
encoded_array = ohe.fit_transform(
    df[categorical_cols]
)

# Convert NumPy array into DataFrame
encoded_df = pd.DataFrame(
    encoded_array,
    columns=ohe.get_feature_names_out(categorical_cols),
    index=df.index
)

print("\nOne-Hot Encoding using Sklearn:")
print(encoded_df.head())


# ==========================================
# 4. COMBINE ENCODED COLUMNS WITH REMAINING DATA
# ==========================================

# Remove original categorical columns
df_remaining = df.drop(columns=categorical_cols)

# Combine remaining columns with encoded columns
df_final = pd.concat(
    [df_remaining, encoded_df],
    axis=1
)

print("\nFinal Encoded Dataset:")
print(df_final.head())


# ==========================================
# 5. SAVE FINAL DATASET
# ==========================================

df_final.to_csv(
    r"D:\Sem 5th\MachineLearning\FeatureEng\cars_encoded.csv",
    index=False
)

print("\nEncoded dataset saved successfully!")
