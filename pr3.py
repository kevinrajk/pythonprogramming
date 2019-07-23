i,j=input().split()
char=abs(len(j)-len(i))
for g in range(len(i)):
  if(len(j)==1 and b[g] in i):
    break
  if(i[g]!=j[g]):
    char=char+1
print(char)
