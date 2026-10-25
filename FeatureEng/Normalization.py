
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "D:/Sem 5th/MachineLearning/FeatureEng/wine_data.csv",
    header=None,
    usecols=[0, 1, 2]
)

df.columns = ["Class label", "Alcohol", "Malic acid"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df.drop("Class label", axis=1),
    df["Class label"],
    test_size=0.3,
    random_state=0
)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

# Fit only on training data
scaler.fit(X_train)

# Transform training and test data
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert arrays back to DataFrames
X_train_scaled = pd.DataFrame(
    X_train_scaled, columns=X_train.columns, index=X_train.index
)
X_test_scaled = pd.DataFrame(
    X_test_scaled, columns=X_test.columns, index=X_test.index
)

print("Training shape:", X_train.shape, X_test.shape)
print("\nScaled data summary:")
print(np.round(X_train_scaled.describe(), 2))

# Compare before and after scaling
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))

ax1.scatter(X_train["Alcohol"], X_train["Malic acid"], c=y_train)
ax1.set_title("Before Scaling")
ax1.set_xlabel("Alcohol")
ax1.set_ylabel("Malic acid")

ax2.scatter(
    X_train_scaled["Alcohol"],
    X_train_scaled["Malic acid"],
    c=y_train
)
ax2.set_title("After MinMax Scaling")
ax2.set_xlabel("Alcohol (scaled)")
ax2.set_ylabel("Malic acid (scaled)")

plt.tight_layout()
plt.show()
