from pprint import pprint

f=open('cmd.txt', encoding='utf-8').read()
list1=f.split('\n')
dic1={}
for i in list1:
    dic1[i[0:i.index('-')]]=i[i.index('-')+1:len(i)]
pprint(dic1)