a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b) and (a>c):
    print(a," is largest among entered numbers")
elif(b>a) and (b>c):
    print(b," is largest among entered numbers")
else:
    print(c," is largest among entered numbers")