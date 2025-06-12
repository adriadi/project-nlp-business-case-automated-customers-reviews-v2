import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

def visualize_pca(df_filtered):
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df_filtered["cleaned_text"])

    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X.toarray())

    fig, ax = plt.subplots(figsize=(10, 7))
    scatter = ax.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=df_filtered["reviews.rating"],
        cmap="viridis",
        alpha=0.6,
    )
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label("Review Rating")
    ax.set_title("PCA visualization of Amazon Reviews")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    return fig
