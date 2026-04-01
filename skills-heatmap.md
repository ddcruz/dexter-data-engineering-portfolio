%% Mermaid doesn't have a native heatmap, so we simulate one using a matrix-style table.
%% Darker colors = stronger proficiency + more project coverage.

flowchart LR

    %% Define styles
    classDef high fill:#2ecc71,stroke:#1e8449,color:#fff
    classDef med fill:#f1c40f,stroke:#b7950b,color:#000
    classDef low fill:#e67e22,stroke:#a04000,color:#fff
    classDef none fill:#e74c3c,stroke:#922b21,color:#fff

    %% Skills
    S1[Databricks / Lakehouse]
    S2[Airflow / Orchestration]
    S3[dbt / Analytics Engineering]
    S4[Data Modeling<br>DV2 / Dimensional]
    S5[Spark / PySpark / SQL]
    S6[CDC / Streaming<br>Qlik / Kafka]
    S7[Cloud Architecture<br>AWS / Azure / Fabric]
    S8[MLflow / ML Enablement]
    S9[Vector Search / Embeddings]
    S10[Kubernetes / Platform Engineering]
    S11[Monitoring / SRE]
    S12[Domain Knowledge<br>Insurance / CRM]

    %% Projects
    P1[Airflow Orchestration]
    P2[dbt Lakehouse]
    P3[MLflow Pipeline]
    P4[Data Vault 2.0]
    P5[Spark on Kubernetes]
    P6[Microsoft Fabric Lakehouse]
    P7[Vector Search Engine]
    P8[Salesforce Ingestion]
    P9[Qlik Replicate CDC]
    P10[Postgres → Delta ETL]
    P11[Insurance Claims Lakehouse]
    P12[Databricks Monitoring Toolkit]

    %% Connections (colored by proficiency level)
    %% Databricks / Lakehouse
    S1 --- P1:::high
    S1 --- P2:::high
    S1 --- P3:::high
    S1 --- P4:::high
    S1 --- P10:::high
    S1 --- P11:::high

    %% Airflow
    S2 --- P1:::high
    S2 --- P6:::med

    %% dbt
    S3 --- P2:::high
    S3 --- P11:::med

    %% Data Modeling
    S4 --- P2:::med
    S4 --- P4:::high
    S4 --- P11:::med

    %% Spark / PySpark
    S5 --- P1:::high
    S5 --- P2:::high
    S5 --- P3:::high
    S5 --- P10:::high
    S5 --- P11:::high

    %% CDC / Streaming
    S6 --- P9:::high
    S6 --- P1:::med
    S6 --- P10:::med

    %% Cloud Architecture
    S7 --- P5:::high
    S7 --- P6:::high
    S7 --- P1:::med
    S7 --- P10:::med

    %% MLflow
    S8 --- P3:::high
    S8 --- P11:::med

    %% Vector Search
    S9 --- P7:::high

    %% Kubernetes / Platform
    S10 --- P5:::high
    S10 --- P1:::med
    S10 --- P12:::med

    %% Monitoring / SRE
    S11 --- P12:::high
    S11 --- P1:::med
    S11 --- P3:::med

    %% Domain Knowledge
    S12 --- P11:::high
    S12 --- P8:::