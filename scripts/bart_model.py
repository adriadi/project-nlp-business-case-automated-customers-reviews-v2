from transformers import BartForConditionalGeneration, BartTokenizer
from collections import Counter
from IPython.display import display

bart_model_name = "facebook/bart-large-cnn"
bart_tokenizer = BartTokenizer.from_pretrained(bart_model_name)
bart_model = BartForConditionalGeneration.from_pretrained(bart_model_name)


def build_bart_summary_prompt(text):
    return f"Summarize this review: {text}"


def get_top_products(data):
    # Get the top 3 most reviewed products in df_filtered
    top_products_bart = data["name"].value_counts().head(3).index.tolist()
    top_product_dfs_bart = [data[data["name"] == prod] for prod in top_products_bart]

    # Show basic info and BART summaries for each top product
    for idx, prod in enumerate(top_products_bart):
        print(f"\nProduct {idx+1}: {prod}")
        print(f"Number of reviews: {len(top_product_dfs_bart[idx])}")
        print("Average rating:", top_product_dfs_bart[idx]["reviews.rating"].mean())
        print("Brands:", top_product_dfs_bart[idx]["brand"].unique())
        print(
            "Primary Categories:",
            top_product_dfs_bart[idx]["primaryCategories"].unique(),
        )
        # Summarize the first review using BART
        text = top_product_dfs_bart[idx]["cleaned_text"].iloc[0]
        inputs = bart_tokenizer(
            [text], max_length=512, truncation=True, return_tensors="pt"
        )
        summary_ids = bart_model.generate(
            inputs["input_ids"], num_beams=4, max_length=60, early_stopping=True
        )
        summary = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("BART summary:", summary)


def compare_differences(data):
    top_products_bart = data["name"].value_counts().head(3).index.tolist()
    top_product_dfs_bart = [data[data["name"] == prod] for prod in top_products_bart]
    print("\nDifferences between top products:")
    for i in range(2):
        for j in range(i + 1, 3):
            print(f"\nProduct {i+1} vs Product {j+1}:")
            brand_diff = set(top_product_dfs_bart[i]["brand"].unique()) ^ set(
                top_product_dfs_bart[j]["brand"].unique()
            )
            cat_diff = set(top_product_dfs_bart[i]["primaryCategories"].unique()) ^ set(
                top_product_dfs_bart[j]["primaryCategories"].unique()
            )
            print("Brand difference:", brand_diff)
            print("Primary category difference:", cat_diff)
            avg_rating_diff = (
                top_product_dfs_bart[i]["reviews.rating"].mean()
                - top_product_dfs_bart[j]["reviews.rating"].mean()
            )
            print("Average rating difference:", avg_rating_diff)


def extract_common_complaints(data):
    try:
        stopwords
    except NameError:
        stopwords = set(
            [
                "the",
                "and",
                "to",
                "a",
                "of",
                "is",
                "it",
                "in",
                "i",
                "this",
                "that",
                "was",
                "for",
                "with",
                "my",
                "on",
                "but",
                "have",
                "so",
                "not",
                "as",
                "are",
                "had",
                "at",
                "be",
                "they",
                "you",
                "we",
                "all",
                "if",
                "just",
                "or",
                "me",
                "very",
                "from",
                "by",
                "an",
                "has",
                "were",
                "would",
                "when",
                "which",
                "one",
                "about",
                "out",
                "up",
                "what",
                "there",
                "their",
                "can",
                "more",
                "will",
                "no",
                "do",
                "he",
                "she",
                "them",
                "too",
                "than",
                "who",
                "after",
                "because",
                "did",
                "been",
                "our",
                "also",
                "could",
            ]
        )

    # Add sentiment column to df_filtered if not present
    if "sentiment" not in data.columns:

        def map_sentiment(rating):
            if rating in [1, 2]:
                return "Negative"
            elif rating == 3:
                return "Neutral"
            elif rating in [4, 5]:
                return "Positive"
            else:
                return None

        data["sentiment"] = data["reviews.rating"].apply(map_sentiment)

    # Get all negative reviews from df_filtered
    negative_reviews_bart = data[data["sentiment"] == "Negative"]["cleaned_text"]

    # Tokenize and count words, excluding stopwords
    complaint_words = []
    for review in negative_reviews_bart:
        complaint_words.extend([w for w in review.split() if w not in stopwords])

    common_complaints_bart = Counter(complaint_words).most_common(20)

    # Use BART to summarize the most common complaint reviews
    print("BART summaries of reviews containing common complaint words:")
    shown_bart = set()
    for word, count in common_complaints_bart[:10]:
        for review in negative_reviews_bart:
            if word in review.split() and (word, review) not in shown_bart:
                inputs = bart_tokenizer(
                    [review], max_length=512, truncation=True, return_tensors="pt"
                )
                summary_ids = bart_model.generate(
                    inputs["input_ids"], num_beams=4, max_length=60, early_stopping=True
                )
                summary = bart_tokenizer.decode(
                    summary_ids[0], skip_special_tokens=True
                )
                print(f"\nWord: {word} (count: {count})")
                print("Original review:", review)
                print("BART summary:", summary)
                shown_bart.add((word, review))
                break


def get_worst_products(data):
    # Group by primaryCategories and product name, calculate mean rating
    worst_products_bart = (
        data.groupby(["primaryCategories", "name"])["reviews.rating"]
        .mean()
        .reset_index()
        .sort_values(["primaryCategories", "reviews.rating"])
        .groupby("primaryCategories")
        .first()
        .reset_index()
    )

    print("Worst product by primary category (BART):")
    display(worst_products_bart[["primaryCategories", "name", "reviews.rating"]])

    # Summarize a negative review for each worst product using BART
    for idx, row in worst_products_bart.iterrows():
        prod_reviews = data[
            (data["primaryCategories"] == row["primaryCategories"])
            & (data["name"] == row["name"])
        ]
        neg_review = prod_reviews[prod_reviews["sentiment"] == "Negative"][
            "cleaned_text"
        ]
        if not neg_review.empty:
            text = neg_review.iloc[0]
            inputs = bart_tokenizer(
                [text], max_length=512, truncation=True, return_tensors="pt"
            )
            summary_ids = bart_model.generate(
                inputs["input_ids"], num_beams=4, max_length=60, early_stopping=True
            )
            summary = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            print(
                f"\nCategory: {row['primaryCategories']}\nProduct: {row['name']}\nBART summary of a negative review:\n{summary}"
            )
