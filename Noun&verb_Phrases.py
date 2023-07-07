import nltk

text = "The quick brown fox jumps over the lazy dog"

tokens = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(tokens)

grammar = r"""
  NP: {<DT|JJ|NN.*>+} # chunk sequences of DT, JJ, NN
  VP: {<VB.*><NP|PP|CLAUSE>+$} # chunk verbs and their arguments
"""
chunk_parser = nltk.RegexpParser(grammar)
chunked_tokens = chunk_parser.parse(pos_tags)

noun_phrases = []
verb_phrases = []
for subtree in chunked_tokens.subtrees():
    if subtree.label() == 'NP':
        noun_phrases.append(" ".join([token[0] for token in subtree.leaves()]))
    elif subtree.label() == 'VP':
        verb_phrases.append(" ".join([token[0] for token in subtree.leaves()]))

print("Noun phrases:", noun_phrases)
print("Verb phrases:", verb_phrases)
