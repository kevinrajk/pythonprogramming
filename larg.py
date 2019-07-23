na1,na2,na3 = map(int,input().split())

 
if (na1 > na2) and (na1 > na3):
   largest = na1
elif (na2 > na1) and (na2 > na3):
   largest = na2
else:
   largest = na3
 
print("",largest)

