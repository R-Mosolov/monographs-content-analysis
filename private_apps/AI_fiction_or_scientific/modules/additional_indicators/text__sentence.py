from nltk.tokenize import sent_tokenize

from modules.preparation import centralize_texts


def calc():
    text = centralize_texts.run()
    tokenized_text = sent_tokenize(text)

    return len(tokenized_text)
