#a=int(input("enter the number colume : "))
#b=int(input("print the number in the colume : "))
c=1
for i in range(1,5+1):
    for j in range(1,5+1):
        if ((i+j==4)or(i-j==-2)or(i==3)):
            print(f'{c}',end=" ")
        else:
            print("*",end=" ")
    print()
