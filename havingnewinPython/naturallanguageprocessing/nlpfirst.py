import nltk
from nltk.tokenize import sent_tokenize
parg="hi am sumon. from daffodil international university. atrai is my native village."
ar=sent_tokenize(parg)
print(ar)
from nltk.tokenize import word_tokenize
separate=word_tokenize(parg)
print(separate)

#there are some several way for tokenize
#from nltk.tokenize import TreebankWordTokenizer
#tk1=TreebankWordTokenizer(parg)

#from nltk.tokenize import WordPunctTokenizer
peg="Don't make a lie it's very bad. hope's from . I the boy of thorne actors Am wanna Doing Something"
#tkl2=WordPunctTokenizer(peg,"[\w']+")

from nltk.tokenize import regexp_tokenize
peg=peg.lower()
tkl2=regexp_tokenize(peg,"[\w']+")
print(tkl2)

#stop word means to dont calculate this meaning of word

from nltk.corpus import stopwords

wordinclude=stopwords.words('english')
#print(wordinclude)

#now i filter this sentence for some basic owrds
filterinf=[mains for mains in tkl2 if mains not in wordinclude]
print(filterinf)


