a=input("enter the name of the employe : ")
b=input("enter the employe id : ")
c=input("enter the position of the employe : ")
d=int(input("enter the salary of the employe : "))
e=float(input("enter the pf of the employe : "))
f=float(input("enter the EDI of the employe : "))
g=(e/100)*d
h=d-g
i=(f/100)*h
j=h-i
print(f'employe                      : {a} ')
print(f'employe id                   : {b} ')
print(f'position of the employe      : {c} ')
print(f'PF                           : {h} ')
print(f'EDI                          : {j} \n')
print(f'the total salary of the employe : {j} ')
