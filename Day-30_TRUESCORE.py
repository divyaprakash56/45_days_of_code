# Read the number of test cases
T = int(input().strip())
results = []

# Process each test case
for _ in range(T):
    # Initial score A:B
    A, B = map(int, input().strip().split())
    # Desired final score C:D
    C, D = map(int, input().strip().split())
    
    # Check if the desired score is possible
    if C >= A and D >= B:
        results.append("POSSIBLE")
    else:
        results.append("IMPOSSIBLE")

# Print each result on a new line
print("\n".join(results))