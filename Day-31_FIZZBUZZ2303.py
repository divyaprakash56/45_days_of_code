# cook your dish here
# Number of test cases
T = int(input())

# For each test case, calculate the result
results = []
for _ in range(T):
    N = int(input())
    results.append(N * (N - 1))

# Output all results, one per line
for result in results:
    print(result)
