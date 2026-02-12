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
│   ├── Dockerfile.superset         # Superset container image
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
│   ├── Dockerfile.airflow          # airflow container image
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
- `pyarrow>=12.0`

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

### 🧪 Development Mode (Manual Testing)

**Ideal for:** Development, debugging, demos, and understanding the pipeline flow

**Terminal 1: Start IoT Data Producer**
```bash
docker exec -it smartcity-spark python3 /app/kafka/producer_iot.py
```
*Generates synthetic sensor events every 5 seconds*

**Terminal 2: Launch Spark Streaming Job**
```bash
docker exec -it smartcity-spark spark-submit /app/spark/streaming_job.py
```
*Consumes Kafka events, processes stream, writes to Parquet*

**Terminal 3: Aggregate and Load KPIs** (after collecting data)
```bash
# Wait 2-3 minutes for data collection, then:
docker exec -it smartcity-spark python3 /app/scripts/load_postgres.py
```
*Reads Parquet files, calculates metrics, loads to PostgreSQL*

**Verify Data in PostgreSQL:**
```bash
docker exec -it smartcity-postgres psql -U postgres -d smartcity_db \
  -c "SELECT * FROM smartcity_kpi;"
```

---

### 🚀 Production Mode (Automated with Airflow)

**Ideal for:** Production deployments, scheduled runs, enterprise environments

**Step 1: Access Airflow Web UI**
```
http://localhost:8080
Login: admin / admin
```

**Step 2: Activate the DAG**
- Navigate to DAGs page
- Find `smartcity_iot_pipeline`
- Toggle the switch to **ON**
- The pipeline will run automatically **every hour** (`@hourly` schedule)

**Step 3: Manual Trigger (Optional)**
- Click on `smartcity_iot_pipeline`
- Click **"Trigger DAG"** button for immediate execution

**Step 4: Monitor Execution**
- View task status in Graph View
- Check logs for each task
- Set up alerts for failures (email/Slack integration)

**DAG Tasks:**
1. **spark_streaming**: Processes Kafka stream → Parquet
2. **load_postgres**: Aggregates KPIs → PostgreSQL

**Benefits:**
- ✅ Automated scheduling (hourly/daily/custom cron)
- ✅ Retry logic on failures
- ✅ Email alerts (configurable)
- ✅ Centralized logging and monitoring
- ✅ DAG versioning and history

---

### 🔄 Continuous Producer

For 24/7 data generation, add a dedicated producer service in `docker-compose.yml`:
```yaml
  kafka-producer:
    image: docker-spark
    container_name: smartcity-producer
    command: python3 /app/kafka/producer_iot.py
    volumes:
      - ../kafka:/app/kafka
    depends_on:
      - kafka
    networks:
      - smartcity-network
    restart: unless-stopped
```

Then start it:
```bash
docker compose -f docker/docker-compose.yml up -d kafka-producer
```

---

## 🌐 Web Interfaces

| Service          | URL                          | Credentials            |
|------------------|------------------------------|------------------------|
| **Airflow**      | http://localhost:8080        | `admin` / `admin`      |
| **Spark UI**     | http://localhost:4040        | N/A (active when running) |
| **Superset**     | http://localhost:8088        | Setup required*        |

**Superset Initial Setup:**
```bash
docker exec -it smartcity-superset superset fab create-admin \
    --username admin --firstname Admin --lastname User \
    --email aitoufkirbrahimab@gmail.com --password admin

docker exec -it smartcity-superset superset db upgrade
docker exec -it smartcity-superset superset init
```
**Use the connection string to connect Superset to Postgres:** 
postgresql://postgres:postgres@smartcity-postgres:5432/smartcity_db


## 📈 KPIs & Analytics

The pipeline calculates real-time metrics:

- **Environmental Metrics**
  - Average temperature per sensor/zone
  - CO₂ concentration trends
  
- **Traffic Analytics**
  - Traffic density indicators
  - Congestion patterns and peak hours
  
- **Operational KPIs**
  - Event throughput (messages/second)
  - Sensor health monitoring
  - Data processing latency

**Sample Query:**
```sql
SELECT 
    sensor_id,
    avg_temperature,
    avg_co2,
    avg_traffic,
    events_count
FROM smartcity_kpi
ORDER BY events_count DESC;
```

---

## 🎯 What This Project Demonstrates

### Technical Expertise

✔ **Real-time stream processing** with Kafka & Spark Structured Streaming  
✔ **Event-driven architecture** for scalable data ingestion  
✔ **Data lake engineering** with columnar Parquet format  
✔ **OLAP-ready data modeling** in PostgreSQL  
✔ **Workflow orchestration** with Airflow DAGs  
✔ **Containerized deployments** using Docker Compose  
✔ **Production vs Development** environment management  

### Business Capabilities

✔ **End-to-end pipeline development** from ingestion to visualization  
✔ **Scalable architecture** handling high-velocity IoT data  
✔ **Production-ready monitoring** and error handling  
✔ **Analytics-ready data models** for BI tools  
✔ **Cloud-native design** (AWS/GCP/Azure compatible)  
✔ **DevOps best practices** (IaC, containerization, CI/CD ready)  

---

## 💼 Ideal For Freelance Projects

**Perfect for:**

- Smart City analytics platforms
- IoT data pipeline implementations  
- Real-time monitoring dashboards
- Kafka / Spark consulting engagements
- Data platform MVPs and prototypes
- ETL/ELT modernization projects

**Typical Deliverables:**
- Custom streaming data pipelines
- Real-time analytics platforms
- Cloud migration strategies (AWS EMR, GCP Dataproc, Azure HDInsight)
- Performance optimization & tuning
- Data governance frameworks
- Training and knowledge transfer

---

## 🔧 Troubleshooting

**Services not starting?**
```bash
docker compose -f docker/docker-compose.yml logs [service-name]
```

**Airflow scheduler not running?**
```bash
docker compose -f docker/docker-compose.yml restart airflow-scheduler
docker logs smartcity-airflow-scheduler
```

**Spark job failing with Kafka connector error?**
```bash
# Ensure Kafka JARs are included in spark-submit
docker exec -it smartcity-spark spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 \
  /app/spark/streaming_job.py
```

**Reset everything:**
```bash
# Warning: This deletes all data volumes
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
```

**Check data persistence:**
```bash
# View generated Parquet files
docker exec -it smartcity-spark ls -lh /app/data/processed/smartcity/

# Check PostgreSQL data
docker exec -it smartcity-postgres psql -U postgres -d smartcity_db \
  -c "SELECT COUNT(*) FROM smartcity_kpi;"
```

---

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
- Team training and mentorship

---

## 📄 License

MIT License
