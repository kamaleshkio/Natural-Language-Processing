import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

sentence = "The quick brown foxes jumped over the lazy dogs"

tokens = nltk.word_tokenize(sentence)

pos_tags = nltk.pos_tag(tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for token, tag in pos_tags:
    if tag.startswith('NN'):
        pos = wordnet.NOUN
    elif tag.startswith('VB'):
        pos = wordnet.VERB
    elif tag.startswith('JJ'):
        pos = wordnet.ADJ
    elif tag.startswith('R'):
        pos = wordnet.ADV
    else:
        pos = wordnet.NOUN
    lemmatized_tokens.append(lemmatizer.lemmatize(token, pos))

print(lemmatized_tokens)
