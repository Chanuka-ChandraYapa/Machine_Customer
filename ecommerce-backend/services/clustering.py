import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from services.requirements import user_criteria
from sklearn.metrics import silhouette_score  # Ensure silhouette_score is imported



def scale_features(df, numerical_features):
    """Scale the numerical features to normalize the data."""
    available_numerical_features = [feature for feature in numerical_features if feature in df.columns]
    if available_numerical_features:
        scaler = StandardScaler()
        return scaler.fit_transform(df[available_numerical_features])
    return np.empty((df.shape[0], 0))

def cluster_distance(centroid, user_vector):
    """Compute Euclidean distance between a cluster centroid and user vector."""
    return np.linalg.norm(centroid - user_vector)

def find_optimal_clusters(X):
    n_samples = len(X)
    if n_samples < 3:
        raise ValueError("Clustering cannot be performed with less than 3 samples.")

    max_clusters = min(10, n_samples - 1)  # Maximum clusters allowed
    silhouette_scores = []

    for n_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
        labels = kmeans.labels_
        silhouette = silhouette_score(X, labels)
        silhouette_scores.append((n_clusters, silhouette))

    # Select the number of clusters with the highest silhouette score
    best_n_clusters = max(silhouette_scores, key=lambda x: x[1])[0]
    return best_n_clusters

def cluster(products, method='KMeans'):
    """Cluster products based on user criteria."""
    df = pd.DataFrame(products)
    numerical_features = ['price', 'rating', 'review_sentiment', 'shipping_time']

    # Filter features based on user_criteria
    available_features = [feature for feature in numerical_features if feature in user_criteria]
    if not available_features:
        return []

    # Scale the features
    X = scale_features(df, available_features)

    # Select clustering method
    if method == 'KMeans':
        n_clusters = find_optimal_clusters(X)
        model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    elif method == 'DBSCAN':
        model = DBSCAN(eps=0.5, min_samples=5)
    elif method == 'Agglomerative':
        model = AgglomerativeClustering(n_clusters=2)  # Default to 2 clusters
    elif method == 'GMM':
        model = GaussianMixture(n_components=2, random_state=42)
    else:
        raise ValueError("Unsupported clustering method")

    # Fit the model
    if method == 'GMM':
        df['cluster'] = model.fit_predict(X)
    else:
        df['cluster'] = model.fit_predict(X)

    # Calculate distances to user vector
    user_vector = np.array([user_criteria[feature] for feature in available_features])
    if method in ['KMeans', 'GMM']:
        centroids = model.means_ if method == 'GMM' else model.cluster_centers_
        cluster_distances = {i: cluster_distance(centroids[i], user_vector) for i in range(len(centroids))}
    else:
        cluster_distances = {}
        for i in range(max(df['cluster']) + 1):
            cluster_points = X[df['cluster'] == i]
            if len(cluster_points) > 0:
                centroid = np.mean(cluster_points, axis=0)
                cluster_distances[i] = cluster_distance(centroid, user_vector)

    # Find the closest cluster
    relevant_cluster = min(cluster_distances, key=cluster_distances.get)
    relevant_products = df[df['cluster'] == relevant_cluster]

    return relevant_products.to_dict(orient='records')
