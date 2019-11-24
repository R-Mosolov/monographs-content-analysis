from modules import centralizing_few_texts
from modules import sentences_number_in_text
from modules import words_number_in_text
from modules import words_number_mean_in_sentence
from modules import letters_number_mean_in_word


# 1. CENTRALIZING FEW TEXTS
centralizing_few_texts.centralization()


# 2. GETTING MAIN AND ADDITIONAL INDICATORS

# 2.1. Getting sentences number in the text
print('Количество предложений в тексте: ' + str(sentences_number_in_text.get()))

# 2.2. Getting words number in the text
print('Количество слов в тексте: ' + str(words_number_in_text.get()))

# 2.3. Getting average words number in a sentence
print('Среднее число слов в предложении: ' + str(words_number_mean_in_sentence.get()))

# 2.4. Getting average letters number in a word
print('Среднее число букв в слове: ' + str(letters_number_mean_in_word.get()))
