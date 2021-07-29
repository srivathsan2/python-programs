for i in range(5):
    for j in range(5):
        if ((i+j==2)or(i+j==6)or(i==3 and j==1)or(i==1 and j==3)):  
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
