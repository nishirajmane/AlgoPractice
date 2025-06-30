 """
Title: Recurrent Neural Networks (RNN) Basics in Machine Learning

Definition:
A Recurrent Neural Network (RNN) is a type of deep learning model that is good at processing sequences, like sentences or time series. It remembers information from previous steps to help make predictions.

Problem Statement:
Suppose you want to predict the next word in a sentence. RNNs help you do this by remembering the words that came before.

Working:
- The network processes one element of the sequence at a time.
- It keeps a hidden state that remembers information from previous steps.
- The output at each step depends on the current input and the hidden state.

Steps:
1. Prepare sequence data (like a list of numbers or words).
2. Build an RNN that processes the sequence step by step.
3. Use the RNN to make predictions for the next element in the sequence.

Example:
Let’s build a simple RNN in Python to process a sequence of numbers.
"""

import numpy as np

# Example sequence: [1, 2, 3, 4]
sequence = [1, 2, 3, 4]

# Simple RNN cell
hidden_state = 0
for x in sequence:
    hidden_state = np.tanh(x + hidden_state)
    print(f"Input: {x}, Hidden state: {hidden_state:.2f}")

"""
Explanation:
- The RNN processes each number in the sequence and updates its hidden state.
- The hidden state remembers information from previous steps.
- RNNs are used for text, speech, and time series data.
"""