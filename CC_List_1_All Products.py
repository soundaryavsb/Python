CargoIdsList=list(map(int,input("Enter the Numbers in List-1\n").split(" ")))
CargoPriceList=list(map(int,input("Enter the Numbers in List-2\n").split(" ")))

count=0
for i in CargoIdsList:
    for j in CargoPriceList:
        if((i*j)%2!=0):
            print(i*j,end=' ')
            count=1
            
if(count==0):
    print("No such Elements in the list")
