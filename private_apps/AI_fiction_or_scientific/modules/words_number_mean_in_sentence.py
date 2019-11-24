from modules import words_number_in_text
from modules import sentences_number_in_text


def get():
    average_words_number_in_sentence = words_number_in_text.get() / sentences_number_in_text.get()

    return str(round(average_words_number_in_sentence, 2))
