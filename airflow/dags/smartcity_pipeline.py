from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "smartcity_iot_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@hourly",
    catchup=False,
    max_active_runs=1
) as dag:

    # Task 1: Batch read from Kafka → Write to Parquet
    stream = BashOperator(
        task_id="spark_streaming",
        bash_command=(
            "docker exec smartcity-spark spark-submit "
            "/app/spark/streaming_job.py "
            "--checkpoint /app/checkpoints/{{ ds }}/{{ execution_date.hour }} "
            "--output /app/data/processed/smartcity/{{ ds }}/{{ execution_date.hour }}"
        )
    )

    # Task 2: Load KPIs into PostgreSQL
    load_kpi = BashOperator(
        task_id="load_postgres",
        bash_command=(
            "docker exec smartcity-spark python3 /app/scripts/load_postgres.py "
            "--input /app/data/processed/smartcity/{{ ds }}/{{ execution_date.hour }}"
        )
    )

    stream >> load_kpi