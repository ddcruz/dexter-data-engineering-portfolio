# Data Vault 2.0 Lakehouse Implementation

## 📌 Project Overview
A DV2 warehouse built on Databricks using Hubs, Links, and Satellites with automated loading patterns.

## 🏗️ Architecture Diagram

        +----------------------+
        |     Raw Data         |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |       Hubs           |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |       Links          |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |     Satellites       |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   Business Vault     |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |  Information Marts   |
        +----------------------+


## 🛠️ Tech Stack
- Databricks
- Delta Lake
- PySpark
- DV2 modeling patterns

## ✨ Features
- Hubs, Links, Satellites
- Automated DV2 load patterns
- Comparison with Medallion Architecture

## 📂 Project Structure
hubs/
links/
satellites/
dv2-load-patterns/


## 🚀 How to Run
1. Load raw data  
2. Run DV2 load notebooks  
3. Validate link integrity  

## 🧠 Design Decisions
- Why DV2 for enterprise modeling  
- Hash key strategy  
- Satellite historization  

## 🔮 Future Enhancements
- Add PIT tables  
- Add bridge tables  

## 📚 Key Learnings
(Add your reflections)
