"""
Title: Decision Trees in Machine Learning

Definition:
A Decision Tree is a machine learning algorithm that uses a tree-like model to make decisions. Each internal node represents a question, each branch represents an answer, and each leaf node represents a result or decision.

Problem Statement:
Suppose you want to decide if you should play outside based on the weather (sunny, rainy, cloudy). A decision tree helps you make this decision by asking simple questions.

Working:
- The tree starts at the root and asks a question.
- Depending on the answer, it moves to the next node or makes a decision.

Steps:
1. Collect data with features and outcomes.
2. Build the tree by splitting data based on questions.
3. Use the tree to make predictions for new data.

Example:
Let's use a decision tree to decide if you should play outside based on weather.
"""

from sklearn.tree import DecisionTreeClassifier

# Example data
# Features: [0=sunny, 1=rainy, 2=cloudy]
weather = [[0], [1], [2], [0], [1]]
play = [1, 0, 1, 1, 0]  # 1 = play, 0 = don't play

model = DecisionTreeClassifier()
model.fit(weather, play)

# Predict for sunny weather
prediction = model.predict([[0]])
print("Play outside" if prediction[0] == 1 else "Don't play outside")

"""
Explanation:
- We used sklearn to create a decision tree model.
- The model predicts if you should play outside based on the weather.
- Decision trees are easy to understand and visualize.
""" 