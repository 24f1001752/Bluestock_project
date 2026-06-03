--to create all tables in SQLite 


CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code         TEXT PRIMARY KEY,
    fund_house        TEXT NOT NULL,
    scheme_name       TEXT NOT NULL,
    category          TEXT,
    sub_category      TEXT,
    plan              TEXT,
    launch_date       DATE,
    benchmark         TEXT,
    expense_ratio_pct REAL,
    exit_load_pct     REAL,
    fund_manager      TEXT,
    risk_category     TEXT,
    sebi_category_code TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    date       DATE NOT NULL UNIQUE,
    year       INTEGER,
    month      INTEGER,
    quarter    INTEGER,
    month_name TEXT,
    is_weekday INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code    TEXT REFERENCES dim_fund(amfi_code),
    date         DATE,
    nav          REAL,
    daily_return REAL
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    tx_id              TEXT PRIMARY KEY,
    investor_id        TEXT,
    amfi_code          TEXT REFERENCES dim_fund(amfi_code),
    transaction_date   DATE,
    transaction_type   TEXT,
    amount_inr         INTEGER,
    state              TEXT,
    city               TEXT,
    city_tier          TEXT,
    age_group          TEXT,
    gender             TEXT,
    annual_income_lakh REAL,
    payment_mode       TEXT,
    kyc_status         TEXT
);

CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code        TEXT REFERENCES dim_fund(amfi_code),
    return_1yr_pct   REAL,
    return_3yr_pct   REAL,
    return_5yr_pct   REAL,
    benchmark_3yr_pct REAL,
    alpha            REAL,
    beta             REAL,
    sharpe_ratio     REAL,
    sortino_ratio    REAL,
    std_dev_ann_pct  REAL,
    max_drawdown_pct REAL,
    morningstar_rating INTEGER
);

CREATE TABLE IF NOT EXISTS fact_aum (
    fund_house   TEXT,
    quarter      TEXT,
    aum_crore    REAL,
    num_schemes  INTEGER
);

CREATE TABLE IF NOT EXISTS fact_sip_industry (
    month                      TEXT PRIMARY KEY,
    sip_inflow_crore           REAL,
    active_sip_accounts_crore  REAL,
    new_sip_accounts_lakh      REAL,
    sip_aum_lakh_crore         REAL,
    yoy_growth_pct             REAL
);