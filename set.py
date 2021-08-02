num1={1,2,3,4,5,6}
num2={4,5,6,7,8,9}
print(num1.intersection(num2))
print(num2.union(num1))
print(num1.issubset(num2))
print(num1.difference(num2))
num2.add(1)
print(num1)