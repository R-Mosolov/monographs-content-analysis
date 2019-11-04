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
    text = request.form['data-field']
    tokenized_text = sent_tokenize(text)

    from nltk.tokenize import word_tokenize
    tokenized_word = word_tokenize(text)

    # 2. Delete punctuation signs

    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    text_without_punctuation_signs = tokenizer.tokenize(text)

    # 3. Delete stop-words

    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('russian'))

    filtered_sent = []
    for w in text_without_punctuation_signs:
        if w not in stop_words:
            filtered_sent.append(w)

    # 4. Calculate TOP-words

    from nltk.probability import FreqDist
    fdist = FreqDist(filtered_sent)

    result = fdist.most_common(5)

    # 5. Return result in HTML

    result1 = result[0]
    result2 = result[1]
    result3 = result[2]
    result4 = result[3]
    result5 = result[4]
    return render_template('result.html', r1=result1, r2=result2, r3=result3, r4=result4,  r5=result5)


if __name__ == '__main__':
    app.run(debug=True)
