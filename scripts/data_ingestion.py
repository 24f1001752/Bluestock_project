import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"

files = {
    "fund_master":          "01_fund_master.csv",
    "nav_history":          "02_nav_history.csv",
    "aum_by_fund_house":    "03_aum_by_fund_house.csv",
    "monthly_sip_inflows":  "04_monthly_sip_inflows.csv",
    "category_inflows":     "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance":   "07_scheme_performance.csv",
    "investor_transactions":"08_investor_transactions.csv",
    "portfolio_holdings":   "09_portfolio_holdings.csv",
    "benchmark_indices":    "10_benchmark_indices.csv",
}

datasets = {}
for name, filename in files.items():
    df = pd.read_csv(RAW / filename)
    datasets[name] = df
    print(f"\n{'='*50}")
    print(f" {filename}")
    print(f" Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f" Columns: {list(df.columns)}")
    print(f" Dtypes:\n{df.dtypes.to_string()}")
    print(f" Head:\n{df.head(3).to_string()}")

    print("\n All 10 datasets loaded successfully!")