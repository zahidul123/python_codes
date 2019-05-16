from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

textword=[w.lower()for w in webtext.words('pirates.txt')]
txtfinder=BigramCollocationFinder.from_words(textword)
print(txtfinder.nbest(BigramAssocMeasures.likelihood_ratio,10))
ignoreword=set(stopwords.words('english'))
#another way to delete some  word
filtering=lambda wor:len(wor)<3 or wor  in ignoreword
#for calling lambda function
txtfinder.apply_word_filter(filtering)
txtfinder.nbest(BigramAssocMeasures.likelihood_ratio,10)

#now we are showing trigram
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

textwords=[w.lower()for w in webtext.words('pirates.txt')]
tfinder=TrigramCollocationFinder.from_words(textwords)
tfinder.nbest(TrigramAssocMeasures.likelihood_ratio,10)
ignoreword=set(stopwords.words('english'))
filtering=lambda wor:len(wor)<3 or wor  in ignoreword
#for calling lambda function
tfinder.apply_word_filter(filtering)
tfinder.apply_freq_filter(3)
tfinder.nbest(BigramAssocMeasures.likelihood_ratio,10)
