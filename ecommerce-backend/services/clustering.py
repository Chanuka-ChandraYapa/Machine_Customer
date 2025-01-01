import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from services.requirements import user_criteria

def scale_features(df, numerical_features):
    """Scale the numerical features to normalize the data."""
    scaler = StandardScaler()
    return scaler.fit_transform(df[numerical_features].values)

def cluster_distance(centroid, user_vector):
    """Compute Euclidean distance between a cluster centroid and user vector."""
    return np.linalg.norm(centroid - user_vector)

def find_optimal_clusters(X):
    """Find the optimal number of clusters using silhouette score."""
    best_score = -1
    best_n_clusters = 2
    for n_clusters in range(2, min(11, len(X))):  # Ensure n_clusters doesn't exceed the number of samples
        model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        model.fit(X)
        score = silhouette_score(X, model.labels_)
        if score > best_score:
            best_score = score
            best_n_clusters = n_clusters
    return best_n_clusters

def cluster(products, method='KMeans'):
    # Convert list of dictionaries to pandas DataFrame
    df = pd.DataFrame(products)

    # Extract relevant numerical features for clustering
    numerical_features = ['price', 'rating', 'review_sentiment', 'shipping_time']
    X = scale_features(df, numerical_features)

    # Step 1: Determine the optimal number of clusters
    if method == 'KMeans':
        n_clusters = find_optimal_clusters(X)
    elif method == 'DBSCAN':
        model = DBSCAN(eps=0.5, min_samples=5)
        labels = model.fit_predict(X)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    elif method == 'Agglomerative':
        model = AgglomerativeClustering()
        model.fit(X)
        n_clusters = len(set(model.labels_))
    elif method == 'GMM':
        model = GaussianMixture()
        model.fit(X)
        n_clusters = model.n_components
    else:
        raise ValueError("Unsupported clustering method")

    # Step 2: Apply the selected clustering algorithm
    if method == 'KMeans':
        model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    elif method == 'Agglomerative':
        model = AgglomerativeClustering(n_clusters=n_clusters)
    elif method == 'DBSCAN':
        model = DBSCAN(eps=0.5, min_samples=5)
    elif method == 'GMM':
        model = GaussianMixture(n_components=n_clusters, random_state=42)
    else:
        raise ValueError("Unsupported clustering method")

    # Fit the model
    if method == 'GMM':
        df['cluster'] = model.predict(X)
    else:
        df['cluster'] = model.fit_predict(X)

    user_vector = np.array([user_criteria[feature] for feature in numerical_features])

    # Step 3: Calculate the Distance of Each Cluster to User Criteria
    cluster_centroids = None
    if method == 'KMeans' or method == 'GMM':
        cluster_centroids = model.means_ if method == 'GMM' else model.cluster_centers_
        cluster_distances = {
            cluster_idx: cluster_distance(centroid, user_vector)
            for cluster_idx, centroid in enumerate(cluster_centroids)
        }
    else:
        # For Agglomerative and DBSCAN, use the cluster labels directly for distance computation
        cluster_distances = {}
        for cluster_idx in range(n_clusters):
            cluster_points = X[df['cluster'] == cluster_idx]
            centroid = np.mean(cluster_points, axis=0)
            cluster_distances[cluster_idx] = cluster_distance(centroid, user_vector)

    # Identify the most relevant cluster
    relevant_cluster = min(cluster_distances, key=cluster_distances.get)

    # Step 4: Filter Products in the Relevant Cluster
    relevant_products = df[df['cluster'] == relevant_cluster]

    # Return Relevant Products
    return relevant_products.to_dict(orient='records')
