"""
Title: Hierarchical Clustering in Machine Learning

Definition:
Hierarchical Clustering is an unsupervised machine learning algorithm that groups data into clusters by building a hierarchy (tree) of clusters.

Problem Statement:
Suppose you want to group animals based on their similarities. Hierarchical clustering helps you see which animals are most similar by building a tree of clusters.

Working:
- Each data point starts as its own cluster.
- The closest clusters are merged together step by step.
- This process continues until all points are in one big cluster.

Steps:
1. Start with each point as its own cluster.
2. Find the two closest clusters and merge them.
3. Repeat until all points are in one cluster.
4. The result can be shown as a tree (dendrogram).

Example:
Let's group animals based on their features using hierarchical clustering.
"""

from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Example data: [feature1, feature2]
data = np.array([[1, 2], [2, 3], [5, 8], [8, 8]])

model = AgglomerativeClustering(n_clusters=2)
labels = model.fit_predict(data)

print("Cluster labels:", labels)

"""
Explanation:
- We used sklearn to perform hierarchical clustering.
- The model grouped data into 2 clusters based on their features.
- Hierarchical clustering helps visualize how data points are related.
""" 