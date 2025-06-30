"""
Title: Random Forest in Machine Learning

Definition:
Random Forest is a machine learning algorithm that uses many decision trees to make better predictions. It is called an ensemble method because it combines the results of multiple trees.

Problem Statement:
Suppose you want to predict if a patient has a disease based on several test results. Random Forest helps you make accurate predictions by using many decision trees.

Working:
- The algorithm creates many decision trees using different parts of the data.
- Each tree makes a prediction.
- The final prediction is the one that most trees agree on (majority vote).

Steps:
1. Collect data with features and labels.
2. Build many decision trees on random parts of the data.
3. Each tree makes a prediction.
4. The final result is the most common prediction.

Example:
Let's use Random Forest to predict if a patient is sick based on test results.
"""

from sklearn.ensemble import RandomForestClassifier

# Example data: [test1, test2]
X = [[1, 2], [2, 3], [3, 1], [4, 5]]
y = [0, 0, 1, 1]  # 0 = healthy, 1 = sick

model = RandomForestClassifier(n_estimators=10, random_state=0)
model.fit(X, y)

# Predict for a new patient: test1=2, test2=2
prediction = model.predict([[2, 2]])
print("Sick" if prediction[0] == 1 else "Healthy")

"""
Explanation:
- We used sklearn to create a Random Forest model.
- The model predicts if a patient is sick or healthy based on test results.
- Random Forest is powerful and works well for many types of data.
""" 