a=input(" enter the letter : ")
b=a[0]
c=a[-1]
print(f'the 1st letter is : {b}')
print(f'the last letter is : {c}')
if (b=="a" or b=="e" or b=="i" or b=="o" or b=="u"):
    print(f' the given 1st letter {b} is an vowels ')
    if (c=="a" or c=="e" or c=="i" or c=="o" or c=="u"):
        print(f'the given last letter {c} is an vowel')
    else:
        print("the given last letter is not an vowel ")
else:
    print("the given 1st letter is not a vowel ")
    if (c=="a" or c=="e" or c=="i" or c=="o" or c=="u"):
        print(f'the given last letter {c} is an vowel')
    else:
        print("the given letter is not an vowel ")
