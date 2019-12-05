# For starting code type in terminal: % pip install nltk

import nltk
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    # 1. Add text

    from nltk.tokenize import sent_tokenize
    text = request.form['data-field'].lower()
    tokenized_text = sent_tokenize(text)

    from nltk.tokenize import word_tokenize
    tokenized_word = word_tokenize(text)

    # 2. Delete punctuation signs

    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    text_without_punctuation_signs = tokenizer.tokenize(text)

    # 3. Delete stop-words

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

    # 4. Calculate TOP-words

    from nltk.probability import FreqDist
    fdist = FreqDist(filtered_sent)

    result = fdist.most_common(10)

    # 5. Return result in HTML

    word1 = result[0][0]
    word2 = result[1][0]
    word3 = result[2][0]
    word4 = result[3][0]
    word5 = result[4][0]
    word6 = result[5][0]
    word7 = result[6][0]
    word8 = result[7][0]
    word9 = result[8][0]
    word10 = result[9][0]

    freq1 = result[0][1]
    freq2 = result[1][1]
    freq3 = result[2][1]
    freq4 = result[3][1]
    freq5 = result[4][1]
    freq6 = result[5][1]
    freq7 = result[6][1]
    freq8 = result[7][1]
    freq9 = result[8][1]
    freq10 = result[9][1]

    return render_template('result.html',
       w1=word1, w2=word2, w3=word3, w4=word4, w5=word5, w6=word6, w7=word7, w8=word8, w9=word9, w10=word10,
       f1=freq1, f2=freq2, f3=freq3, f4=freq4,  f5=freq5, f6=freq6, f7=freq7, f8=freq8, f9=freq9,  f10=freq10)


if __name__ == '__main__':
    app.run(debug=True)
