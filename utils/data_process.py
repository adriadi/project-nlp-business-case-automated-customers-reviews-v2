import pandas as pd
from scripts.get_dataset import csv_file
import re

df = pd.read_csv(csv_file)


def tokenize(df):
    df["tokens"] = df["reviews.text"].astype(str).str.split()
    return df


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def filter_data(data):
    df_filtered = data[data["cleaned_text"].str.split().apply(len) > 10]
    return df_filtered


def remove_empty(data):
    df_filtered = data[
        data["cleaned_text"].notnull() & (data["cleaned_text"].str.strip() != "")
    ]
    df_filtered = data[data["cleaned_text"].apply(lambda x: len(set(x.split())) > 2)]
    return df_filtered


def remove_duplicates(data):
    df_filtered = data.drop_duplicates(subset=["cleaned_text"])
    df_filtered = data.reset_index(drop=True)
    return df_filtered
