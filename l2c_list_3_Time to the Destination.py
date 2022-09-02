R = int(input())
if R>=0 and R<=100:
    
    C = 3
    count=0  
    # Initialize matrix
    value = []
    matrix = []
 
    for i in range(R):          # A for loop for row entries
        value=input().split(" ")
        a =[]
        for j in range(C):      # A for loop for column entries
            a.append(int(value[j]))
        matrix.append(a)
    for i in range(R):
        for j in range(C):
            if matrix[i][0]<0 or matrix[i][0]>1000 or matrix[i][1]<1 or matrix[i][1]>1000 or matrix[i][2]<1 or matrix[i][2]>1000:
                count = count+1
            else:
                #print(matrix[i][j])
                if matrix[0][1]>matrix[0][2]:
                    first=matrix[0][1]
                else:
                    first=matrix[0][2]
                if matrix[1][0]>first:
                    second=matrix[1][0]-first
                else:
                    second=matrix[1][2]-first
                third=matrix[1][1]
    if count != 0:
        print("Invalid input")
    else:
        Total=first+second+third
        print(Total)
else:
    print("Invalid input")
