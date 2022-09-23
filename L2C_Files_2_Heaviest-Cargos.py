count=int(input("Enter the n value :\n"))
num_lines=sum(1 for line in open('readlines.txt'))
lineno=1
check=num_lines-count
for line in (list(open("readlines.txt"))):
    if lineno>check:
        print(line.rstrip())
    lineno=lineno+1
