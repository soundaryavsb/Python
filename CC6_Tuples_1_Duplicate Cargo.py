numbers=input().split(',')
Cargonumbers=list(dict.fromkeys(numbers))
Final_list=map(int,Cargonumbers)
print(tuple(Final_list))
