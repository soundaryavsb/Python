from datetime import datetime,timedelta

day=input()
NoOfDays=int(input())
ShipmentStartDate=input()
value=1
Weekday={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
workday=[1,2,3,4,5]
holiday=[6,7]
newInput=Weekday[day]+1
#print(ShipmentStartDate)
while(NoOfDays>1):
    if newInput in range(1,6):
        Shipmentdate=datetime.strptime(ShipmentStartDate,'%d-%m-%Y')
        ship=Shipmentdate+timedelta(value)
        NoOfDays=NoOfDays-1
        print(ship.strftime('%d')+ship.strftime('-%m')+ship.strftime('-%Y'))
        value=value+1
        newInput+=1
    else:
        value=value+1
        newInput+=1
        if newInput==8:
            newInput=1
