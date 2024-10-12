from collections import Counter

# Read number of test cases
T = int(input())

for _ in range(T):
    # Read number of animals
    N = int(input())
    
    # Read the animal types
    animals = list(map(int, input().split()))
    
    # Count the occurrences of each animal type
    count = Counter(animals)
    
    # Check if all counts are even
    possible = all(c % 2 == 0 for c in count.values())
    
    # Output the result
    if possible:
        print("YES")
    else:
        print("NO")
