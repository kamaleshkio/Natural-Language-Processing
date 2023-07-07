import nltk
from collections import Counter
from nltk.corpus import stopwords

text = "This is a sample sentence to demonstrate how to find the most common words in a text while excluding stop words using NLP."
tokens = nltk.word_tokenize(text.lower())

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token not in stop_words]

word_counts = Counter(filtered_tokens)

most_common_words = word_counts.most_common(5)
print(most_common_words)
