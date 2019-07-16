ne = input()
vowels = ["a","e","i","o","u"]
if ne in vowels:
    print("Vowel")
elif(ne>='b' and ne<='z' and ne!='e' and ne!='i' and ne!='o' and ne!='u'):
    print("constant")
else:
    print("invalid")
