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
    │   + Zookeeper       │
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
│   ├── Dockerfile.spark            # Spark container image
│   └── docker-compose.yml          # Multi-service orchestration
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

| Layer              | Technology                      |
|--------------------|---------------------------------|
| **Language**       | Python 3.10+                    |
| **Streaming**      | Apache Kafka 7.5 (Confluent)    |
| **Processing**     | Apache Spark 3.4.1              |
| **Orchestration**  | Apache Airflow 2.8.1            |
| **Storage**        | Parquet Data Lake               |
| **Analytics DB**   | PostgreSQL 15                   |
| **Visualization**  | Apache Superset                 |
| **Infrastructure** | Docker & Docker Compose         |

**Key Python Libraries:**
- `pyspark==3.4.1`
- `kafka-python>=2.0`
- `pandas>=2.0`
- `sqlalchemy>=2.0`
- `psycopg2-binary>=2.9`
- `pyarrow`

---

## 🚀 Quick Start

### Prerequisites

- **Docker Desktop** (Windows 11 / macOS / Linux)
- Docker Engine 20.10+
- Docker Compose v2+
- 8 GB RAM minimum (16 GB recommended)
- 10 GB free disk space

### Deployment
```bash
# Clone the repository
git clone https://github.com/biko2020/smartcity-iot-bigdata-pipeline.git
cd smartcity-iot-bigdata-pipeline

# Launch all services
docker compose -f docker/docker-compose.yml up -d

# Verify services are running
docker compose -f docker/docker-compose.yml ps
```

**Wait for all services to be healthy** (30-60 seconds)

---

## ▶️ Pipeline Execution

**1️⃣ Start IoT data simulation**
```bash
docker exec -it smartcity-spark python3 /app/kafka/producer_iot.py
```
*Generates synthetic sensor events every 5 seconds*

**2️⃣ Launch Spark Streaming** (in a new terminal)
```bash
docker exec -it smartcity-spark spark-submit /app/spark/streaming_job.py
```
*Consumes Kafka events and writes to Parquet*

**3️⃣ Load KPIs into PostgreSQL** (after data collection)
```bash
docker exec -it smartcity-spark python3 /app/scripts/load_postgres.py
```
*Aggregates metrics and loads to database*

**4️⃣ Verify data in PostgreSQL**
```bash
docker exec -it smartcity-postgres psql -U postgres -d smartcity_db -c "SELECT * FROM smartcity_kpi;"
```

---

## 🌐 Web Interfaces

| Service          | URL                          | Credentials         |
|------------------|------------------------------|---------------------|
| **Airflow**      | http://localhost:8080        | `admin` / `admin`   |
| **Superset**     | http://localhost:8088        | Setup required*     |
| **Spark UI**     | http://localhost:4040        | N/A (when job runs) |

*Superset setup:
```bash
docker exec -it smartcity-superset superset fab create-admin \
    --username admin --firstname Admin --lastname User \
    --email admin@example.com --password admin
docker exec -it smartcity-superset superset db upgrade
docker exec -it smartcity-superset superset init
```

---

## 📈 KPIs & Analytics

The pipeline calculates real-time metrics:

- **Environmental**: Average temperature, CO₂ concentration per sensor
- **Traffic**: Traffic density indicators, congestion analysis
- **Operational**: Event throughput (msg/sec), sensor health, data latency

---

## 🎯 What This Project Demonstrates

### Technical Expertise

✔ Real-time stream processing with Kafka & Spark  
✔ Event-driven architecture design  
✔ Data lake engineering with Parquet  
✔ OLAP-ready PostgreSQL modeling  
✔ Workflow automation with Airflow  
✔ Containerized production deployments  

### Business Capabilities

✔ End-to-end pipeline development  
✔ Scalable architecture for high-velocity data  
✔ Production-ready monitoring & orchestration  
✔ Analytics-ready data modeling  
✔ Cloud-native deployment strategies  

---

## 💼 Ideal For Freelance Projects

**Perfect for:**

- Smart City analytics platforms
- IoT data pipeline implementations
- Real-time dashboard solutions
- Kafka / Spark consulting engagements
- Data platform MVPs and prototypes

**Typical Deliverables:**
- Custom data ingestion pipelines
- Real-time analytics platforms
- Cloud migration strategies (AWS EMR, GCP Dataproc, Azure HDInsight)
- Performance optimization & tuning

---

## 🔧 Troubleshooting

**Services not starting?**
```bash
docker compose -f docker/docker-compose.yml logs [service-name]
```

**Reset everything:**
```bash
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
```

## 📞 Contact

**AIT OUFKIR BRAHIM**  
*Big Data Engineer | Spark • Kafka • Airflow Specialist*

📧 **Email:** [aitoufkirbrahimab@gmail.com](mailto:aitoufkirbrahimab@gmail.com)  
💻 **GitHub:** [@biko2020](https://github.com/biko2020)  
💼 **LinkedIn:** [brahim-aitoufkir](https://www.linkedin.com/in/brahim-aitoufkir-74506021a/)

**Open to:**
- Freelance data engineering projects
- Big Data consulting engagements
- Technical architecture reviews
- Cloud migration strategies

---

## 📄 License

MIT License
