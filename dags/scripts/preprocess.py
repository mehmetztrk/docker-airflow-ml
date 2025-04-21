from sklearn.datasets import load_iris
import pandas as pd
import os

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Output folder
output_path = "/opt/airflow/dags/output"
os.makedirs(output_path, exist_ok=True)

# Save to CSV
df.to_csv(f"{output_path}/iris.csv", index=False)

print("✅ Preprocessing complete: iris.csv created.")
