from private_apps.AI_fiction_or_scientific.modules.additional_indicators import text__sentence
from private_apps.AI_fiction_or_scientific.modules.additional_indicators import text__word


def calc():
    text__word_mean = text__word.calc() / text__sentence.calc()

    return round(text__word_mean, 2)
