import streamlit as st
import joblib
import numpy as np

model = joblib.load("heart_disease_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💓 Heart Disease Predictor")

age = st.slider("Age", 20, 80, 50)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Serum Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of ST", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = normal, 2 = fixed, 3 = reversible)", [1, 2, 3])

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease!")
    else:
        st.success("✅ No Heart Disease Risk Detected.")
