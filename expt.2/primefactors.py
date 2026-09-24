n = int(input("Enter a 3 digit number: "))
print("Prime factors: ", end = " ")

i = 2
while i < n:
    while n % i == 0:
        print(i,end = " ")
        n = n // i
    
    i += 1