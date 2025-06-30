"""
Title: Anomaly Detection in Machine Learning

Definition:
Anomaly detection is the process of finding unusual or rare items in data. Algorithms like Isolation Forest and One-Class SVM help detect outliers.

Problem Statement:
Suppose you want to find fraudulent transactions in bank data. Anomaly detection helps you spot transactions that are very different from normal ones.

Working:
- The algorithm learns what normal data looks like.
- It marks data points that are very different as anomalies (outliers).

Steps:
1. Collect data (like transaction amounts).
2. Train an anomaly detection model on normal data.
3. Use the model to predict if new data is normal or an anomaly.

Example:
Let's use Isolation Forest to detect anomalies in simple data.
"""

from sklearn.ensemble import IsolationForest
import numpy as np

# Example data: mostly normal, one outlier
X = np.array([[10], [12], [11], [13], [100]])

model = IsolationForest(contamination='0.2', random_state=0)
model.fit(X)
predictions = model.predict(X)
print("Predictions (1=normal, -1=anomaly):", predictions)

"""
Explanation:
- The model predicts which data points are normal and which are anomalies.
- Anomaly detection is used in fraud detection, network security, and more.
""" 