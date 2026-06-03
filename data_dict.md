#data Dict Bluestock MF Capstone project

## dim_fund
| Column | Type | Description |
|---|---|---|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | AMC name |
| scheme_name | TEXT | Full scheme name |
| category | TEXT | Equity / Debt / Hybrid |
| sub_category | TEXT | Large Cap, Mid Cap, etc. |
| expense_ratio_pct | REAL | Annual fee in % |
| risk_category | TEXT | SEBI risk grade |

## fact_nav
| Column | Type | Description |
|---|---|---|
| amfi_code | TEXT | Foreign key to dim_fund |
| date | DATE | NAV date (business days only) |
| nav | REAL | NAV value in Rs. |
| daily_return | REAL | Daily return % |

## fact_transactions
| Column | Type | Description |
|---|---|---|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Amount in rupees |
| state | TEXT | Investor's state |
| city_tier | TEXT | T30 or B30 |
| age_group | TEXT | Age bracket |
| kyc_status | TEXT | Verified or Pending |

## fact_performance
| Column | Type | Description |
|---|---|---|
| return_1yr_pct | REAL | 1-year return % |
| return_3yr_pct | REAL | 3-year CAGR % |
| sharpe_ratio | REAL | Risk-adjusted return |
| alpha | REAL | Excess return vs benchmark |
| beta | REAL | Market sensitivity |
| max_drawdown_pct | REAL | Worst peak-to-trough fall |