
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(
    "D:/Sem 5th/MachineLearning/FeatureEng/Social_Network_Ads.csv"
)

# Encode Gender column
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

# Separate input features and output target
X = df.drop(["User ID", "Purchased"], axis=1)
y = df["Purchased"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=0
)

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

# Standardization
scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data using training statistics
X_test_scaled = scaler.transform(X_test)

# Convert scaled arrays into DataFrames
X_train_scaled_df = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)

X_test_scaled_df = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)

# Display scaler parameters
print("\nMean:", scaler.mean_)
print("Scale:", scaler.scale_)

# Display standardized data summary
print("\nStandardized training data summary:")
print(X_train_scaled_df.describe().round(2))

# Graph: Before vs After Standardization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Before scaling
axes[0].scatter(
    X_train["Age"],
    X_train["EstimatedSalary"],
    c=y_train,
    cmap="coolwarm",
    alpha=0.7
)

axes[0].set_title("Before Standardization")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Estimated Salary")

# After scaling
axes[1].scatter(
    X_train_scaled_df["Age"],
    X_train_scaled_df["EstimatedSalary"],
    c=y_train,
    cmap="coolwarm",
    alpha=0.7
)

axes[1].set_title("After Standardization")
axes[1].set_xlabel("Age (scaled)")
axes[1].set_ylabel("Estimated Salary (scaled)")

plt.tight_layout()
plt.show()
