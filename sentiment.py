import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
text = "I love this movie! The acting was great and the plot was really interesting."
scores = analyzer.polarity_scores(text)
print("Negative score:", scores['neg'])
print("Neutral score:", scores['neu'])
print("Positive score:", scores['pos'])
print("Compound score:", scores['compound'])
