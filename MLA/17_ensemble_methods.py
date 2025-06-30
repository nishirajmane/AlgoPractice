"""
Title: Ensemble Methods in Machine Learning

Definition:
Ensemble methods combine several machine learning models to make better predictions than any single model alone. Common types are Bagging, Boosting, and Stacking.

Problem Statement:
Suppose you want to predict if a student will pass an exam. Using several models together (ensemble) can give more accurate results than just one model.

Working:
- Bagging: Builds several models independently and combines their results (e.g., Random Forest).
- Boosting: Builds models one after another, each learning from the mistakes of the previous one (e.g., Gradient Boosting).
- Stacking: Combines different types of models and uses another model to make the final prediction.

Steps:
1. Choose several models to combine.
2. Train each model on the data.
3. Combine their predictions (by voting or averaging).
4. For stacking, use another model to learn from the combined predictions.

Example:
Let's use bagging and boosting with sklearn.
"""

from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

# Example data: [hours studied, attendance]
X = [[2, 80], [4, 90], [6, 85], [8, 95]]
y = [0, 0, 1, 1]  # 0 = fail, 1 = pass

# Bagging
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=5, random_state=0)
bagging.fit(X, y)
print("Bagging prediction:", bagging.predict([[5, 88]]))

# Boosting
boosting = GradientBoostingClassifier(n_estimators=5, random_state=0)
boosting.fit(X, y)
print("Boosting prediction:", boosting.predict([[5, 88]]))

"""
Explanation:
- Bagging uses many models in parallel and combines their results.
- Boosting builds models one after another, each learning from the last.
- Ensemble methods are powerful for improving accuracy.
""" 