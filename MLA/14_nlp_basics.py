"""
Title: Natural Language Processing (NLP) Basics in Machine Learning

Definition:
Natural Language Processing (NLP) is a field of machine learning that helps computers understand and work with human language (like English, Hindi, etc.).

Problem Statement:
Suppose you want to make a computer program that can understand and reply to messages in English. NLP helps you do this by teaching computers to process language.

Working:
- NLP breaks down sentences into words and understands their meaning.
- It can be used for translation, chatbots, and more.

Steps:
1. Collect text data (like sentences).
2. Break the text into words (tokenization).
3. Remove common words (stopwords) and convert words to their base form (stemming/lemmatization).
4. Use the processed text for tasks like translation or sentiment analysis.

Example:
Let's process a simple sentence using basic NLP steps.
"""

from sklearn.feature_extraction.text import CountVectorizer

sentences = ["I love apples", "You love oranges"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

print("Word counts:")
print(X.toarray())
print("Vocabulary:", vectorizer.vocabulary_)

"""
Explanation:
- We used sklearn to count the words in two sentences.
- The model shows how many times each word appears.
- NLP is used in chatbots, translation, and more.
""" 