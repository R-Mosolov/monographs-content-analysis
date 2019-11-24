from modules import centralizing_few_texts
from modules import adding_the_text
from modules import sentences_number_in_text


# 1. Centralizing few texts
centralizing_few_texts.centralization()


# 2.1. Adding the text
adding_the_text.adding()


# 2.2. Sentences number in the text
stage_result = sentences_number_in_text.calculate()
print(stage_result)


# 3. Selecting analysis indicators

# 3.1. Main analysis indicators
median_of_words_number_in_sentences = 0

# 3.2. Additional analysis indicators
sentences_number_in_text = 0
words_number_in_text = 0
