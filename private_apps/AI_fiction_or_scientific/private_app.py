import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist


# 0. Uniting few texts

def create_full_path(path_link):
    test_paths = os.listdir(path_link)
    test_arr = []

    for path in test_paths:
        if path != '.DS_Store':
            test_arr.append(path_link + path)

    return test_arr


all_texts = ''

defoe = create_full_path('txt/fiction_literature/foreign/Defoe/')
dikkens = create_full_path('txt/fiction_literature/foreign/Dikkens/')
vern = create_full_path('txt/fiction_literature/foreign/Vern/')

bulgakov = create_full_path('txt/fiction_literature/russian/Bulgakov/')
chehov = create_full_path('txt/fiction_literature/russian/Chehov/')
dostoevskiy = create_full_path('txt/fiction_literature/russian/Dostoevskiy/')
gogol = create_full_path('txt/fiction_literature/russian/Gogol/')
pushkin = create_full_path('txt/fiction_literature/russian/Pushkin/')
tolstoy = create_full_path('txt/fiction_literature/russian/Tolstoy/')
turgenev = create_full_path('txt/fiction_literature/russian/Turgenev/')

texts_arr = (defoe + dikkens + vern) + (bulgakov + chehov + dostoevskiy + gogol + pushkin + tolstoy + turgenev)

for text in texts_arr:
    all_texts += open(text, 'r').read().lower()

print(all_texts)

# 1. Adding the text

text = all_texts
tokenized_text = sent_tokenize(text)

tokenized_word = word_tokenize(text)

# 2. Deleting punctuation signs

tokenizer = RegexpTokenizer(r'\w+')
text_without_punctuation_signs = tokenizer.tokenize(text)

# 3. Deleting stop-words

stop_words = stopwords.words('russian')
stop_words.extend(['не', 'это', 'что', 'именно', 'эта', 'лишь', 'очень', 'либо', 'или', 'ru', 'которые', 'конец',
                   'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '1', '2', '3', '4', '5', '6',
                   '7', '8', '9', '0', '', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                   'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

filtered_sent = []

for w in text_without_punctuation_signs:
    if w not in stop_words:
        filtered_sent.append(w)

# 4. Calculating TOP-words

fdist = FreqDist(filtered_sent)

result = fdist.most_common(50)

print(result)
