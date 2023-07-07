import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

data = "'AI' was Introdused in the year '1956'. but, it gained popularity recently"
sentence = re.sub("[^a-zA-Z0-9]+", " " , data)
print(sentence)
stopword = set(stopwords.words('english'))
words = word_tokenize(sentence)
wordfiltered = []

for i in words :
    if i not in stopword:
        wordfiltered.append(i)

print(wordfiltered)

