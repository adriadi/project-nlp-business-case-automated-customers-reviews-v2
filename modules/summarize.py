# Add parent directory to Python path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.t5_model import summarize_with_t5
from scripts.bart_model import summarize_with_bart

def summarize_text(text: str, model_type: str = "t5-small") -> str:
    """
    Summarizes input text using either T5 or BART.
    """
    if not text.strip():
        return "No input text provided."

    if model_type == "Get a super short summary (*t5*)":
        return summarize_with_t5(text)
    elif model_type == "Summarise long text (*bart*)":
        return summarize_with_bart(text)
    else:
        return "Invalid model type. Choose 'Get a super short summary (*t5*)' or 'Summarise long text (*bart*)'."