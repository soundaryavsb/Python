Dry_Storage_1=int(input())
Dry_Storage_2=int(input())
Dry_Storage_3=int(input())
Dry_Storage_4=int(input())

Reagan_Cargo_number=int(input())

if Reagan_Cargo_number-Dry_Storage_1<=0:
    Dry_Storage=1
    print(Dry_Storage)
elif Reagan_Cargo_number-(Dry_Storage_1+Dry_Storage_2)<=0:
    Dry_Storage=2
    print(Dry_Storage)
elif Reagan_Cargo_number-(Dry_Storage_1+Dry_Storage_2+Dry_Storage_3)<=0:
    Dry_Storage=3
    print(Dry_Storage)
elif Reagan_Cargo_number-(Dry_Storage_1+Dry_Storage_2+Dry_Storage_3+Dry_Storage_4)<=0:
    Dry_Storage=4
    print(Dry_Storage)
else:
    print("Not Possible")
