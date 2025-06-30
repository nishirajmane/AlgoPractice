"""
Title: Neural Networks in Machine Learning

Definition:
A neural network is a machine learning model inspired by the human brain. It consists of layers of connected nodes (neurons) that can learn complex patterns in data.

Problem Statement:
Suppose you want to recognize handwritten digits from images. Neural networks help you do this by learning from many examples.

Working:
- The network has an input layer, hidden layers, and an output layer.
- Each neuron receives inputs, processes them, and passes the result to the next layer.
- The network learns by adjusting the connections (weights) based on errors.

Steps:
1. Prepare the data (inputs and outputs).
2. Build the neural network with layers.
3. Train the network on data.
4. Use the trained network to make predictions.

Example:
Let's use a simple neural network to classify points as above or below a line.
"""

from sklearn.neural_network import MLPClassifier

# Example data: [x, y] points
X = [[1, 2], [2, 3], [3, 1], [4, 5]]
y = [0, 0, 1, 1]  # 0 = below line, 1 = above line

model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=0)
model.fit(X, y)

# Predict for a new point: (3, 4)
prediction = model.predict([[3, 4]])
print("Above line" if prediction[0] == 1 else "Below line")

"""
Explanation:
- We used sklearn to create a simple neural network.
- The model predicts if a point is above or below a line.
- Neural networks are powerful for learning complex patterns in data.
""" 