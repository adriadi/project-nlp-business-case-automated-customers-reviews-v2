from sklearn.manifold import TSNE
from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib.pyplot as plt


def visualize_tsne(df_filtered):
    sample_df = (
        df_filtered.sample(n=1000, random_state=42)
        if len(df_filtered) > 1000
        else df_filtered
    )

    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(sample_df["cleaned_text"])

    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    X_embedded = tsne.fit_transform(X.toarray())

    plt.figure(figsize=(10, 7))
    plt.scatter(
        X_embedded[:, 0],
        X_embedded[:, 1],
        c=sample_df["reviews.rating"],
        cmap="viridis",
        alpha=0.6,
    )
    plt.colorbar(label="Review Rating")
    plt.title("t-SNE visualization of Amazon Reviews")
    plt.xlabel("t-SNE 1")
    plt.ylabel("t-SNE 2")
    plt.show()
