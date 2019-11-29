from modules.additional_indicators import text__sentence
from modules.additional_indicators import text__word


def get():
    text__word_mean = text__word.get() / text__sentence.get()

    return round(text__word_mean, 2)
