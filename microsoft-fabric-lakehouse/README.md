# Microsoft Fabric Lakehouse

## 📌 Project Overview
A Fabric Lakehouse + Warehouse implementation with OneLake ingestion and Fabric Pipelines.

## 🏗️ Architecture Diagram
flowchart TD
    A[Source Data] --> B[OneLake Storage]
    B --> C[Fabric Lakehouse<br>Tables & Files]
    C --> D[Fabric Warehouse<br>SQL Endpoint]
    C --> E[Fabric Pipelines<br>Orchestration]
    D --> F[Power BI Reports]
    E --> C


## 🛠️ Tech Stack
- Microsoft Fabric
- OneLake
- Fabric Pipelines
- Power BI

## ✨ Features
- Fabric Lakehouse creation
- Warehouse modeling
- Pipeline orchestration
- Power BI reporting

## 📂 Project Structure
lakehouse/
pipelines/
warehouse/


## 🚀 How to Run
1. Import dataset into OneLake  
2. Build Lakehouse tables  
3. Run Fabric Pipeline  

## 🧠 Design Decisions
- Why Fabric vs Databricks  
- Warehouse vs Lakehouse usage  

## 🔮 Future Enhancements
- Add KQL queries  
- Add Real-Time Analytics  

## 📚 Key Learnings
(Add your reflections)
