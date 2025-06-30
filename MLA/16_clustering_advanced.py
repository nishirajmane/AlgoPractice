"""
Title: Advanced Clustering (DBSCAN, Agglomerative) in Machine Learning

Definition:
Advanced clustering algorithms like DBSCAN and Agglomerative Clustering help group data points that are close together, even if the clusters are not regular shapes.

Problem Statement:
Suppose you want to group customers based on their shopping habits, but the groups are not clearly separated. Advanced clustering helps you find these groups.

Working:
- DBSCAN groups points that are close together and marks points that are far away as outliers.
- Agglomerative clustering builds clusters step by step by merging the closest points or groups.

Steps for DBSCAN:
1. Choose a distance threshold and minimum points for a cluster.
2. Group points that are close together.
3. Mark points that don't fit as outliers.

Steps for Agglomerative:
1. Start with each point as its own cluster.
2. Merge the closest clusters step by step.
3. Stop when the desired number of clusters is reached.

Example:
Let's use DBSCAN and Agglomerative Clustering on simple data.
"""

from sklearn.cluster import DBSCAN, AgglomerativeClustering
import numpy as np

# Example data
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])

# DBSCAN
dbscan = DBSCAN(eps=3, min_samples=2)
db_labels = dbscan.fit_predict(X)
print("DBSCAN labels:", db_labels)

# Agglomerative Clustering
agg = AgglomerativeClustering(n_clusters=2)
agg_labels = agg.fit_predict(X)
print("Agglomerative labels:", agg_labels)

"""
Explanation:
- DBSCAN finds clusters based on distance and marks outliers.
- Agglomerative clustering merges points into clusters step by step.
- These methods are useful for finding groups in complex data.
""" 