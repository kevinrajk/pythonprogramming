d=int(input())
string=input()
v="aeiou"
final_string=""
for i in string:
    if(i not in v):
        final_string+=i
print("".join(reversed(final_string)))
