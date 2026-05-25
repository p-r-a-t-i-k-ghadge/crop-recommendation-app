import numpy as np

FEATURE_NAMES = [
    "Nitrogen",
    "Phosphorus",
    "Potassium",
    "Temperature",
    "Humidity",
    "Soil pH",
    "Rainfall"
]

def get_feature_importance(model, input_scaled):
    importances = model.feature_importances_

    impact = importances * input_scaled[0]

    sorted_features = sorted(
        zip(FEATURE_NAMES, impact),
        key=lambda x: abs(x[1]),
        reverse=True
    )

    return sorted_features
