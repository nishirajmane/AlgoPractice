"""
Title: Recommendation Systems (Collaborative Filtering) in Machine Learning

Definition:
A recommendation system suggests items (like movies, products, or songs) to users based on their preferences. Collaborative filtering is a popular method that uses the preferences of many users to make recommendations.

Problem Statement:
Suppose you want to suggest movies to a user based on what similar users liked. Recommendation systems help you do this automatically.

Working:
- The system collects ratings or preferences from many users.
- It finds users who are similar to the target user.
- It recommends items that similar users liked but the target user hasn't seen yet.

Steps:
1. Collect user-item ratings (like a table of users and their movie ratings).
2. Find users who are similar to the target user (using similarity measures).
3. Recommend items liked by similar users.

Example:
Let's use a simple collaborative filtering example with Python.
"""

import numpy as np

# Example user-item rating matrix (rows: users, columns: movies)
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4],
])

# Find the most similar user to user 0 (using dot product)
similarities = ratings @ ratings[0]
most_similar = np.argmax(similarities[1:]) + 1
print("Most similar user to user 0:", most_similar)

# Recommend a movie that similar user liked but user 0 hasn't seen
for movie in range(ratings.shape[1]):
    if ratings[0, movie] == 0 and ratings[most_similar, movie] > 0:
        print(f"Recommend movie {movie} to user 0")

"""
Explanation:
- We used a simple similarity measure to find similar users.
- The system recommends movies liked by similar users.
- Recommendation systems are used by Netflix, Amazon, and YouTube.
""" 