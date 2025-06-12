import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer


def visualize_pca(df_filtered):
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df_filtered["cleaned_text"])

    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X.toarray())

    plt.figure(figsize=(10, 7))
    plt.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=df_filtered["reviews.rating"],
        cmap="viridis",
        alpha=0.6,
    )
    plt.colorbar(label="Review Rating")
    plt.title("PCA visualization of Amazon Reviews")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.show()
