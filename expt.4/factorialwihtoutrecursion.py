def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
    
#Main Program
num = int(input("Enter the number you want to find the factorial of: "))

result = factorial(num)

print("Factorial of", num, "is", result)