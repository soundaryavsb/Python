Cargo_price=int(input())

if Cargo_price>=0 and Cargo_price<=1000:
    print("Saver")
elif Cargo_price>=1001 and Cargo_price<=10000:
    print("Economy")
else:
    print("Flexi")
