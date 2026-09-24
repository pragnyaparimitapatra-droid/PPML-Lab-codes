list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))
list3 = list(map(int, input("Enter elements of third list: ").split()))

result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

print("Sum of three lists:", result)
    