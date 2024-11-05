# cook your dish here
# Function to determine the third number needed for Chef to win
def third_number_to_win(A, B):
    # Calculate the third number required to reach exactly 21
    C = 21 - (A + B)
    # Check if this third number is within the allowed range
    return C if 1 <= C <= 10 else -1

# Read the number of test cases
T = int(input().strip())
results = []
for _ in range(T):
    # Read each pair of numbers A and B
    A, B = map(int, input().strip().split())
    # Append the result for this test case
    results.append(third_number_to_win(A, B))

# Output all results
print("\n".join(map(str, results)))
