a=input("enter the product name : ")
b=int(input("enter the price of the product : "))
c=int(input("enter the number of the product : "))
d=int(input("enter the discount of the product : "))
e=b*c
f=(d/100)*e
g=e-f
print(f'the product name is {a}')
print(f'price of the product is {b}')
print(f'number of the product is {c}')
print(f'the discount given to the product is {d}%')
print(f'the total price of the product is {e} ')
print(f'the discounted price of the product is : {g}')

