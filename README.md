# Credit Risk Modelling — Lauki Finance

Streamlit app that estimates an applicant's **probability of default**, maps it to a **300–900 credit score**, and assigns a rating: Poor / Average / Good / Excellent.

**Live demo:** https://ml-project-credit-risk-modelling-4hzmmlqypqwucbdwscfauv.streamlit.app/

## Problem
An NBFC loan officer needs a quick, explainable check before sanctioning a loan. The model uses application + bureau-style features available at decision time (no post-disbursal leakage).

## Data
50,000 customers / loans / bureau rows joined on `cust_id`.
Target `default` rate ≈ 8.6%.

## Features used in the app
- Age, income, loan amount, tenure
- Loan-to-income ratio
- Avg DPD per delinquency, delinquency ratio
- Credit utilization, open accounts
- Residence type, loan purpose, loan type

## Model
- Logistic regression (`class_weight="balanced"`)
- StandardScaler on train only
- Test AUC on the slim (app) feature set is reported in `notebooks/03_model_logistic.ipynb`
- Score: `300 + (1 - PD) * 600`

## Project layout
app/                Streamlit UI + prediction helper
artifacts/          Saved model + scaler + feature list
data/raw/           Original CSVs
notebooks/          Load/clean, EDA, model
text


Commit + push:

```bat
cd /d D:\Downloads\namaste_ankit_sql\ml_project_2
git add README.md
git commit -m "Add project README with live app link"
git push