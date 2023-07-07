import nltk
from nltk.corpus import stopwords


text_content = open("E:\samp.txt", "r")
text_string = text_content.read().replace("\n", " ")
text_content.close()
print(text_string)
token = nltk.word_tokenize(text_string)


# Using stopwords from English Languages
english_stops = set(stopwords.words('english'))
print(token)

