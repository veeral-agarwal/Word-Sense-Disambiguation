from nltk.wsd import lesk
from string import punctuation as puncts
sentence = "how are you"
sentence = sentence.lower().strip()
for i in puncts:
    sentence = sentence.replace(i,'')
words = sentence.split(' ')
for word in words:
    print((words, word))