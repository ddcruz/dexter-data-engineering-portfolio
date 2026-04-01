# Airflow Orchestration Pipeline

## 📌 Project Overview
This project demonstrates a production-style orchestration layer using Apache Airflow to manage ingestion, transformation, and validation workflows across Databricks and cloud storage.

## 🏗️ Architecture Diagram

        +----------------------+
        |   API / Source Data  |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   Airflow Ingestion  |
        |        Task          |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Airflow Transform    |
        |   (Databricks Job)   |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   Delta Lake (Bronze)|
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Data Quality Checks  |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |  Silver / Gold Data  |
        +----------------------+


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
