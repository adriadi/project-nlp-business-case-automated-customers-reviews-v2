
from importlib import reload
import pandas as pd
import nltk



# Get the CSV path from the dataset folder (where kagglehub put it)
csv_file = "./code/dataset/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv"

def load_data():
    return pd.read_csv(csv_file)


# Reload modules to make sure the latest code is used
import functions.data_process
import functions.metadata
import functions.text_cleaning
# import functions.validate_clustering     <-- available for future use
# import functions.visualize_pca
# import functions.visualize_tsne

reload(functions.data_process)
reload(functions.metadata)
reload(functions.text_cleaning)
# reload(functions.validate_clustering)
# reload(functions.visualize_pca)
# reload(functions.visualize_tsne)

# Import functions
from functions.data_process import tokenize, clean_text, filter_data, remove_empty, remove_duplicates
from functions.text_cleaning import preprocess_reviews
from functions.metadata import unique_brands, unique_categories, unique_primary_categories, unique_manufacturers, unique_product_names
# from functions.validate_clustering import validate_clustering
# from functions.visualize_pca import visualize_pca   
# from functions.visualize_tsne import visualize_tsne

if 'df' in locals():
    print("\nChecking 'reviews.text' column...")
    if "reviews.text" in df.columns:
        print("✅ 'reviews.text' column found.")
    else:
        print("❌ 'reviews.text' column is missing. Check dataset format.")
else:
    print("\n⚠️ Skipping column check — df not loaded.")


# Check load_data
print("\nChecking load_data...")
try:
    df = load_data()
    print("✅ load_data() succeeded.")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
except Exception as e:
    print("❌ load_data() failed:", e)

# Check 'reviews.text' column
print("\nChecking 'reviews.text' column...")
if "reviews.text" in df.columns:
    print("✅ 'reviews.text' column found.")
else:
    print("❌ 'reviews.text' column is missing. Check dataset format.")

# Check preprocess_reviews
print("\nChecking preprocess_reviews...")
try:
    df_sample = df.head(3).copy()
    df_cleaned = preprocess_reviews(df_sample, column="reviews.text")
    print("✅ preprocess_reviews() succeeded.")
    print("Sample cleaned text:\n", df_cleaned["reviews.text"])
except Exception as e:
    print("❌ preprocess_reviews() failed:", e)
