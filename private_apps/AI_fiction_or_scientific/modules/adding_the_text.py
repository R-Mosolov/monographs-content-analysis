from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from modules import centralizing_few_texts


def adding():
    text = centralizing_few_texts.centralization()
    tokenized_text = sent_tokenize(text)
    tokenized_word_arr = []

    for sentence in tokenized_text:
        tokenized_word = word_tokenize(sentence)
        tokenized_word_arr.append(tokenized_word)

    tokenized_word_arr_without_tokenized = ''

    for word in tokenized_word_arr[0]:
        tokenized_word_arr_without_tokenized += (word + ' ')

    return tokenized_word_arr_without_tokenized
