import subprocess

# Absolute path to Ollama executable
OLLAMA_PATH = r"C:\Users\Pratik G\AppData\Local\Programs\Ollama\ollama.exe"

def explain_with_llm(crop, features, confidence):
    """
    Generates a farmer-friendly explanation for the predicted crop
    using a locally running LLM (Mistral via Ollama).
    """

    prompt = f"""
You are an agricultural expert helping Indian farmers.

STRICT RULES (VERY IMPORTANT):
- Use ONLY the exact values provided below.
- DO NOT guess, assume, or invent any numbers.
- DO NOT change any values.
- Classify each factor as GOOD, WARNING, or POOR based on suitability.
- Be practical and farmer-friendly.
- No technical jargon.

Predicted Crop: {crop}
Model Confidence: {confidence:.2f}

EXACT INPUT VALUES:
Nitrogen (N): {features[0]}
Phosphorus (P): {features[1]}
Potassium (K): {features[2]}
Temperature: {features[3]} °C
Humidity: {features[4]} %
Soil pH: {features[5]}
Rainfall: {features[6]} mm

TASK:
1. List GOOD factors supporting this crop.
2. List WARNING or WEAK factors.
3. Give 2–3 clear, actionable farming suggestions.

IMPORTANT:
- Do NOT add any new numbers.
- Do NOT assume ideal ranges unless obvious from context.
- Keep explanation short, clear, and trustworthy.
"""

    result = subprocess.run(
        [OLLAMA_PATH, "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
