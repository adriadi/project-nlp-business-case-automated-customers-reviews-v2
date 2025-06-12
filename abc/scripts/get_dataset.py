import kagglehub
import shutil
import os

# Download the dataset from Kaggle
path = kagglehub.dataset_download("datafiniti/consumer-reviews-of-amazon-products")

# Check if the file already exists in ../dataset
dataset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dataset")
target_csv = "Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv"
target_csv_path = os.path.join(dataset_dir, target_csv)

if os.path.exists(target_csv_path):
    main_csv = target_csv
    path = dataset_dir  # Set path to dataset directory for consistency
else:
    # Find the main CSV file in the downloaded dataset
    csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
    main_csv = csv_files[0]  # Use the first CSV file found
    # Save the main CSV file to the ./dataset directory
    os.makedirs("dataset", exist_ok=True)
    shutil.copy(os.path.join(path, main_csv), os.path.join("dataset", main_csv))

# Find the first CSV file in the dataset directory
files = [f for f in os.listdir(path) if f.endswith(".csv")]
csv_file = os.path.join(path, files[0])
