import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_reviews(df, column="reviews.text"):
    df = df.dropna(subset=[column])
    df[column] = df[column].str.lower()
    df[column] = df[column].str.replace(r"[^\w\s]", "", regex=True)
    df[column] = df[column].str.replace(r"\d+", "", regex=True)
    df[column] = df[column].str.strip()

    def clean_text(text):
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stop_words]
        lemmatized = [lemmatizer.lemmatize(word) for word in tokens]
        return " ".join(lemmatized)

    df[column] = df[column].apply(clean_text)
    return df
 