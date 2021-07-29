a=int(input("enter the times of tables : "))
b=int(input("enter the number of tables : "))
for i in range(1,a+1):
    c=int(input("which table want to print : "))
    for j in range (1,b+1):
        d=c*j
        print(f'{c}*{j}={d}')
