import  re
rexpress=re.compile(r'don\'t')
fst="i don't go to school"
correct=rexpress.sub('do not',fst)
print("the correct ans is :",correct)

para="first  i'd like to invite. he didn't like it very much. i'll go to school tomorrow"
reglist=[(r'\'d',' would'),(r'\'s',' is'),(r'didn\'t','did not'),(r'\'ll',' will')]

def replace(text,pattern):
    for (raw,rep) in pattern:
        reg=re.compile(raw)
        text=reg.sub(rep,text)
    print(text)

replace(para,reglist)