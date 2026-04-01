# Salesforce → Databricks Ingestion Pipeline

## 📌 Project Overview
A CRM ingestion pipeline using Salesforce REST APIs, cloud storage, and Delta Lake transformations.

## 🏗️ Architecture Diagram

        +----------------------+
        | Salesforce REST API  |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Extraction Script    |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Cloud Storage        |
        | (S3 / ADLS)          |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Databricks Ingestion |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Delta Lake Layers    |
        | Bronze / Silver /Gold|
        +----------------------+


## 🛠️ Tech Stack
- Salesforce REST API
- Python
- Databricks
- Delta Lake

## ✨ Features
- API extraction
- Incremental ingestion
- Delta Lake transformations

## 📂 Project Structure
api-scripts/
ingestion/
transformations/


## 🚀 How to Run
1. Configure Salesforce credentials  
2. Run extraction script  
3. Process data in Databricks  

## 🧠 Design Decisions
- API pagination strategy  
- Incremental load logic  

## 🔮 Future Enhancements
- Add CDC  
- Add dbt models  

## 📚 Key Learnings
(Add your reflections)
