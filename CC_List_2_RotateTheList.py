Inputlist=list(map(int,input("Enter the Numbers in List\n").split(' ')))
print("Before Rotating :")
for i in Inputlist:
    print(i,end=" ")
print("After Rotating : ")

count=0
for j in Inputlist:
    if count!=0:
        print(j,end=" ")
    count=count+1
print(Inputlist[0])

#******************************************************
