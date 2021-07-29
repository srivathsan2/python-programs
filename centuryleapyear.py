a=int(input("enter the year :"))
if(a%4==0):
    print(f'the given year {a} is a leap year ')
    if(a%400==0):
        print(f'the given year {a} is a century leap year ')
    else:
        print(f'the given year {a} is not a century leap year ')
else:
    print(f'the given year {a} is not a leap year ')
