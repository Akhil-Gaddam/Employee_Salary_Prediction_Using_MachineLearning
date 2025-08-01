import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature columns
model = joblib.load("model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(page_title="Employee Salary Prediction", layout="centered")
st.title("Employee Salary Prediction App")

st.markdown("Fill in the employee details below to predict their salary in USD and converted INR.")

# User inputs

work_year = st.selectbox("Work Year", [2020, 2021, 2022, 2023])
experience_level = st.selectbox("Experience Level", ['EN', 'MI', 'SE', 'EX'])
employment_type = st.selectbox("Employment Type", ['FT', 'PT', 'CT', 'FL'])
remote_ratio = st.slider("Remote Work Ratio (%)", 0, 100, 50)
company_size = st.selectbox("Company Size", ['S', 'M', 'L'])

# Job Title dropdown
job_title = st.selectbox("Job Title", [
    'Data Engineer', 'Data Scientist', 'Data Analyst', 'Machine Learning Engineer',
    'Analytics Engineer', 'Data Architect', 'Research Scientist', 'Applied Scientist',
    'Data Science Manager', 'Research Engineer', 'ML Engineer', 'Data Manager',
    'Machine Learning Scientist', 'Data Science Consultant', 'Data Analytics Manager',
    'Computer Vision Engineer', 'AI Scientist', 'BI Data Analyst', 'Business Data Analyst',
    'Data Specialist'
])

# Employee Residence dropdown
employee_residence = st.selectbox("Employee Residence", [
    'US', 'GB', 'CA', 'ES', 'IN', 'DE', 'FR', 'PT', 'BR', 'GR',
    'NL', 'AU', 'MX', 'PK', 'IT', 'IE', 'JP', 'NG', 'AR', 'AT'
])

# Company Location dropdown
company_location = st.selectbox("Company Location", [
    'US', 'GB', 'CA', 'ES', 'IN', 'DE', 'FR', 'BR', 'GR', 'PT',
    'AU', 'NL', 'MX', 'IE', 'SG', 'AT', 'JP', 'NG', 'PL', 'CH'
])


# Create a dataframe from user inputs
user_input = pd.DataFrame([{
    "work_year": work_year,
    "experience_level": experience_level,
    "employment_type": employment_type,
    "job_title": job_title,
    "employee_residence": employee_residence,
    "remote_ratio": remote_ratio,
    "company_location": company_location,
    "company_size": company_size
}])

# One-hot encode user input using training feature columns
user_encoded = pd.get_dummies(user_input)
user_encoded = user_encoded.reindex(columns=feature_columns, fill_value=0)

# Predict salary
if st.button("Predict Salary"):
    prediction_usd = model.predict(user_encoded)[0]
    prediction_inr = prediction_usd * 83  # Adjust conversion rate if needed

    formatted_usd = f"$ {prediction_usd:,.2f}"
    formatted_inr = f"{prediction_inr:,.2f}"

    st.subheader("Predicted Salary:")
    st.markdown(f"**USD:** {formatted_usd}  \n**INR:** {formatted_inr}")
