def even(a):
    return [x for x in a if x % 2 == 0]
a = list(map(int, input("Enter numbers: ").split()))
print("New List: ", even(a))