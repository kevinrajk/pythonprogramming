e = input()
vowels = ["a","e","i","o","u"]
if e in vowels:
    print("Vowel")
elif(e>='b' and e<='z' and e!='e' and e!='i' and e!='o' and e!='u'):
    print("Consonant")
else:
    print("invalid")
