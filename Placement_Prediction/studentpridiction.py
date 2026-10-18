import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(
    "D:/Sem 5th/MachineLearning/Placement_Prediction/student_placement_100.csv"
)
# print(df.head())



im = plt.scatter(
    df['cgpa'],
    df['iq'],
    c=df['placement'].map({'Y': 'green', 'N': 'red'})
)

plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('Student Placement Prediction')
# plt.show()





# Convert Y/N into numeric values for correlation
df["placement_num"] = df["placement"].map({
    "N": 0,
    "Y": 1
})

# print(df[["cgpa", "iq", "placement_num"]].corr())


# Extract input and output columns

X = df[["cgpa", "iq"]]
y = df["placement"]

# print(X.head())
# print(y.head())





#Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_test shape:", y_test.shape)

#Scale the features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# print("\nScaled training data:")
# print(X_train_scaled[:5])





model = LogisticRegression()

model.fit(X_train_scaled, y_train)

# print("Model training completed!")



from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Predict on test data
y_pred = model.predict(X_test_scaled)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=["N", "Y"]))

# Precision, Recall, F1-score
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


import joblib

joblib.dump(model, "placement_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully!")





