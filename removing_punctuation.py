import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords





sentence = "@facebook https://facebook.com/2y1zl - they post there's community Guidelines. so, we have to follow the guide lines."
sentence = re.sub("[^a-zA-Z]+", " " , sentence)
print(sentence)

















# pat1 = r'@[A-Za-z0-9]+'
# pat2 = r'https://[A-Za-Z0-9./]+'
#
# sentences = [pat1, pat2]
# for sentence in sentences:
#     generic_re = re.compile("(%s|%s)" % (pat1, pat2)).findall(sentence)
# def text_clean(text):
#     stripped = re.sub(text)
#     print(stripped)
#
# text = "@facebook https://facebook.com/2y1zl - they post there's community Guidelines. so, we have to follow the guide lines."
#
# print(text_clean(text))