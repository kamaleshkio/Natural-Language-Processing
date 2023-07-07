from nltk.corpus import wordnet

word = 'happy'

synonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

synonyms = set(synonyms)
print("Synonyms of", word, ":", synonyms)

antonyms = []
for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

antonyms = set(antonyms)
print("Antonyms of", word, ":", antonyms)
