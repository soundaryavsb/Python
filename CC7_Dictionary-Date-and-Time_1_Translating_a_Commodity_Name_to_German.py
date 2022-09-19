pair=dict()
p=[]
a=0
word=input("").split(",")
for i in word:
    j=i.split(" ")
    key=j[0]
    value=j[1]
    pair[key]=value
    
sen=input("").split(" ")
for k in sen:
    p.append(pair.get(k))
    
for k in p:
    if k==None:
        a=1
if a==1:
    print("The sentence cannot be translated")
else:
    print(*p)
