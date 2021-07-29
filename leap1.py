a=int(input("enter the year : "))
if(a<999):
    print(f'the given year is invalid{a}')
elif(a%4==0):
    print(f'the given year {a} is a leap year ')
else:
    print(f'the given year {a} is  a not leap year  ')
