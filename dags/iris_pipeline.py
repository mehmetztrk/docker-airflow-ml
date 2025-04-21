from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2025, 4, 26),
    'retries': 1
}

with DAG('iris_ml_pipeline',
         default_args=default_args,
         schedule_interval=None,
         catchup=False,
         description='Train a simple ML model using Iris dataset') as dag:

    preprocess = BashOperator(
        task_id='preprocess_data',
        bash_command='python /opt/airflow/dags/scripts/preprocess.py'
    )

    train = BashOperator(
        task_id='train_model',
        bash_command='python /opt/airflow/dags/scripts/train_model.py'
    )

    preprocess >> train
