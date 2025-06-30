"""
Title: k-Nearest Neighbors (k-NN) in Machine Learning

Definition:
k-Nearest Neighbors (k-NN) is a simple machine learning algorithm used for classification and regression. It predicts the output for a new data point by looking at the 'k' closest data points in the training set.

Problem Statement:
Suppose you want to predict if a fruit is an apple or an orange based on its weight and color. k-NN helps you decide by looking at the most similar fruits in your data.

Working:
- For a new data point, k-NN finds the 'k' nearest neighbors (using distance).
- It checks the labels of these neighbors.
- For classification, it picks the most common label among the neighbors.

Steps:
1. Choose the value of k (e.g., 3).
2. Calculate the distance between the new point and all other points.
3. Pick the k closest points.
4. For classification, choose the most common label among them.

Example:
Let's classify a fruit based on its weight and color using k-NN.
"""

# Example data
from sklearn.neighbors import KNeighborsClassifier

# Features: [weight, color (0=green, 1=orange)]
X = [[150, 0], [170, 1], [140, 0], [130, 1]]
# Labels: 0 = apple, 1 = orange
y = [0, 1, 0, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict for a new fruit: weight=160, color=0 (green)
prediction = model.predict([[160, 0]])
print("Apple" if prediction[0] == 0 else "Orange")

"""
Explanation:
- We used sklearn to create a k-NN model.
- The model predicts if a fruit is an apple or orange based on its features.
- k-NN is simple and works well for small datasets.
""" 