from modules.preparation import centralize_texts
from modules.preparation import record_result

from modules.additional_indicators import text__sentence
from modules.additional_indicators import text__word
from modules.additional_indicators import text__sign_abs

from modules.main_indicators import text__sign_rel
from modules.main_indicators import sentence__word
from modules.main_indicators import word__letter
from modules.main_indicators import text__adjective
from modules.main_indicators import text__number
from modules.main_indicators import text__dialog


# 1. CENTRALIZING FEW TEXTS
centralize_texts.run()


# # 2. GETTING MAIN AND ADDITIONAL INDICATORS
print('РЕЗУЛЬТАТ АНАЛИЗА')

# 2.1. Getting sentences number in texts
print('1. Количество предложений в тексте (ед.): ' + str(text__sentence.get()))

# 2.2. Getting words number in texts
print('2. Количество слов в тексте (ед.): ' + str(text__word.get()))

# 2.3. Getting punctuation signs number in texts
print('3. Абсолютное количество знаков препинаний в тексте (ед.): ' + str(text__sign_abs.get()))

# 2.4. Getting punctuation signs number in texts
print('4. Относительное количество знаков препинаний в тексте (%): ' + str(text__sign_rel.get()))

# 2.5. Getting words number mean in a sentence
print('5. Среднее число слов в предложении (ед.): ' + str(sentence__word.get()))

# 2.6. Getting letters number mean in a word
print('6. Среднее число букв в слове (ед.): ' + str(word__letter.get()))

# 2.7. Getting adjectives number mean in texts
print('7. Среднее количество прилагательных в тексте (ед.): ' + str(text__adjective.get()))

# 2.8. Getting number of number mean in texts
print('8. Среднее количество чисел в тексте (ед.): ' + str(text__number.get()))

# 2.9. Getting mean of dialog signs number in texts
print('9. Среднее количество знаков начала диалога в тексте (ед.): ' + str(text__dialog.get()))


# # 3. Recording the analysis result
record_result.run()