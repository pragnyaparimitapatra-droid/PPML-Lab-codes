List = []

N = int(input("Enter the number of terms: "))

for i in range(N):
    n = int(input("Enter Elements: "))
    List.append(n)
  
  
even = []

  
for i in range(N):
    if List[i] % 2 == 0:
        even.append(List[i])
        
print("The new List with the only even Values are: ", even)