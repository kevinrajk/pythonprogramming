c=int(input())
mult=1
if c==0:
  print(mult)
elif c>0:
  for i in range(1,c+1):
    mult*=i
  print(mult)
