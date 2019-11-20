# 0. Uniting few texts

all_texts = ''
texts_arr = ['txt/Faust_Manually.txt', 'txt/Tolstoyi_L._Voyinaimir1._Voyina_I_Mir_Kniga_1.txt',
             'txt/Tolstoyi_L._Voyinaimir2._Voyina_I_Mir_Kniga_2.txt', 'txt/Tolstoyi_L._Anna_KareninaI.txt',
             'txt/Tolstoyi_L._Vse_Luchshie_Skazki_I_Ras.txt', 'txt/Vern_J._Tainstvennyiyi_OstrovI.txt']

for text in texts_arr:
    all_texts += open(text, 'r').read().lower()

# 1. Adding the text

from nltk.tokenize import sent_tokenize
text = all_texts
tokenized_text = sent_tokenize(text)

from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(text)

# 2. Deleting punctuation signs

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
text_without_punctuation_signs = tokenizer.tokenize(text)

# 3. Deleting stop-words

from nltk.corpus import stopwords
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

from nltk.probability import FreqDist
fdist = FreqDist(filtered_sent)

result = fdist.most_common(50)

print(result)