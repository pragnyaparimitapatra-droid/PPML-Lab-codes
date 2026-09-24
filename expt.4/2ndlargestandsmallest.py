
numbers = []

for i in range(10):
    n = int(input("Enter an integer: "))
    numbers.append(n)


numbers.sort()

print(numbers)

print("Second smallest element:", numbers[1])
print("Second largest element:", numbers[-2])