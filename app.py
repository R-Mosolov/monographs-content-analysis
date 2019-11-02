# for starting code type in terminal: % pip install nltk

import nltk
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    from nltk.tokenize import sent_tokenize
    text = request.form['data-field']
    tokenized_text = sent_tokenize(text)
    # print(tokenized_text)

    from nltk.tokenize import word_tokenize
    tokenized_word = word_tokenize(text)
    # print(tokenized_word)

    from nltk.probability import FreqDist
    fdist = FreqDist(tokenized_word)
    # print(fdist)

    calculating_result = fdist.most_common(5)
    # print(calculating_result[0])

    import matplotlib.pyplot as plt
    # fdist.plot(30, cumulative=False)
    # plt.show()

    result1 = calculating_result[0]
    result2 = calculating_result[1]
    result3 = calculating_result[2]
    result4 = calculating_result[3]
    result5 = calculating_result[4]
    return render_template('result.html', r1=result1, r2=result2, r3=result3, r4=result4,  r5=result5)


if __name__ == '__main__':
    app.run(debug=True)
