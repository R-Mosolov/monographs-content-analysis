from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize

sent = """Hello Mr. Smith, how are you doing today? Hello The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat Hello cardboard Hello"""
cfdist = ConditionalFreqDist()

for word in word_tokenize(sent):
    condition = len(word)
    cfdist[condition][word] += 1

cfdist = ConditionalFreqDist((len(word), word) for word in word_tokenize(sent))

print(cfdist[5])

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

print(stop_words)
