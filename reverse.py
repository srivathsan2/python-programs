n = int(input("enter the number : "))
b = 0
for i in range(len(str(n))):
    a = n % 10
    b = b * 10 + a
    n = n // 10
 
print(f'reverse value is : {b}')
