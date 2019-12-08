from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import mean_calculator
from private_apps.AI_fiction_or_scientific.modules.main_indicators import text__sign_rel


def run():
    TEXT__SIGN_REL = mean_calculator.run()[0]
    result = text__sign_rel.calc()

    return [TEXT__SIGN_REL, result]


print(run())
