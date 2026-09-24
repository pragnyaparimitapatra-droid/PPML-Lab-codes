a = int(input("enter the first number"))
b = int(input("enter the second number"))

print("Before swapping: ")
print("a=", a)
print("b=", b)

a = a^b
b = b^a
a = b^a

print("After swapping: ")
print("a=",a)
print("b=",b)
