from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define Airflow DAG for SmartCity IoT data pipeline
with DAG(
    "smartcity_iot_pipeline",
    start_date=datetime(2025, 1, 1),      # Pipeline start date
    schedule_interval="@hourly",           # Run every hour
    catchup=False                          # Skip historical runs
) as dag:
    
    # Task 1: Execute Spark streaming job to process Kafka data
    stream = BashOperator(
        task_id="spark_streaming",
        bash_command="docker exec spark spark-submit /app/spark/streaming_job.py"
    )
    
    # Task 2: Aggregate sensor data and load KPIs to PostgreSQL
    load_kpi = BashOperator(
        task_id="load_postgres",
        bash_command="docker exec spark python3 /app/scripts/load_postgres.py"
    )
    
    # Define task dependencies: streaming must complete before loading KPIs
    stream >> load_kpi