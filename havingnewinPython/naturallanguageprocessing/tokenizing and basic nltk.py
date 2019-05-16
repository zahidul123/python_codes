from nltk.tokenize import sent_tokenize
import nltk
text="hello my name is sumon. iam a student of cse in diu. very poor student in knowledge."
nowtoken=sent_tokenize(text)
print(nowtoken)
nowtokenw=nltk.word_tokenize(text)
print(nowtokenw)

from nltk.corpus import wordnet
synonyms=[]
for syn in wordnet.synsets('AI'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)
antonyms=[]
for syn in wordnet.synsets('happy'):
        for l in syn.lemmas():
                if l.antonyms():
                          antonyms.append(l.antonyms()[0].name())
print(antonyms)
import nltk

from nltk.tokenize import PunktSentenceTokenizer
text='I am a human being, capable of doing terrible things'
sentences=nltk.sent_tokenize(text)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))

from nltk.corpus import stopwords
text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever!"
stopwords=set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
words=word_tokenize(text)
wordsFiltered=[]
for w in words:
        if w not in stopwords:
                 wordsFiltered.append(w)
print(wordsFiltered)