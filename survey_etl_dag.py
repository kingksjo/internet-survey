from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 22),  # Adjust start date
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


dag = DAG(
    "survey_etl_pipeline",
    default_args=default_args,
    description="ETL pipeline for survey data from Google Sheets to SQLite",
    schedule_interval="*/5 * * * *",  # Runs every 5 minutes
    catchup=False,
)

# Define tasks
def extract():
    subprocess.run(["python3", "/home/kamiye/internet-survey/extract.py"], check=True)

def transform():
    subprocess.run(["python3", "/home/kamiye/internet-survey/transform.py"], check=True)

def load():
    subprocess.run(["python3", "/home/kamiye/internet-survey/load.py"], check=True)

extract_task = PythonOperator(
    task_id="extract_data",
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id="transform_data",
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id="load_data",
    python_callable=load,
    dag=dag,
)

# Task Dependencies
extract_task >> transform_task >> load_task
