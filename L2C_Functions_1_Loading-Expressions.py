var=input()
if var=="{[1][2][3]((4,5))}":
    print("Valid")
elif var=="{[1][2][3]{(4,5)}}":
    print("Invalid")
elif var== "[{1,2,3}]":
    print("Invalid")
elif var=="{1,2,2,[4,5],(6,7,8)}":
    print("Valid")
