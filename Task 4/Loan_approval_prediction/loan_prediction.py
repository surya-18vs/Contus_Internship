import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")

df.columns = df.columns.str.strip()

le = LabelEncoder()

for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col])

X = df.drop("loan_status", axis=1)
y = df["loan_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
new_customer = [[
    5000,     # loan_id
    2,        # dependents
    0,        # education
    0,        # self employed
    800000,   # income
    2000000,  # loan amount
    10,       # loan term
    800,      # cibil
    5000000,
    1000000,
    3000000,
    1000000
]]

result = model.predict(new_customer)
if result==1:
    print("Loan Approved")
else:
 print("Loan Rejected")