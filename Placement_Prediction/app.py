
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓"
)

st.title("🎓 Student Placement Predictor")
st.write("Enter student details below.")

# Load trained model and scaler from this script's directory
APP_DIR = Path(__file__).resolve().parent
model = joblib.load(APP_DIR / "placement_model.pkl")
scaler = joblib.load(APP_DIR / "scaler.pkl")

# User inputs
cgpa = st.number_input(
    "Enter CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.5,
    step=0.1
)

iq = st.number_input(
    "Enter IQ",
    min_value=1,
    max_value=200,
    value=110,
    step=1
)

if st.button("Predict Placement"):
    student = pd.DataFrame({
        "cgpa": [cgpa],
        "iq": [iq]
    })

    # Scale input using the saved scaler
    student_scaled = scaler.transform(student)

    # Make prediction
    prediction = model.predict(student_scaled)[0]

    # Get model-estimated probability
    probabilities = model.predict_proba(student_scaled)[0]
    classes = list(model.classes_)
    probability_y = probabilities[classes.index("Y")]

    st.subheader("Prediction Result")

    if prediction == "Y":
        st.success("Model Prediction: Placement YES")
    else:
        st.warning("Model Prediction: Placement NO")

    st.write(
        f"Estimated probability of Y: "
        f"{probability_y * 100:.2f}%"
    )

    st.caption(
        "Practice project using synthetic data; "
        "this is not a reliable real-world placement prediction."
    )
