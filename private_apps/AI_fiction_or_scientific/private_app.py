from modules import centralizing_few_texts
from modules import sentences_number_in_text
from modules import words_number_in_text
from modules import punctuation_signs_number_in_text
from modules import relative_punctuation_signs_number_in_text
from modules import words_number_mean_in_sentence
from modules import letters_number_mean_in_word
from modules import recording_the_result


# 1. CENTRALIZING FEW TEXTS
centralizing_few_texts.centralization()


# 2. GETTING MAIN AND ADDITIONAL INDICATORS
print('РЕЗУЛЬТАТ АНАЛИЗА')

# 2.1. Getting sentences number in the text
print('1. Количество предложений в тексте (ед.): ' + str(sentences_number_in_text.get()))

# 2.2. Getting words number in the text
print('2. Количество слов в тексте (ед.): ' + str(words_number_in_text.get()))

# 2.3. Getting punctuation signs number in the text
print('3. Абсолютное количество знаков препинаний в тексте (ед.): ' + str(punctuation_signs_number_in_text.get()))

# 2.4. Getting punctuation signs number in the text
print('4. Относительное количество знаков препинаний в тексте (%): ' + str(relative_punctuation_signs_number_in_text.get()))

# 2.5. Getting average words number in a sentence
print('5. Среднее число слов в предложении (ед.): ' + str(words_number_mean_in_sentence.get()))

# 2.6. Getting average letters number in a word
print('6. Среднее число букв в слове (ед.): ' + str(letters_number_mean_in_word.get()))


# 3. Recording the analysis result
recording_the_result.record()