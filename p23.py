#a
s,r=map(int,input().split())
space=input()
m=list(map(int,input().split()))
n=list(map(int,input().split()))
c=[]
for i in range(len(n)):
  m.append(n[i])
  c.append(max(m))
print(*c,sep=' ')
