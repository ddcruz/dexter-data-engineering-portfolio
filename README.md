# dexter-data-engineering-portfolio

Dexter D’Cruz — Data Engineering & Lakehouse Architecture Portfolio

Welcome to my hands‑on portfolio showcasing real-world, end‑to‑end data engineering, cloud architecture, and Databricks Lakehouse solutions.This repository brings together a curated set of projects that demonstrate my expertise across:

Databricks (DLT, Delta Lake, Unity Catalog, Workflows)

Apache Spark / PySpark

Airflow orchestration

dbt modeling

Data Vault 2.0 architecture

Kubernetes/EKS

Microsoft Fabric

MLflow & ML enablement

Vector search & AI‑driven data engineering

CDC ingestion (Debezium, Qlik Replicate)

SRE/monitoring & cost optimization

Cloud platforms: AWS + Azure

Each project is designed to reflect real enterprise use cases, with architecture diagrams, reproducible code, and clear explanations of design decisions.

Portfolio Overview

Below is a structured view of the projects included in this portfolio. Each folder contains:

Source code / notebooks

Architecture diagrams

A detailed README

Setup instructions

Design decisions & trade-offs

/dexter-data-engineering-portfolio
│
├── airflow-orchestration/
├── dbt-lakehouse/
├── mlflow-pipeline/
├── data-vault-2.0/
├── kubernetes-spark/
├── microsoft-fabric-lakehouse/
├── vector-search-engine/
├── salesforce-ingestion/
├── qlik-replicate-cdc/
├── postgres-to-delta/
├── insurance-lakehouse/
└── databricks-monitoring/

Project Summaries

1. Airflow Orchestration

A production-style orchestration layer using Airflow to run ingestion, transformation, and validation pipelines across Databricks and cloud storage.

2. dbt Lakehouse Modeling

A dbt project implementing Bronze → Silver → Gold models on Delta Lake, complete with tests, snapshots, and documentation.

3. MLflow Training & Inference Pipeline

A Databricks-based ML pipeline with experiment tracking, model registry, and batch inference.

4. Data Vault 2.0 Warehouse

A DV2 implementation with hubs, links, satellites, and automated loading patterns.

5. Kubernetes Spark Deployment

A PySpark job containerized and deployed on Kubernetes (minikube/EKS) with Helm and autoscaling.

6. Microsoft Fabric Lakehouse

A Fabric Lakehouse + Warehouse + Pipeline implementation with OneLake integration and a Power BI report.

7. Vector Search Engine

A Databricks vector index + embeddings pipeline with a similarity search API.

8. Salesforce → Databricks Ingestion

A CRM ingestion pipeline using Salesforce REST APIs, cloud storage, and Delta Lake transformations.

9. Qlik Replicate CDC Pipeline

A CDC ingestion pipeline using Qlik Replicate to land changes into Delta Lake.

10. PostgreSQL → Delta ETL

A JDBC-based ingestion pipeline with incremental loads and schema evolution handling.

11. Insurance Claims Lakehouse

A domain-specific Lakehouse with claims, policies, underwriting, and KPI dashboards.

12. Databricks Monitoring & SRE Toolkit

Dashboards, alerts, cost optimization, and SLA/SLO definitions for Lakehouse operations.

🧩 Skills Demonstrated

Databricks & Spark

Delta Live Tables

Delta Lake

Unity Catalog

Workflows

Spark SQL / PySpark

Cloud Platforms

AWS (VPC, IAM, ECS/Fargate, S3, RDS, CloudWatch)

Azure (ADF, ADLS, DevOps, Monitor)

Modern Data Engineering

ETL/ELT pipelines

CDC ingestion (Debezium, Qlik Replicate)

Streaming (Kafka/MSK)

Data modeling (Dimensional, DV2, Medallion)

Orchestration & Automation

Airflow

Databricks Workflows

CI/CD (GitHub Actions, Azure DevOps)

Terraform

ML & AI Enablement

MLflow

Feature engineering

Vector search

Embeddings

Platform Engineering

Kubernetes / Helm

Containerization

Monitoring & SRE practices

🧱 Architecture Map (High-Level)

Below is a conceptual view of how these projects fit together into a modern enterprise Lakehouse ecosystem:

                           +--------------------------------------+
                           |            SOURCE SYSTEMS            |
                           |--------------------------------------|
                           |  APIs  |  Databases  |  Salesforce   |
                           | Kafka  |  Files/Docs |  Streaming    |
                           +------------------+-------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                           INGESTION & ORCHESTRATION                              |
|----------------------------------------------------------------------------------|
|  Airflow DAGs   |   ADF / Fabric Pipelines   |   Qlik Replicate (CDC)            |
|  JDBC Ingestion |   API Extractors           |   Kafka / Streaming Ingest        |
+-----------------+----------------------------+-----------------------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                                LANDING ZONE                                      |
|----------------------------------------------------------------------------------|
|                     Cloud Storage (S3 / ADLS / OneLake)                          |
|                     Delta Lake — BRONZE (Raw Ingested Data)                      |
+----------------------------------------------------------------------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                             TRANSFORMATION LAYER                                 |
|----------------------------------------------------------------------------------|
|  Databricks Notebooks (PySpark / SQL)                                            |
|  Delta Live Tables (DLT)                                                         |
|  dbt Models — SILVER → GOLD                                                      |
|  Data Vault 2.0 (Hubs, Links, Satellites)                                        |
+----------------------------------------------------------------------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                         ADVANCED ANALYTICS & MACHINE LEARNING                    |
|----------------------------------------------------------------------------------|
|  MLflow Tracking & Model Registry                                                |
|  Batch Inference Pipelines                                                       |
|  Vector Search Engine (Embeddings + Index)                                       |
+----------------------------------------------------------------------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                                CONSUMPTION LAYER                                 |
|----------------------------------------------------------------------------------|
|  Gold Tables / Marts                                                             |
|  Power BI / Tableau Dashboards                                                   |
|  Applications / APIs (Search, ML Apps, Services)                                 |
+----------------------------------------------------------------------------------+
                                              |
                                              v
+----------------------------------------------------------------------------------+
|                               PLATFORM ENGINEERING                               |
|----------------------------------------------------------------------------------|
|  Kubernetes / EKS (Spark on K8s)                                                 |
|  CI/CD (GitHub Actions / Azure DevOps)                                           |
|  Unity Catalog (Governance, Security, Lineage)                                   |
|  Monitoring & SRE Toolkit (CloudWatch / Azure Monitor)                           |
+----------------------------------------------------------------------------------+


📬 How to Explore This Portfolio

Each project folder includes:

A detailed README

Architecture diagrams

Setup instructions

Code/notebooks

Design decisions

Resume‑ready bullet points

You can explore them in any order, but the recommended flow is:

Airflow → dbt → Databricks

DV2 → Fabric → Kubernetes

MLflow → Vector Search → Monitoring

🤝 About Me

I’m a Senior Data Engineer & Cloud Architect with 15+ years of experience designing and building enterprise data platforms across AWS, Azure, Databricks, and modern Lakehouse ecosystems. I specialize in:

Databricks platform engineering

Streaming + CDC ingestion

Lakehouse architecture

CI/CD automation

Data modeling & governance

Operational excellence

This portfolio reflects my passion for building scalable, reliable, and elegant data systems.