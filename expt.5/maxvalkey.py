d = eval(input("Enter a dictionary: "))

max_key = max(d, key=d.get)

print("Key having maximum value:", max_key)
