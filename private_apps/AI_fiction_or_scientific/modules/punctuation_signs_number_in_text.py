from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from modules import centralizing_few_texts


def get():
    # Coping data from the other function
    text = centralizing_few_texts.centralization()
    tokenized_text = sent_tokenize(text)
    text_with_punctuation_signs = word_tokenize(text)

    tokenized_word_arr = []

    for sentence in tokenized_text:
        tokenized_word = word_tokenize(sentence)
        tokenized_word_arr.append(tokenized_word)

    # Deleting punctuation signs
    tokenizer = RegexpTokenizer(r'\w+')
    text_without_punctuation_signs = tokenizer.tokenize(text)

    # Getting result
    return len(text_with_punctuation_signs) - len(text_without_punctuation_signs)
