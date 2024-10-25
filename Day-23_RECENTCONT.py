# cook your dish here
# Number of test cases
T = int(input().strip())

# Iterate over each test case
results = []
for _ in range(T):
    # Read the number of problems in the contest
    N = int(input().strip())
    # Read the list of contest codes
    contests = input().strip().split()
    
    # Count occurrences of START38 and LTIME108
    start38_count = contests.count("START38")
    ltime108_count = contests.count("LTIME108")
    
    # Store result for this test case
    results.append(f"{start38_count} {ltime108_count}")

# Output each result
for result in results:
    print(result)
