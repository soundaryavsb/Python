Input_Profit=input().split(",")
length=len(Input_Profit)
Cargo_Profit=[]
Maximum_Profit=0
for value in Input_Profit:
    Cargo_Profit.append(int(value))

Cargo_Profit.sort(reverse=True)

container_capacity=int(input())

for i in range(0,container_capacity):
    Maximum_Profit=Maximum_Profit+Cargo_Profit[i]

print(Maximum_Profit)

    

