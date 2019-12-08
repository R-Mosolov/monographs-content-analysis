from private_apps.AI_fiction_or_scientific.modules.additional_indicators import text__word
from private_apps.AI_fiction_or_scientific.modules.additional_indicators import text__sign_abs


def calc():
    return round((text__sign_abs.calc() * 100 / text__word.calc()), 2)
