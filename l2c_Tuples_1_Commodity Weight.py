Weight = list(map(int, input().split()))
Number_of_pieces=int(input())
value=[]

for i in Weight:
    value.append(i*Number_of_pieces)
    
output=tuple(value)
print(output)
    
