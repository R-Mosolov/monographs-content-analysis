from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.main_indicators import text__sign_rel
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.main_indicators import sentence__word
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.main_indicators import word__letter
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.main_indicators import text__adjective
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.main_indicators import text__dialog

from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.text_marker import text__marker_skazal
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.text_marker import text__marker_skazala
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.text_marker import text__marker_govorit
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.text_marker import text__marker_govoril
from private_apps.AI_fiction_or_scientific.modules.results.result_calculator.text_marker import text__marker_sprosil


def run():
    indicators_results = [text__sign_rel.run(),
                          sentence__word.run(),
                          word__letter.run(),
                          text__adjective.run(),
                          text__dialog.run(),

                          text__marker_skazal.run(),
                          text__marker_skazala.run(),
                          text__marker_govorit.run(),
                          text__marker_govoril.run(),
                          text__marker_sprosil.run()]

    results_arr = []
    for indicator in indicators_results:
        results_arr.append(indicator)

    arr_elements_sum = 0
    for indicator in results_arr:
        arr_elements_sum += indicator

    if arr_elements_sum >= 5:
        analysis_solution = 'Результат анализа: текст является художественным!'
    else:
        analysis_solution = 'Результат анализа: текст является научным!'

    return analysis_solution


print(run())
