"""
Title: Gradient Boosting in Machine Learning

Definition:
Gradient Boosting is a machine learning technique that builds a strong model by combining many weak models (usually decision trees) in a step-by-step way.

Problem Statement:
Suppose you want to predict house prices based on many features. Gradient boosting helps you make accurate predictions by improving the model step by step.

Working:
- The algorithm starts with a simple model.
- It looks at the errors (mistakes) made by the model.
- It builds a new model to correct those errors.
- This process repeats, and all models are combined for the final prediction.

Steps:
1. Start with a simple model.
2. Find the errors made by the model.
3. Build a new model to fix the errors.
4. Add the new model to the previous ones.
 
"""

from sklearn.ensemble import GradientBoostingClassifier

# Example usage:
model = GradientBoostingClassifier(n_estimators=10, random_state=0)
model.fit(X, y)

# Predict for a new student: 5 hours, 88% attendance
prediction = model.predict([[5, 88]])
print("Pass" if prediction[0] == 1 else "Fail")

"""
Explanation:
- We used sklearn to create a gradient boosting model.
- The model predicts if a student will pass based on hours studied and attendance.
- Gradient boosting is powerful for making accurate predictions.
"""
 