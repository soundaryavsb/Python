Input_Status=input().split(",")

Cargo_Status=input()
i=1
count=0
for status in Input_Status:
    if status==Cargo_Status:
        print(i)
        count=count+1
    i=i+1
    
if count==0:
    print(count)
