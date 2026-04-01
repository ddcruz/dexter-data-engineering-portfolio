# PostgreSQL → Delta Lake ETL Pipeline

## 📌 Project Overview
A JDBC-based ingestion pipeline with incremental loads and schema evolution handling.

## 🏗️ Architecture Diagram
flowchart TD
    A[PostgreSQL] --> B[JDBC Ingestion<br>PySpark]
    B --> C[Delta Lake<br>Bronze]
    C --> D[Transformations<br>Silver]
    D --> E[Aggregations<br>Gold]
    E --> F[BI / ML Consumers]


## 🛠️ Tech Stack
- PostgreSQL
- Databricks
- Delta Lake
- PySpark

## ✨ Features
- JDBC ingestion
- Incremental ETL
- Schema evolution

## 📂 Project Structure
ingestion/
jdbc/
transformations/


## 🚀 How to Run
1. Start Postgres instance  
2. Configure JDBC connection  
3. Run ingestion notebook  

## 🧠 Design Decisions
- Incremental load strategy  
- Handling schema changes  

## 🔮 Future Enhancements
- Add CDC  
- Add dbt models  

## 📚 Key Learnings
(Add your reflections)
