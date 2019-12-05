from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist

from modules.preparation import centralize_texts
from modules.additional_indicators import text__word


def calc(analysed_word):
    # Adding the text
    text = centralize_texts.run().lower()

    # Deleting punctuation signs
    tokenizer = RegexpTokenizer(r'\w+')
    text_without_punctuation_signs = tokenizer.tokenize(text)

    # Deleting stop-words
    stop_words = stopwords.words('russian')
    stop_words.extend(['не', 'это', 'что', 'именно', 'эта', 'лишь', 'очень', 'либо', 'или', 'ru', 'которые',
                       'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '1', '2', '3', '4', '5', '6',
                       '7', '8', '9', '0', '', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                       'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

    filtered_sent = []

    for word in text_without_punctuation_signs:
        if word not in stop_words:
            filtered_sent.append(word)

    # Calculating TOP-words
    fdist = FreqDist(filtered_sent)
    top_words = fdist.most_common(1000)

    # Calculating frequency of the marker word
    returned_result = ''

    for word in top_words:
        word_value = word[0]
        word_freq = word[1]

        if word_value == analysed_word:
            returned_result = word_freq

    if returned_result == '':
        returned_result = 'The word is not find'

    # Calculating a relative indicator of the marker word
    relative_indicator = 0

    if returned_result != 'The word is not find':
        relative_indicator = returned_result * 100 / text__word.calc()

    # Calculating the result
    return round(relative_indicator, 3)
