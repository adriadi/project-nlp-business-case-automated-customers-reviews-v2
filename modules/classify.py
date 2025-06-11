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
    label = result["label"].capitalize()
    score = round(result["score"] * 100, 1)
    return f"{label} ({score}%)"
