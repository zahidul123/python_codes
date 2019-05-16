from nltk.stem  import PorterStemmer
from nltk.stem  import LancasterStemmer
from nltk.stem  import RegexpStemmer

postammer=PorterStemmer()
print(postammer.stem('dancing'))

from nltk.stem import WordNetLemmatizer

lzr=WordNetLemmatizer()

print(lzr.lemmatize('dancing'))

#but if we want to make it any converting then we use

print(lzr.lemmatize('dancing',pos='v'))
lstemmer=LancasterStemmer()
print(lstemmer('cooking'))
#it just cut down the part what we givw in regexpress
Rexpress=RegexpStemmer('er')
print(Rexpress.stem('cooker'))
