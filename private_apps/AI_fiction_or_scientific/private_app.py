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
from modules.main_indicators import text__marker


# 1. CENTRALIZING FEW TEXTS
centralize_texts.run()


# 2. GETTING MAIN AND ADDITIONAL ANALYSIS INDICATORS
print('РЕЗУЛЬТАТ АНАЛИЗА')

# 2.1. Getting sentences number in text(s)
print('1. Количество предложений в тексте(-ах) (ед.): ' + str(text__sentence.calc()))

# 2.2. Getting words number in text(s)
print('2. Количество слов в тексте(-ах) (ед.): ' + str(text__word.calc()))

# 2.3. Getting punctuation signs number in text(s)
print('3. Абсолютное количество знаков препинаний в тексте(-ах) (ед.): ' + str(text__sign_abs.calc()))

# 2.4. Getting punctuation signs number in text(s)
print('4. Относительное количество знаков препинаний в тексте(-ах) (%): ' + str(text__sign_rel.calc()))

# 2.5. Getting words number mean in a sentence
print('5. Среднее число слов в предложении (ед.): ' + str(sentence__word.calc()))

# 2.6. Getting letters number mean in a word
print('6. Среднее число букв в слове (ед.): ' + str(word__letter.calc()))

# 2.7. Getting adjectives number mean in text(s)
print('7. Среднее количество прилагательных в тексте(-ах) (ед.): ' + str(text__adjective.calc()))

# 2.8. Getting number of number mean in text(s)
print('8. Среднее количество чисел в тексте(-ах) (ед.): ' + str(text__number.calc()))

# 2.9. Getting mean of dialog signs number in text(s)
# print('9. Среднее количество знаков начала диалога в тексте(-ах) (ед.): ' + str(text__dialog.calc()))


# 2.10. Getting mean of marker words number in text(s)

# 2.10.1. Getting mean of dialog signs number in text(s)
print('10.1. Среднее количество слова-маркера "сказал" в тексте(-ах) (ед.): ' + str(text__marker.calc('сказал')))

# 2.10.2. Getting mean of dialog signs number in text(s)
print('10.2. Среднее количество слова-маркера "сказала" в тексте(-ах) (ед.): ' + str(text__marker.calc('сказала')))

# 2.10.3. Getting mean of dialog signs number in text(s)
print('10.3. Среднее количество слова-маркера "говорит" в тексте(-ах) (ед.): ' + str(text__marker.calc('говорит')))

# 2.10.4. Getting mean of dialog signs number in text(s)
print('10.4. Среднее количество слова-маркера "говорил" в тексте(-ах) (ед.): ' + str(text__marker.calc('говорил')))

# 2.10.5. Getting mean of dialog signs number in text(s)
print('10.5. Среднее количество слова-маркера "спросил" в тексте(-ах) (ед.): ' + str(text__marker.calc('спросил')))


# 3. Recording the analysis result
record_result.run()