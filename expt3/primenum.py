def is_prime(n):
    if n < 2:
        return false
    for i in range (2,int(n ** 0.5) + 1):
        if n % i == 0:
           return False
    return True


def twin_prime(N):
    print("Twin prime Numbers 1 and ", N, "are: ")
    for i in range(2, N - 1):
        if is_prime(i) and is_prime(i+2):
            print("(", i, ",", i + 2, ")")


#Main Program
N = int(input("Enter the number of twin prime numbers you want: "))
twin_prime(N)