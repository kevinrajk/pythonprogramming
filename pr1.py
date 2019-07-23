v=int(input())
l=[]
for i in range(v):
  a=input('')
  l.append(a)
li=[]
for u in zip(*l):
  if (u.count(u[0])==len(u)):
    li.append(u[0])
  else:
    break
print("".join(li))
