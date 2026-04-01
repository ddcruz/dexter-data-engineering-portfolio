# MLflow Training & Inference Pipeline

## 📌 Project Overview
A Databricks-based ML pipeline demonstrating experiment tracking, model registry usage, and batch inference.

## 🏗️ Architecture Diagram

        +----------------------+
        | Feature Table (Delta)|
        +----------+-----------+
                   |
                   v
        +----------------------+
        |  Training Notebook   |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | MLflow Tracking      |
        | (Metrics, Params)    |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | MLflow Model Registry|
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Batch Inference Job  |
        +----------------------+


## 🛠️ Tech Stack
- MLflow
- Databricks
- Python
- Delta Lake

## ✨ Features
- Model training with MLflow tracking
- Model registry integration
- Batch inference pipeline
- Metrics and artifact logging

## 📂 Project Structure
notebooks/
experiments/
inference/


## 🚀 How to Run
1. Open notebooks in Databricks  
2. Run training notebook  
3. Trigger inference pipeline  

## 🧠 Design Decisions
- Why MLflow for tracking  
- Registry versioning strategy  

## 🔮 Future Enhancements
- Add real-time inference  
- Add feature store integration  

## 📚 Key Learnings
(Add your reflections)
