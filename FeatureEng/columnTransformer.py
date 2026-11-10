
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv(
    r"D:\Sem 5th\MachineLearning\FeatureEng\covid_toy.csv"
)

print("Original Data:")
print(df.head())

print("\nDataset Information:")
print(df.info())


# ==========================================
# 1. SEPARATE INPUT AND OUTPUT
# ==========================================

X = df.drop(columns=['has_covid'])
y = df['has_covid']

print("\nInput Features:")
print(X.head())

print("\nTarget:")
print(y.head())


# ==========================================
# 2. COLUMN TRANSFORMER
# ==========================================

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Numerical pipeline
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical pipeline
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(
        drop='first',
        handle_unknown='ignore'
    ))
])

# Apply ColumnTransformer
transformer = ColumnTransformer(
    transformers=[
        ('num', num_pipeline, ['age', 'fever']),
        ('cat', cat_pipeline, ['gender', 'cough', 'city'])
    ],
    remainder='drop'
)

# Fit and transform
X_transformed = transformer.fit_transform(X)

print("\nTransformed Array:")
print(X_transformed)


# ==========================================
# 3. CONVERT INTO DATAFRAME
# ==========================================

feature_names = transformer.get_feature_names_out()

X_transformed = pd.DataFrame(
    X_transformed,
    columns=feature_names,
    index=X.index
)

print("\nFinal Transformed DataFrame:")
print(X_transformed.head())

print("\nTransformed Column Names:")
print(X_transformed.columns.tolist())


# ==========================================
# 4. SAVE FINAL DATASET
# ==========================================

df_final = pd.concat([X_transformed, y], axis=1)

df_final.to_csv(
    r"D:\Sem 5th\MachineLearning\FeatureEng\covid_toy_transformed.csv",
    index=False
)

print("\nFinal dataset saved successfully!")
