x,y=map(str,input('').split())
t=[]
t.append(x)
t.append(y)
s=[]
for i in zip(*l):
    if i.count(i[0])==len(i):
        s.append(i[0])
    else:
        break
m=max(t,key=len)
k=len(m)-len(s)
print(k)
