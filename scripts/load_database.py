import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

PROCESSED = Path(__file__).parent.parent / "data" / "processed"
DB_PATH   = Path(__file__).parent.parent / "data" / "db" / "bluestock_mf.db"
DB_PATH.parent.mkdir(exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")

#loading schema
SCHEMA = Path(__file__).parent.parent / "sql" / "database.sql"
with engine.connect() as conn:
    for stmt in SCHEMA.read_text().split(";"):
        stmt = stmt.strip()
        if stmt:
            conn.execute(text(stmt))
    conn.commit()
print("Schema created")

#mapping cleaned files to table name
tables = {
    "clean_fund_master.csv":       "dim_fund",
    "clean_nav.csv":               "fact_nav",
    "clean_transactions.csv":      "fact_transactions",
    "clean_performance.csv":       "fact_performance",
    "clean_aum.csv":               "fact_aum",
    "clean_sip_inflows.csv":       "fact_sip_industry",
}

for filename, table in tables.items():
    filepath = PROCESSED / filename
    if not filepath.exists():
        print(f"  skipping {filename} — file not found")
        continue
    df = pd.read_csv(filepath)
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"loaded {len(df)} rows into {table}")

print("Database ready at data/db/bluestock_mf.db")