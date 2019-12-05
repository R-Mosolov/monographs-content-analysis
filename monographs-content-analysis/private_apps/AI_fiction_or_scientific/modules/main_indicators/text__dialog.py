from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from modules.preparation import centralize_texts
from modules.additional_indicators import text__word


def calc():
    # Separating texts on sentences
    text = centralize_texts.run()
    tokenized_text = sent_tokenize(text)

    # Separating sentences on words
    tokenized_word_arr = []

    for sentence in tokenized_text:
        tokenized_word = word_tokenize(sentence)
        tokenized_word_arr.append(tokenized_word)

    # Searching dialog signs in words
    stop_words = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                  'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    dialogs = []

    for sentence in tokenized_word_arr:
        if sentence[0] == '-' or sentence[0] == '–' or sentence[0] == '—':
            if sentence[1][0] not in stop_words:
                dialogs.append(sentence)

    # Calculating a relative indicator
    relative_indicator = round(len(dialogs) * 100 / text__word.calc(), 2)

    # Calculating the result
    return relative_indicator
