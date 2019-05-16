from reexpressionpackage import RegexpressReplacer
from reexpressionpackage import Repeatreplacer
from reexpressionpackage import Wordreplacer
from nltk.tokenize import word_tokenize
replacer=RegexpressReplacer()
showcorr=replacer.replace("he'd gone")
print(showcorr)


repeat=Repeatreplacer()
result=repeat.replace('booook')
print(result)

wordmap={'bday':'birthday','sup':'whats up','tom':'tomorrow'}
replacing=Wordreplacer(wordmap)

tknz=word_tokenize('sup u this is awesome')
print(tknz)
for word in tknz:
    res=replacing.replacer(word)
    print(res)
result=replacing.replacer('tom')
print(result)



#Negation replacing

from reexpressionpackage import AntonomyReplacer

rep=AntonomyReplacer()
jarward=rep.replace('cowardice')
print(jarward)