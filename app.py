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
    stop_words_ru = set(stopwords.words('russian'))
    stop_words_eng = set(stopwords.words('english'))

    filtered_sent = []

    for w in text_without_punctuation_signs:
        if w not in stop_words_ru:
            filtered_sent.append(w)

    for w in text_without_punctuation_signs:
        if w not in stop_words_eng:
            filtered_sent.append(w)

    # 4. Calculate TOP-words

    from nltk.probability import FreqDist
    fdist = FreqDist(filtered_sent)

    result = fdist.most_common(10)

    # 5. Return result in HTML

    result1 = result[0]
    result2 = result[1]
    result3 = result[2]
    result4 = result[3]
    result5 = result[4]
    result6 = result[5]
    result7 = result[6]
    result8 = result[7]
    result9 = result[8]
    result10 = result[9]
    return render_template('result.html', r1=result1, r2=result2, r3=result3, r4=result4,  r5=result5,
                           r6=result6, r7=result7, r8=result8, r9=result9,  r10=result10)


if __name__ == '__main__':
    app.run(debug=True)
