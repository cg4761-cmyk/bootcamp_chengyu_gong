# Applied Financial Engineering — Framework Guide

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined the task as building a small ML pipeline to demonstrate financial data workflow, with the goal of predicting labels from simple synthetic features. | Ambiguity in scope (demo vs. real finance). | Kept scope small, emphasized reproducibility and clarity. | Start with a real dataset (e.g., returns, volatility) for more realism. |
| **2. Tooling Setup** | Configured environment with `pandas`, `numpy`, `sklearn`, `flask`, `matplotlib`. | Dependency version mismatches. | Used conda env and `requirements.txt` to lock versions. | Automate setup with Docker. |
| **3. Python Fundamentals** | Applied Python basics: data structures, loops, functions, imports. | Some functions written in notebooks first. | Refactored reusable code into `/src/utils.py`. | More consistent unit testing. |
| **4. Data Acquisition / Ingestion** | Generated synthetic dataset; allowed fallback if CSV missing. | No live financial data. | Built synthetic generator + CSV loader. | Connect to real APIs (Yahoo Finance, Quandl). |
| **5. Data Storage** | Stored raw and processed data in `/data/` folder. | Manual organization. | Adopted folder convention. | Add database backend for scalability. |
| **6. Data Preprocessing** | Cleaned nulls, normalized, encoded features. | Deciding imputation vs. drop. | Tried both median and mean; documented assumptions. | Automate profiling + data validation checks. |
| **7. Outlier Analysis** | Tested rule-based outlier removal (3σ). | Hard to distinguish true signals from noise. | Compared with median-imputation baseline. | Use robust stats or isolation forests. |
| **8. Exploratory Data Analysis (EDA)** | Plotted scatter, bar, and line charts. | Choosing clear visuals for stakeholders. | Used seaborn with consistent style and labels. | Add correlation heatmaps, rolling windows. |
| **9. Feature Engineering** | Created simple features from cleaned dataset. | Limited creativity with synthetic data. | Focused on clarity, documented features. | Add domain-specific ratios or time-series lags. |
| **10. Modeling** | Fit Logistic Regression classifier. | Overfitting risk with small data. | Kept features minimal, tracked accuracy. | Try Random Forests, Gradient Boosting. |
| **11. Evaluation & Risk Communication** | Reported accuracy and metrics. | Communicating assumptions in plain language. | Used thresholds (AUC < 0.6 triggers alert). | Add confidence intervals, cross-validation. |
| **12. Results Reporting & Communication** | Generated charts, Markdown report, stakeholder summary. | Translating technical results into plain insights. | Used concise bullets, images in `/reports/`. | Add interactive dashboard. |
| **13. Productization** | Saved model as `model.pkl`, created `/model/` folder. | Initial save failed (no folder). | Used `Path.mkdir()` to ensure directory exists. | Add version control for models. |
| **14. Deployment & Monitoring** | Deployed Flask API with endpoints (`/predict`, `/plot`). | Testing locally and handling JSON inputs. | Added error handling, tested with `requests`. | Add monitoring: latency, null rate, rolling AUC. |
| **15. Orchestration & System Design** | Wrote orchestration plan with DAG and checkpoints. | Deciding which steps to automate vs manual. | Automated data → train → save → API; manual stakeholder report. | Implement workflow manager (Airflow/Prefect). |
| **16. Lifecycle Review & Reflection** | Reviewed project end-to-end, mapped to lifecycle. | Hard to balance realism vs. simplicity. | Focused on reproducibility and clarity over complexity. | Next time, expand dataset and scale to more realistic finance scenario. |

---

## Reflection Prompts

- **Most difficult stage:** Deployment & Monitoring — designing alerts and ownership structure was abstract without a real production setting.  
- **Most rewarding stage:** Orchestration & Productization — seeing a full pipeline run end-to-end felt like a complete system.  
- **Connections:** Early data-cleaning choices (median vs. mean imputation) affected model results and reporting clarity. Productization required all earlier steps to be modular.  
- **Do differently next time:** Start with a real financial dataset earlier, and set up automated validation from day one.  
- **Skills to strengthen:** System design, workflow automation, and advanced modeling for time-series financial data.  
