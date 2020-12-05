from nltk.wsd import lesk
from nltk.corpus import stopwords
sw = stopwords.words('english')

from string import punctuation as puncts

def leskalgo(sentence):
    sentence = sentence.lower().strip()
    for i in puncts:
         sentence = sentence.replace(i,'')
    words = sentence.split(' ')
    for word in words:
        if word not in sw:
            print(word,':\t',lesk(words, word))

leskalgo("You must have seen today's newspaper")
