import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required data once
nltk.download('punkt_tab')
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
    Cleans a single text string:
    - Lowercase, remove punctuation/numbers
    - Tokenize, remove stopwords, lemmatize
    """
    import re

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(lemmatized)

def preprocess_reviews(df, column="reviews.text"):
    """
    Cleans a column of reviews in a DataFrame using clean_text().
    """
    df = df.dropna(subset=[column])
    df[column] = df[column].apply(clean_text)
    return df
