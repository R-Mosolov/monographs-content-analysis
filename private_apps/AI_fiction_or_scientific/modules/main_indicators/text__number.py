from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

from modules.preparation import centralize_texts


def get():
    # Coping data from the other function
    text = centralize_texts.run().lower()
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
                       'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '', 'а', 'б', 'в', 'г', 'д', 'е',
                       'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
                       'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

    filtered_sent = []

    for word in text_without_punctuation_signs:
        if word not in stop_words:
            filtered_sent.append(word)

    # for word in filtered_sent:
    #     print(word)

    # # Searching numbers in the text
    # numbers = []
    #
    # for word in filtered_sent:
    #     if word[0] == '1' or word[0] == '2' or word[0] == '3' or word[0] == '4' or word[0] == '5' or word[0] == '6' \
    #             or word[0] == '7' or word[0] == '8' or word[0] == '9' or word[0] == '0':
    #         word = int(word)
    #         numbers.append(word)
    #
    # print(numbers)

    # Getting the result
    # return len(numbers)
