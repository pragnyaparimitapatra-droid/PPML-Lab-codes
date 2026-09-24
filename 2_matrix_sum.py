a = []

for i in range(3):
    a.append(list(map(int, input().split())))

print("Matrix:")
for r in a:
    print(r)

print("Row sums:")
for r in a:
    print(sum(r))

print("Column sums:")
for j in range(3):
    print(sum(a[i][j] for i in range(3)))