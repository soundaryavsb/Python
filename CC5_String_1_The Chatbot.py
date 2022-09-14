ShippingInput=input().lower().split(' ')
C=0
F=0
E=0
for Contain in ShippingInput:
    if Contain.startswith('medicine') or Contain.startswith('tablet') or Contain.startswith('drugs'):
        C+=1
    if Contain.startswith('chocolate') or Contain.startswith('meat') or Contain.startswith('fruit'):
        F+=1
    if Contain.startswith('electronics') or Contain.startswith('mobile') or Contain.startswith('PC'):
        E+=1
if C>0:
    print("C-Cargo")
if F>0:
    print("F-Cargo")
if E>0:
    print("E-Cargo")

