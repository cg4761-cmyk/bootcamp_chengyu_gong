# Predicting Bitcoin Price Movements Using Gold Dollar Volume Change

## Project Overview
This project explores whether gold market activity—measured by the change rate of *Gold Close Price × Volume* (dollar volume)—can help predict Bitcoin’s short-term price movements.  

The study follows a simplified end-to-end ML lifecycle:
1. Problem framing and scoping  
2. Data acquisition and storage  
3. Preprocessing and feature engineering  
4. Exploratory data analysis (EDA)  
5. Modeling (regression and classification)  
6. Evaluation and risk communication  
7. Results reporting  

---

## Repository Structure
bootcamp_chengyu_gong/
├── project/
│ ├── data/
│ │ ├── raw/ # Raw datasets (gold & BTC close price, volume)
│ │ └── processed/ # Processed data (returns, dollar volume change)
│ ├── docs/
│ │ └── report.md # Project report with results and discussion
│ ├── notebooks/ # Jupyter notebooks (data prep, modeling)
│ ├── model/ # Trained models (.pkl)
│ ├── image/ # Generated plots (confusion matrix, etc.)
│ └── src/ # Source code scripts
└── README.md # Project overview (this file)


---

## Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd bootcamp_chengyu_gong
```

### 2. Create and activate virtual environment
```bash
conda create -n bootcamp_env python=3.9 -y
conda activate bootcamp_env
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Key Features
- **Data Acquisition:** Yahoo Finance (`yfinance`) API  
- **Feature Engineering:** Constructed Gold and BTC dollar volume, computed daily percentage changes  
- **Modeling:**  
  - Linear Regression (returns prediction)  
  - Logistic Regression (up/down classification)  
- **Visualization:**  
  - Time series plots  
  - Confusion matrix heatmap  

---

## Results Summary
### Regression
- MAE ≈ 0.024  
- RMSE ≈ 0.034  
- R² ≈ -0.005 (almost no explanatory power)  

### Classification
- Accuracy ≈ 52%  
- F1 ≈ 0.68 (but degenerated to always predicting “up”)  

**Conclusion:**  
Gold dollar volume change is not a reliable standalone predictor of Bitcoin’s short-term price direction. Multi-factor approaches are required for meaningful predictive power.  

---

## Future Work
- Add macroeconomic features (USD index, interest rates, VIX, etc.)  
- Incorporate crypto-specific metrics (on-chain activity, funding rates, sentiment data)  
- Test more advanced models (Random Forests, Gradient Boosting, LSTMs)  
- Build a monitoring dashboard for continuous evaluation  

---

## Author
**Chengyu Gong**  
University of Washington → NYU Tandon (Financial Engineering)  
Interested in quantitative research, financial data science, and ML applications in finance  

