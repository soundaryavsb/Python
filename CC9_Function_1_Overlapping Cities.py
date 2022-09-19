City_list1=input()
City_list2=input()
City5=City_list1.split(",")
City6=City_list2.split(",")

City3=City_list1.lower().split(",")
City4=City_list2.lower().split(",")
print(City5)
print(City6)
count=0

for cities in City4:
    if cities in City3:
        count=1
        break
if count==1:
    print("Overlapping")
else:
    print("Non Overlapping")
