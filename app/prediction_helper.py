from pathlib import Path
import joblib
import pandas as pd

ART = Path(__file__).resolve().parents[1] / "artifacts" / "model_data.joblib"
BUNDLE = joblib.load(ART)
MODEL = BUNDLE["model"]
SCALER = BUNDLE["scaler"]
FEATURES = BUNDLE["features"]

def pd_to_score_rating(p: float):
    score = int(round(300 + (1 - p) * 600))
    score = min(900, max(300, score))
    if score <= 499:
        rating = "Poor"
    elif score <= 649:
        rating = "Average"
    elif score <= 749:
        rating = "Good"
    else:
        rating = "Excellent"
    return score, rating

def predict(
    age, income, loan_amount, loan_tenure_months,
    avg_dpd_per_delinquency, delinquency_ratio,
    credit_utilization_ratio, number_of_open_accounts,
    residence_type, loan_purpose, loan_type,
):
    loan_to_income = loan_amount / income if income else 0.0
    row = pd.DataFrame([{
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "loan_tenure_months": loan_tenure_months,
        "loan_to_income": loan_to_income,
        "avg_dpd_per_delinquency": avg_dpd_per_delinquency,
        "delinquency_ratio": delinquency_ratio,
        "credit_utilization_ratio": credit_utilization_ratio,
        "number_of_open_accounts": number_of_open_accounts,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type,
    }])
    row = pd.get_dummies(row, columns=["residence_type", "loan_purpose", "loan_type"], drop_first=True)
    row = row.reindex(columns=FEATURES, fill_value=0)
    xs = SCALER.transform(row)
    p = float(MODEL.predict_proba(xs)[0, 1])
    score, rating = pd_to_score_rating(p)
    return p, score, rating