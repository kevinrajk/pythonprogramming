s,r = map(int,input().split())
for i in range(1,min(s,r)+1) :
    if (s%i==0)  and (r%i==0) : 
      anser = i
print(anser)
