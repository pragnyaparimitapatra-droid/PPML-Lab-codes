numbers = list(map(int, input("Enter numbers : ").split()))

tripled = list(map(lambda x: x * 3, numbers))

print("Tripled numbers:", tripled)
