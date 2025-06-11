# Add parent directory to Python path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.map_sentiments import predict_sentiment

def classify_text(text: str) -> str:
    """
    Classifies the sentiment of a single review.
    Returns: 'Negative', 'Neutral', or 'Positive'
    """
    if not text.strip():
        return "No input"
    prediction = predict_sentiment([text])
    return prediction[0]
