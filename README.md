smartcity-iot-bigdata-pipeline/
│
├── airflow/
│   └── dags/
│       └── smartcity_pipeline.py
│
├── streaming/
│   ├── kafka_producer.py
│   └── spark_streaming.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── warehouse/
│   └── load_postgres.py
│
├── superset/
│   └── dashboards/
│
├── docker-compose.yml
├── Dockerfile.spark
├── requirements.txt
└── README.md
