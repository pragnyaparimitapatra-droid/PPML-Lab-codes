a = list(map(int, input("Enter array 1: ").split()))
b = list(map(int, input("Enter array 2: ").split()))

add = lambda x, y: x + y

print([add(x, y) for x, y in zip(a, b)])