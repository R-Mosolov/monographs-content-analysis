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
                       'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '1', '2', '3', '4', '5', '6',
                       '7', '8', '9', '0', '', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                       'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

    filtered_sent = []

    for w in text_without_punctuation_signs:
        if w not in stop_words:
            filtered_sent.append(w)

    # Searching adjectives in the text
    adjectives = []

    for word in filtered_sent:
        if word[len(word) - 2] == 'а' and word[len(word) - 1] == 'я' \
                or word[len(word) - 2] == 'о' and word[len(word) - 1] == 'е'\
                or word[len(word) - 2] == 'е' and word[len(word) - 1] == 'е'\
                or word[len(word) - 2] == 'о' and word[len(word) - 1] == 'й'\
                or word[len(word) - 2] == 'ы' and word[len(word) - 1] == 'е'\
                or word[len(word) - 2] == 'и' and word[len(word) - 1] == 'е'\
                or word[len(word) - 2] == 'ы' and word[len(word) - 1] == 'й':
            adjectives.append(word)

    # Deleting conjunctions
    for word in adjectives:
        if word[0] == 'к' and word[1] == 'о' and word[2] == 'т' and word[3] == 'о' and word[4] == 'р' \
                or word[0] == 'к' and word[1] == 'а' and word[2] == 'к':
            adjectives.remove(word)

    # Getting the result
    return len(adjectives)
