import streamlit as st
import joblib
import numpy as np
model = joblib.load("random_forest.pkl")
st.title("Loan Approval Prediction")
st.write("Enter details:")
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
income = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=0)
cibil = st.number_input("CIBIL Score", min_value=300, max_value=900)
residential = st.number_input("Residential Assets Value", min_value=0)
self_employed_val = 1 if self_employed == "Yes" else 0
if st.button("Predict"):
    input_data = np.array([[
        self_employed_val,
        income,
        loan_amount,
        loan_term,
        cibil,
        residential
    ]])
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)
    approval_prob = prob[0][0] 
    if approval_prob > 0.7:
        risk = "Low Risk"
    elif approval_prob > 0.4:
        risk = "Medium Risk"
    else:
        risk = "High Risk"
    if prediction[0] == 0:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
    st.info(f"Approval Probability: {approval_prob:.2f}")
    st.warning(f"Risk Level: {risk}")
