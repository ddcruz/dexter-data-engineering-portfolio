# Qlik Replicate CDC Pipeline

## 📌 Project Overview
A CDC ingestion pipeline using Qlik Replicate to land changes into Delta Lake.

## 🏗️ Architecture Diagram
flowchart TD
    A[Source Database<br>Postgres / SQL Server] --> B[Qlik Replicate<br>CDC Stream]
    B --> C[Landing Zone<br>Cloud Storage]
    C --> D[Databricks CDC Loader]
    D --> E[Delta Lake<br>Bronze/Silver]
    E --> F[Gold Layer / Marts]


## 🛠️ Tech Stack
- Qlik Replicate
- Databricks
- Delta Lake

## ✨ Features
- CDC capture
- Incremental loads
- Schema evolution handling

## 📂 Project Structure
configs/
scripts/
delta-lake-target/


## 🚀 How to Run
1. Configure Qlik Replicate task  
2. Start CDC stream  
3. Validate Delta Lake output  

## 🧠 Design Decisions
- Why Qlik vs Debezium  
- Handling schema drift  

## 🔮 Future Enhancements
- Add SCD logic  
- Add monitoring  

## 📚 Key Learnings
(Add your reflections)
