from importlib import reload
import sys

sys.path.append("..")

# Reload modules to make sure the latest code is used
import scripts.get_dataset
import utils.text_cleaning
import utils.data_process  # optional

reload(scripts.get_dataset)
reload(utils.text_cleaning)
reload(utils.data_process)

# Import functions
from scripts.get_dataset import load_data
from utils.text_cleaning import preprocess_reviews

# Check load_data
print("\nChecking load_data...")
try:
    df = load_data()
    print("load_data() succeeded.")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
except Exception as e:
    print("load_data() failed:", e)

# Check 'reviews.text' column ===
print("\nChecking 'reviews.text' column...")
if "reviews.text" in df.columns:
    print("'reviews.text' column found.")
else:
    print("'reviews.text' column is missing. Check dataset format.")

# Check preprocess_reviews ===
print("\nChecking preprocess_reviews...")
try:
    df_sample = df.head(3).copy()
    df_cleaned = preprocess_reviews(df_sample, column="reviews.text")
    print("preprocess_reviews() succeeded.")
    print("Sample cleaned text:\n", df_cleaned["reviews.text"])
except Exception as e:
    print("preprocess_reviews() failed:", e)
