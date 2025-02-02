import numpy as np
from sklearn.cluster import KMeans

def train_kmeans(X, num_clusters=5):
    """Trains a K-Means model and returns the model and cluster labels."""
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    return kmeans, labels

def get_top_terms(kmeans, vectorizer, n_terms=2):  # Change n_terms to 2
    """Gets the top terms and their importance scores for each cluster."""
    terms = vectorizer.get_feature_names_out()
    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]

    top_terms = {}
    for cluster in range(kmeans.n_clusters):
        words = []
        for ind in order_centroids[cluster, :n_terms * 3]:  # Fetch more initially, then limit
            word = terms[ind]
            score = kmeans.cluster_centers_[cluster, ind]
            if word not in ["book", "description", "page", "chapter"]:  # Exclude common words
                words.append((word, score))
            if len(words) == n_terms:  # Stop when we have 2 words
                break
        top_terms[cluster] = words

    return top_terms