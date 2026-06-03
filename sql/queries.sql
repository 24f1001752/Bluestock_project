-- top 5 fund houses by total AUM
SELECT fund_house, ROUND(SUM(aum_crore), 0) AS total_aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;

--avg NAV per month for HDFC top 100
SELECT SUBSTR(date, 1, 7) AS month, ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
WHERE amfi_code = '125497'
GROUP BY month
ORDER BY month;

--SIP inflow yr-on-yr growth
SELECT SUBSTR(month, 1, 4) AS year,
       ROUND(SUM(sip_inflow_crore), 0) AS total_sip_inflow
FROM fact_sip_industry
GROUP BY year
ORDER BY year;

--total transaction amnt by state
SELECT state, ROUND(SUM(amount_inr)/1e7, 2) AS total_crore
FROM fact_transactions
GROUP BY state
ORDER BY total_crore DESC;

--funds with expense ratio below 1%
SELECT amfi_code, scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

--top 5 funds by sharpe ratio
SELECT f.scheme_name, p.sharpe_ratio, p.return_3yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;

--SIP vs lumpsum vs redemption split
SELECT transaction_type,
       COUNT(*) AS num_transactions,
       ROUND(SUM(amount_inr)/1e7, 2) AS total_crore
FROM fact_transactions
GROUP BY transaction_type;

--avg SIP amnt by age grp
SELECT age_group,
       ROUND(AVG(amount_inr), 0) AS avg_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY age_group
ORDER BY age_group;

--fund with highest max drawdown (worst loss)
SELECT f.scheme_name, p.max_drawdown_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.max_drawdown_pct ASC
LIMIT 5;

--count of investors by city tier (T30 vs B30)
SELECT city_tier, COUNT(DISTINCT investor_id) AS num_investors,
       ROUND(SUM(amount_inr)/1e7, 2) AS total_crore
FROM fact_transactions
GROUP BY city_tier;