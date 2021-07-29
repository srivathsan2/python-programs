c=0
d=0
a=['sdfg','123456','nhgt']
b=len(a)
for i in a:
    if(i.isalpha()):
        c=c+1
        print(c)
    else:
        d=d+1
print(f'the number of letter in given list {c}')
print(f'the given number in given list {d}')
