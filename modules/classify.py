import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.map_sentiments import predict_sentiment
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"  # or another T5 model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def classify_text(text: str) -> str:
    """
    Classifies the sentiment of a single review.
    Returns: 'Negative', 'Neutral', or 'Positive'
    """
    if not text.strip():
        return "No input"

    # Pass model and tokenizer here:
    prediction = predict_sentiment([text], model, tokenizer)
    return prediction[0]
