import re
import string
from nltk.corpus import stopwords
stoplist = stopwords.words('english')

from collections import defaultdict
from operator import itemgetter

def toptenwords(mycorpus):
    words = mycorpus.words()
    no_capitals = set([word.lower() for word in words])
    filtered = [word for word in no_capitals if word not in stoplist]
    no_punct = [s.translate(None, string.punctuation) for s in filtered]
    wordcounter = {}
    for word in no_punct:
        if word in wordcounter:
            wordcounter[word] += 1
        else:
            wordcounter[word] = 1
    sorting = sorted(wordcounter.iteritems(), key = itemgetter, reverse = True)
    return sorting

txt = "hey there how are you hey hey hey"
result = toptenwords(txt)
print(result)