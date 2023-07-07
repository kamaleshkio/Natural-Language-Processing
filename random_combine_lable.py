import nltk
import random

# Load the names corpus
nltk.download('names')
names = nltk.corpus.names

# Get a list of male names and female names
male_names = names.words('male.txt')
female_names = names.words('female.txt')

# Combine the names and add a label to each name
labeled_names = [(name, 'male') for name in male_names] + [(name, 'female') for name in female_names]

# Shuffle the list of labeled names
random.shuffle(labeled_names)

# Print the first 15 labeled names
for name, gender in labeled_names[:15]:
    print(name, gender)
