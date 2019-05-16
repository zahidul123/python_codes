import re
import imp
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
reglist=[(r'\'d',' would'),(r'\'s','is'),(r'didn\'t','did not'),(r'\'ll',' will')]

class RegexpressReplacer(object):
    def __init__(self):
        self.pattern=reglist

    def replace(self,text):
        for (raw, rep) in self.pattern:
            reg = re.compile(raw)
            text = reg.sub(rep, text)
        return text


class Repeatreplacer(object):
    def __init__(self):
        self.regex=re.compile(r'(\w*)(\w)\2(\w*)')
        self.repel=r'\1\2\3'

    def replace(self,word):
        if wordnet.synsets(word):
            return word
        loop_res=self.regex.sub(self.repel,word)
        if(word==loop_res):
            return word
        else:
            return self.replace(loop_res)


class Wordreplacer:
    def __init__(self,word_map):
        self.word_map=word_map

    def replacer(self,text):
        return self.word_map.get(text,text)




class AntonomyReplacer():
    def replace(self,word):
        antonyms=set()
        for syns in wordnet.synsets(word):
            for lemma in syns.lemmas():
                for antomnom in lemma.antonyms():
                    antonyms.add(antomnom.name())

        if len(antonyms)==1:
            return antonyms.pop()

        else:
            return None




    def rereplace(self,string):
        i=0
        sent=word_tokenize(string)
        len_sent=len(sent)

        words=[]
        while i<len_sent:
            word=sent[i]
            if word=='not' and i+1<len_sent:
                ant=self.replace(sent[i+1])
                if ant:
                    words.append(ant)
                    i=i+2

        return words


