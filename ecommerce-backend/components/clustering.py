import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# User's criteria (example)
user_criteria = {
    "price": 1099.0,             # Preference for lower price (normalized)
    "rating": 4.5,            # Preference for highest rating (normalized)
    "review_sentiment": 0.1,  # Preference for positive reviews
    "shipping_time": 1,     # Moderate preference for fast shipping
}


def cluster_distance(centroid, user_vector):
    """Compute Euclidean distance between a cluster centroid and user vector."""
    return np.linalg.norm(centroid - user_vector)


def cluster(products):

    # convert list of dictionaries to pandas dataframe
    df = pd.DataFrame(products)

    # Extract relevant numerical features for clustering
    numerical_features = ['price', 'rating',
                          'review_sentiment', 'shipping_time']
    X = df[numerical_features].values

    # Step 1: Apply K-Means Clustering
    n_clusters = 3  # Number of clusters; can be tuned
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X)

    user_vector = np.array([user_criteria[feature]
                           for feature in numerical_features])

    # Step 2: Calculate the Distance of Each Cluster to User Criteria
    cluster_centroids = kmeans.cluster_centers_
    cluster_distances = {
        cluster_idx: cluster_distance(centroid, user_vector)
        for cluster_idx, centroid in enumerate(cluster_centroids)
    }

    # Identify the most relevant cluster
    relevant_cluster = min(cluster_distances, key=cluster_distances.get)

    # Step 3: Filter Products in the Relevant Cluster
    relevant_products = df[df['cluster'] == relevant_cluster]

    # Display Relevant Products
    print("Relevant Products Based on User Criteria:")
    print(relevant_products[['id', 'price', 'rating',
                             'review_sentiment', 'shipping_time', 'brand']])

    return relevant_products.to_dict(orient='records')
