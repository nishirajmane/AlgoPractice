 """
Title: Trie (Prefix Tree) in Data Structures

Definition:
A trie is a tree-like data structure used to store a dynamic set of strings, where keys are usually strings. It is very efficient for searching words by their prefixes.

Problem Statement:
Suppose you want to quickly check if a word or prefix exists in a dictionary. A trie helps you do this efficiently.

Working:
- Each node represents a character of a word.
- Words are stored by linking characters from the root to the end of the word.
- Each node can have multiple children (one for each possible character).

Steps:
1. Start from the root node.
2. For each character in the word, move to the child node (create if not exists).
3. Mark the end of the word.

Example:
Let’s insert and search for words in a trie.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

trie = Trie()
trie.insert("cat")
trie.insert("car")
print("Is 'cat' in trie?", trie.search("cat"))
print("Is 'can' in trie?", trie.search("can"))

"""
Explanation:
- Each node represents a character.
- Words are inserted character by character.
- Trie is used in autocomplete, spell checkers, and IP routing.
"""