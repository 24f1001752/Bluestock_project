"""
Fund Recommender — Bluestock MF Capstone
Recommends top 3 funds based on investor risk appetite.
"""
import pandas as pd
from pathlib import Path

PROCESSED = Path(__file__).parent.parent / "data" / "processed"

def recommend_funds(risk_appetite: str) -> pd.DataFrame:
    """
    Recommend top 3 funds based on risk appetite.
    
    Parameters:
        risk_appetite: "Low", "Moderate", or "High"
    
    Returns:
        DataFrame with top 3 recommended funds
    """
    scorecard = pd.read_csv(PROCESSED / "fund_scorecard.csv")
    fm        = pd.read_csv(PROCESSED / "clean_fund_master.csv")
    
    join_cols = ["amfi_code", "risk_category"]
    if "expense_ratio_pct" in fm.columns:
        join_cols.append("expense_ratio_pct")

    merged = scorecard.merge(fm[join_cols], on="amfi_code", how="left")
    if "expense_ratio_pct" not in merged.columns:
        merged["expense_ratio_pct"] = pd.NA
    
    # map user input to SEBI risk categories
    risk_map = {
        "Low"      : ["Low", "Low to Moderate"],
        "Moderate" : ["Moderate", "Low to Moderate"],
        "High"     : ["High", "Very High"],
    }
    
    risk_appetite = risk_appetite.strip().title()
    if risk_appetite not in risk_map:
        print(f"Invalid input. Choose from: Low, Moderate, High")
        return pd.DataFrame()
    
    valid_categories = risk_map[risk_appetite]
    filtered = merged[merged["risk_category"].isin(valid_categories)].copy()
    
    if filtered.empty:
        print(f"No funds found for risk appetite: {risk_appetite}")
        return pd.DataFrame()
    
    # rank by composite score
    cols = ["scheme_name", "sub_category", "risk_category",
            "sharpe_ratio", "cagr_3yr_pct", "composite_score"]
    if "expense_ratio_pct" in filtered.columns:
        cols.insert(-1, "expense_ratio_pct")

    top3 = (filtered.sort_values("composite_score", ascending=False)
                    .head(3)
                    [cols]
                    .reset_index(drop=True))
    
    top3.index = top3.index + 1  # rank starts at 1
    return top3


if __name__ == "__main__":
    for appetite in ["Low", "Moderate", "High"]:
        print(f"\n{'='*60}")
        print(f"Top 3 Funds for {appetite.upper()} risk appetite:")
        print('='*60)
        result = recommend_funds(appetite)
        if not result.empty:
            print(result.to_string())