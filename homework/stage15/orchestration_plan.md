# Orchestration Plan

## 1. Pipeline Overview
This project can be represented as a pipeline with the following main tasks:

1. **Ingest Data**  
2. **Clean & Transform Data**  
3. **Feature Engineering**  
4. **Train Model**  
5. **Save Model**  
6. **Serve via API**  
7. **Generate Report**

---

## 2. Dependencies (DAG)
- Ingest → Clean → Feature Engineering → Train → Save  
- Serve via API depends on the saved model  
- Generate Report depends on both the trained model and evaluation metrics  

A simplified DAG:

Ingest → Clean → Feature Engineering → Train → Save → Serve → Generate Report


---

## 3. Task Details

| Task                  | Input(s)                | Output(s)                | Idempotent | Logging                 | Checkpoints                |
|-----------------------|-------------------------|--------------------------|------------|-------------------------|----------------------------|
| Ingest Data           | Raw CSV files (/data/)  | Clean copy (/data/raw)   | Yes        | logs/ingest.log         | Save snapshot              |
| Clean & Transform     | /data/raw               | /data/clean.csv          | Yes        | logs/clean.log          | Save intermediate dataset  |
| Feature Engineering   | /data/clean.csv         | /data/features.csv       | Yes        | logs/features.log       | Save features file         |
| Train Model           | /data/features.csv      | model/model.pkl          | No         | logs/train.log          | Save metrics + checkpoints |
| Save Model            | model object            | /model/model.pkl         | Yes        | logs/save.log           | Store versioned model      |
| Serve via API         | model/model.pkl         | JSON predictions         | N/A        | logs/api.log            | None                       |
| Generate Report       | metrics + predictions   | reports/final_report.pdf | Yes        | logs/report.log         | Store PDF in /reports/     |

---

## 4. Reliability Plan
- **Failure Points:**  
  - Ingest may fail due to missing/invalid data  
  - Training may fail if input features are empty or corrupted  
  - API may fail under heavy load  

- **Retry Policies:**  
  - Data ingestion retries up to 3 times  
  - Training failure requires manual intervention  
  - API requests log errors, trigger alert if >1% failure  

---

## 5. Automation Decisions
- **Automate Now:**  
  - Ingest, clean, feature engineering, train, save (scripted steps with logging)  
  - API deployment (Flask app auto-start with script)  

- **Manual for Now:**  
  - Stakeholder report review and publishing  
  - Model retraining approval (human-in-the-loop for quality)  

Rationale: Automation of core pipeline ensures reproducibility. Stakeholder-facing deliverables and approval require human oversight.
