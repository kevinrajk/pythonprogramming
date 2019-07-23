nu1 = float(input("Enter first number: "))
nu2 = float(input("Enter second number: "))
nu3 = float(input("Enter third number: "))
 
if (nu1 > nu2) and (nu1 > nu3):
   largest = nu1
elif (nu2 > nu1) and (nu2 > nu3):
   largest = nu2
else:
   largest = nu3
 
print("The largest number is",largest)
