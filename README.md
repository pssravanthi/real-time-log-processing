# Real-Time Log Processing Pipeline

## 📌 Project Overview
This project implements a **real-time log processing pipeline** using **Kafka, Spark, FastAPI, and Snowflake**. It enables:
- **Streaming log generation** via Kafka.
- **Real-time anomaly detection** using Spark.
- **Storage & retrieval** via Snowflake.
- **REST API exposure** using FastAPI.
- **Monitoring** via Prometheus & Grafana.

## 🛠️ Tech Stack
- **Apache Kafka** → Log streaming.
- **Apache Spark** → Real-time processing.
- **FastAPI** → REST API for log retrieval.
- **Snowflake** → Cloud data storage.
- **Docker & Kubernetes** → Containerized deployment.
- **Prometheus & Grafana** → Monitoring & visualization.

## 🚀 How to Run

### 1️⃣ Start Kafka & Zookeeper
```bash
docker-compose up -d
```

### 2️⃣ Run Log Producer (Generates Logs)
```bash
python log_producer.py
```

### 3️⃣ Run Spark Processing (Detects Anomalies)
```bash
python log_processor.py
```

### 4️⃣ Run API (Exposes Processed Logs)
```bash
uvicorn log_api:app --reload
```

### 5️⃣ Run Monitoring Services
```bash
docker run -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
docker run -p 3000:3000 grafana/grafana
```

## 📡 API Endpoints
- `GET /logs` → Fetch latest processed logs.

## 🔧 Deployment
For production, deploy using **Docker Compose** or **Kubernetes**:
```bash
docker-compose up -d
```
OR
```bash
kubectl apply -f deployment.yaml
```

## 📊 Monitoring with Grafana
- Open **http://localhost:3000** (Grafana UI)
- Open **http://localhost:9090** (Prometheus Metrics)

## 📝 License
This project is open-source and available under the **MIT License**.
