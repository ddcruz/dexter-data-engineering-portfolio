# Airflow Orchestration Pipeline

## 📌 Project Overview
This project demonstrates a production-style orchestration layer using Apache Airflow to manage ingestion, transformation, and validation workflows across Databricks and cloud storage.

## 🏗️ Architecture Diagram
flowchart TD
    A[API / Source Systems] --> B[Airflow DAG<br>Ingestion Task]
    B --> C[Airflow DAG<br>Transform Task]
    C --> D[Databricks Notebook<br>DLT / PySpark]
    D --> E[Delta Lake<br>Bronze/Silver/Gold]
    E --> F[Validation Task<br>Data Quality Checks]
    F --> G[Downstream Consumers<br>BI / ML / Apps]


## 🛠️ Tech Stack
- Apache Airflow
- Databricks (Jobs API / Workflows)
- Python
- Cloud Storage (S3/ADLS)
- Delta Lake

## ✨ Features
- Multi-stage DAG (Ingest → Transform → Validate)
- Databricks operator integration
- Retry logic, SLAs, and alerting
- Parameterized pipelines

## 📂 Project Structure
dags/
notebooks/
configs/
docker-compose.yml


## 🚀 How to Run
1. Start Airflow locally using Docker Compose  
2. Configure Databricks connection  
3. Trigger the DAG manually or via schedule  

## 🧠 Design Decisions
- Why Airflow vs Databricks Workflows  
- How tasks were modularized  
- Error handling strategy  

## 🔮 Future Enhancements
- Add lineage tracking  
- Add dbt integration  

## 📚 Key Learnings
(Add your reflections here)
