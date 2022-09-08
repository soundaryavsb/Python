from datetime import datetime,timedelta

inputdate=input("Enter a input in FullMonthName/DD/YY: ")
formatdate='%B/%d/%y'
days=int(input("Enter number of days to add with input: "))

OutputDate=datetime.strptime(inputdate,formatdate)+timedelta(days)

print("The output is: ",OutputDate)
