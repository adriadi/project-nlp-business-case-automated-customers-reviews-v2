import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Still useful just in case

from transformers import pipeline

# ✅ Explicitly set framework='pt' to skip Keras/TensorFlow
classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment",
    framework="pt"
)

def classify_text(text: str) -> str:
    if not text.strip():
        return "No input"

    result = classifier(text)[0]
    label_map = {
        "LABEL_0": "Negative 😡", # <-- emojis for fun, fun, fun
        "LABEL_1": "Neutral 😐",
        "LABEL_2": "Positive 😍"
    }
    label = label_map.get(result["label"], result["label"])
    score = round(result["score"] * 100, 1)

    if score >= 80:
        confidence = "Definitely"
    elif score >= 60:
        confidence = "Likely"
    else:
        confidence = "Possibly"

    return f"{confidence} {label} ({score}%)"
