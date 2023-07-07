import textblob
from textblob import TextBlob
x = "thankss forr comming, vissit agin"

def spellcor(x):
    splc = TextBlob(x).correct()
    print(splc)

spellcor(x)