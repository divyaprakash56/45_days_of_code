# Read the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the initial locations of the policeman and the thief
    X, Y = map(int, input().split())
    
    # Calculate the minimum time taken by the policeman to catch the thief
    time = abs(X - Y) / 1
    
    # Print the minimum time
    print(int(time))