numbers = list(map(int, input("Enter the numbers: ").split()))

result = [num ** i for i, num in enumerate(numbers)]

print("Result:", result)
