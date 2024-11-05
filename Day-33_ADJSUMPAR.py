def can_form_array_b(N, B):
    A = [1]  # Start with an initial value for A_1
    
    # Construct the array A based on B
    for i in range(N-1):
        if B[i] == 0:
            A.append(A[-1])  # Same parity
        else:
            A.append(A[-1] + 1)  # Opposite parity
    
    # Check if the constructed A satisfies the condition for B_N
    if (A[0] + A[-1]) % 2 == B[-1]:
        return "YES"
    else:
        return "NO"

# Reading the input
T = int(input().strip())
results = []
for _ in range(T):
    N = int(input().strip())
    B = list(map(int, input().strip().split()))
    results.append(can_form_array_b(N, B))

# Printing results for all test cases
print("\n".join(results))