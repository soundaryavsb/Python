from datetime import datetime
Inputdate=input()
formatdate='%b %d %Y'
Date=datetime.strptime(Inputdate,formatdate)

print(Date)
