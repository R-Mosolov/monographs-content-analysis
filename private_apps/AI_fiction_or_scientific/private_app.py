from modules.preparation import centralize_texts

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

from modules.results import record_result


# 1. CENTRALIZING FEW TEXTS
centralize_texts.run()


# 2. GETTING MAIN AND ADDITIONAL ANALYSIS INDICATORS
print('РЕЗУЛЬТАТ АНАЛИЗА')

# 2.1. Getting sentences number in text(s)
print('1. Количество предложений: ' + str(text__sentence.calc()) + ' ед./текс.')

# 2.2. Getting words number in text(s)
print('2. Количество слов: ' + str(text__word.calc()) + ' ед./текс.')

# 2.3. Getting punctuation signs number in text(s)
print('3. Абсолютное число знаков препинания: ' + str(text__sign_abs.calc()) + ' ед./текс.')

# 2.4. Getting punctuation signs number in text(s)
print('4. Относительное число знаков препинания: ' + str(text__sign_rel.calc()) + ' %/текст.')

# 2.5. Getting words number mean in a sentence
print('5. Среднее число слов: ' + str(sentence__word.calc()) + ' ед./пред.')

# 2.6. Getting letters number mean in a word
print('6. Среднее число букв: ' + str(word__letter.calc()) + ' ед./текс.')

# 2.7. Getting adjectives number mean in text(s)
print('7. Среднее число прилагательных: ' + str(text__adjective.calc()) + ' %/текс.')

# 2.8. Getting number of number mean in text(s)
print('8. Среднее число цифр: ' + str(text__number.calc()) + ' ед./текс.')

# 2.9. Getting mean of dialog signs number in text(s)
print('9. Среднее число знаков диалога: ' + str(text__dialog.calc()) + ' %/текс.')

# 2.10. GETTING MEAN OF MARKER WORDS NUMBER IN TEXT(S)
print('10. АНАЛИЗ СЛОВ-МАРКЕРОВ')

# 2.10.1. Getting mean of dialog signs number in text(s)
print('10.1. Среднее число слова-маркера "сказал": ' + str(text__marker.calc('сказал')) + ' %/текс.')

# 2.10.2. Getting mean of dialog signs number in text(s)
print('10.2. Среднее число слова-маркера "сказала": ' + str(text__marker.calc('сказала')) + ' %/текс.')

# 2.10.3. Getting mean of dialog signs number in text(s)
print('10.3. Среднее число слова-маркера "говорит": ' + str(text__marker.calc('говорит')) + ' %/текс.')

# 2.10.4. Getting mean of dialog signs number in text(s)
print('10.4. Среднее число слова-маркера "говорил": ' + str(text__marker.calc('говорил')) + ' %/текс.')

# 2.10.5. Getting mean of dialog signs number in text(s)
print('10.5. Среднее число слова-маркера "спросил": ' + str(text__marker.calc('спросил')) + ' %/текс.')


# 3. Recording the analysis result
record_result.run()