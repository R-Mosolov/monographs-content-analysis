from modules import punctuation_signs_number_in_text
from modules import words_number_in_text


def get():
    return round((punctuation_signs_number_in_text.get() * 100 / words_number_in_text.get()), 2)
