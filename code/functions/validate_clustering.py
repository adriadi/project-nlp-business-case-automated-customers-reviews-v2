from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score,
)
from sklearn.feature_extraction.text import TfidfVectorizer


def validate_clustering(data):
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(data["cleaned_text"].astype(str))

    scores = []
    for n_clusters in range(2, 11):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        sil_score = silhouette_score(X, labels)
        ch_score = calinski_harabasz_score(X.toarray(), labels)
        db_score = davies_bouldin_score(X.toarray(), labels)
        scores.append(
            {
                "n_clusters": n_clusters,
                "silhouette": sil_score,
                "calinski_harabasz": ch_score,
                "davies_bouldin": db_score,
            }
        )

    return scores
