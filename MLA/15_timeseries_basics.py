"""
Title: Time Series Basics in Machine Learning

Definition:
A time series is a sequence of data points collected or recorded at regular time intervals. Time series analysis helps us understand patterns over time.

Problem Statement:
Suppose you want to predict the temperature for the next day based on past temperatures. Time series analysis helps you do this by looking at trends and patterns.

Working:
- Data is collected over time (like daily temperature).
- We can plot the data to see trends, seasonality, and patterns.
- Models can be used to predict future values.

Steps:
1. Collect data over time.
2. Plot the data to see patterns.
3. Use a simple model to predict the next value.

Example:
Let's plot and predict a simple time series using Python.
"""

import matplotlib.pyplot as plt
import numpy as np

# Example data: temperatures over 7 days
temps = np.array([30, 32, 31, 29, 28, 27, 26])
days = np.arange(1, 8)

plt.plot(days, temps, marker='o')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Temperature Over a Week')
plt.show()

# Simple prediction: next day's temp is same as last day's temp
print("Predicted temperature for next day:", temps[-1])

"""
Explanation:
- We plotted temperatures over a week.
- The last value is used as a simple prediction for the next day.
- Time series analysis is used in weather forecasting, stock prices, and more.
""" 