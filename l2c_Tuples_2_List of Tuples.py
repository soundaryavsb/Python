Record=int(input())
values=[]

for i in range(Record):
    a =input().split(",")
    values.append(tuple(a))

Date= input()
print(values)
Datecombo=Date.split("-")

for i in range(Record):
    valuecombo=values[i][1].split("-")
    if int(Datecombo[2])< int(valuecombo[2]):
        print(values[i][0])
    elif int(Datecombo[2])== int(valuecombo[2]):
        if int(Datecombo[1])< int(valuecombo[1]):
            print(values[i][0])
        elif int(Datecombo[1])== int(valuecombo[1]):
            if int(Datecombo[0])<= int(valuecombo[0]):
                print(values[i][0])

