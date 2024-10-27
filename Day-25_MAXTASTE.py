# Function to calculate maximum tastiness
def max_tastiness(a, b, c, d):
    # Calculate all possible combinations of tastiness
    return max(a + c, a + d, b + c, b + d)

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the tastiness values
    a, b, c, d = map(int, input().split())
    # Calculate and print the maximum tastiness
    print(max_tastiness(a, b, c, d))