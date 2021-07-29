a=int(input("enter the number of colume to print : "))
b=int(input("enter the number to print in a colume : "))
c=a
for i in range(a):
    c=c-1
    for j in range(b):
        print(f'{c}',end=" ")
    print(" ")
