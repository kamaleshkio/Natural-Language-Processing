import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

txt = "AI was Introdused in the year 1956 but it gained popularity recently"
s_words = set(stopwords.words('english'))
wordt = word_tokenize(txt)
stopword = []

for i in wordt:
    if i not in s_words:
        stopword.append(i)

print(stopword)

