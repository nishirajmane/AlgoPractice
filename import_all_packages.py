"""
This file imports all the packages required to run the DSA and MLA codes in the project.
Run this file to ensure all dependencies are available.
"""

def try_import(module, import_statement):
    try:
        exec(import_statement, globals())
        print(f"[OK] {module}")
    except Exception as e:
        print(f"[ERROR] {module}: {e}")

# For numerical operations and arrays
try_import('numpy', 'import numpy as np')

# For machine learning algorithms and utilities
try_import('sklearn', 'import sklearn')
try_import('LogisticRegression', 'from sklearn.linear_model import LogisticRegression')
try_import('KNeighborsClassifier', 'from sklearn.neighbors import KNeighborsClassifier')
try_import('DecisionTreeClassifier', 'from sklearn.tree import DecisionTreeClassifier')
try_import('RandomForestClassifier', 'from sklearn.ensemble import RandomForestClassifier')
try_import('GradientBoostingClassifier', 'from sklearn.ensemble import GradientBoostingClassifier')
try_import('BaggingClassifier', 'from sklearn.ensemble import BaggingClassifier')
try_import('IsolationForest', 'from sklearn.ensemble import IsolationForest')
try_import('MultinomialNB', 'from sklearn.naive_bayes import MultinomialNB')
try_import('KMeans', 'from sklearn.cluster import KMeans')
try_import('AgglomerativeClustering', 'from sklearn.cluster import AgglomerativeClustering')
try_import('DBSCAN', 'from sklearn.cluster import DBSCAN')
try_import('PCA', 'from sklearn.decomposition import PCA')
try_import('SVC', 'from sklearn.svm import SVC')
try_import('OneClassSVM', 'from sklearn.svm import OneClassSVM')
try_import('MLPClassifier', 'from sklearn.neural_network import MLPClassifier')
try_import('CountVectorizer', 'from sklearn.feature_extraction.text import CountVectorizer')

# For deep learning (CNNs)
try_import('tensorflow', 'import tensorflow as tf')
try_import('Sequential', 'from tensorflow.keras.models import Sequential')
try_import('Conv2D', 'from tensorflow.keras.layers import Conv2D')
try_import('MaxPooling2D', 'from tensorflow.keras.layers import MaxPooling2D')
try_import('Flatten', 'from tensorflow.keras.layers import Flatten')
try_import('Dense', 'from tensorflow.keras.layers import Dense')

# For plotting (time series, etc.)
try_import('matplotlib.pyplot', 'import matplotlib.pyplot as plt')

# For heap operations (min-heap)
try_import('heapq', 'import heapq')

# For system operations (used in Dijkstra\'s)
try_import('sys', 'import sys')

print("\nAll required packages for DSA and MLA codes have been checked.")
