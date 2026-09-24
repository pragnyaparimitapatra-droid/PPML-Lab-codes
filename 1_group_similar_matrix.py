import random

rows = 4
cols = 4

matrix = [[random.randint(1, 5) for j in range(cols)] for i in range(rows)]

print("Matrix:")
for row in matrix:
    print(row)