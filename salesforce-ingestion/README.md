# Salesforce → Databricks Ingestion Pipeline

## 📌 Project Overview
A CRM ingestion pipeline using Salesforce REST APIs, cloud storage, and Delta Lake transformations.

## 🏗️ Architecture Diagram
flowchart TD
    A[Salesforce REST API] --> B[Extraction Script<br>Python]
    B --> C[Cloud Storage<br>S3 / ADLS]
    C --> D[Databricks Ingestion Notebook]
    D --> E[Delta Lake<br>Bronze/Silver/Gold]
    E --> F[Analytics / ML / Dashboards]


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
