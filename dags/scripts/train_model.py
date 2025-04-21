import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load preprocessed data
df = pd.read_csv("/opt/airflow/dags/output/iris.csv")
X = df.drop('target', axis=1)
y = df['target']

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the model
joblib.dump(model, "/opt/airflow/dags/output/iris_model.pkl")

print("✅ Model trained and saved as iris_model.pkl")
