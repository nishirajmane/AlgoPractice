"""
Title: Naive Bayes in Machine Learning

Definition:
Naive Bayes is a simple and fast machine learning algorithm used for classification. It is based on Bayes' Theorem and assumes that all features are independent of each other.

Problem Statement:
Suppose you want to classify emails as 'spam' or 'not spam' based on the words they contain. Naive Bayes helps you make this decision.

Working:
- The algorithm calculates the probability of each class (e.g., spam or not spam) given the input features.
- It picks the class with the highest probability.

Steps:
1. Collect data with features and labels.
2. Calculate the probability of each class.
3. For a new input, calculate the probability for each class.
4. Choose the class with the highest probability.

Example:
Let's classify emails as spam or not spam using Naive Bayes.
"""

from sklearn.naive_bayes import MultinomialNB

# Example data
# Features: [number of spam words, number of normal words]
X = [[3, 1], [1, 4], [2, 2], [4, 0]]
# Labels: 1 = spam, 0 = not spam
y = [1, 0, 0, 1]

model = MultinomialNB()
model.fit(X, y)

# Predict for a new email: 2 spam words, 1 normal word
prediction = model.predict([[2, 1]])
print("Spam" if prediction[0] == 1 else "Not Spam")

"""
Explanation:
- We used sklearn to create a Naive Bayes model.
- The model predicts if an email is spam or not based on word counts.
- Naive Bayes is simple and works well for text classification.
""" 