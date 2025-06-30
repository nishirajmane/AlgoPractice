 """
Title: A* (A-star) Search Algorithm in Data Structures

Definition:
A* is a pathfinding algorithm used to find the shortest path from a start node to a goal node in a graph. It uses both the actual cost to reach a node and an estimated cost (heuristic) to the goal.

Problem Statement:
Suppose you want to find the shortest route from your home to a destination on a map. A* helps you find the best path efficiently using a heuristic (like straight-line distance).

Working:
- A* keeps track of the cost to reach each node and an estimate of the cost to reach the goal.
- It always explores the node with the lowest total estimated cost.

Steps:
1. Add the start node to an open set.
2. While the open set is not empty:
   a. Pick the node with the lowest estimated total cost.
   b. If it's the goal, stop.
   c. Otherwise, update costs for its neighbors and add them to the open set.

Example:
Let’s find the shortest path in a simple grid using A*.
"""

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(start, goal, neighbors):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return []

def grid_neighbors(pos):
    x, y = pos
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            yield (nx, ny)

start = (0, 0)
goal = (2, 2)
path = a_star(start, goal, grid_neighbors)
print("Path from", start, "to", goal, ":", path)

"""
Explanation:
- A* uses both the cost so far and an estimate to the goal.
- It finds the shortest path efficiently using a heuristic.
- A* is used in maps, games, and robotics.
"""