# 🌱 AI Crop Recommendation System

> **ML + Explainable AI + Local LLM — Decision Support System for Smart Farming**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)](https://scikit-learn.org)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-green.svg)](https://ollama.ai)

---

## 🎯 What is this?

An intelligent crop recommendation web application that takes **7 soil and climate parameters** as input and recommends the most suitable crop to grow — powered by a trained **Random Forest Classifier**, **Explainable AI (XAI)**, and a **local Large Language Model via Ollama** for natural language farming advice.

Built as a complete Decision Support System for smart, data-driven agriculture.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌾 **Crop Prediction** | Predicts best crop from 22 classes with confidence score |
| 📊 **Top 3 Alternatives** | Shows ranked crop alternatives with probability scores |
| 🧠 **Why This Crop? (XAI)** | Highlights top soil factors that drove the prediction |
| ✅ **Good Factors** | Shows which parameters are favorable for the predicted crop |
| ⚠️ **Warning Factors** | Flags nutrient deficiencies and weak soil conditions |
| 🤖 **AI Explanation (LLM)** | Ollama generates structured natural language farming advice |
| 💊 **Farming Suggestions** | Actionable tips for soil correction, irrigation, fertilizers |

---

## 🧪 Input Parameters

| Parameter | Unit | Description |
|---|---|---|
| Nitrogen (N) | mg/kg | Nitrogen content in soil |
| Phosphorus (P) | mg/kg | Phosphorus content in soil |
| Potassium (K) | mg/kg | Potassium content in soil |
| Temperature | °C | Average ambient temperature |
| Humidity | % | Relative humidity level |
| Soil pH | — | Acidity / alkalinity of soil |
| Rainfall | mm | Average annual rainfall |

---

## 📊 Sample Output

```
Input:  N=50, P=50, K=50, Temp=25°C, Humidity=60%, pH=6.5, Rainfall=100mm

Recommended Crop : MANGO (26.75% confidence)
Top Alternatives : Papaya (23.33%), Pigeonpeas (12.84%)

Why this crop?   : Humidity ✓  Phosphorus ✓  Rainfall ✓  Temperature ✓

AI Explanation:
  GOOD    → Temperature slightly favorable | Soil pH suitable
  WARNING → Nitrogen deficiency | Low rainfall | Low Potassium
  TIPS    → Apply organic fertilizers | Regular irrigation | Soil testing
```

---

## 🤖 Tech Stack

```
├── Machine Learning     → Scikit-learn (Random Forest Classifier)
├── Explainability       → Custom XAI Module (Feature Importance)
├── LLM Integration      → Ollama (runs fully offline/locally)
├── Frontend             → Streamlit
├── Data Processing      → Pandas, NumPy
└── Model Persistence    → Pickle (.pkl)
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai) installed and running locally

### Step 1 — Clone the repo
```bash
git clone https://github.com/p-r-a-t-i-k-ghadge/crop-recommendation-app
cd crop-recommendation-app
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Start Ollama
```bash
# Run whichever model you have installed
ollama run llama3
# or
ollama run mistral
```

### Step 4 — Launch the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
crop-recommendation-app/
│
├── app.py                     # Main Streamlit application
├── explainability.py          # XAI — feature importance module
├── llm_helper.py              # Ollama LLM integration
├── requirements.txt           # Python dependencies
│
├── soil_crop_rf_model.pkl     # Trained Random Forest model (~9.9 MB)
├── soil_crop_label_map.pkl    # Crop class label encoder
└── soil_feature_scaler.pkl    # Feature scaler (StandardScaler)
```

---

## 🌾 22 Supported Crop Classes

```
Rice · Maize · Chickpea · Kidney Beans · Pigeon Peas · Moth Beans
Mung Bean · Black Gram · Lentil · Pomegranate · Banana · Mango
Grapes · Watermelon · Muskmelon · Apple · Orange · Papaya
Coconut · Cotton · Jute · Coffee
```

---

## 💡 System Architecture

```
User Input (7 soil/climate parameters)
            ↓
   Feature Scaling (StandardScaler)
            ↓
   Random Forest Classifier (22 classes)
            ↓
   ┌─────────────────────────────────┐
   │  Confidence Score               │
   │  Top 3 Crop Alternatives        │
   └─────────────────────────────────┘
            ↓
   XAI Module → Contributing Factors
            ↓
   Ollama LLM → Natural Language Advice
   (Good Factors / Warnings / Farming Tips)
```

---

## 👨‍💻 Author

**Pratik Ghadge**
B.Tech CSE (AI & ML) — Vishwakarma Institute of Information Technology, Pune

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/pratik-ghadge-99b83028a)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/p-r-a-t-i-k-ghadge)

---

⭐ **Star this repo if you found it useful!**
