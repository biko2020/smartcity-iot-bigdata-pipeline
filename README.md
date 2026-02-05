# SmartCity IoT Big Data Pipeline (Real-Time & Batch)

End-to-end **Big Data Engineering project** designed to ingest, process, store and visualize **real-time IoT data** using modern, production-grade technologies.

This project demonstrates how to build a **scalable, containerized data platform** suitable for Smart Cities, Industry 4.0, and real-time analytics use cases.

---

##  Business Use Case

Smart cities generate massive volumes of IoT data (air quality, traffic, temperature, sensors).  
This pipeline enables:

- Real-time ingestion of IoT events
- Large-scale processing with Spark
- Reliable storage in Data Lake and PostgreSQL
- Automated orchestration with Airflow
- Interactive dashboards with Superset

---

## Architecture Overview

    ┌─────────────────────────────┐
    │   IoT Sensors / APIs        │ ← Data Sources
    └──────────┬──────────────────┘
               │
        ┌──────▼──────────────┐
        │   Apache Kafka      │ ← Real-Time Ingestion
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │ Spark Structured    │ ← Stream Processing
        │    Streaming        │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │   Parquet Data      │ ← Storage Layer
        │      Lake           │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │   PostgreSQL        │ ← Analytics & KPIs
        │  (OLAP/Analytics)   │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │  Superset           │ ← Visualization & BI
        │   Dashboards        │
        └──────┬──────────────┘
               │
        ┌──────▼──────────────┐
        │  Apache Airflow     │ ← Orchestration & Monitoring
        │ (Orchestration)     │
        └─────────────────────┘

---

## Project Structure

smartcity-iot-bigdata-pipeline/
│
├── data/
│   ├── raw/                        # Raw ingested data
│   └── processed/                  # Cleaned & aggregated Parquet
│
├── scripts/                        # Batch ETL logic
│   ├── extract.py                  # Data ingestion (API / batch)
│   ├── transform.py                # PySpark transformations
│   └── load.py                     # Load to PostgreSQL
│
├── kafka/
│   └── producer_iot.py             # Real-time IoT producer
│
├── spark/
│   └── streaming_job.py            # Spark Structured Streaming
│
├── airflow/
│   └── dags/
│       └── smartcity_etl_dag.py    # Automated pipeline (DAG)
│
├── superset/
│   └── dashboards/                 # BI dashboards
│
├── docker/
│   ├── Dockerfile.spark
│   └── docker-compose.yml
│
├── requirements.txt
└── README.md

---

## Technology Stack

Python 3
Apache Kafka
Apache Spark (Batch & Streaming)
Apache Airflow
PostgreSQL
Apache Superset
Docker & Docker Compose
Parquet Data Lake

---

## How to Run the Project

1️⃣ Start the environment
	docker compose up -d

2️⃣ Run batch ETL (optional)
	docker exec -it spark python3 /app/scripts/extract.py
	docker exec -it spark spark-submit /app/scripts/transform.py
	docker exec -it spark python3 /app/scripts/load.py

3️⃣ Run real-time streaming
	docker exec -it spark spark-submit /app/spark/streaming_job.py

---

## Access Services

| Service    | URL                                            |
| ---------- | ---------------------------------------------- |
| Spark UI   | [http://localhost:8080](http://localhost:8080) |
| Superset   | [http://localhost:8088](http://localhost:8088) |
| PostgreSQL | localhost:5432                                 |
| Airflow    | [http://localhost:8081](http://localhost:8081) |

---

## Example KPIs

- Average CO₂ per sensor
- Temperature trends
- Traffic congestion index
- Real-time alerts
- Sensor health monitoring

---

## This project demonstrates the ability to:

- Design production-ready Big Data architectures
- Handle real-time and batch workloads
- Automate pipelines with Airflow
- Deliver analytics-ready data to BI tools
- Deploy everything using Docker
- Typical freelance missions:
- Big Data Engineer
- Streaming Data Architect
- Spark / Kafka Consultant
- Data Platform Setup

---

## Author

AIT OUFKIR BRAHIM
- Data Engineer | Big Data | Spark | Kafka | Airflow
    Email: aitoufkirbrahimab@gmail.com
    GitHub: https://github.com/biko2020