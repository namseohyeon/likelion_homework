import random
from typing import final

dic_mbti = {}
word=''

def mbti():
    x1 = random.choice('EI')
    mylist = list(x1)
    x2 = random.choice('SN')
    mylist.append(x2)
    x3 = random.choice('FT')
    mylist.append(x3)
    x4 = random.choice('JP')
    mylist.append(x4)
    string=''.join(mylist)
    # print(string)
    return string

def dic(word):           
    if word in dic_mbti:
        dic_mbti[word]=final.count(word)
    else:
        dic_mbti[word] = 1    

for i in range(200):
    word = mbti()
    if i==0:
        final = []
        final.append(word) 
    else:
        final.append(word)
    dic(word)        

print(dic_mbti)

#딕셔너리 형태 없이 출력
# for key,value in dic_mbti.items():
#     print(key,value)











