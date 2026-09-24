a = list(map(int, input("Enter list: ").split()))
x = int(input("Enter value: "))

check = lambda x: x in a

print("Present" if check(x) else "Not Present")