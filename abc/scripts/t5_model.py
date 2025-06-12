from collections import Counter
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ✅ Load model and tokenizer directly (no caching)
MODEL_NAME = "t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def build_summary_prompt(text):
    return f"summarize: {text}"


def summarize_with_t5(text: str) -> str:
    """
    Uses a T5 model to generate a summary from input text.
    """
    prompt = build_summary_prompt(text)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(**inputs, max_length=100, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary


# ⬇️ Optional helper/debug functions
def example_prompt(data):
    return build_summary_prompt(data["cleaned_text"].iloc[0])


def get_top_products(data):
    top_products = data["name"].value_counts().head(3).index.tolist()
    top_product_dfs = [data[data["name"] == prod] for prod in top_products]
    for idx, prod in enumerate(top_products):
        print(f"\nProduct {idx+1}: {prod}")
        print(f"Number of reviews: {len(top_product_dfs[idx])}")
        print("Average rating:", top_product_dfs[idx]["reviews.rating"].mean())
        print("Brands:", top_product_dfs[idx]["brand"].unique())
        print("Primary Categories:", top_product_dfs[idx]["primaryCategories"].unique())
        print("Sample review:", top_product_dfs[idx]["cleaned_text"].iloc[0][:200])


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

    if "sentiment" in data.columns:
        negative_reviews = data[data["sentiment"] == "Negative"]["cleaned_text"]
    else:
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

    common_complaints = Counter(complaint_words).most_common(20)
    print("\nMost common complaint words and example reviews:")
    shown = set()
    for word, count in common_complaints[:10]:
        for review in negative_reviews:
            if word in review.split() and (word, review) not in shown:
                print(f"\nWord: {word} (count: {count})")
                print("Example review:", review)
                shown.add((word, review))
                break


def get_worst_products(data):
    worst_products = (
        data.groupby(["primaryCategories", "name"])["reviews.rating"]
        .mean().reset_index()
        .sort_values(["primaryCategories", "reviews.rating"])
        .groupby("primaryCategories")
        .first()
        .reset_index()
    )
    return worst_products
