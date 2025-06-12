from collections import Counter
from IPython.display import display
from transformers import BartForConditionalGeneration, BartTokenizer, pipeline

# ✅ Load model + tokenizer directly
bart_model_name = "sshleifer/distilbart-cnn-12-6"
bart_tokenizer = BartTokenizer.from_pretrained(bart_model_name)
bart_model = BartForConditionalGeneration.from_pretrained(bart_model_name)

# ✅ Load pipeline separately for summary function
bart_summarizer = pipeline("summarization", model=bart_model, tokenizer=bart_tokenizer, framework="pt")


def build_bart_summary_prompt(text):
    return f"Summarize this review: {text}"


def summarize_with_bart(text: str) -> str:
    """
    Takes long review text and returns a short summary using DistilBART.
    """
    result = bart_summarizer(text, max_length=60, min_length=15, do_sample=False)
    return result[0]["summary_text"]


def get_top_products(data):
    top_products = data["name"].value_counts().head(3).index.tolist()
    top_product_dfs = [data[data["name"] == prod] for prod in top_products]

    for idx, prod in enumerate(top_products):
        print(f"\nProduct {idx+1}: {prod}")
        print(f"Number of reviews: {len(top_product_dfs[idx])}")
        print("Average rating:", top_product_dfs[idx]["reviews.rating"].mean())
        print("Brands:", top_product_dfs[idx]["brand"].unique())
        print("Primary Categories:", top_product_dfs[idx]["primaryCategories"].unique())

        text = top_product_dfs[idx]["cleaned_text"].iloc[0]
        summary = summarize_with_bart(text)
        print("BART summary:", summary)


def compare_differences(data):
    top_products = data["name"].value_counts().head(3).index.tolist()
    top_product_dfs = [data[data["name"] == prod] for prod in top_products]

    print("\nDifferences between top products:")
    for i in range(2):
        for j in range(i + 1, 3):
            print(f"\nProduct {i+1} vs Product {j+1}:")
            brand_diff = set(top_product_dfs[i]["brand"].unique()) ^ set(top_product_dfs[j]["brand"].unique())
            cat_diff = set(top_product_dfs[i]["primaryCategories"].unique()) ^ set(top_product_dfs[j]["primaryCategories"].unique())
            print("Brand difference:", brand_diff)
            print("Primary category difference:", cat_diff)
            avg_rating_diff = top_product_dfs[i]["reviews.rating"].mean() - top_product_dfs[j]["reviews.rating"].mean()
            print("Average rating difference:", avg_rating_diff)


def extract_common_complaints(data):
    try:
        stopwords
    except NameError:
        stopwords = set([
            "the", "and", "to", "a", "of", "is", "it", "in", "i", "this", "that", "was", "for", "with",
            "my", "on", "but", "have", "so", "not", "as", "are", "had", "at", "be", "they", "you", "we",
            "all", "if", "just", "or", "me", "very", "from", "by", "an", "has", "were", "would", "when",
            "which", "one", "about", "out", "up", "what", "there", "their", "can", "more", "will", "no",
            "do", "he", "she", "them", "too", "than", "who", "after", "because", "did", "been", "our",
            "also", "could"
        ])

    if "sentiment" not in data.columns:
        def map_sentiment(rating):
            if rating in [1, 2]: return "Negative"
            elif rating == 3: return "Neutral"
            elif rating in [4, 5]: return "Positive"
            else: return None
        data["sentiment"] = data["reviews.rating"].apply(map_sentiment)

    negative_reviews = data[data["sentiment"] == "Negative"]["cleaned_text"]
    complaint_words = []

    for review in negative_reviews:
        complaint_words.extend([w for w in review.split() if w not in stopwords])

    common = Counter(complaint_words).most_common(20)

    print("BART summaries of reviews containing common complaint words:")
    shown = set()
    for word, count in common[:10]:
        for review in negative_reviews:
            if word in review.split() and (word, review) not in shown:
                summary = summarize_with_bart(review)
                print(f"\nWord: {word} (count: {count})")
                print("Original review:", review)
                print("BART summary:", summary)
                shown.add((word, review))
                break


def get_worst_products(data):
    worst = (
        data.groupby(["primaryCategories", "name"])["reviews.rating"]
        .mean().reset_index()
        .sort_values(["primaryCategories", "reviews.rating"])
        .groupby("primaryCategories")
        .first()
        .reset_index()
    )

    print("Worst product by primary category (BART):")
    display(worst[["primaryCategories", "name", "reviews.rating"]])

    for _, row in worst.iterrows():
        prod_reviews = data[
            (data["primaryCategories"] == row["primaryCategories"]) &
            (data["name"] == row["name"])
        ]
        neg_review = prod_reviews[prod_reviews["sentiment"] == "Negative"]["cleaned_text"]
        if not neg_review.empty:
            summary = summarize_with_bart(neg_review.iloc[0])
            print(f"\nCategory: {row['primaryCategories']}")
            print(f"Product: {row['name']}")
            print("BART summary of a negative review:", summary)
