n = int(input("Enter n: "))
a = [list(map(int, input().split())) for i in range(n)]

print("Transpose:")
for j in range(n):
    print([a[i][j] for i in range(n)])