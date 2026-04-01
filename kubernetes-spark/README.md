# Spark on Kubernetes (EKS/minikube)

## 📌 Project Overview
A PySpark job containerized and deployed on Kubernetes with Helm and autoscaling.

## 🏗️ Architecture Diagram
flowchart TD
    A[PySpark Job<br>Docker Image] --> B[Container Registry]
    B --> C[Helm Deployment]
    C --> D[Kubernetes Cluster<br>EKS / minikube]
    D --> E[Spark Driver Pod]
    D --> F[Spark Executor Pods]
    F --> G[Delta Lake / Cloud Storage]


## 🛠️ Tech Stack
- Kubernetes / EKS
- Helm
- Docker
- PySpark

## ✨ Features
- Containerized Spark job
- Helm deployment
- Autoscaling configuration
- Cloud-native Spark execution

## 📂 Project Structure
docker/
helm/
manifests/


## 🚀 How to Run
1. Build Docker image  
2. Deploy via Helm  
3. Monitor Spark job execution  

## 🧠 Design Decisions
- Why K8s vs Databricks clusters  
- Resource allocation strategy  

## 🔮 Future Enhancements
- Add Spark operator  
- Add CI/CD deployment  

## 📚 Key Learnings
(Add your reflections)
