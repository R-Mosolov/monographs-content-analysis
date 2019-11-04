import nltk


# Adding text

from nltk.tokenize import sent_tokenize
text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome. 
The sky is pinkish-blue. You shouldn't eat cardboard."""
tokenized_text = sent_tokenize(text)
print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(text)
print(tokenized_word)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)

fdist.most_common(5)


# Deleting punctuation signs

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
text_without_punctuation_signs = tokenizer.tokenize(text)
print("Text without punctuation signs:", tokenizer.tokenize(text))


# Deleting stop-words

from nltk.corpus import stopwords
stop_words = set(stopwords.words("russian"))
print(stop_words)

filtered_sent = []
for w in text_without_punctuation_signs:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:", text_without_punctuation_signs)
print("Filtered Sentence:", filtered_sent)