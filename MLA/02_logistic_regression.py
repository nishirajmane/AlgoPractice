"""
Title: Logistic Regression in Machine Learning

Definition:
Logistic Regression is a machine learning algorithm used for classification problems. It predicts the probability that an input belongs to a certain class (like yes/no, true/false).

Problem Statement:
Suppose you want to predict if a student will pass (yes) or fail (no) an exam based on the number of hours they studied. Logistic regression helps you make this prediction.

Working:
- The algorithm uses a special function called the sigmoid function to predict probabilities between 0 and 1.
- If the probability is greater than 0.5, we predict "yes"; otherwise, we predict "no".

Steps:
1. Collect data (e.g., hours studied and pass/fail result).
2. Fit the logistic regression model to the data.
3. Use the model to predict the outcome for new data.

Example:
Let's predict if a student will pass based on hours studied using a simple example.
"""

# Example data
hours = [1, 2, 3, 4, 5]
passed = [0, 0, 0, 1, 1]  # 0 = fail, 1 = pass

# Simple logistic regression using sklearn
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array(hours).reshape(-1, 1)
y = np.array(passed)

model = LogisticRegression()
model.fit(X, y)

# Predict for 3 hours of study
prediction = model.predict([[3]])
print("Pass" if prediction[0] == 1 else "Fail")

"""
Explanation:
- We used sklearn to fit a logistic regression model.
- The model predicts if a student will pass or fail based on hours studied.
- Logistic regression is used for problems where the answer is yes/no or true/false.
""" 