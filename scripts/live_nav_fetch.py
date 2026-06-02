import requests
import pandas as pd
from pathlib import Path

RAW = Path(__file__).parent.parent / "data" / "raw"

schemes = {
    "125497": "HDFC_Top100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_LargeCap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip",
}

for code, name in schemes.items():
    print(f"Fetching {name} (code: {code})...")
    try:
        response = requests.get(f"https://api.mfapi.in/mf/{code}", timeout=10)
        data = response.json()
        df = pd.DataFrame(data["data"])
        df["amfi_code"] = code
        df["scheme_name"] = data["meta"].get("scheme_name", name)
        df = df.rename(columns={"date": "nav_date"})
        df = df[["amfi_code", "scheme_name", "nav_date", "nav"]]
        out_path = RAW / f"live_nav_{code}_{name}.csv"
        df.to_csv(out_path, index=False)
        print(f" Saved {len(df)} rows → {out_path.name}")
    except Exception as e:
        print(f" Failed: {e}")

print("\n Live NAV fetch complete!")