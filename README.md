# Goal:
This project analyzes whether the CSE behaves as an efficient market. In an efficient market, trends in financial indicators like Earnings Per Share (EPS) and Net Asset Value (NAV) should be positively correlated with price trends. Additionally, the cash dividends can act as a litmus test to validate the authenticity of reported EPS and NAV figures.
Steps: 
1)Access the correlation between EPS and NAV with price trends of CSE-listed companies
2)Evaluate whether dividend issuance supports the validity of reported EPS and NAV.
3)Estimate the proportion of the CSE market that demonstrates efficiency.

# Findings from the [Dashboard]( https://public.tableau.com/app/profile/jariatun.islam/viz/AnalyzingtheEfficiencyoftheChittagongStockExchange/Dashboard1)
1)83% of the market is efficiently priced based on EPS, reflecting earnings growth in share prices.
2)NAV shows a lower 66% correlation, as asset valuation increases don’t always boost productivity; stronger NAV correlation may appear over longer periods.
3)17% of securities are inefficiently priced, offering short-term trading opportunities and benefits for long-term investors.
4)Gradient of 0.21 that is 21% indicates ROI in the market is higher than the bank’s average return of on avaerage 8.5%.

# Analyzing-the-Efficiency-of-the-Chittagong-Stock-Exchange-CSE-

## Build From Sources and Run the scrapper file

1. Clone the repo

```bash
git clone https://github.com/JariatunIslam/Analyzing-the-Efficiency-of-the-Chittagong-Stock-Exchange-CSE-.git
```

2. Initialize and activate virtual environment

```bash
vitualenv --no-site-packages venv
sources venv/bin/activate
```

3. Install dependemcies

```bash
pip install -r requirements.txt
```

4. Run the Scrapper

```bash
python Web_Scrapper/Nav_EPS_Dataset_Scrapper.py
```

5. Scrappeed Data File name: Companies'_EPS_NAV_Dividend.csv
   Scrappeed data : https://github.com/JariatunIslam/Analyzing-the-Efficiency-of-the-Chittagong-Stock-Exchange-CSE-/blob/main/Web_Scrapper/Companies'_EPS_NAV_Dividend.csv
