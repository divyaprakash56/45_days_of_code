# cook your dish here
# Function to calculate total skipped strings
def total_skipped_strings(plucks):
    total_skips = 0
    for i in range(len(plucks) - 1):
        total_skips += abs(plucks[i + 1] - plucks[i]) - 1
    return total_skips

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the number of plucks
    N = int(input())
    # Read the plucked strings
    plucks = list(map(int, input().split()))
    # Calculate and print the total number of skipped strings
    print(total_skipped_strings(plucks))
    