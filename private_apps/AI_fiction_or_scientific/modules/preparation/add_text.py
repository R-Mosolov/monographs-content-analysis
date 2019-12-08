from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from private_apps.AI_fiction_or_scientific.modules.preparation import centralize_texts


def adding():
    # Coping data from the other function
    text = centralize_texts.run()
    tokenized_text = sent_tokenize(text)

    tokenized_word_arr = []

    for sentence in tokenized_text:
        tokenized_word = word_tokenize(sentence)
        tokenized_word_arr.append(tokenized_word)

    tokenized_word_arr_without_tokenized = ''

    for word in tokenized_word_arr:
        tokenized_word_arr_without_tokenized += (word + ' ')

    # Returning the result
    return tokenized_word_arr_without_tokenized
