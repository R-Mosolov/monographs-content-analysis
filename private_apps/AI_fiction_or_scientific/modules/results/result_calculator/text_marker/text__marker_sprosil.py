from private_apps.AI_fiction_or_scientific.modules.main_indicators import text__marker
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import fiction_indicators
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import scientific_indicators
from private_apps.AI_fiction_or_scientific.modules.preparation.indicators_constants import mean_calculator


def run():
    analyzed_text = text__marker.calc('спросил')
    fiction_mean = fiction_indicators.TEXT__MARKER_SPROSIL
    scientific_mean = scientific_indicators.TEXT__MARKER_SPROSIL
    fiction_and_scientific_mean = mean_calculator.run()[9]

    print(['Показатель проанализированного текста: ' + str(analyzed_text),
           'Среднее худ. книг: ' + str(fiction_mean),
           'Среднее науч. книг: ' + str(scientific_mean),
           'Среднее между константами: ' + str(fiction_and_scientific_mean)])

    if fiction_mean > scientific_mean:
        if analyzed_text > (fiction_mean - fiction_and_scientific_mean):
            is_fiction_text = True
        else:
            is_fiction_text = False
    else:
        if analyzed_text > (scientific_mean - fiction_and_scientific_mean):
            is_fiction_text = False
        else:
            is_fiction_text = True

    if is_fiction_text:
        print('Проанализированный текст – художественный')
    else:
        print('Проанализированный текст – научный')

run()
