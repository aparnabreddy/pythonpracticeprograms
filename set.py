
num1={1,2,3,4,5,6}
num2={4,5,6,7,8,9}
print(num1.intersection(num2))
print(num2.union(num1))
print(num1.issubset(num2))
print(num1.difference(num2))
num2.add(1)
print(num1)

flowers={"rose","jasmine","marigold","rose","crysantamum"}
flow={"rose","lily","tulip"}
# flowers.add("lily")
# flowers.add("daisy")
# print(flowers)
# flowers.remove("marigold")
# flowers.remove("lotus")  #shows error when try deleting the element that is not there
# flowers.discard("Tulio") # doesn't shows error when try deleting the element that is not there
# print(flowers)
# print(flowers.intersection(flow))
# print(flowers.union(flow))
# print(flow.issubset(flowers))
# print(flow.issuperset(flowers))
# print(flow.difference(flowers))

