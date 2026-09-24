s = input("Enter a sequence: ")

# Remove duplicate characters
s = ''.join(dict.fromkeys(s))

# Convert to uppercase and lowercase using map()
uppercase = ''.join(map(str.upper, s))
lowercase = ''.join(map(str.lower, s))

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
