# PostgreSQL → Delta Lake ETL Pipeline

## 📌 Project Overview
A JDBC-based ingestion pipeline with incremental loads and schema evolution handling.

## 🏗️ Architecture Diagram

        +----------------------+
        |    PostgreSQL        |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | JDBC Ingestion       |
        | (PySpark)            |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Delta Lake (Bronze)  |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Transformations      |
        | (Silver / Gold)      |
        +----------------------+


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
