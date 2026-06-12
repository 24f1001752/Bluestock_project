# Bluestock MF Capstone — Mutual Fund Analytics Platform

## Project Overview
A full-stack Mutual Fund Analytics Platform built for Bluestock Fintech 
as part of the Data Analyst Internship Capstone (June 2026).

The platform ingests publicly available mutual fund data from AMFI India, 
transforms it through an ETL pipeline, stores it in a SQLite database, 
computes risk-return metrics, and presents insights via an interactive dashboard.

## Project Structure

bluestock_mf_capstone/

├── data/

│   ├── raw/            ← Original CSV datasets (10 files)

│   ├── processed/      ← Cleaned and transformed CSVs

│   └── db/             ← SQLite database (bluestock_mf.db)

├── notebooks/

│   ├── 01_data_ingestion.ipynb

│   ├── 03_eda_analysis.ipynb

│   ├── 04_performance_analytics.ipynb

│   └── 05_advanced_analytics.ipynb

├── scripts/

│   ├── data_ingestion.py

│   ├── data_cleaning.py

│   ├── load_database.py

│   ├── recommender.py

│   └── run_pipeline.py

├── sql/

│   ├── schema.sql

│   └── queries.sql

├── dashboard/

│   └── bluestock_mf_dashboard.pbix

├── reports/

│   ├── Final_Report.pdf

│   └── *.png (all exported charts)

├── data_dictionary.md

├── requirements.txt

└── README.md

## Tech Stack
| Tool | Purpose |
|---|---|
| Python 3.13 | ETL pipeline, analytics, scripting |
| Pandas / NumPy | Data cleaning, transformation, metrics |
| Matplotlib / Seaborn / Plotly | Data visualisation |
| SQLite + SQLAlchemy | Relational database |
| SciPy | OLS regression for Alpha/Beta |
| Power BI | Interactive dashboard |
| Git + GitHub | Version control |

## Datasets Used
| File | Rows | Description |
|---|---|---|
| 01_fund_master.csv | 40 | Master list of 40 MF schemes |
| 02_nav_history.csv | ~46,000 | Daily NAV Jan 2022 – May 2026 |
| 03_aum_by_fund_house.csv | 90 | Quarterly AUM for top 10 AMCs |
| 04_monthly_sip_inflows.csv | 48 | Monthly SIP inflow data |
| 05_category_inflows.csv | 144 | Net inflows by category |
| 06_industry_folio_count.csv | 21 | Industry folio growth |
| 07_scheme_performance.csv | 40 | Pre-computed risk metrics |
| 08_investor_transactions.csv | ~55,000 | Investor transaction records |
| 09_portfolio_holdings.csv | 320 | Equity fund stock holdings |
| 10_benchmark_indices.csv | ~8,000 | Daily benchmark index values |


## how to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/bluestock_mf_capstone.git
cd bluestock_mf_capstone
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the full ETL pipeline
```bash
python scripts/run_pipeline.py
```

### 4. Open notebooks for analysis
```bash
jupyter notebook
```

### 5. Open the dashboard
Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop.

## Key Metrics Computed
- CAGR (1yr, 3yr, 5yr) for all 40 funds
- Sharpe Ratio and Sortino Ratio
- Alpha and Beta vs Nifty 100 benchmark
- Maximum Drawdown
- Value at Risk (VaR 95%) and CVaR
- Rolling 90-day Sharpe Ratio
- Fund Composite Scorecard (0–100)
- Sector HHI Concentration Score


## Dashboard Pages
1. **Industry Overview** — AUM trends, SIP inflows, folio growth
2. **Fund Performance** — Risk-return scatter, fund scorecard, NAV vs benchmark
3. **Investor Analytics** — Geographic distribution, demographics, transaction patterns
4. **SIP & Market Trends** — SIP vs Nifty 50, category inflows, top performers

## Author
Anish Abhyankar
