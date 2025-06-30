"""
Title: Hash Tables in Data Structures

Definition:
A hash table is a data structure that stores key-value pairs. It uses a hash function to compute an index into an array of buckets, from which the desired value can be found very quickly.

Problem Statement:
Suppose you want to store and quickly look up student names by their roll numbers. A hash table helps you do this efficiently.

Working:
- The key (like roll number) is passed through a hash function to get an index.
- The value (like student name) is stored at that index.
- If two keys hash to the same index (collision), use a list at that index (chaining).

Steps:
1. Choose a hash function.
2. Store key-value pairs using the hash function to find the index.
3. Handle collisions using chaining.

Example:
Let's store and look up student names by roll number using a simple hash table.
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_func(self, key):
        return key % self.size
    def insert(self, key, value):
        idx = self.hash_func(key)
        self.table[idx].append((key, value))
    def search(self, key):
        idx = self.hash_func(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

ht = HashTable(10)
ht.insert(101, "Alice")
ht.insert(102, "Bob")
ht.insert(111, "Charlie")
print("Student with roll 102:", ht.search(102))

"""
Explanation:
- We used a simple hash function (key % size).
- Collisions are handled by storing a list at each index.
- Hash tables are used for fast lookups in dictionaries, databases, and more.
""" 