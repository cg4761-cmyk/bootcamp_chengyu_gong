# Bootcamp Repo

## Project Title
Exploiting Uncertainty from Public Economic Data Releases for Short-Term Arbitrage Across Different Markets

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
In financial markets, major economic data releases (such as CPI, non-farm payrolls, and interest rate decisions) often trigger sharp price movements. These fluctuations may create short-term arbitrage opportunities.

The goal of this project is to explore whether public macroeconomic data releases create short-lived arbitrage opportunities in U.S. equities and cryptocurrency markets, and to further analyze whether, in most cases, the arbitrage direction tends to be long or short.

## Stakeholder & User
- **Stakeholders:** Academic researchers, quantitative research teams, hedge funds, and retail investors. They are interested in whether markets are efficient and whether data releases generate tradeable opportunities in the immediate aftermath.  
- **End Users:** Retail and institutional traders who want to know whether to adjust positions or adopt defensive strategies around data releases.

## Useful Answer & Decision
- **Descriptive:** Show typical volatility patterns in U.S. equities and cryptocurrencies around major economic data releases.  
- **Predictive:** Explore whether different data types (e.g., CPI, employment reports) can predict short-term price direction.  
- **Deliverable:** An event study–based analysis report with charts and conclusions, showing whether arbitrage exists and whether opportunities are more often long or short.

## Assumptions & Constraints
- Historical market data is available (e.g., minute-level U.S. equity data, crypto exchange data).  
- The release times of macroeconomic data are accurate and verifiable. 
- In this project, ‘different markets’ refers specifically to the U.S. equity market and the cryptocurrency market.

## Known Unknowns / Risks
- High-frequency arbitrage opportunities may disappear within milliseconds, making them invisible in public datasets.  
- The 24/7 nature of cryptocurrency markets may lead to different sensitivity and reaction patterns compared to U.S. equities.  
- Data cleaning and synchronization (event time vs. market reaction time) may be challenging.  
- Even when volatility is evident, it may be difficult to determine whether the arbitrage tendency is long or short.  

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Define problem → Stage 01 → README.md + stakeholder memo  
- Collect & align data → Stage 02 → Clean dataset in `/data/`  
- Event study & modeling → Stage 03 → Analysis results in `/notebooks/`  
- Draft conclusions & present → Stage 04 → Final report and presentation in `/docs/`

## Data Storage

This project follows an environment-driven storage layout.

### Folder Structure
```
data/
  raw/        # Raw data saved as CSV (human-readable, universal format)
  processed/  # Processed data saved as Parquet (efficient, compressed, typed)
```

### Formats
- **CSV (in `data/raw/`)**  
  Easy to read in any text editor or spreadsheet tool, widely compatible.  
  Used to store raw datasets as-is.

- **Parquet (in `data/processed/`)**  
  Columnar storage format that is smaller, faster, and preserves data types better than CSV.  
  Used for processed datasets that will be consumed by analysis and modeling code.

### Environment Variables
Storage paths are defined in `.env` for reproducibility and portability:

```
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

These are loaded in notebooks using `python-dotenv`:

```python
from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

RAW_DIR = Path(os.getenv("DATA_DIR_RAW"))
PROCESSED_DIR = Path(os.getenv("DATA_DIR_PROCESSED"))

print("Raw data dir:", RAW_DIR)
print("Processed data dir:", PROCESSED_DIR)
```
