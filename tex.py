import nltk
text_content = open("E:\samp.txt", "r")
text_string = text_content.read().replace("\n", " ")
text_content.close()
print(text_string)
token = nltk.word_tokenize(text_string)
print(token)