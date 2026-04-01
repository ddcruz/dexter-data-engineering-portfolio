# Spark on Kubernetes (EKS/minikube)

## 📌 Project Overview
A PySpark job containerized and deployed on Kubernetes with Helm and autoscaling.

## 🏗️ Architecture Diagram

        +----------------------+
        | PySpark Job (Docker) |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Container Registry   |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Kubernetes Cluster   |
        | (EKS / minikube)     |
        +----------+-----------+
                   |
        +----------+-----------+
        | Spark Driver Pod     |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Spark Executor Pods  |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | Delta Lake / Storage |
        +----------------------+


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
