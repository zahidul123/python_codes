from nltk.corpus import wordnet
import imp
word="win"
synoname=wordnet.synsets(word)
print(synoname)
print(synoname[0].definition())
print(synoname[0].name())
print(synoname[0].hypernyms())
print(synoname[0].hyponyms())
wordofinterest=synoname[2]

print(wordofinterest.lemmas())

syntonamearr=[]
antonamearr=[]

for syn in synoname:
    for leam in syn.lemmas():
        syntonamearr.append(leam.name())

print(syntonamearr)
print(set(syntonamearr))

#now i will print antonymes

for syn in  synoname:
    for leam in syn.lemmas():
        for antoname in leam.antonyms():
            antonamearr.append(antoname.name())

print(set(antonamearr))

#finding similiraty between words

saynarr1=wordnet.synsets('cake')
saynarr2=wordnet.synsets('loaf')
saynarr3=wordnet.synsets('bread')

sim1=saynarr1[0].wup_similarity(saynarr2[0])
print(sim1)
sim2=saynarr2[0].wup_similarity(saynarr2[1])
print(sim2)
sim3=saynarr2[0].wup_similarity(saynarr3[0])
print(sim3)
sim3=saynarr2[1].wup_similarity(saynarr3[0])
print(sim3)
sim4=saynarr1[0].wup_similarity(saynarr3[0])
print(sim4)

ref=saynarr1[0].hypernyms()[0]
print(saynarr2[0].shortest_path_distsnce(ref))

