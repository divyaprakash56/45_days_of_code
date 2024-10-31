# cook your dish here
def rearrange_array(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        # Sort the array
        A.sort()
        
        # Create a new array to hold the rearranged elements
        rearranged = [0] * N
        
        # Fill even indices with the smallest elements
        for i in range(0, N, 2):
            rearranged[i] = A[i // 2]
        
        # Fill odd indices with the largest elements
        for i in range(1, N, 2):
            rearranged[i] = A[N - 1 - (i // 2)]
        
        results.append(' '.join(map(str, rearranged)))
    
    return results

# Input handling
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

# Get results
results = rearrange_array(test_cases)

# Output results
for result in results:
    print(result)