Container_Weight=int(input())
Number_of_Cargos=0

for i in range(Container_Weight):
    Cargos_Weight=int(input())
    Container_Weight=Container_Weight - Cargos_Weight
    if Container_Weight>=0:
        Number_of_Cargos=Number_of_Cargos+1
    else:
        break
    
print(Number_of_Cargos)
