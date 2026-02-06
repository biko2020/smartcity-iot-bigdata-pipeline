# 🏙️ SmartCity IoT Big Data Pipeline

> **Production-grade real-time data platform for Smart Cities & Industry 4.0**

A complete end-to-end Big Data streaming solution showcasing modern data engineering practices: real-time ingestion, distributed stream processing, analytics-ready storage, and BI visualization — all containerized and production-oriented.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-3.4.1-orange.svg)](https://spark.apache.org/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-Latest-black.svg)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)

---

## 📊 Business Value

Smart cities and IoT platforms generate continuous high-velocity data streams from sensors monitoring traffic, air quality, temperature, noise, and infrastructure usage.

**This pipeline enables:**

✅ Real-time ingestion of IoT events  
✅ Scalable stream processing with Spark Structured Streaming  
✅ Reliable data lake storage using Parquet  
✅ Analytics-ready PostgreSQL warehouse  
✅ Business dashboards for operational insights  
✅ Automated orchestration & monitoring  

**Target Use Cases:**  
Smart Cities • Industry 4.0 • Environmental Monitoring • Traffic Analytics • Predictive Maintenance

---

## 🏗️ Architecture
```
┌─────────────────────────────┐
│   IoT Sensors / APIs        │
└──────────┬──────────────────┘
           │
    ┌──────▼──────────────┐
    │   Apache Kafka      │  ← Real-time ingestion
    └──────┬──────────────┘
           │
    ┌──────▼──────────────┐
    │ Spark Structured    │  ← Stream processing
    │    Streaming        │
    └──────┬──────────────┘
           │
    ┌──────▼──────────────┐
    │ Parquet Data Lake   │  ← Scalable storage
    └──────┬──────────────┘
           │
    ┌──────▼──────────────┐
    │ PostgreSQL          │  ← Analytics / KPIs
    └──────┬──────────────┘
           │
    ┌──────▼──────────────┐
    │ Apache Superset     │  ← BI Dashboards
    └──────┬──────────────┘
           │
    ┌──────▼──────────────┐
    │ Apache Airflow      │  ← Orchestration
    └─────────────────────┘
```

### Design Principles

- **Streaming-first architecture**
- **Fault-tolerant** (Spark checkpoints)
- **Horizontally scalable**
- **Cloud-agnostic** (AWS / GCP / Azure / on-prem)
- **Production-ready containerization**

---

## 📁 Project Structure
```
smartcity-iot-bigdata-pipeline/
│
├── data/                           # Data Lake (mounted volume)
│   ├── raw/                        # Kafka landing (optional)
│   └── processed/                  # Parquet from Spark Streaming
│
├── kafka/
│   └── producer_iot.py             # IoT / sensor simulator
│
├── spark/
│   └── streaming_job.py            # Spark Structured Streaming
│
├── superset/
│   └── dashboards/
│
├── scripts/
│   └── load_postgres.py            # KPIs from Parquet → PostgreSQL
│
├── airflow/
│   └── dags/
│       └── smartcity_pipeline.py   # Orchestration
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

| Layer              | Technology                |
|--------------------|---------------------------|
| **Language**       | Python 3.10+              |
| **Streaming**      | Apache Kafka              |
| **Processing**     | Apache Spark 3.4.1        |
| **Orchestration**  | Apache Airflow            |
| **Storage**        | Parquet Data Lake         |
| **Analytics DB**   | PostgreSQL 15             |
| **Visualization**  | Apache Superset           |
| **Infrastructure** | Docker & Docker Compose   |

**Key Python Libraries:**
- `pyspark`
- `kafka-python`
- `pandas`
- `sqlalchemy`
- `psycopg2-binary`
- `pyarrow`

---

## 🚀 Quick Start

### Prerequisites

- Docker Engine 20.10+
- Docker Compose v2
- 8 GB RAM minimum (16 GB recommended)

### Deployment
```bash
git clone https://github.com/biko2020/smartcity-iot-bigdata-pipeline.git
cd smartcity-iot-bigdata-pipeline
docker compose -f docker/docker-compose.yml up -d
```

### Verify Services
```bash
docker ps
```

---

## ▶️ Pipeline Execution

**1️⃣ Start IoT data simulation**
```bash
docker exec -it smartcity-kafka python3 /app/kafka/producer_iot.py
```

**2️⃣ Launch Spark Streaming**
```bash
docker exec -it smartcity-spark spark-submit /app/spark/streaming_job.py
```

**3️⃣ Load KPIs into PostgreSQL**
```bash
docker exec -it smartcity-spark python3 /app/scripts/load_postgres.py
```

---

## 🌐 Web Interfaces

| Service      | URL                          |
|--------------|------------------------------|
| **Spark UI** | http://localhost:4040        |
| **Airflow**  | http://localhost:8080        |
| **Superset** | http://localhost:8088        |

---

## 📈 KPIs & Analytics

- Average temperature per zone
- Pollution level trends
- Traffic density indicators
- Event throughput (msg/sec)
- Sensor activity & latency

---

## 🎯 What This Project Proves

### Technical Skills

✔ Kafka streaming ingestion  
✔ Spark Structured Streaming  
✔ Data Lake engineering  
✔ OLAP-ready PostgreSQL modeling  
✔ Airflow orchestration  
✔ Dockerized production stack  

### Freelance-Ready Value

✔ End-to-end delivery  
✔ Scalable architecture  
✔ Client-ready demo  
✔ Cloud migration friendly  

---

## 💼 Ideal Freelance Use

**Perfect for:**

- Smart City analytics platforms
- IoT data pipelines
- Real-time dashboards
- Kafka / Spark consulting
- Data platform MVPs

---

## 📞 Contact

**AIT OUFKIR BRAHIM**  
*Big Data Engineer | Spark • Kafka • Airflow*

📧 **Email:** [aitoufkirbrahimab@gmail.com](mailto:aitoufkirbrahimab@gmail.com)  
💻 **GitHub:** [@biko2020](https://github.com/biko2020)  
💼 **LinkedIn:** [brahim-aitoufkir](https://www.linkedin.com/in/brahim-aitoufkir-74506021a/)

---

## 📄 License

MIT License

---