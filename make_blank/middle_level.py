import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
text = "This is an example sentence. and I'll tell you about dogs."
target=''
tokens = word_tokenize(text)
print(nltk.pos_tag(tokens=tokens))
replaced_text='_'
# 그냥 품사 상관없이 다 띄기.