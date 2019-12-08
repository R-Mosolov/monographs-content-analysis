import statistics
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from private_apps.AI_fiction_or_scientific.modules.preparation import centralize_texts


def calc():
    # Coping data from the other function
    text = centralize_texts.run()
    tokenized_text = sent_tokenize(text)

    tokenized_word_arr = []

    for sentence in tokenized_text:
        tokenized_word = word_tokenize(sentence)
        tokenized_word_arr.append(tokenized_word)

    # Deleting punctuation signs
    tokenizer = RegexpTokenizer(r'\w+')
    text_without_punctuation_signs = tokenizer.tokenize(text)

    # Deleting stop-words
    stop_words = stopwords.words('russian')
    stop_words.extend(['не', 'это', 'что', 'именно', 'эта', 'лишь', 'очень', 'либо', 'или', 'ru', 'которые', 'конец',
                       'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '1', '2', '3', '4', '5', '6',
                       '7', '8', '9', '0', '', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                       'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

    filtered_sent = []

    for w in text_without_punctuation_signs:
        if w not in stop_words:
            filtered_sent.append(w)

    # Calculating mean of letters number
    letters_number_arr = []

    for word in filtered_sent:
        letters_number_arr.append(len(word))

    # Calculating the result
    return round(statistics.mean(letters_number_arr), 2)
