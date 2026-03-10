import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Loan Approval Predictor", page_icon="🏦", layout="wide")

model = pickle.load(open("loan_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# Sidebar
st.sidebar.title("📊 Model Overview")
st.sidebar.write("""
**Model Used:** Random Forest
**Evaluation Metrics:**
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
""")
st.sidebar.info("This tool predicts whether a loan application will be approved based on applicant information.")

# Title
st.markdown("<h1 style='text-align: center;'>🏦 Loan Approval Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.subheader("Applicant Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", [0,1,2,3])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])

with col2:
    app_income = st.number_input("Applicant Income", min_value=0)
    coapp_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Amount Term", min_value=1)
    credit_history = st.selectbox("Credit History", [0,1])
    property_area = st.selectbox("Property Area", ["Rural","Semiurban","Urban"])

st.markdown("---")

if st.button("🔍 Predict Loan Status"):

    data = {
        "Gender": 1 if gender=="Male" else 0,
        "Married": 1 if married=="Yes" else 0,
        "Dependents": dependents,
        "Education": 1 if education=="Graduate" else 0,
        "Self_Employed": 1 if self_employed=="Yes" else 0,
        "ApplicantIncome": app_income,
        "CoapplicantIncome": coapp_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": {"Rural":0,"Semiurban":1,"Urban":2}[property_area]
    }

    df = pd.DataFrame([data])

    df["Total_Income"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

    if df["Total_Income"].iloc[0] == 0:
        st.error("Total income cannot be zero.")
        st.stop()

    df["Loan_to_Income_Ratio"] = df["LoanAmount"] / df["Total_Income"]
    df["EMI_to_Income_Ratio"] = df["LoanAmount"] / df["Loan_Amount_Term"]

    df = df[model_columns]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    st.markdown("## 📌 Prediction Result")

    colA, colB = st.columns(2)

    with colA:
        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    with colB:
        st.metric("Approval Probability", f"{probability*100:.2f}%")

    st.progress(float(probability))

    # Risk Interpretation
    if probability >= 0.75:
        st.info("Risk Level: Low")
    elif probability >= 0.50:
        st.warning("Risk Level: Moderate")
    else:
        st.error("Risk Level: High")

    st.markdown("---")
    st.subheader("📈 Financial Indicators")
    st.write(f"Total Income: {df['Total_Income'].iloc[0]:,.2f}")
    st.write(f"Loan-to-Income Ratio: {df['Loan_to_Income_Ratio'].iloc[0]:.4f}")
    st.write(f"EMI-to-Income Ratio: {df['EMI_to_Income_Ratio'].iloc[0]:.4f}")
