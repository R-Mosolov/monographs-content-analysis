# print(text_without_punctuation_signs[0])

# for i in tokenized_word:
#     tokenized_word_arr.append(tokenized_word[i])
#
# print(tokenized_word_arr)

# tokenized_word = word_tokenize(text)
# print(tokenized_word)


# 3. Deleting punctuation signs

# tokenizer = RegexpTokenizer(r'\w+')
# text_without_punctuation_signs = tokenizer.tokenize(text)
#
# print(text_without_punctuation_signs)

# 4. Deleting stop-words

stop_words = stopwords.words('russian')
stop_words.extend(['не', 'это', 'что', 'именно', 'эта', 'лишь', 'очень', 'либо', 'или', 'ru', 'которые', 'конец',
                   'которая', 'который', 'ибо', 'см', 'n', 'например', 'является', '1', '2', '3', '4', '5', '6',
                   '7', '8', '9', '0', '', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                   'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

filtered_sent = []

for w in text_without_punctuation_signs:
    if w not in stop_words:
        filtered_sent.append(w)


# 5. Calculating TOP-words

fdist = FreqDist(filtered_sent)

result = fdist.most_common(50)

# print(result)