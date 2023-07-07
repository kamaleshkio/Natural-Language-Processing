import nltk
from nltk.stem import WordNetLemmatizer
wordlem = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for i in tokenization:
    print("lemma for {} is {}".format(i, wordlem.lemmatize(i)))