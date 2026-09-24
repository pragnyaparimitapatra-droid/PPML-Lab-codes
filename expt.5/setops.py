s1 = eval(input("Enter First Set: "))
s2 = eval(input("Enter Second Set: "))

print("UNION = ", s1 | s2)
print("INTERSECTION = ", s1 & s2)
print("DIFFERENCE = ", s1 - s2)
print("DIFFERENCE (S2 -S1) = ", s2 - s1)
print("SYMMETRIC DIFFERENCE = ", s1 ^ s2)
