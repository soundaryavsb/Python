import re
Number_of_Cargo=input()

length=len(Number_of_Cargo)
destination=re.findall(r'[a-zA-Z]+',Number_of_Cargo)

if (Number_of_Cargo[0].isdigit() != True)and (Number_of_Cargo[length-1].isdigit() == True):
    if len(destination)>1:
        print("{} to {}".format(destination[0],destination[1]))
    else:
       print("Invalid Input")
else:
    print("Invalid Input")
