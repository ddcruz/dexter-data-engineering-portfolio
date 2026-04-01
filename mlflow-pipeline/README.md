# MLflow Training & Inference Pipeline

## 📌 Project Overview
A Databricks-based ML pipeline demonstrating experiment tracking, model registry usage, and batch inference.

## 🏗️ Architecture Diagram
flowchart TD
    A[Feature Table<br>Delta Lake] --> B[Training Notebook]
    B --> C[MLflow Tracking<br>Metrics, Params, Artifacts]
    C --> D[MLflow Model Registry]
    D --> E[Batch Inference Pipeline]
    E --> F[Predictions Table<br>Delta Lake]
    F --> G[Downstream Apps / BI]


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
