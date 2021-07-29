b=[1,2,3,4,5,6]
a=[]
c=[]
for i in range(len(b)):
    if i%2==0:
        a.append(b[i])

    else:
        c.append(b[i])
print(f'the odd number position are {c}')
print(f'the even number position are {a}')
