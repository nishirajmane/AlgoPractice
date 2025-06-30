"""
Title: Convolutional Neural Networks (CNN) Basics in Machine Learning

Definition:
A Convolutional Neural Network (CNN) is a type of deep learning model especially good at processing images. It uses special layers to find patterns like edges, shapes, and objects in pictures.

Problem Statement:
Suppose you want to build a computer program that can recognize handwritten digits from images. CNNs help you do this by learning patterns in the images.

Working:
- The network has convolutional layers that scan the image for patterns.
- Pooling layers reduce the size of the data while keeping important information.
- Fully connected layers make the final prediction.

Steps:
1. Prepare image data (like 28x28 pixel images of digits).
2. Build a CNN with convolutional, pooling, and fully connected layers.
3. Train the network on labeled images.
4. Use the trained network to predict new images.

Example:
Let's build a simple CNN using Keras (no real training, just structure).
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(10, activation='softmax')
])

model.summary()

"""
Explanation:
- The CNN has a convolutional layer, pooling layer, and dense layer.
- It can learn to recognize patterns in images.
- CNNs are used in image recognition, self-driving cars, and more.
""" 