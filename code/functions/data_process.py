import pandas as pd
from get_dataset import csv_file

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)
df.head()
