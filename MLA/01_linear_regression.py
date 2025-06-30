"""
Title: Linear Regression in Machine Learning

Definition:
Linear Regression is a simple machine learning algorithm that tries to find the relationship between two variables by fitting a straight line (called a regression line) through the data points.

Problem Statement:
Suppose you want to predict a student's marks based on the number of hours they studied. Linear regression helps you find the best line that predicts marks from hours studied.

Working:
- The algorithm finds the best-fit line through the data points.
- The line is represented by the equation: y = mx + c
  where y is the predicted value, x is the input, m is the slope, and c is the intercept.

Steps:
1. Collect data (e.g., hours studied and marks obtained).
2. Plot the data points.
3. Find the best-fit line.
4. Use the line to make predictions.

Example:
Let's predict marks based on hours studied using a simple example.
"""

# Example data
hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 75]

# Simple calculation for best-fit line (using numpy for simplicity)
import numpy as np

# Calculate the slope (m) and intercept (c)
m, c = np.polyfit(hours, marks, 1)

# Predict marks for 6 hours of study
predicted_marks = m * 6 + c
print(f"Predicted marks for 6 hours of study: {predicted_marks:.2f}")

"""
Explanation:
- We used numpy to find the best-fit line.
- The model predicts marks for any given hours of study.
- Linear regression is used in many real-life situations to predict outcomes.
""" 