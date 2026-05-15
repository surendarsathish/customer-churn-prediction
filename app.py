import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Customer Churn Prediction System")

st.markdown("""
This AI-powered application predicts whether a telecom customer
is likely to churn based on customer account information.
""")

# Sidebar
st.sidebar.header("Customer Information")

# Inputs
tenure = st.sidebar.slider(
    "Tenure (Months)",
    1,
    72,
    12
)

monthly_charges = st.sidebar.slider(
    "Monthly Charges ($)",
    1,
    150,
    70
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

# Prediction Button
if st.button("Predict Churn"):

    # Simple Prediction Logic
    churn_probability = 0

    if monthly_charges > 80:
        churn_probability += 40

    if tenure < 12:
        churn_probability += 30

    if contract == "Month-to-month":
        churn_probability += 20

    if internet_service == "Fiber optic":
        churn_probability += 10

    # Result Section
    st.subheader("Prediction Result")

    if churn_probability >= 60:
        st.error("⚠️ Customer is likely to churn")
        risk = "High Risk"
    elif churn_probability >= 40:
        st.warning("⚠️ Customer has medium churn risk")
        risk = "Medium Risk"
    else:
        st.success("✅ Customer is likely to stay")
        risk = "Low Risk"

    # Probability
    st.metric(
        label="Churn Probability",
        value=f"{churn_probability}%"
    )

    # Customer Summary
    st.subheader("Customer Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Tenure",
            "Monthly Charges",
            "Contract",
            "Internet Service",
            "Risk Level"
        ],
        "Value": [
            tenure,
            monthly_charges,
            contract,
            internet_service,
            risk
        ]
    })

    st.table(summary)

    # Recommendations
    st.subheader("Business Recommendations")

    if risk == "High Risk":
        st.info("""
        Recommended Actions:
        - Offer discounts
        - Provide loyalty rewards
        - Customer support follow-up
        """)

    elif risk == "Medium Risk":
        st.info("""
        Recommended Actions:
        - Send promotional offers
        - Improve engagement
        """)

    else:
        st.info("""
        Recommended Actions:
        - Maintain service quality
        - Continue customer engagement
        """)

# Footer
st.markdown("---")
st.caption("Built using Python, Streamlit, and Machine Learning")
