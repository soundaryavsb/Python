Container_length=int(input())
Cargo_length=int(input())
Cargo_ID=int(input())

first=int(Container_length/Cargo_length)
second=first*first

if Cargo_ID%second==0:
    x=first-1
    y=first-1
    z=int(Cargo_ID/second)-1
else:
    z=int(Cargo_ID/second)
    remainder=Cargo_ID%second
    x= int((remainder-1)%first)
    if remainder%first==0:
        y=y=int(remainder/first)-1
    else:
        y=int(remainder/first)
    

print("({},{},{})".format(x,y,z))
