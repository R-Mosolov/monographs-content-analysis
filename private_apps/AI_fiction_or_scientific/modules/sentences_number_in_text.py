from nltk.tokenize import sent_tokenize

from modules import centralizing_few_texts


def get():
    text = centralizing_few_texts.centralization()
    tokenized_text = sent_tokenize(text)

    return len(tokenized_text)
