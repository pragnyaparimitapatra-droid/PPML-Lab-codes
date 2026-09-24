import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are:", root1, "and", root2)

elif d == 0:
    root = -b / (2*a)
    print("The root is:", root)

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-d) / (2*a)
    print("The roots are:")
    print(real, "+", imaginary, "i")
    print(real, "-", imaginary, "i")
