import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re

# You only need to run these once — can comment out after first successful run
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')

# Init
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def full_preprocess_reviews(df, column="reviews.text"):
    # Drop rows with empty reviews
    df = df.dropna(subset=[column])

    # Remove duplicates
    df = df.drop_duplicates(subset=[column])

    # 3. Clean text
    df[column] = df[column].str.lower()
    df[column] = df[column].str.replace(r"[^\w\s]", "", regex=True)
    df[column] = df[column].str.replace(r"\d+", "", regex=True)
    df[column] = df[column].str.strip()

    # Tokenize, remove stopwords, lemmatize
    def clean_text(text):
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stop_words]
        lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
        return " ".join(lemmatized)

    df[column] = df[column].apply(clean_text)

    return df.reset_index(drop=True)
