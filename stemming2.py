import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for i in tokenization:
    print("stemming  for {} is {}".format(i,porter_stemmer.stem(i)))