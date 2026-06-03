import pandas as pd
import numpy as np
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"
PROCESSED = Path(__file__).parent.parent / "data" / "processed"
PROCESSED.mkdir(exist_ok=True)

#clean NAV hist
print("Cleaning nav_history")
nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates(subset=["amfi_code", "date"])
nav = nav[nav["nav"] > 0]

#fill missing NAV
nav = nav.set_index("date").groupby("amfi_code").apply(
    lambda x: x.reindex(pd.bdate_range(x.index.min(), x.index.max())).ffill()
).drop(columns="amfi_code").reset_index()
nav = nav.rename(columns={"level_1": "date"})

nav.to_csv(PROCESSED / "clean_nav.csv", index=False)
print(f"done — {len(nav)} rows saved")

#Clean investor transact
print("Cleaning investor_transactions")
tx = pd.read_csv(RAW / "08_investor_transactions.csv")

tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])
tx["transaction_type"] = tx["transaction_type"].str.strip().str.title()
tx = tx[tx["amount_inr"] > 0]
tx = tx.drop_duplicates()
tx["kyc_status"] = tx["kyc_status"].str.strip()
valid_kyc = ["Verified", "Pending"]
tx = tx[tx["kyc_status"].isin(valid_kyc)]

tx.to_csv(PROCESSED / "clean_transactions.csv", index=False)
print(f"  done — {len(tx)} rows saved")

#clean scheme perf 
print("Cleaning scheme_performance...")
perf = pd.read_csv(RAW / "07_scheme_performance.csv")

numeric_cols = ["return_1yr_pct","return_3yr_pct","return_5yr_pct",
                "sharpe_ratio","sortino_ratio","alpha","beta",
                "std_dev_ann_pct","max_drawdown_pct"]
for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf = perf[perf["expense_ratio_pct"].between(0.1, 2.5)] if "expense_ratio_pct" in perf.columns else perf
perf = perf.dropna(subset=["return_1yr_pct","sharpe_ratio"])

perf.to_csv(PROCESSED / "clean_performance.csv", index=False)
print(f"done — {len(perf)} rows saved")

#clean fund master 
print("Cleaning fund_master")
fm = pd.read_csv(RAW / "01_fund_master.csv")
fm = fm.drop_duplicates(subset="amfi_code")
fm["launch_date"] = pd.to_datetime(fm["launch_date"])
fm["expense_ratio_pct"] = pd.to_numeric(fm["expense_ratio_pct"], errors="coerce")
fm.to_csv(PROCESSED / "clean_fund_master.csv", index=False)
print(f"done — {len(fm)} rows saved")

#cleaning remaining files
simple_files = {
    "03_aum_by_fund_house.csv":    "clean_aum.csv",
    "04_monthly_sip_inflows.csv":  "clean_sip_inflows.csv",
    "05_category_inflows.csv":     "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_folio_count.csv",
    "09_portfolio_holdings.csv":   "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv":    "clean_benchmark_indices.csv",
}
for raw_file, clean_file in simple_files.items():
    df = pd.read_csv(RAW / raw_file)
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    df.to_csv(PROCESSED / clean_file, index=False)
    print(f"  {clean_file} — {len(df)} rows saved")

print("All datasets cleaned and saved to data/processed/")