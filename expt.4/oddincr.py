numbers = []

for i in range(20):
    n = int(input("Enter any 20 Integers: "))
    numbers.append(n)
    
for i in range(20):
    if numbers[i] % 2 == 1:
        numbers[i] = numbers[i] + 5
        
        
print("The Final Array looks like: ", numbers)