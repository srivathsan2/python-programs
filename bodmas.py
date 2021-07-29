a=int(input("enter the principle : "))
b=int(input("enter the number of the year : "))
c=float(input("enter the percentage of the principle : "))
d=(c/100)*a
e=a+d
f=b*12
g=e/f
print(f'amount of intrest in per year : {d}')
print(f'amount of intrest in per month : {g}')
print(f'the total amount of the intrest : {e}')
