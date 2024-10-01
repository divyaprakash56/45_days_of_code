# cook your dish here
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())
    
    # Calculate total working hours
    total_hours = (X * 4) + Y
    
    # Print the result
    print(total_hours)
