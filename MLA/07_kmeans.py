"""
Title: K-Means Clustering in Machine Learning

Definition:
K-Means is an unsupervised machine learning algorithm used to group data into clusters based on similarity.

Problem Statement:
Suppose you want to group students into study groups based on their marks. K-Means helps you find groups (clusters) of students with similar marks.

Working:
- The algorithm picks 'k' cluster centers (means) randomly.
- Each data point is assigned to the nearest cluster center.
- The cluster centers are updated based on the points assigned to them.
- This process repeats until the clusters do not change.

Steps:
1. Choose the number of clusters (k).
2. Assign each point to the nearest cluster center.
3. Update the cluster centers.
4. Repeat until clusters are stable.

Example:
Let's group students based on their marks using K-Means.
"""

from sklearn.cluster import KMeans
import numpy as np

# Example data: marks of students
marks = np.array([[55], [60], [65], [70], [90], [95]])

model = KMeans(n_clusters=2, random_state=0)
model.fit(marks)

# Print cluster labels for each student
print("Cluster labels:", model.labels_)

"""
Explanation:
- We used sklearn to create a K-Means model.
- The model grouped students into 2 clusters based on their marks.
- K-Means is useful for finding groups in data without labels.
""" 