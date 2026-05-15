import streamlit as st

st.title("Customer Churn Prediction")

tenure = st.slider("Tenure", 1, 72)
monthly = st.slider("Monthly Charges", 1, 150)

if monthly > 80:
    st.error("High chance of churn")
else:
    st.success("Low chance of churn")
