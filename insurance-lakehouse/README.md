# Insurance Claims Lakehouse

## 📌 Project Overview
A domain-specific Lakehouse for insurance claims, policies, and underwriting with KPI dashboards.

## 🏗️ Architecture Diagram
flowchart TD
    A[Claims / Policies / Underwriting Data] --> B[Bronze Layer]
    B --> C[Silver Layer<br>Cleaned & Modeled]
    C --> D[Gold Layer<br>KPI Tables]
    D --> E[Dashboards<br>Loss Ratio, Claim Frequency]


## 🛠️ Tech Stack
- Databricks
- Delta Lake
- Power BI / Tableau

## ✨ Features
- Bronze/Silver/Gold layers
- Claims + policy modeling
- KPI dashboards (loss ratio, claim frequency)

## 📂 Project Structure
bronze/
silver/
gold/
dashboards/


## 🚀 How to Run
1. Load raw insurance data  
2. Run transformations  
3. Build dashboard  

## 🧠 Design Decisions
- Domain modeling choices  
- KPI definitions  

## 🔮 Future Enhancements
- Add DV2 model  
- Add dbt tests  

## 📚 Key Learnings
(Add your reflections)
