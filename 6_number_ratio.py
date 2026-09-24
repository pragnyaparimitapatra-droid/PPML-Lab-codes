arr = list(map(int, input("Enter integers : ").split()))

positive = sum(map(lambda x: x > 0, arr))
negative = sum(map(lambda x: x < 0, arr))
zero = sum(map(lambda x: x == 0, arr))

total = len(arr)

print("Ratio of positive numbers:", positive / total)
print("Ratio of negative numbers:", negative / total)
print("Ratio of zeroes:", zero / total)
