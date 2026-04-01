# dbt Lakehouse Modeling on Delta Lake

## 📌 Project Overview
A dbt project implementing Bronze → Silver → Gold transformations on Delta Lake with tests, snapshots, and documentation.

## 🏗️ Architecture Diagram

        +----------------------+
        |   Bronze Layer       |
        |   (Raw Delta)        |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   dbt Models         |
        |   (Silver Layer)     |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   dbt Models         |
        |   (Gold Layer)       |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   dbt Tests & Docs   |
        +----------------------+


## 🛠️ Tech Stack
- dbt Core / dbt Cloud
- Databricks SQL
- Delta Lake

## ✨ Features
- Layered Lakehouse modeling
- dbt tests (unique, not null, accepted values)
- Snapshots for SCD handling
- Auto-generated documentation

## 📂 Project Structure
models/
snapshots/
tests/
profiles.yml (example)


## 🚀 How to Run
1. Install dbt  
2. Configure Databricks profile  
3. Run `dbt run` and `dbt test`  

## 🧠 Design Decisions
- Why dbt for Lakehouse modeling  
- Naming conventions  
- Testing strategy  

## 🔮 Future Enhancements
- Add macros  
- Add incremental models  

## 📚 Key Learnings
(Add your reflections)
