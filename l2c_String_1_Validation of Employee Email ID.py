emailId=input()

emailIdspilt=emailId.split("@")
user_name=emailIdspilt[0]
domainsplit=emailIdspilt[1].split(".")
domain=domainsplit[1]
domain_name=domainsplit[0]

count=0
Rule1=0
Rule2=0
Rule3=0
#Rule1
domain_allowed=['com','in','edu']
if domain in domain_allowed:
    pass
else:
    count=count+1
    Rule1=1
#Rule2
if len(domain_name)>3:
    pass
else:
    count=count+1
    Rule2 = 2
#Rule3
special_char=['.','_','-']
for char in user_name:
    if char.isupper():
        count=count+1
        Rule3=3
    if ((not char.isalnum())and (char not in special_char)):
        count=count+1
        Rule3=3
    
if user_name[0] in special_char:
    count=count+1
    Rule3=3
if user_name[len(user_name)-1] in special_char:
    count=count+1
    Rule3=3
    
#output
if (count==0):
    print("Valid")
else:
    print("Invalid")
    if(Rule1==1):
        print("1")
    if(Rule2==2):
        print("2")
    if(Rule3==3):
        print("3")
