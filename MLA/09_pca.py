"""
Title: Principal Component Analysis (PCA) in Machine Learning

Definition:
Principal Component Analysis (PCA) is a technique used to reduce the number of features (dimensions) in data while keeping the most important information.

Problem Statement:
Suppose you have a dataset with many features (like height, weight, age, marks, etc.) and want to make it simpler for analysis. PCA helps you reduce the number of features.

Working:
- PCA finds new features (called principal components) that capture the most information (variance) in the data.
- The data is transformed into these new features, which are fewer than the original ones.

Steps:
1. Standardize the data (make all features have similar scale).
2. Find the principal components.
3. Transform the data into the new components.
4. Use the reduced data for analysis or machine learning.

Example:
Let's reduce a dataset with 2 features to 1 feature using PCA.
"""

from sklearn.decomposition import PCA
import numpy as np

# Example data: [height, weight]
data = np.array([[150, 50], [160, 60], [170, 65], [180, 80]])

pca = PCA(n_components=1)
reduced_data = pca.fit_transform(data)

print("Reduced data:", reduced_data)

"""
Explanation:
- We used sklearn to perform PCA.
- The data was reduced from 2 features (height, weight) to 1 feature.
- PCA helps make data simpler and easier to analyze.
""" 