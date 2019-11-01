# for starting code type in terminal: % pip install nltk

import nltk
from flask import Flask, render_template, request

from nltk.tokenize import sent_tokenize
text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
# print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
# print(tokenized_word)

from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
# print(fdist)

calculating_result=fdist.most_common(2)
# print(result)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    result = calculating_result
    return render_template('result.html', r=result)

if __name__ == '__main__':
    app.run(debug=True)