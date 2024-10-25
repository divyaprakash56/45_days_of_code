# cook your dish here
# Number of test cases
T = int(input().strip())

# Iterate over each test case
results = []
for _ in range(T):
    # Read the number of terms in the polynomial
    N = int(input().strip())
    # Read the coefficients
    coefficients = list(map(int, input().strip().split()))
    
    # Traverse coefficients from the last term to find the highest power with a non-zero coefficient
    degree = -1
    for i in range(N - 1, -1, -1):
        if coefficients[i] != 0:
            degree = i
            break
    
    # Store result for this test case
    results.append(degree)

# Output each result
for result in results:
    print(result)
