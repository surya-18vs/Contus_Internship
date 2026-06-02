import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Load Dataset
df = pd.read_csv("creditcard.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Features and Target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
print("\nAccuracy:")
print(accuracy_score(y_test, pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

# Real World Prediction Example
sample_transaction = X.iloc[[0]]

prediction = model.predict(sample_transaction)

print("\nSample Transaction Prediction:")

if prediction[0] == 1:
    print("Fraudulent Transaction")
else:
    print("Legitimate Transaction")