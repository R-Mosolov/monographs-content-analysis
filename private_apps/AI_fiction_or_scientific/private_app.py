import os
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist


# 0. Uniting few texts

all_texts = ''

defoe_path = 'txt/fiction_literature/foreign/Defoe/'
defoe = os.listdir(defoe_path)

dikkens_path = 'txt/fiction_literature/foreign/Dikkens/'
dikkens = os.listdir(dikkens_path)

vern_path = 'txt/fiction_literature/foreign/Vern/'
vern = os.listdir(vern_path)

turgenev_path = 'txt/fiction_literature/russian/Turgenev/'
turgenev = os.listdir(turgenev_path)

tolstoy_path = 'txt/fiction_literature/russian/Tolstoy/'
tolstoy = os.listdir(tolstoy_path)

texts_arr = defoe + dikkens + vern + turgenev + tolstoy

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
stop_words.extend(['не', 'это', 'что', 'именно', 'эта', 'лишь', 'очень', 'либо', 'или', 'ru', 'которые',
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
