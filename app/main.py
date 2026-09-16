import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Lauki Finance: Credit Risk", page_icon="📊")
st.title("Lauki Finance: Credit Risk Modelling")

r1 = st.columns(3)
r2 = st.columns(3)
r3 = st.columns(3)
r4 = st.columns(3)

with r1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, value=28)
with r1[1]:
    income = st.number_input("Income", min_value=0, value=1_200_000, step=10000)
with r1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=2_560_000, step=10000)

lti = loan_amount / income if income else 0
st.caption(f"Loan-to-income ratio: {lti:.2f}")

with r2[0]:
    loan_tenure_months = st.number_input("Loan tenure (months)", min_value=1, value=36)
with r2[1]:
    avg_dpd = st.number_input("Avg DPD per delinquency", min_value=0.0, value=0.0)
with r2[2]:
    delinq = st.number_input("Delinquency ratio", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

with r3[0]:
    util = st.number_input("Credit utilization ratio", min_value=0, max_value=100, value=30)
with r3[1]:
    open_acc = st.number_input("Open loan accounts", min_value=0, value=2)
with r3[2]:
    residence_type = st.selectbox("Residence type", ["Owned", "Mortgage", "Rented"])

with r4[0]:
    loan_purpose = st.selectbox("Loan purpose", ["Auto", "Home", "Personal", "Education"])
with r4[1]:
    loan_type = st.selectbox("Loan type", ["Secured", "Unsecured"])

if st.button("Calculate Risk"):
    p, score, rating = predict(
        age, income, loan_amount, loan_tenure_months,
        avg_dpd, delinq, util, open_acc,
        residence_type, loan_purpose, loan_type,
    )
    st.metric("Default probability", f"{p:.2%}")
    st.metric("Credit score", score)
    st.metric("Rating", rating)