from modules.additional_indicators import text__word
from modules.additional_indicators import text__sign_abs


def get():
    return round((text__sign_abs.get() * 100 / text__word.get()), 2)
