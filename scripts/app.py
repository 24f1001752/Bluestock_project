import streamlit as st
import pandas as pd
from pathlib import Path

PROCESSED = Path(__file__).parent.parent / "data" / "processed"

st.set_page_config(page_title="Bluestock MF Analytics", layout="wide")
st.title("Bluestock Fintech — Mutual Fund Analytics Platform")

# sidebar
page = st.sidebar.selectbox("Select Page", 
    ["Industry Overview", "Fund Performance", "Investor Analytics"])

if page == "Industry Overview":
    st.header("Industry Overview")
    aum = pd.read_csv(PROCESSED / "clean_aum.csv")
    sip = pd.read_csv(PROCESSED / "clean_sip_inflows.csv")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total AUM (Crore)", f"Rs. {aum['aum_crore'].sum():,.0f}")
    col2.metric("Latest SIP Inflow", f"Rs. {sip['sip_inflow_crore'].max():,.0f} Cr")
    col3.metric("Active SIP Accounts", f"{sip['active_sip_accounts_crore'].max():.2f} Cr")
    
    st.subheader("AUM by Fund House")
    aum_grouped = aum.groupby("fund_house")["aum_crore"].sum().sort_values(ascending=False)
    st.bar_chart(aum_grouped)

elif page == "Fund Performance":
    st.header("Fund Performance")
    scorecard = pd.read_csv(PROCESSED / "fund_scorecard.csv")
    
    st.subheader("Fund Scorecard")
    st.dataframe(
        scorecard[["scheme_name","sub_category","cagr_3yr_pct",
                   "sharpe_ratio","composite_score"]]
        .sort_values("composite_score", ascending=False)
        .reset_index(drop=True),
        use_container_width=True
    )

elif page == "Investor Analytics":
    st.header("Investor Analytics")
    tx = pd.read_csv(PROCESSED / "clean_transactions.csv")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Transactions by Type")
        st.bar_chart(tx["transaction_type"].value_counts())
    with col2:
        st.subheader("Investors by State")
        st.bar_chart(tx.groupby("state")["amount_inr"].sum().sort_values(ascending=False))