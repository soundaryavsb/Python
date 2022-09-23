import xml.etree.ElementTree as ET
tree=ET.parse("candidate.xml")
root = tree.getroot()
for age in root.iter("candidate"):
    if (age.find('age').text)>="25":
        age1=str(age.find('candidateName').text)
        print(age1+" :",end=" ")
        print(age.find('age').text)
