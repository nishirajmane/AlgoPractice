"""
Title: Reinforcement Learning in Machine Learning

Definition:
Reinforcement Learning is a type of machine learning where an agent learns to make decisions by trying actions and receiving rewards or penalties.

Problem Statement:
Suppose you want to teach a robot to play a game. Reinforcement learning helps the robot learn the best moves by rewarding good actions and punishing bad ones.

Working:
- The agent takes an action in an environment.
- The environment gives a reward or penalty.
- The agent learns to choose actions that get the most reward over time.

Steps:
1. Define the environment and possible actions.
2. The agent tries different actions.
3. The agent receives rewards or penalties.
4. The agent learns the best actions to maximize rewards.

Example:
Let's show a simple example of reinforcement learning using a game.
"""

# This is a conceptual example (not using a library)

score = 0
for step in range(5):
    action = 'jump' if step % 2 == 0 else 'duck'
    if action == 'jump':
        score += 10  # reward for jumping
    else:
        score -= 5   # penalty for ducking
    print(f"Step {step+1}: Action = {action}, Score = {score}")

"""
Explanation:
- The agent chooses actions (jump or duck).
- It gets rewards or penalties based on the action.
- Over time, the agent learns which actions give the best score.
- Reinforcement learning is used in robotics, games, and self-driving cars.
""" 