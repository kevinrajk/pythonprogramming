m,n=map(int,input().split())
l=list(map(int,input().split()[:m]))
s=0
for i in range(n):
    s=s+l[i]
print(s)
