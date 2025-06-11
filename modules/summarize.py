# Add parent directory to Python path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.t5_model import build_summary_prompt, example_prompt, get_top_products, compare_differences, extract_common_complaints, extract_common_complaints, get_worst_products
from scripts.bart_model import build_bart_summary_prompt, get_top_products, compare_differences, extract_common_complaints, get_worst_products

def summarize_text(text: str, model_type: str = "t5") -> str:
    """
    Summarizes input text using either T5 or BART.
    """
    if not text.strip():
        return "No input text provided."

    if model_type == "t5":
        return summarize_with_t5(text)
    elif model_type == "bart":
        return summarize_with_bart(text)
    else:
        return "Invalid model type. Choose 't5' or 'bart'."
