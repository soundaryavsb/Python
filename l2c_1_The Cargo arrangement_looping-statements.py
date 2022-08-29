container_length=int(input())

x=1
y=container_length-1
for timerun in range(container_length):
    print("#" * y +"*" * x + "+" * y)
    x=x+2
    y=y-1
    
