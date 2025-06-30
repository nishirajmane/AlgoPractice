"""
Title: Support Vector Machine (SVM) in Machine Learning

Definition:
Support Vector Machine (SVM) is a machine learning algorithm used for classification. It finds the best line (or hyperplane) that separates data into different classes.

Problem Statement:
Suppose you want to classify animals as cats or dogs based on their features (like weight and height). SVM helps you find the best boundary to separate them.

Working:
- SVM finds the line (in 2D) or plane (in higher dimensions) that best separates the classes.
- The points closest to the line are called support vectors.

Steps:
1. Collect data with features and labels.
2. Train the SVM model to find the best boundary.
3. Use the model to classify new data points.

Example:
Let's classify animals as cats or dogs using SVM.
"""

from sklearn import svm

# Example data
# Features: [weight, height]
X = [[5, 30], [6, 35], [7, 40], [8, 45]]
# Labels: 0 = cat, 1 = dog
y = [0, 0, 1, 1]

model = svm.SVC()
model.fit(X, y)

# Predict for a new animal: weight=6, height=38
prediction = model.predict([[6, 38]])
print("Cat" if prediction[0] == 0 else "Dog")

"""
Explanation:
- We used sklearn to create an SVM model.
- The model predicts if an animal is a cat or dog based on features.
- SVM is powerful for classification problems with clear boundaries.
""" 