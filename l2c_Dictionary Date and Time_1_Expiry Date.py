from datetime import datetime,timedelta

exp=input()
delivery=input()
days=int(input())

format_data = '%b %d %Y'

expdate = datetime.strptime(exp,format_data)
deldate= datetime.strptime(delivery,format_data)+timedelta(days)

if (expdate>deldate):
    print("Yes")
else:
    print("No")

