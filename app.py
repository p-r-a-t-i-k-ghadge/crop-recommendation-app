import streamlit as st
import numpy as np
import pickle

from explainability import get_feature_importance
from llm_helper import explain_with_llm

# ---------------- LOAD MODELS ----------------
model = pickle.load(open("--soil_crop_rf_model.pkl", "rb"))
scaler = pickle.load(open("--soil_feature_scaler.pkl", "rb"))
label_encoder = pickle.load(open("--crop_label_map.pkl", "rb"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Crop Advisor",
    page_icon="🌱",
    layout="centered"
)

st.title("🌾 AI Crop Recommendation System")
st.caption("ML + Explainable AI + LLM (Decision Support System)")

# ---------------- INPUTS ----------------
N = st.number_input("Nitrogen (N)", 0, 140, 50)
P = st.number_input("Phosphorus (P)", 0, 145, 50)
K = st.number_input("Potassium (K)", 0, 205, 50)
temp = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

# ---------------- PREDICTION ----------------
if st.button("Predict Crop"):

    input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)

    # Predict probabilities
    probs = model.predict_proba(input_scaled)[0]
    best_idx = np.argmax(probs)

    crop = label_encoder.inverse_transform([best_idx])[0]
    confidence = probs[best_idx] * 100

    st.success(f"🌱 Recommended Crop: **{crop.upper()}**")
    st.info(f"📊 Confidence: **{confidence:.2f}%**")

    # ---------------- TOP 3 CROPS ----------------
    st.subheader("🥇 Top Crop Alternatives")
    top3_idx = np.argsort(probs)[-3:][::-1]

    for i in top3_idx:
        st.write(
            f"{label_encoder.inverse_transform([i])[0]} → {probs[i]*100:.2f}%"
        )

    # ---------------- EXPLAINABILITY ----------------
    st.subheader("🧠 Why this crop?")
    features = get_feature_importance(model, input_scaled)

    for f, score in features[:4]:
        st.write(f"✔ {f}")

    # ---------------- LLM EXPLANATION ----------------
    st.subheader("🤖 AI Explanation & Suggestions")

    with st.spinner("Generating explanation using AI..."):
        explanation = explain_with_llm(crop, features, confidence)

    st.write(explanation)
