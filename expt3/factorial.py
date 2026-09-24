def factorial(N):
    fact = 1
    
    if(N == 1):
        return 1
    elif(N == 0):
        return 0
    for i in range (1, N + 1):
        fact = fact * i
        
        print("The factorial of ", N, "is: ", fact)
        
    
#main program
N = int(input("Enter the Number of factorials you want: "))
factorial(N)