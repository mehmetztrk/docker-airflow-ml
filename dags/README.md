# 🧠 Iris ML Pipeline with Airflow & Docker

This project demonstrates a simple end-to-end machine learning pipeline using **Apache Airflow** orchestrated in **Docker**, where the classic Iris dataset is used for classification via logistic regression.

---

## 📊 Overview

The pipeline is built using Airflow DAGs and performs:

1. **Preprocessing**  
   - Loads Iris dataset (from scikit-learn)  
   - Saves preprocessed data as `iris.csv`

2. **Model Training**  
   - Trains a `LogisticRegression` model  
   - Saves the model as `iris_model.pkl`

---

## 🔧 Tech Stack

- Python 3.8  
- Apache Airflow 2.8.1  
- Docker & Docker Compose  
- scikit-learn, pandas, joblib  
- LocalExecutor + PostgreSQL backend

---

## 🗂️ Project Structure

```
docker-airflow-ml/
│
├── dags/
│   ├── iris_pipeline.py          ← Airflow DAG
│   ├── scripts/
│   │   ├── preprocess.py         ← Preprocesses Iris dataset
│   │   └── train_model.py        ← Trains and saves logistic regression model
│   └── output/
│       ├── iris.csv              ← Preprocessed data
│       └── iris_model.pkl        ← Trained ML model
├── Dockerfile                    ← Custom Airflow image with ML packages
├── docker-compose.yaml           ← Stack definition
```

---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone git@github.com:mehmetztrk/monthly-sales-forecast.git
cd monthly-sales-forecast
```

2. **Build and run the stack**

```bash
docker-compose down --volumes --remove-orphans
docker-compose build
docker-compose run airflow-webserver airflow db init
docker-compose up
```

3. **Create admin user (if needed)**

```bash
docker-compose run airflow-webserver airflow users create \
  --username airflow --password airflow \
  --firstname Admin --lastname User \
  --role Admin --email admin@example.com
```

4. **Visit Airflow**

➡ http://localhost:8080  
Login with: `airflow / airflow`  
Enable and trigger `iris_ml_pipeline`

---

## ✅ Output Files

After successful DAG run:
- `dags/output/iris.csv` — cleaned Iris dataset  
- `dags/output/iris_model.pkl` — trained logistic regression model

---

## 👤 Author

**Mehmet Ozturk** — _Machine Learning & Data Pipeline Enthusiast_  
📧 mhmtztrk1997@hotmail.com  
🌍 GitHub: [@mehmetztrk](https://github.com/mehmetztrk)
